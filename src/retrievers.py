"""
Implementaciones de BaseRetriever.

CosineFaissRetriever  -> retrieval semántico (embeddings), el método del baseline.
BM25Retriever         -> retrieval léxico (frecuencia de términos), método alterno
                         para demostrar que Proposal 2 permite intercambiar el
                         componente de retrieval sin tocar el pipeline.
"""

import logging
import os
import pickle

import faiss
import numpy as np
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer

from src.interfaces import BaseRetriever, Chunk, RetrievedChunk
from src.preprocessing import PlainPreprocessor, Preprocessor

log = logging.getLogger(__name__)


class CosineFaissRetriever(BaseRetriever):
    """FAISS IndexFlatIP sobre vectores normalizados = cosine similarity exacta.
    Si ya existe un índice guardado en disco (construido por rag_ollama.py o por
    este mismo retriever), lo reutiliza en vez de recalcular embeddings."""

    def __init__(
        self,
        embed_model: str = "paraphrase-multilingual-MiniLM-L12-v2",
        index_path: str = "embeddings/faiss.index",
    ):
        self.embed_model_name = embed_model
        self.index_path = index_path
        self._model: SentenceTransformer | None = None
        self.index: faiss.Index | None = None
        self.chunks: list[Chunk] = []

    @property
    def model(self) -> SentenceTransformer:
        if self._model is None:
            self._model = SentenceTransformer(self.embed_model_name)
        return self._model

    def build_index(self, chunks: list[Chunk]) -> None:
        self.chunks = chunks

        if os.path.exists(self.index_path):
            cached = faiss.read_index(self.index_path)
            if cached.ntotal == len(chunks):
                self.index = cached
                return
            log.warning(
                f"Indice {self.index_path} tiene {cached.ntotal} vectores pero hay "
                f"{len(chunks)} chunks; se reconstruye."
            )

        textos = [c.texto for c in chunks]
        embeddings = self.model.encode(
            textos,
            batch_size=32,
            show_progress_bar=False,
            convert_to_numpy=True,
            normalize_embeddings=True,
        ).astype(np.float32)

        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dim)
        self.index.add(embeddings)

        os.makedirs(os.path.dirname(self.index_path), exist_ok=True)
        faiss.write_index(self.index, self.index_path)

    def retrieve(self, query: str, top_k: int) -> list[RetrievedChunk]:
        q_emb = self.model.encode(
            [query], normalize_embeddings=True, convert_to_numpy=True,
        ).astype(np.float32)

        scores, indices = self.index.search(q_emb, top_k)
        resultados = []
        for score, idx in zip(scores[0], indices[0]):
            if idx < 0:
                continue
            resultados.append(RetrievedChunk(chunk=self.chunks[idx], score=float(score)))
        return resultados


class BM25Retriever(BaseRetriever):
    """Retrieval léxico clásico (Okapi BM25). Los scores NO están acotados
    0-1 como en CosineFaissRetriever -- no son comparables directamente
    entre retrievers; es una limitación a declarar al justificar métricas."""

    def __init__(self, index_path: str = "bm25_index/bm25.pkl", preprocessor: Preprocessor | None = None):
        self.index_path = index_path
        self.pre: Preprocessor = preprocessor or PlainPreprocessor()
        self.bm25: BM25Okapi | None = None
        self.chunks: list[Chunk] = []

    def build_index(self, chunks: list[Chunk]) -> None:
        self.chunks = chunks

        if os.path.exists(self.index_path):
            with open(self.index_path, "rb") as f:
                cached = pickle.load(f)
            if cached.corpus_size == len(chunks):
                self.bm25 = cached
                return
            log.warning(
                f"Indice {self.index_path} tiene {cached.corpus_size} documentos pero hay "
                f"{len(chunks)} chunks; se reconstruye."
            )

        corpus = self.pre.tokens_many([c.texto for c in chunks])
        self.bm25 = BM25Okapi(corpus)

        os.makedirs(os.path.dirname(self.index_path), exist_ok=True)
        with open(self.index_path, "wb") as f:
            pickle.dump(self.bm25, f)

    def retrieve(self, query: str, top_k: int) -> list[RetrievedChunk]:
        tokens = self.pre.tokens(query)
        if not tokens:
            log.warning(f"La consulta no tiene terminos tras el preprocesamiento: {query!r}")
            return []
        scores = self.bm25.get_scores(tokens)
        top_idx = np.argsort(scores)[::-1][:top_k]
        return [
            RetrievedChunk(chunk=self.chunks[i], score=float(scores[i]))
            for i in top_idx
        ]


class HybridRetriever(BaseRetriever):
    """Busqueda hibrida (Configuracion 2 del RFC): fusiona el ranking semantico
    (embeddings + coseno) con el lexico (BM25) mediante Reciprocal Rank Fusion.

    RRF combina POSICIONES, no puntajes, asi que no importa que el coseno vaya de 0
    a 1 y BM25 no este acotado. Cada chunk suma w / (k + posicion) por cada ranking
    donde aparece. El puntaje devuelto es el puntaje fusionado (del orden de 0.01 a
    0.03): no es comparable con el de coseno ni con el de BM25.

    Los chunks que BM25 puntua en 0 (ningun termino de la consulta aparece) no
    entran a la fusion: su orden entre ellos es arbitrario y solo meteria ruido."""

    def __init__(
        self,
        dense: CosineFaissRetriever,
        lexical: BM25Retriever,
        rrf_k: int = 60,
        dense_weight: float = 0.5,
        lexical_weight: float = 0.5,
        fusion_depth: int = 20,
    ):
        self.dense = dense
        self.lexical = lexical
        self.rrf_k = rrf_k
        self.dense_weight = dense_weight
        self.lexical_weight = lexical_weight
        self.fusion_depth = fusion_depth

    def build_index(self, chunks: list[Chunk]) -> None:
        self.dense.build_index(chunks)
        self.lexical.build_index(chunks)

    def retrieve(self, query: str, top_k: int) -> list[RetrievedChunk]:
        depth = max(self.fusion_depth, top_k)
        dense_hits = self.dense.retrieve(query, depth)
        lexical_hits = [r for r in self.lexical.retrieve(query, depth) if r.score > 0]

        fused: dict[str, float] = {}
        by_id: dict[str, Chunk] = {}
        for weight, hits in ((self.dense_weight, dense_hits), (self.lexical_weight, lexical_hits)):
            for rank, hit in enumerate(hits, 1):
                by_id[hit.chunk.id] = hit.chunk
                fused[hit.chunk.id] = fused.get(hit.chunk.id, 0.0) + weight / (self.rrf_k + rank)

        ordered = sorted(fused.items(), key=lambda kv: -kv[1])[:top_k]
        return [RetrievedChunk(chunk=by_id[cid], score=score) for cid, score in ordered]
