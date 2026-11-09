"""
evaluador.py -- corre el conjunto completo de preguntas (evaluation/questions.json)
contra una configuracion RAG y guarda los resultados crudos en JSONL.

Uso:
    python evaluation/evaluador.py --config configs/cosine.yaml
    python evaluation/evaluador.py --config configs/bm25.yaml --out results/bm25
"""

import argparse
import json
import logging
import os
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from evaluation.schema import Question, load_questions
from src.interfaces import GenerationResult, PipelineResult
from src.config import build_pipeline, load_chunks_for, load_config

log = logging.getLogger(__name__)


def setup_logging(out_dir: str) -> None:
    os.makedirs(out_dir, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(f"{out_dir}/evaluador_{ts}.log", encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )
    # Cada carga del modelo de embeddings dispara decenas de lineas HTTP INFO
    # (verificacion de cache contra Hugging Face) que no aportan al log real.
    for noisy in ("httpx", "httpcore", "huggingface_hub", "sentence_transformers", "urllib3", "filelock"):
        logging.getLogger(noisy).setLevel(logging.WARNING)


def result_to_record(config_name: str, question: Question, result) -> dict:
    return {
        "question_id": question.id,
        "tipo": question.tipo,
        "is_trap": question.is_trap,
        "puntos_clave": question.puntos_clave,
        "config": config_name,
        "query": result.query,
        "chunks": [
            {
                "rank": i,
                "score": rc.score,
                "chunk_id": rc.chunk.id,
                "fuente": rc.chunk.fuente,
                "inicio_palabra": rc.chunk.inicio_palabra,
                "fin_palabra": rc.chunk.fin_palabra,
                "texto": rc.chunk.texto,
            }
            for i, rc in enumerate(result.retrieved, 1)
        ],
        "prompt": result.generation.prompt,
        "respuesta": result.generation.respuesta,
        "t_retrieval_s": result.t_retrieval,
        "t_generacion_s": result.generation.latency_s,
        "t_total_s": result.t_total,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def main():
    parser = argparse.ArgumentParser(description="Corre questions.json contra una config RAG.")
    parser.add_argument("--config", required=True, help="Ruta al YAML de configuracion (configs/cosine.yaml)")
    parser.add_argument("--questions", default="evaluation/questions.json")
    parser.add_argument("--out", default=None, help="Directorio de salida (default: results/<nombre_config>)")
    parser.add_argument("--retrieval-only", action="store_true",
                        help="Solo recuperacion, sin LLM (no necesita Ollama). Escribe por omision en "
                             "results/retrieval/<config> para no pisar resultados con generacion")
    parser.add_argument("--top-k", type=int, default=None,
                        help="Sobrescribe top_k del YAML (p. ej. 50 para evaluar a presupuesto de contexto igual)")
    args = parser.parse_args()

    cfg = load_config(args.config)
    if args.top_k:
        cfg.top_k = args.top_k
    config_slug = os.path.splitext(os.path.basename(args.config))[0]
    out_dir = args.out or (f"results/retrieval/{config_slug}" if args.retrieval_only else f"results/{config_slug}")
    setup_logging(out_dir)

    log.info(f"=== evaluador.py -- config: {cfg.nombre} ({args.config}) ===")

    questions = load_questions(args.questions)
    log.info(f"{len(questions)} preguntas cargadas desde {args.questions}")

    pipeline = build_pipeline(cfg)
    chunks = load_chunks_for(cfg, pipeline.chunker)
    log.info(f"Indexando {len(chunks)} chunks...")
    pipeline.index(chunks)

    out_path = f"{out_dir}/results.jsonl"
    t0 = time.time()
    with open(out_path, "w", encoding="utf-8") as f:
        for i, q in enumerate(questions, 1):
            log.info(f"[{i}/{len(questions)}] {q.id} ({q.tipo}): {q.pregunta}")
            if args.retrieval_only:
                retrieved, t_ret = pipeline.retrieve(q.pregunta, top_k=cfg.top_k)
                result = PipelineResult(
                    query=q.pregunta, retrieved=retrieved,
                    generation=GenerationResult(respuesta="", prompt="", latency_s=0.0),
                    t_retrieval=t_ret, t_total=t_ret,
                )
            else:
                result = pipeline.answer(q.pregunta, top_k=cfg.top_k)
            record = result_to_record(config_slug, q, result)
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
            f.flush()
            log.info(
                f"    retrieval={result.t_retrieval:.3f}s  "
                f"generacion={result.generation.latency_s:.3f}s  "
                f"total={result.t_total:.3f}s"
            )

    t_total = time.time() - t0
    log.info(f"=== Listo: {len(questions)} preguntas en {t_total:.1f}s -> {out_path} ===")


if __name__ == "__main__":
    main()
