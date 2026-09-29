"""
metrics.py -- calcula Precision@5, Recall@5, MRR, Faithfulness y Latencia
a partir de una hoja de evaluacion manual ya anotada (eval_sheet.md) y los
resultados crudos (results.jsonl) de evaluador.py.

Uso:
    python evaluation/metrics.py --results results/cosine/results.jsonl \
        --sheet results/cosine/eval_sheet.md
"""

import argparse
import json
import re
import statistics


def split_question_blocks(sheet_text: str) -> list[str]:
    parts = re.split(r"\n(?=## )", sheet_text)
    return [p for p in parts if p.startswith("## ")]


def parse_question_id(block: str) -> str:
    m = re.match(r"## (\S+) —", block)
    return m.group(1) if m else "?"


def parse_total_relevantes(block: str) -> int | None:
    m = re.search(r"Total de chunks relevantes en el corpus \(estimado.*?\):\**\s*(\d+)", block)
    return int(m.group(1)) if m else None


def parse_checked_ranks(table_text: str) -> tuple[list[int], int]:
    """Devuelve (ranks marcados como relevantes/respaldados, total de filas de datos).
    Parseo linea por linea (no regex multi-linea) para no confundir la fila
    separadora de Markdown (|---|---|) con una fila de datos."""
    checked = []
    total = 0
    for raw_line in table_text.splitlines():
        line = raw_line.strip()
        if not line.startswith("|") or not line.endswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        first, last = cells[0], cells[-1]
        if not re.fullmatch(r"\d+", first):
            continue  # salta encabezado ("Rank"/"#") y separador ("---")
        m = re.fullmatch(r"\[([ xX])\]", last)
        if not m:
            continue
        total += 1
        if m.group(1).lower() == "x":
            checked.append(int(first))
    return checked, total


def extract_table(block: str, section_title: str) -> str:
    m = re.search(rf"### {re.escape(section_title)}.*?\n(.*?)(?=\n###|\n---|\Z)", block, re.DOTALL)
    return m.group(1) if m else ""


def compute_question_metrics(block: str) -> dict:
    qid = parse_question_id(block)

    chunks_table = extract_table(block, "Chunks recuperados")
    relevant_ranks, n_chunks = parse_checked_ranks(chunks_table)
    precision_at_k = (len(relevant_ranks) / n_chunks) if n_chunks else None
    mrr = (1.0 / min(relevant_ranks)) if relevant_ranks else 0.0

    total_relevantes = parse_total_relevantes(block)
    recall_at_k = (len(relevant_ranks) / total_relevantes) if total_relevantes else None

    claims_table = extract_table(block, "Faithfulness — afirmaciones de la respuesta")
    backed_claims, n_claims = parse_checked_ranks(claims_table)
    faithfulness = (len(backed_claims) / n_claims) if n_claims else None

    return {
        "question_id": qid,
        "precision_at_5": precision_at_k,
        "recall_at_5": recall_at_k,
        "mrr": mrr,
        "faithfulness": faithfulness,
        "n_chunks_relevantes": len(relevant_ranks),
        "n_chunks_total": n_chunks,
        "n_claims_respaldadas": len(backed_claims),
        "n_claims_total": n_claims,
    }


def load_results(path: str) -> dict[str, dict]:
    out = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rec = json.loads(line)
                out[rec["question_id"]] = rec
    return out


def mean_or_none(values: list[float]) -> float | None:
    values = [v for v in values if v is not None]
    return round(statistics.mean(values), 4) if values else None


def main():
    parser = argparse.ArgumentParser(description="Calcula metricas desde una eval_sheet.md anotada")
    parser.add_argument("--results", required=True)
    parser.add_argument("--sheet", required=True)
    parser.add_argument("--out", default=None)
    args = parser.parse_args()

    out_path = args.out or args.sheet.replace("eval_sheet.md", "metrics.json")

    results = load_results(args.results)
    with open(args.sheet, "r", encoding="utf-8") as f:
        sheet_text = f.read()

    blocks = split_question_blocks(sheet_text)

    per_question = []
    for block in blocks:
        m = compute_question_metrics(block)
        rec = results.get(m["question_id"])
        if rec:
            m["t_retrieval_s"] = rec["t_retrieval_s"]
            m["t_generacion_s"] = rec["t_generacion_s"]
            m["t_total_s"] = rec["t_total_s"]
        per_question.append(m)

    latencias_totales = [q.get("t_total_s") for q in per_question if q.get("t_total_s") is not None]

    aggregate = {
        "n_preguntas_anotadas": len(per_question),
        "precision_at_5": mean_or_none([q["precision_at_5"] for q in per_question]),
        "recall_at_5": mean_or_none([q["recall_at_5"] for q in per_question]),
        "recall_at_5_cobertura": sum(1 for q in per_question if q["recall_at_5"] is not None),
        "mrr": mean_or_none([q["mrr"] for q in per_question]),
        "faithfulness": mean_or_none([q["faithfulness"] for q in per_question]),
        "faithfulness_cobertura": sum(1 for q in per_question if q["faithfulness"] is not None),
        "latencia_total_s_media": mean_or_none(latencias_totales),
        "latencia_total_s_max": max(latencias_totales) if latencias_totales else None,
    }

    output = {"aggregate": aggregate, "per_question": per_question}

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"Generado: {out_path}")
    print(json.dumps(aggregate, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
