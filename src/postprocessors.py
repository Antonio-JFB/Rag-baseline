"""Implementaciones de BasePostprocessor."""

from src.interfaces import BasePostprocessor, RetrievedChunk


class NoOpPostprocessor(BasePostprocessor):
    """Identidad -- igual que el baseline actual (sin reranking ni filtrado)."""

    def process(self, query: str, resultados: list[RetrievedChunk]) -> list[RetrievedChunk]:
        return resultados
