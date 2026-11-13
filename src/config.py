"""
Config validada con Pydantic + factory de pipelines.

build_pipeline() es el único lugar que conoce las clases concretas.
Cambiar de método de retrieval = cambiar `retriever: cosine` -> `retriever: bm25`
en el YAML; el pipeline y el evaluador no se tocan.
"""

from typing import Literal

import yaml
from pydantic import BaseModel

from src.chunkers import ParagraphChunker, SlidingWindowChunker
from src.generators import OllamaGenerator
from src.interfaces import BaseChunker, Chunk
from src.pipeline import RAGPipeline, load_chunks, load_corpus_chunks
from src.postprocessors import NoOpPostprocessor
from src.preprocessing import build_preprocessor
from src.retrievers import BM25Retriever, CosineFaissRetriever, HybridRetriever


class PipelineConfig(BaseModel):
    nombre: str
    retriever: Literal["cosine", "bm25", "hybrid"]
    embed_model: str = "paraphrase-multilingual-MiniLM-L12-v2"
    top_k: int = 5
    chunking: Literal["sliding_window", "paragraph"] = "sliding_window"
    chunk_size: int = 300
    chunk_overlap: int = 50
    chunk_max_words: int = 85
    index_dir: str | None = None
    lexical_preprocessing: Literal["none", "lemma_stopwords"] = "none"
    rrf_k: int = 60
    dense_weight: float = 0.5
    lexical_weight: float = 0.5
    fusion_depth: int = 20
    ollama_model: str = "gemma3:12b"
    ollama_url: str = "http://localhost:11434/api/generate"


def load_config(path: str) -> PipelineConfig:
    with open(path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)
    return PipelineConfig(**raw)


def _cosine(cfg: PipelineConfig) -> CosineFaissRetriever:
    kwargs = {"index_path": f"{cfg.index_dir}/faiss.index"} if cfg.index_dir else {}
    return CosineFaissRetriever(embed_model=cfg.embed_model, **kwargs)


def _bm25(cfg: PipelineConfig) -> BM25Retriever:
    kwargs = {"index_path": f"{cfg.index_dir}/bm25.pkl"} if cfg.index_dir else {}
    return BM25Retriever(preprocessor=build_preprocessor(cfg.lexical_preprocessing), **kwargs)


def _hybrid(cfg: PipelineConfig) -> HybridRetriever:
    return HybridRetriever(
        _cosine(cfg), _bm25(cfg),
        rrf_k=cfg.rrf_k, dense_weight=cfg.dense_weight,
        lexical_weight=cfg.lexical_weight, fusion_depth=cfg.fusion_depth,
    )


RETRIEVERS = {"cosine": _cosine, "bm25": _bm25, "hybrid": _hybrid}

CHUNKERS = {
    "sliding_window": lambda cfg: SlidingWindowChunker(chunk_size=cfg.chunk_size, overlap=cfg.chunk_overlap),
    "paragraph": lambda cfg: ParagraphChunker(max_words=cfg.chunk_max_words),
}


def load_chunks_for(config: PipelineConfig, chunker: BaseChunker) -> list[Chunk]:
    """Chunks que debe indexar esta configuracion. El baseline (ventana de 300 palabras con
    traslape de 50) usa los chunks de Fase 0 ya guardados (verificado: identicos a re-chunkear
    data/); cualquier otro chunker o tamano de ventana re-chunkea el corpus, porque los chunks
    guardados no le sirven."""
    if config.chunking == "sliding_window" and (config.chunk_size, config.chunk_overlap) == (300, 50):
        return load_chunks()
    return load_corpus_chunks(chunker)


def build_pipeline(config: PipelineConfig) -> RAGPipeline:
    chunker = CHUNKERS[config.chunking](config)
    retriever = RETRIEVERS[config.retriever](config)
    postprocessor = NoOpPostprocessor()
    generator = OllamaGenerator(model=config.ollama_model, url=config.ollama_url)
    return RAGPipeline(chunker, retriever, postprocessor, generator, top_k=config.top_k)
