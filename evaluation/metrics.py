"""
metrics.py -- calcula Precision@5, Recall@5, MRR, Faithfulness y Latencia
a partir de una hoja de evaluacion manual ya anotada (eval_sheet.md) y los
resultados crudos (results.jsonl) de evaluador.py.

Solo cuentan las preguntas con la casilla '**Anotada:** [x]'; las demas se
excluyen de los promedios (la latencia se calcula sobre todas, no requiere
anotacion).

Reglas de calculo (tambien quedan escritas en el metrics.json):
  - Las filas 'Fuentes:' de la tabla de afirmaciones no cuentan para Faithfulness.
  - Los chunks recuperados con texto identico (articulo duplicado en el corpus)
    cuentan una sola vez; el distinto es relevante si alguna copia esta marcada.
  - Las filas de tabla de varias lineas se leen completas; si alguna fila esta
    mal formada se descarta y se avisa.

Uso:
    python evaluation/metrics.py --results results/cosine/results.jsonl \
        --sheet results/cosine/eval_sheet.md
    python evaluation/metrics.py --results ... --sheet ... --status   # avance
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


def parse_anotada(block: str) -> bool | None:
    """True/False segun la casilla '**Anotada:** [x]'; None si la hoja no trae el marcador."""
    m = re.search(r"\*\*Anotada:\*\*\s*\[( |x|X)\]", block)
    if not m:
        return None
    return m.group(1).lower() == "x"


def parse_total_relevantes(block: str) -> int | None:
    m = re.search(r"Total de chunks relevantes en el corpus \(estimado.*?\):\**\s*(\d+)", block)
    return int(m.group(1)) if m else None


ROW_START = re.compile(r"^\|\s*\d+\s*\|")
SOURCES_LINE = re.compile(r"^[\s*_>\-]*fuentes?\b", re.IGNORECASE)


def parse_table_rows(table_text: str) -> tuple[list[tuple[int, str, bool]], int]:
    """Filas de datos de una tabla Markdown como (numero, texto, marcada), mas el
    numero de filas descartadas por estar mal formadas.

    Una fila puede ocupar varias lineas (una celda con viñetas o saltos de linea):
    se acumulan lineas hasta que la fila cierra con '|'. Solo se usan la primera
    celda (numero) y la ultima (casilla); el texto intermedio puede contener '|'."""
    rows: list[tuple[int, str, bool]] = []
    dropped = 0

    def flush(buf: str) -> None:
        nonlocal dropped
        cells = buf.strip().strip("|").split("|")
        first = cells[0].strip()
        if not re.fullmatch(r"\d+", first):
            return  # encabezado ("Rank"/"#") o separador ("---")
        m = re.fullmatch(r"\[([ xX])\]", cells[-1].strip()) if len(cells) >= 2 else None
        if not m:
            dropped += 1
            return
        rows.append((int(first), "|".join(cells[1:-1]).strip(), m.group(1).lower() == "x"))

    buf = None
    for raw in table_text.splitlines():
        line = raw.strip()
        if buf is None:
            if line.startswith("|"):
                buf = line
            else:
                continue
        else:
            if ROW_START.match(line):
                dropped += 1  # la fila anterior nunca cerro: se descarta y se avisa
                buf = line
            else:
                buf += "\n" + line
        if buf.endswith("|"):
            flush(buf)
            buf = None
    if buf is not None:
        dropped += 1
    return rows, dropped


def extract_table(block: str, section_title: str) -> str:
    m = re.search(rf"### {re.escape(section_title)}.*?\n(.*?)(?=\n###|\n---|\Z)", block, re.DOTALL)
    return m.group(1) if m else ""


def duplicate_groups(rec: dict | None, ranks: list[int]) -> dict[int, int]:
    """rank -> grupo; los chunks con texto identico (p. ej. un articulo duplicado en
    el corpus) comparten grupo y cuentan una sola vez."""
    texts = {}
    if rec:
        texts = {c["rank"]: c["texto"] for c in rec["chunks"]}
    first_seen: dict[str, int] = {}
    groups: dict[int, int] = {}
    for r in ranks:
        key = texts.get(r)
        if key is None:
            groups[r] = r
        else:
            groups[r] = first_seen.setdefault(key, r)
    return groups


def compute_question_metrics(block: str, rec: dict | None = None) -> dict:
    qid = parse_question_id(block)

    chunk_rows, dropped_chunks = parse_table_rows(extract_table(block, "Chunks recuperados"))
    ranks = [r for r, _, _ in chunk_rows]
    groups = duplicate_groups(rec, ranks)
    distinct = sorted(set(groups.values()))
    relevant_groups = {groups[r] for r, _, checked in chunk_rows if checked}
    n_distinct, n_relevant = len(distinct), len(relevant_groups)

    precision_at_k = (n_relevant / n_distinct) if n_distinct else None
    first_relevant = next((i for i, g in enumerate(distinct, 1) if g in relevant_groups), None)
    mrr = (1.0 / first_relevant) if first_relevant else 0.0

    total_relevantes = parse_total_relevantes(block)
    recall_at_k = (n_relevant / total_relevantes) if total_relevantes else None

    claim_rows, dropped_claims = parse_table_rows(
        extract_table(block, "Faithfulness — afirmaciones de la respuesta"))
    factual = [(n, t, c) for n, t, c in claim_rows if not SOURCES_LINE.match(t)]
    backed = sum(1 for _, _, c in factual if c)
    faithfulness = (backed / len(factual)) if factual else None

    return {
        "question_id": qid,
        "anotada": parse_anotada(block),
        "precision_at_5": precision_at_k,
        "recall_at_5": recall_at_k,
        "mrr": mrr,
        "faithfulness": faithfulness,
        "n_chunks_relevantes": n_relevant,
        "n_chunks_distintos": n_distinct,
        "n_chunks_total": len(chunk_rows),
        "n_claims_respaldadas": backed,
        "n_claims_total": len(factual),
        "n_filas_fuentes_excluidas": len(claim_rows) - len(factual),
        "filas_descartadas": dropped_chunks + dropped_claims,
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
    parser.add_argument("--status", action="store_true",
                        help="Solo lista que preguntas estan anotadas y cuales faltan")
    args = parser.parse_args()

    out_path = args.out or args.sheet.replace("eval_sheet.md", "metrics.json")

    results = load_results(args.results)
    with open(args.sheet, "r", encoding="utf-8") as f:
        sheet_text = f.read()

    blocks = split_question_blocks(sheet_text)
    all_questions = [compute_question_metrics(b, results.get(parse_question_id(b))) for b in blocks]

    has_markers = any(q["anotada"] is not None for q in all_questions)
    if not has_markers:
        print("AVISO: la hoja no trae la casilla '**Anotada:**'. Se tratan TODAS las "
              "preguntas como anotadas; las que no hayas revisado contaran como 0 y "
              "los promedios saldran sesgados. Regenera la hoja con eval_sheet.py.")
        for q in all_questions:
            q["anotada"] = True

    annotated_ids = [q["question_id"] for q in all_questions if q["anotada"]]
    pending_ids = [q["question_id"] for q in all_questions if not q["anotada"]]

    if args.status:
        print(f"Anotadas: {len(annotated_ids)}/{len(all_questions)}")
        print("Pendientes:", ", ".join(pending_ids) if pending_ids else "ninguna")
        return

    for q in all_questions:
        rec = results.get(q["question_id"])
        if rec:
            q["t_retrieval_s"] = rec["t_retrieval_s"]
            q["t_generacion_s"] = rec["t_generacion_s"]
            q["t_total_s"] = rec["t_total_s"]

    # La latencia no requiere anotacion: se calcula sobre todas las preguntas.
    latencias_totales = [q["t_total_s"] for q in all_questions if "t_total_s" in q]
    per_question = [q for q in all_questions if q["anotada"]]

    aggregate = {
        "n_preguntas_total": len(all_questions),
        "n_preguntas_anotadas": len(per_question),
        "preguntas_pendientes": pending_ids,
        "precision_at_5": mean_or_none([q["precision_at_5"] for q in per_question]),
        "recall_at_5": mean_or_none([q["recall_at_5"] for q in per_question]),
        "recall_at_5_cobertura": sum(1 for q in per_question if q["recall_at_5"] is not None),
        "mrr": mean_or_none([q["mrr"] for q in per_question]),
        "faithfulness": mean_or_none([q["faithfulness"] for q in per_question]),
        "faithfulness_cobertura": sum(1 for q in per_question if q["faithfulness"] is not None),
        "filas_descartadas_total": sum(q["filas_descartadas"] for q in per_question),
        "latencia_total_s_media": mean_or_none(latencias_totales),
        "latencia_total_s_max": max(latencias_totales) if latencias_totales else None,
    }

    if aggregate["filas_descartadas_total"]:
        bad = [q["question_id"] for q in per_question if q["filas_descartadas"]]
        print(f"AVISO: se descartaron filas mal formadas en {', '.join(bad)}; "
              "esas preguntas pueden tener metricas incompletas. Revisa las tablas.")

    output = {
        "reglas": [
            "Las filas 'Fuentes:' no cuentan como afirmaciones de Faithfulness.",
            "Los chunks con texto identico cuentan una sola vez (relevante si alguna copia esta marcada).",
            "El total estimado de Recall@5 se interpreta como chunks DISTINTOS.",
        ],
        "aggregate": aggregate,
        "per_question": per_question,
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"Generado: {out_path}")
    print(json.dumps(aggregate, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
