"""
eval_sheet.py -- genera la hoja de evaluacion manual (eval_sheet.md) a partir
de resultados crudos (results.jsonl) producidos por evaluador.py.

ATENCION: sobrescribe la hoja de destino. Si ya empezaste a anotar una hoja, no
vuelvas a generarla (o usa --out para escribir en otro archivo).

Uso:
    python evaluation/eval_sheet.py --results results/bm25/results.jsonl
    python evaluation/eval_sheet.py --results ... --out otra_hoja.md
"""

import argparse
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from evaluation.keypoints import find_candidates, keypoint_hits, load_chunk_set

PREVIEW_CHARS = 300
ABBREVIATIONS = {
    "dr", "dra", "sr", "sra", "srta", "lic", "ing", "gral", "gen", "cnel", "col", "cap",
    "vs", "num", "pag", "aprox", "av", "ed", "vol", "tel", "fig", "no", "pp",
    "a", "n", "e", "c", "d",
}
SOURCES_BLOCK = re.compile(r"(?im)^[\s*_>\-]*fuentes?\b.*")
BULLET = re.compile(r"^\s*[*\-•]\s+")


def split_sentences(text: str) -> list[str]:
    """Parte en oraciones sin cortar en abreviaturas ('a. n. e.') ni iniciales ('Francisco I. Madero')."""
    parts, start = [], 0
    for m in re.finditer(r"([.!?]+)(\s+)", text):
        end, nxt = m.end(1), text[m.end():m.end() + 1]
        if not nxt or nxt.islower():
            continue
        if m.group(1) == ".":
            tok = re.findall(r"(\w+)$", text[start:end - 1])
            if tok and (tok[-1].lower() in ABBREVIATIONS or (len(tok[-1]) == 1 and tok[-1].isalpha())):
                continue
        parts.append(text[start:end].strip())
        start = m.end()
    parts.append(text[start:].strip())
    return [p for p in parts if p]


def split_claims(respuesta: str) -> list[str]:
    """Afirmaciones a verificar (Faithfulness): una por oracion o viñeta. Se omiten el
    bloque 'Fuentes:' (no es una afirmacion) y las lineas que solo introducen una lista
    (terminan en ':'). Cada afirmacion queda en una sola linea para no romper la tabla."""
    m = SOURCES_BLOCK.search(respuesta)
    body = respuesta[: m.start()] if m else respuesta
    claims = []
    for line in body.splitlines():
        line = BULLET.sub("", line).strip()
        if not line or line.endswith(":"):
            continue
        for sent in split_sentences(line):
            sent = re.sub(r"\s+", " ", sent).replace("|", "/").strip()
            if len(sent) > 3:
                claims.append(sent)
    return claims


def clean_cell(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("​", "")).replace("|", "/").strip()


def render_question(record: dict, chunk_set: list[dict] | None) -> str:
    pk = record["puntos_clave"]
    lines = [f"## {record['question_id']} — {record['query']}", ""]
    lines.append(f"**Tipo:** {record['tipo']}" + ("  (pregunta trampa)" if record["is_trap"] else ""))
    if pk:
        lines.append(f"**Puntos clave esperados:** {'; '.join(pk)}")
    lines.append(
        f"**Tiempos:** retrieval={record['t_retrieval_s']:.3f}s · "
        f"generación={record['t_generacion_s']:.3f}s · total={record['t_total_s']:.3f}s"
    )
    lines += ["", "**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_", ""]
    lines.append("**Respuesta del sistema:**")
    lines += [f"> {ln}" if ln.strip() else ">" for ln in record["respuesta"].strip().splitlines()]
    lines.append("")
    if pk and chunk_set is not None:
        cands = find_candidates(chunk_set, pk)
        n2 = sum(1 for c in cands if len(c["hits"]) >= 2)
        lines.append(
            f"_Ayuda para Recall: {len(cands)} chunks distintos del corpus mencionan al menos un punto clave "
            f"({n2} mencionan 2 o más); detalle con `python evaluation/candidates.py --question {record['question_id']}`. "
            "Cuenta solo los realmente relevantes y sin copias._"
        )
        lines.append("")
    lines.append("**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___")
    lines += ["", "### Chunks recuperados",
              "_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. "
              "La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._", ""]
    lines.append("| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |")
    lines.append("|------|-------|-----------------------|------------------------|-----------|")
    seen: dict[str, int] = {}
    for c in record["chunks"]:
        key = hashlib.md5(c["texto"].encode("utf-8")).hexdigest()
        dup = seen.setdefault(key, c["rank"])
        note = f" **(copia exacta del rank {dup}: cuenta una sola vez)**" if dup != c["rank"] else ""
        preview = clean_cell(c["texto"])[:PREVIEW_CHARS] + "..."
        if pk:
            hits = keypoint_hits(c["texto"], pk)
            present = ", ".join(clean_cell(h) for h in hits) if hits else "ninguno"
        else:
            present = "—"
        lines.append(f"| {c['rank']} | {c['score']:.4f} | {clean_cell(c['fuente'])}{note} — _{preview}_ | {present} | [ ] |")
    lines += ["", "### Faithfulness — afirmaciones de la respuesta",
              "_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. "
              "El bloque «Fuentes:» no se evalúa._", ""]
    lines.append("| # | Afirmación | Respaldada |")
    lines.append("|---|------------|------------|")
    claims = split_claims(record["respuesta"])
    if not claims:
        lines.append("| - | _(sin afirmaciones verificables)_ | — |")
    for i, claim in enumerate(claims, 1):
        lines.append(f"| {i} | {claim} | [ ] |")
    lines += ["", "---", ""]
    return "\n".join(lines)


HEADER = (
    "# Hoja de evaluación manual\n\n"
    "Protocolo: para cada pregunta, (1) marca qué chunks recuperados son genuinamente "
    "relevantes para responderla -- usa los **puntos clave esperados** como referencia, "
    "no tu propio conocimiento de historia; (2) marca qué afirmaciones de la respuesta "
    "están respaldadas por el texto de los chunks recuperados (Faithfulness) -- si una "
    "afirmación es correcta históricamente pero no aparece en los chunks, cuenta como "
    "**no respaldada**, porque el sistema no la pudo haber sacado del contexto. Para "
    "preguntas trampa, la respuesta correcta es que el sistema declare que no encontró "
    "la información. Al terminar cada pregunta, marca la casilla **Anotada**.\n\n"
    "Reglas de la herramienta (para que `metrics.py` cuente igual en todas las configuraciones):\n"
    "- La vista previa de cada chunk es parcial (300 caracteres). Si la decisión depende "
    "del resto del texto, léelo completo en `results.jsonl` antes de marcar.\n"
    "- «Puntos clave presentes» es una ayuda automática, no decide la relevancia: un chunk "
    "puede mencionar un punto clave sin ayudar a responder, o ayudar sin mencionarlo literalmente.\n"
    "- Los chunks con texto idéntico (copias) cuentan una sola vez; no hace falta marcar la copia.\n"
    "- El bloque «Fuentes:» de la respuesta no es una afirmación y no se evalúa.\n"
    "- El «Total de chunks relevantes en el corpus» debe contar chunks distintos. Usa la línea "
    "de ayuda de cada pregunta y `python evaluation/candidates.py` en lugar de estimarlo solo con el top-5.\n\n"
)


def main():
    parser = argparse.ArgumentParser(description="Genera eval_sheet.md desde results.jsonl")
    parser.add_argument("--results", required=True)
    parser.add_argument("--out", default=None)
    parser.add_argument("--chunks", choices=["baseline", "paragraph", "none"], default=None,
                        help="Conjunto de chunks del corpus para la ayuda de Recall "
                             "(por omision se deduce del nombre de la configuracion)")
    args = parser.parse_args()

    out_path = args.out or args.results.replace("results.jsonl", "eval_sheet.md")

    records = []
    with open(args.results, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))

    kind = args.chunks or ("paragraph" if "paragraph" in records[0]["config"] else "baseline")
    chunk_set = None if kind == "none" else load_chunk_set(kind)

    body = "\n".join(render_question(r, chunk_set) for r in records)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(HEADER + f"Total de preguntas: {len(records)}\n\n---\n\n" + body)

    print(f"Generado: {out_path} ({len(records)} preguntas; ayuda de Recall sobre chunks '{kind}')")


if __name__ == "__main__":
    main()
