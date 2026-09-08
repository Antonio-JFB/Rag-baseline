"""Orquestador del framework (Proposal 2)."""

import json
import logging
import time

from src.interfaces import (
    BaseChunker,
    BaseGenerator,
    BasePostprocessor,
    BaseRetriever,
    Chunk,
    PipelineResult,
)

log = logging.getLogger(__name__)


def load_chunks(meta_path: str = "embeddings/metadata.json") -> list[Chunk]:
    """Carga los chunks ya construidos en Fase 0 (mismo corpus, mismo chunking)."""
    with open(meta_path, "r", encoding="utf-8") as f:
        raw = json.load(f)
    return [Chunk(**c) for c in raw]


class RAGPipeline:
    """Orquesta retrieve -> postprocess -> generate y captura observabilidad
    completa: query, chunks recuperados + scores, tiempos, prompt completo,
    respuesta (7/7 campos, cierra el hueco de prompt logging del baseline)."""

    def __init__(
        self,
        chunker: BaseChunker,
        retriever: BaseRetriever,
        postprocessor: BasePostprocessor,
        generator: BaseGenerator,
        top_k: int = 5,
    ):
        self.chunker = chunker
        self.retriever = retriever
        self.postprocessor = postprocessor
        self.generator = generator
        self.top_k = top_k

    def index(self, chunks: list[Chunk]) -> None:
        self.retriever.build_index(chunks)

    def answer(self, query: str, top_k: int | None = None) -> PipelineResult:
        top_k = top_k or self.top_k
        t0 = time.time()

        t_r0 = time.time()
        resultados = self.retriever.retrieve(query, top_k)
        resultados = self.postprocessor.process(query, resultados)
        t_retrieval = time.time() - t_r0

        generation = self.generator.generate(query, resultados)
        t_total = time.time() - t0

        result = PipelineResult(
            query=query,
            retrieved=resultados,
            generation=generation,
            t_retrieval=t_retrieval,
            t_total=t_total,
        )
        self._log(result)
        return result

    def _log(self, r: PipelineResult) -> None:
        log.info("=" * 70)
        log.info(f"QUERY     : {r.query}")
        log.info(
            f"RETRIEVAL : {r.t_retrieval:.3f}s | LLM: {r.generation.latency_s:.3f}s | "
            f"Total: {r.t_total:.3f}s"
        )
        log.info(f"CHUNKS RECUPERADOS ({len(r.retrieved)}):")
        for i, rc in enumerate(r.retrieved, 1):
            log.info(
                f"  [{i}] score={rc.score:.4f} | fuente={rc.chunk.fuente} | "
                f"palabras {rc.chunk.inicio_palabra}-{rc.chunk.fin_palabra}"
            )
        log.info(f"PROMPT_ENVIADO:\n{r.generation.prompt}")
        log.info(f"RESPUESTA:\n{r.generation.respuesta}")
        log.info("=" * 70)
