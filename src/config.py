"""
Config validada con Pydantic + factory de pipelines.

build_pipeline() es el único lugar que conoce las clases concretas.
Cambiar de método de retrieval = cambiar `retriever: cosine` -> `retriever: bm25`
en el YAML; el pipeline y el evaluador no se tocan.
"""

from typing import Literal

import yaml
from pydantic import BaseModel

from src.chunkers import SlidingWindowChunker
from src.generators import OllamaGenerator
from src.pipeline import RAGPipeline
from src.postprocessors import NoOpPostprocessor
from src.retrievers import BM25Retriever, CosineFaissRetriever


class PipelineConfig(BaseModel):
    nombre: str
    retriever: Literal["cosine", "bm25"]
    embed_model: str = "paraphrase-multilingual-MiniLM-L12-v2"
    top_k: int = 5
    chunk_size: int = 300
    chunk_overlap: int = 50
    ollama_model: str = "gemma3:12b"
    ollama_url: str = "http://localhost:11434/api/generate"


def load_config(path: str) -> PipelineConfig:
    with open(path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)
    return PipelineConfig(**raw)


RETRIEVERS = {
    "cosine": lambda cfg: CosineFaissRetriever(embed_model=cfg.embed_model),
    "bm25": lambda cfg: BM25Retriever(),
}


def build_pipeline(config: PipelineConfig) -> RAGPipeline:
    chunker = SlidingWindowChunker(chunk_size=config.chunk_size, overlap=config.chunk_overlap)
    retriever = RETRIEVERS[config.retriever](config)
    postprocessor = NoOpPostprocessor()
    generator = OllamaGenerator(model=config.ollama_model, url=config.ollama_url)
    return RAGPipeline(chunker, retriever, postprocessor, generator, top_k=config.top_k)
