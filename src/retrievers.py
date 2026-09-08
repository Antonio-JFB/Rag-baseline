"""
Implementaciones de BaseRetriever.

CosineFaissRetriever  -> retrieval semántico (embeddings), el método del baseline.
BM25Retriever         -> retrieval léxico (frecuencia de términos), método alterno
                         para demostrar que Proposal 2 permite intercambiar el
                         componente de retrieval sin tocar el pipeline.
"""

import os
import pickle
import re

import faiss
import numpy as np
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer

from src.interfaces import BaseRetriever, Chunk, RetrievedChunk


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
            self.index = faiss.read_index(self.index_path)
            return

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


def _tokenize(texto: str) -> list[str]:
    return re.findall(r"\w+", texto.lower())


class BM25Retriever(BaseRetriever):
    """Retrieval léxico clásico (Okapi BM25). Los scores NO están acotados
    0-1 como en CosineFaissRetriever -- no son comparables directamente
    entre retrievers; es una limitación a declarar al justificar métricas."""

    def __init__(self, index_path: str = "bm25_index/bm25.pkl"):
        self.index_path = index_path
        self.bm25: BM25Okapi | None = None
        self.chunks: list[Chunk] = []

    def build_index(self, chunks: list[Chunk]) -> None:
        self.chunks = chunks

        if os.path.exists(self.index_path):
            with open(self.index_path, "rb") as f:
                self.bm25 = pickle.load(f)
            return

        corpus = [_tokenize(c.texto) for c in chunks]
        self.bm25 = BM25Okapi(corpus)

        os.makedirs(os.path.dirname(self.index_path), exist_ok=True)
        with open(self.index_path, "wb") as f:
            pickle.dump(self.bm25, f)

    def retrieve(self, query: str, top_k: int) -> list[RetrievedChunk]:
        scores = self.bm25.get_scores(_tokenize(query))
        top_idx = np.argsort(scores)[::-1][:top_k]
        return [
            RetrievedChunk(chunk=self.chunks[i], score=float(scores[i]))
            for i in top_idx
        ]
