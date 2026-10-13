"""Implementaciones de BaseChunker."""

import re

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


class ParagraphChunker(BaseChunker):
    """Chunking por parrafos (Configuracion 1 del RFC): nunca corta un parrafo a
    la mitad salvo que el parrafo solo ya exceda max_words, y en ese caso lo
    divide en limites de oracion. Los parrafos cortos (titulos de seccion, items
    de lista) se unen con los siguientes hasta llenar max_words, de modo que un
    titulo siempre viaja con el texto que introduce (un titulo nunca queda solo,
    aunque pegarlo rebase max_words por unas pocas palabras).

    max_words=85 equivale a ~128 tokens en este corpus (~1.5 tokens/palabra), el
    limite de secuencia de paraphrase-multilingual-MiniLM-L12-v2: asi el
    embedding representa el chunk completo y no solo su inicio."""

    HEADING_MAX_WORDS = 10
    HEADING_GLUE_WORDS = 15

    def __init__(self, max_words: int = 85):
        self.max_words = max_words

    def _is_heading(self, unit: str) -> bool:
        return len(unit.split()) <= self.HEADING_MAX_WORDS and not unit.rstrip().endswith((".", "!", "?"))

    def _split_long(self, par: str) -> list[str]:
        """Divide un parrafo de mas de max_words palabras por oraciones."""
        sentences = re.split(r"(?<=[.!?])\s+", par.strip())
        pieces, current = [], []
        for sent in sentences:
            words = sent.split()
            if len(words) > self.max_words:
                if current:
                    pieces.append(" ".join(current))
                    current = []
                for i in range(0, len(words), self.max_words):
                    pieces.append(" ".join(words[i:i + self.max_words]))
                continue
            if len(current) + len(words) > self.max_words:
                pieces.append(" ".join(current))
                current = []
            current.extend(words)
        if current:
            pieces.append(" ".join(current))
        return pieces

    def chunk(self, texto: str, fuente: str) -> list[Chunk]:
        units: list[str] = []
        for line in texto.split("\n"):
            line = line.strip()
            if not line:
                continue
            if len(line.split()) > self.max_words:
                units.extend(self._split_long(line))
            else:
                units.append(line)

        groups: list[list[str]] = []
        current: list[str] = []
        current_words = 0
        for unit in units:
            n = len(unit.split())
            only_headings = bool(current) and current_words <= self.HEADING_GLUE_WORDS \
                and all(self._is_heading(u) for u in current)
            if current and current_words + n > self.max_words and not only_headings:
                groups.append(current)
                current, current_words = [], 0
            current.append(unit)
            current_words += n
        if current:
            groups.append(current)

        chunks: list[Chunk] = []
        offset = 0
        for group in groups:
            body = " ".join(group)
            n = len(body.split())
            chunks.append(Chunk(
                id=f"{fuente}_{len(chunks):04d}",
                texto=body,
                fuente=fuente,
                inicio_palabra=offset,
                fin_palabra=offset + n,
                num_palabras=n,
            ))
            offset += n
        return chunks
