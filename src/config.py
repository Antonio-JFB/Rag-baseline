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
from src.retrievers import BM25Retriever, CosineFaissRetriever


class PipelineConfig(BaseModel):
    nombre: str
    retriever: Literal["cosine", "bm25"]
    embed_model: str = "paraphrase-multilingual-MiniLM-L12-v2"
    top_k: int = 5
    chunking: Literal["sliding_window", "paragraph"] = "sliding_window"
    chunk_size: int = 300
    chunk_overlap: int = 50
    chunk_max_words: int = 85
    index_dir: str | None = None
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
    return BM25Retriever(**kwargs)


RETRIEVERS = {"cosine": _cosine, "bm25": _bm25}

CHUNKERS = {
    "sliding_window": lambda cfg: SlidingWindowChunker(chunk_size=cfg.chunk_size, overlap=cfg.chunk_overlap),
    "paragraph": lambda cfg: ParagraphChunker(max_words=cfg.chunk_max_words),
}


def load_chunks_for(config: PipelineConfig, chunker: BaseChunker) -> list[Chunk]:
    """Chunks que debe indexar esta configuracion. El baseline (sliding_window) sigue
    usando los chunks de Fase 0 ya guardados (verificado: identicos a re-chunkear data/);
    cualquier otro chunker re-chunkea el corpus, porque los chunks guardados no le sirven."""
    if config.chunking == "sliding_window":
        return load_chunks()
    return load_corpus_chunks(chunker)


def build_pipeline(config: PipelineConfig) -> RAGPipeline:
    chunker = CHUNKERS[config.chunking](config)
    retriever = RETRIEVERS[config.retriever](config)
    postprocessor = NoOpPostprocessor()
    generator = OllamaGenerator(model=config.ollama_model, url=config.ollama_url)
    return RAGPipeline(chunker, retriever, postprocessor, generator, top_k=config.top_k)
