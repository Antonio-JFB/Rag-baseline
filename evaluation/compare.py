"""
compare.py -- compara dos configuraciones lado a lado a partir de sus hojas de
evaluacion ya anotadas: agregados, desglose por tipo de pregunta y por pregunta.

Solo se comparan las preguntas anotadas en AMBAS configuraciones (comparacion
pareada); el resto se lista como no comparable, para no mezclar poblaciones.
Usa exactamente las mismas reglas de calculo que metrics.py.

Uso:
    python evaluation/compare.py cosine cosine_paragraph
    python evaluation/compare.py cosine hybrid --base results
Escribe results/comparacion_<A>_vs_<B>.md
"""

import argparse
import json
import os
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from evaluation.metrics import (
    compute_question_metrics, load_results, parse_question_id, split_question_blocks,
)

METRICS = [("precision_at_5", "Precision@5"), ("mrr", "MRR"),
           ("recall_at_5", "Recall@5"), ("faithfulness", "Faithfulness")]
TYPE_ORDER = ["factual", "causalidad", "comparativa", "relacional", "multihop", "trampa"]
BIG = 0.2  # diferencia que se resalta


def load_config(base: str, name: str) -> tuple[dict, dict, bool]:
    """(metricas por pregunta anotada, registros de results, ¿la hoja trae el marcador?)"""
    results = load_results(f"{base}/{name}/results.jsonl")
    with open(f"{base}/{name}/eval_sheet.md", "r", encoding="utf-8") as f:
        blocks = split_question_blocks(f.read())
    all_q = [compute_question_metrics(b, results.get(parse_question_id(b))) for b in blocks]
    has_markers = any(q["anotada"] is not None for q in all_q)
    annotated = {q["question_id"]: q for q in all_q if q["anotada"]}
    return annotated, results, has_markers


def mean(values):
    values = [v for v in values if v is not None]
    return statistics.mean(values) if values else None


def fmt(v, nd=2):
    return "-" if v is None else f"{v:.{nd}f}"


def delta(a, b):
    if a is None or b is None:
        return "-"
    d = b - a
    text = f"{d:+.2f}"
    return f"**{text}**" if abs(d) >= BIG else text


def question_types(path: str = "evaluation/questions.json") -> dict[str, str]:
    from evaluation.schema import load_questions
    return {q.id: q.tipo for q in load_questions(path)}


def latency_row(results: dict) -> tuple[float | None, float | None, float | None]:
    """mediana, maximo y arranque en frio (primera pregunta) de la latencia total."""
    ordered = list(results.values())
    if not ordered:
        return None, None, None
    totals = [r["t_total_s"] for r in ordered]
    return statistics.median(totals), max(totals), totals[0]


def main():
    parser = argparse.ArgumentParser(description="Compara dos configuraciones anotadas")
    parser.add_argument("a", help="configuracion A (p. ej. cosine); es la referencia")
    parser.add_argument("b", help="configuracion B (p. ej. cosine_paragraph)")
    parser.add_argument("--base", default="results")
    parser.add_argument("--out", default=None)
    args = parser.parse_args()

    qa, ra, ma = load_config(args.base, args.a)
    qb, rb, mb = load_config(args.base, args.b)
    for name, has in ((args.a, ma), (args.b, mb)):
        if not has:
            print(f"AVISO: la hoja de {name} no trae la casilla 'Anotada'; no se puede saber cuales "
                  "estan anotadas. Regenerala con eval_sheet.py antes de comparar.")
            return

    paired = sorted(set(qa) & set(qb), key=lambda q: list(ra).index(q) if q in ra else 99)
    types = question_types()
    out = [f"# Comparación: {args.a} (A, referencia) vs {args.b} (B)\n",
           f"Anotadas: A = {len(qa)}/20, B = {len(qb)}/20. **Preguntas comparables (anotadas en ambas): {len(paired)}.**\n"]

    if not paired:
        out.append("No hay preguntas anotadas en ambas configuraciones: todavía no se puede comparar.\n")
    else:
        out += ["Δ = B − A. En **negritas**, diferencias de 0.20 o más. Mismas reglas de cálculo que `metrics.py` "
                "(la fila «Fuentes:» no cuenta; las copias exactas cuentan una vez). Con pocas preguntas, "
                "una diferencia puede ser ruido de una sola pregunta.\n",
                "## Agregados (sobre las preguntas comparables)\n",
                "| Métrica | A | B | Δ | n con dato (A/B) |", "|---|---|---|---|---|"]
        for key, label in METRICS:
            va = [qa[q][key] for q in paired]
            vb = [qb[q][key] for q in paired]
            ma_, mb_ = mean(va), mean(vb)
            out.append(f"| {label} | {fmt(ma_)} | {fmt(mb_)} | {delta(ma_, mb_)} | "
                       f"{sum(v is not None for v in va)}/{sum(v is not None for v in vb)} |")
        out.append("")

        out += ["## Por tipo de pregunta\n", "| Tipo | n | P@5 A→B | MRR A→B | Faithfulness A→B |", "|---|---|---|---|---|"]
        for t in TYPE_ORDER:
            ids = [q for q in paired if types.get(q) == t]
            if not ids:
                continue
            cells = []
            for key in ("precision_at_5", "mrr", "faithfulness"):
                x, y = mean([qa[q][key] for q in ids]), mean([qb[q][key] for q in ids])
                cells.append(f"{fmt(x)} → {fmt(y)} ({delta(x, y)})")
            out.append(f"| {t} | {len(ids)} | " + " | ".join(cells) + " |")
        out.append("")

        out += ["## Por pregunta\n",
                "| Pregunta | Tipo | P@5 A | P@5 B | Δ | MRR A | MRR B | Δ | Faith A | Faith B | Δ |",
                "|---|---|---|---|---|---|---|---|---|---|---|"]
        for q in paired:
            row = [q, types.get(q, "?")]
            for key in ("precision_at_5", "mrr", "faithfulness"):
                x, y = qa[q][key], qb[q][key]
                row += [fmt(x), fmt(y), delta(x, y)]
            out.append("| " + " | ".join(row) + " |")
        out.append("")

        better = [q for q in paired if (qb[q]["precision_at_5"] or 0) - (qa[q]["precision_at_5"] or 0) >= BIG]
        worse = [q for q in paired if (qa[q]["precision_at_5"] or 0) - (qb[q]["precision_at_5"] or 0) >= BIG]
        out += ["## Dónde cambia el retrieval (Precision@5, |Δ| ≥ 0.20)\n",
                f"- B mejora a A en: {', '.join(better) if better else 'ninguna'}",
                f"- B empeora a A en: {', '.join(worse) if worse else 'ninguna'}", ""]

    only_a = sorted(set(qa) - set(qb))
    only_b = sorted(set(qb) - set(qa))
    if only_a or only_b:
        out += ["## No comparables\n",
                f"- Anotadas solo en A: {', '.join(only_a) if only_a else '-'}",
                f"- Anotadas solo en B: {', '.join(only_b) if only_b else '-'}", ""]

    out += ["## Latencia total (todas las preguntas, no requiere anotación)\n",
            "| | Mediana | Máximo | Primera pregunta (arranque en frío) |", "|---|---|---|---|"]
    for name, res in ((args.a, ra), (args.b, rb)):
        med, mx, cold = latency_row(res)
        out.append(f"| {name} | {fmt(med, 1)} s | {fmt(mx, 1)} s | {fmt(cold, 1)} s |")
    out.append("\nLa media se distorsiona por el arranque en frío de Ollama; usa la mediana.\n")

    out_path = args.out or f"{args.base}/comparacion_{args.a}_vs_{args.b}.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"Generado: {out_path} | comparables: {len(paired)}")


if __name__ == "__main__":
    main()
