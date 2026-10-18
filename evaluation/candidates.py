"""
candidates.py -- para cada pregunta, lista los chunks DISTINTOS del corpus que
mencionan sus puntos clave. Sirve para estimar con datos el campo "Total de
chunks relevantes en el corpus" (Recall@5), en vez de estimarlo mirando solo el
top-5. Es una lista de CANDIDATOS: tu criterio decide cuantos son realmente
relevantes.

Uso:
    python evaluation/candidates.py                    # baseline (ventana 300/50)
    python evaluation/candidates.py --chunks paragraph # chunks de la Config 1
    python evaluation/candidates.py --question F5 --top 15
Escribe results/candidatos_<chunks>.md
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from evaluation.keypoints import (
    find_candidates, keypoint_hits, load_chunk_set, normalize,
    significant_tokens, split_keypoints,
)
from evaluation.schema import load_questions


def snippet(text: str, puntos_clave: list[str], width: int = 160) -> str:
    clean = text.replace("​", "").replace("\n", " ")
    norm = normalize(clean)
    for kp in split_keypoints(puntos_clave):
        for tok in significant_tokens(kp):
            i = norm.find(tok)
            if i >= 0:
                return "..." + clean[max(0, i - width // 2): i + width // 2].strip() + "..."
    return clean[:width] + "..."


def main():
    parser = argparse.ArgumentParser(description="Chunks candidatos a relevantes por pregunta")
    parser.add_argument("--chunks", choices=["baseline", "paragraph"], default="baseline")
    parser.add_argument("--questions", default="evaluation/questions.json")
    parser.add_argument("--question", default=None, help="Solo esta pregunta (p. ej. F5)")
    parser.add_argument("--top", type=int, default=8, help="Candidatos a listar por pregunta")
    parser.add_argument("--out", default=None)
    args = parser.parse_args()

    chunks = load_chunk_set(args.chunks)
    out_path = args.out or f"results/candidatos_{args.chunks}.md"
    questions = [q for q in load_questions(args.questions) if not args.question or q.id == args.question]

    lines = [
        f"# Chunks candidatos por pregunta ({args.chunks}, {len(chunks)} chunks)\n",
        "Ayuda para estimar el total de chunks relevantes (Recall@5). Los candidatos son "
        "chunks distintos (sin copias exactas) que mencionan algun punto clave; un chunk "
        "puede mencionarlo sin ser relevante. Cuenta solo los que realmente lo son.\n",
        "| Pregunta | con >=1 punto clave | con >=2 |",
        "|---|---|---|",
    ]
    detail = []
    for q in questions:
        if not q.puntos_clave:
            lines.append(f"| {q.id} (trampa) | - | - |")
            detail.append(f"## {q.id} — {q.pregunta}\n\nPregunta trampa: no tiene puntos clave que buscar.\n")
            continue
        cands = find_candidates(chunks, q.puntos_clave)
        n2 = sum(1 for c in cands if len(c["hits"]) >= 2)
        lines.append(f"| {q.id} | {len(cands)} | {n2} |")
        detail.append(f"## {q.id} — {q.pregunta}\n")
        detail.append(f"Puntos clave: {'; '.join(q.puntos_clave)}\n")
        per_kp = {kp: sum(1 for c in chunks if kp in keypoint_hits(c['texto'], [kp])) for kp in split_keypoints(q.puntos_clave)}
        detail.append("Chunks (con copias) por punto clave: " + ", ".join(f"{k}: {v}" for k, v in per_kp.items()) + "\n")
        for c in cands[: args.top]:
            detail.append(f"- **{c['fuente']}** `{c['id']}` — {len(c['hits'])} punto(s) clave: {', '.join(c['hits'])}\n"
                          f"  > {snippet(c['texto'], q.puntos_clave)}")
        detail.append("")

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n\n" + "\n".join(detail))
    print(f"Generado: {out_path}")
    for row in lines[4:]:
        print(row.encode("ascii", "replace").decode())


if __name__ == "__main__":
    main()
