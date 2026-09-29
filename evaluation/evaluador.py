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
from src.config import build_pipeline, load_config
from src.pipeline import load_chunks

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
                "fuente": rc.chunk.fuente,
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
    args = parser.parse_args()

    cfg = load_config(args.config)
    config_slug = os.path.splitext(os.path.basename(args.config))[0]
    out_dir = args.out or f"results/{config_slug}"
    setup_logging(out_dir)

    log.info(f"=== evaluador.py -- config: {cfg.nombre} ({args.config}) ===")

    questions = load_questions(args.questions)
    log.info(f"{len(questions)} preguntas cargadas desde {args.questions}")

    pipeline = build_pipeline(cfg)
    chunks = load_chunks()
    log.info(f"Indexando {len(chunks)} chunks...")
    pipeline.index(chunks)

    out_path = f"{out_dir}/results.jsonl"
    t0 = time.time()
    with open(out_path, "w", encoding="utf-8") as f:
        for i, q in enumerate(questions, 1):
            log.info(f"[{i}/{len(questions)}] {q.id} ({q.tipo}): {q.pregunta}")
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
