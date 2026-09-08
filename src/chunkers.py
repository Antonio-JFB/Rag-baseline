"""Implementaciones de BaseChunker."""

from src.interfaces import BaseChunker, Chunk


class SlidingWindowChunker(BaseChunker):
    """Ventana deslizante por palabras con overlap. Misma lógica que
    chunk_texto() en rag_ollama.py (Fase 0)."""

    def __init__(self, chunk_size: int = 300, overlap: int = 50):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, texto: str, fuente: str) -> list[Chunk]:
        palabras = texto.split()
        chunks: list[Chunk] = []
        inicio = 0

        while inicio < len(palabras):
            fin = min(inicio + self.chunk_size, len(palabras))
            chunks.append(Chunk(
                id=f"{fuente}_{len(chunks):04d}",
                texto=" ".join(palabras[inicio:fin]),
                fuente=fuente,
                inicio_palabra=inicio,
                fin_palabra=fin,
                num_palabras=fin - inicio,
            ))
            if fin == len(palabras):
                break
            inicio += self.chunk_size - self.overlap

        return chunks
