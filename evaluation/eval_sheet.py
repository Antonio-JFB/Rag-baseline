"""
eval_sheet.py -- genera la hoja de evaluacion manual (eval_sheet.md) a partir
de resultados crudos (results.jsonl) producidos por evaluador.py.

Uso:
    python evaluation/eval_sheet.py --results results/cosine/results.jsonl
"""

import argparse
import json
import re


def split_claims(respuesta: str) -> list[str]:
    """Divide la respuesta en oraciones/afirmaciones para la tabla de Faithfulness.
    Heuristica simple (split por . ! ?) -- suficiente como ayuda de anotacion,
    no pretende ser un splitter de oraciones perfecto."""
    partes = re.split(r"(?<=[.!?])\s+", respuesta.strip())
    return [p.strip() for p in partes if len(p.strip()) > 3]


def render_question(record: dict) -> str:
    lines = []
    lines.append(f"## {record['question_id']} — {record['query']}")
    lines.append("")
    lines.append(f"**Tipo:** {record['tipo']}" + ("  (pregunta trampa)" if record["is_trap"] else ""))
    if record["puntos_clave"]:
        lines.append(f"**Puntos clave esperados:** {'; '.join(record['puntos_clave'])}")
    lines.append(
        f"**Tiempos:** retrieval={record['t_retrieval_s']:.3f}s · "
        f"generación={record['t_generacion_s']:.3f}s · total={record['t_total_s']:.3f}s"
    )
    lines.append("")
    lines.append("**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_")
    lines.append("")
    lines.append("**Respuesta del sistema:**")
    lines.append(f"> {record['respuesta'].strip()}")
    lines.append("")
    lines.append("**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___")
    lines.append("")
    lines.append("### Chunks recuperados")
    lines.append("_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._")
    lines.append("")
    lines.append("| Rank | Score | Fuente | Relevante |")
    lines.append("|------|-------|--------|-----------|")
    for c in record["chunks"]:
        preview = c["texto"][:100].strip().replace("\n", " ") + "..."
        lines.append(f"| {c['rank']} | {c['score']:.4f} | {c['fuente']} — _{preview}_ | [ ] |")
    lines.append("")
    lines.append("### Faithfulness — afirmaciones de la respuesta")
    lines.append("_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._")
    lines.append("")
    lines.append("| # | Afirmación | Respaldada |")
    lines.append("|---|------------|------------|")
    claims = split_claims(record["respuesta"])
    if not claims:
        lines.append("| - | _(sin afirmaciones verificables)_ | — |")
    for i, claim in enumerate(claims, 1):
        lines.append(f"| {i} | {claim} | [ ] |")
    lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Genera eval_sheet.md desde results.jsonl")
    parser.add_argument("--results", required=True)
    parser.add_argument("--out", default=None)
    args = parser.parse_args()

    out_path = args.out or args.results.replace("results.jsonl", "eval_sheet.md")

    records = []
    with open(args.results, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))

    header = (
        "# Hoja de evaluación manual\n\n"
        "Protocolo: para cada pregunta, (1) marca qué chunks recuperados son "
        "genuinamente relevantes para responderla -- usa los **puntos clave "
        "esperados** como referencia, no tu propio conocimiento de historia; "
        "(2) marca qué afirmaciones de la respuesta están respaldadas por el "
        "texto de los chunks recuperados (Faithfulness) -- si una afirmación "
        "es correcta históricamente pero no aparece en los chunks, cuenta como "
        "**no respaldada**, porque el sistema no la pudo haber sacado del "
        "contexto. Para preguntas trampa, la respuesta correcta es que el "
        "sistema declare que no encontró la información -- marca eso como "
        "relevante/respaldado si ocurre así. Al terminar cada pregunta, marca "
        "la casilla **Anotada** (así `metrics.py` sabe cuáles ya revisaste y no "
        "confunde una pregunta pendiente con una donde todo resultó irrelevante).\n\n"
        f"Total de preguntas: {len(records)}\n\n---\n\n"
    )

    body = "\n".join(render_question(r) for r in records)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(header + body)

    print(f"Generado: {out_path} ({len(records)} preguntas)")


if __name__ == "__main__":
    main()
