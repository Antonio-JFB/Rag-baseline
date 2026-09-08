"""
Interfaces base del framework (Proposal 2 del RFC: Separation of Concerns).

El evaluador y el pipeline solo conocen estas clases abstractas, nunca las
implementaciones concretas. Cambiar de método de retrieval significa crear
una clase nueva que herede de BaseRetriever, no editar el pipeline.
"""

from abc import ABC, abstractmethod

from pydantic import BaseModel


class Chunk(BaseModel):
    id: str
    texto: str
    fuente: str
    inicio_palabra: int
    fin_palabra: int
    num_palabras: int


class RetrievedChunk(BaseModel):
    chunk: Chunk
    score: float


class GenerationResult(BaseModel):
    respuesta: str
    prompt: str
    latency_s: float


class PipelineResult(BaseModel):
    query: str
    retrieved: list[RetrievedChunk]
    generation: GenerationResult
    t_retrieval: float
    t_total: float


class BaseChunker(ABC):
    @abstractmethod
    def chunk(self, texto: str, fuente: str) -> list[Chunk]:
        """Divide un texto en chunks."""


class BaseRetriever(ABC):
    @abstractmethod
    def build_index(self, chunks: list[Chunk]) -> None:
        """Construye (o carga) el índice a partir de una lista de chunks."""

    @abstractmethod
    def retrieve(self, query: str, top_k: int) -> list[RetrievedChunk]:
        """Devuelve los top_k chunks más relevantes para query."""


class BasePostprocessor(ABC):
    @abstractmethod
    def process(self, query: str, resultados: list[RetrievedChunk]) -> list[RetrievedChunk]:
        """Transforma (reordena, filtra) los resultados del retriever."""


class BaseGenerator(ABC):
    @abstractmethod
    def generate(self, query: str, resultados: list[RetrievedChunk]) -> GenerationResult:
        """Genera una respuesta a partir de la query y el contexto recuperado."""
