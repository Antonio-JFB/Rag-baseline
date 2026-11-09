"""
pln_metrics.py -- metricas, estadistica y reporte del experimento de PLN (solo recuperacion).

Dos juegos de metricas, siempre etiquetados:

  PROXY (automatico, sin anotar): cobertura de puntos clave de questions.json en los chunks
        recuperados. Es una aproximacion heuristica (coincidencia de tokens); sirve para
        tener resultados provisionales y para validar el pipeline, NO sustituye el juicio humano.
  HUMANO (sobre results/pln/anotacion_evidencia.md): evidencia marcada por oracion.
        Un chunk es relevante si CUBRE (>= 50 % de sus palabras) alguna oracion de evidencia.

Reglas (las mismas para las seis configuraciones):
  - Se evaluan chunks DISTINTOS del top-5: dos chunks con el mismo contenido (articulo duplicado)
    cuentan una vez; el numero de huecos perdidos por duplicados se reporta aparte.
  - Solo preguntas NO trampa y (para HUMANO) anotadas y con al menos una evidencia.
  - Intervalos de confianza: bootstrap percentil sobre preguntas (10 000 remuestreos, semilla fija).
  - Contrastes: diferencia pareada por pregunta, IC bootstrap y prueba de permutacion por cambio de
    signo (exacta si n <= 20); correccion de Holm sobre los contrastes planeados (metrica primaria).

Uso:
    python evaluation/pln_metrics.py
    python evaluation/pln_metrics.py --annotation results/pln/anotacion_evidencia.md --determinism results/pln/run2
"""

import argparse
import json
import math
import os
import re
import sys
from itertools import product

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from evaluation.evidence import EvidenceIndex, corpus_manifest
from evaluation.keypoints import keypoint_hits, significant_tokens, split_keypoints
from evaluation.pln_pool import CONFIGS, load_runs
from evaluation.schema import load_questions

OUT_DIR = "results/pln"
SEED = 12345
B = 10_000

LABEL = {
    "cosine": "Densa (baseline 300/50)",
    "cosine_paragraph": "Densa + párrafos (≤85 pal.)",
    "cosine_fixed64": "Densa + ventana 64 (control)",
    "bm25": "BM25 simple",
    "bm25_lemma": "BM25 + lemas + stopwords",
    "hybrid": "Híbrida RRF (denso + BM25 simple)",
}

# Contrastes planeados: (id, A, B, hipotesis). Diferencia = A - B.
CONTRASTS = [
    ("H1", "bm25_lemma", "bm25", "H1: lematizar + quitar palabras vacías ayuda a BM25"),
    ("H2a", "cosine_paragraph", "cosine", "H2: efecto total del chunking por párrafos"),
    ("H2b", "cosine_fixed64", "cosine", "H2: efecto del tamaño solo (ventana 64 vs 300)"),
    ("H2c", "cosine_paragraph", "cosine_fixed64", "H2: efecto de respetar párrafos a tamaño similar"),
    ("H3", "bm25", "cosine", "H3: léxica simple vs. densa (mismos chunks)"),
    ("Hy1", "hybrid", "cosine", "Híbrida vs. densa"),
    ("Hy2", "hybrid", "bm25", "Híbrida vs. BM25 simple"),
]

PRIMARY = {"humano": "recall", "proxy": "kp_cov"}
METRICS_HUMANO = [("p5", "P@5"), ("hit", "Hit@5"), ("mrr", "MRR"), ("recall", "Recall@5 (evidencia)"),
                  ("dens", "Densidad de evidencia")]
METRICS_PROXY = [("kp_cov", "Cobertura de puntos clave"), ("kp_mrr", "MRR (≥50 % puntos clave)")]


# ----------------------------------------------------------------------------- anotacion

def parse_annotation(path: str) -> dict[str, dict]:
    """{question_id: {'anotada': bool, 'evidencia': set(sid), 'filas': n}}"""
    out: dict[str, dict] = {}
    if not os.path.exists(path):
        return out
    text = open(path, encoding="utf-8").read()
    for block in re.split(r"(?m)^## ", text)[1:]:
        qid = block.split()[0]
        anot = bool(re.search(r"\*\*Anotada:\*\*\s*\[[xX]\]", block))
        ev, rows = set(), 0
        for line in block.splitlines():
            if not re.match(r"^\|\s*\d+\s*\|", line):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 3:
                continue
            rows += 1
            if re.fullmatch(r"\[[xX]\]", cells[1]):
                ev.add(cells[-1])
        out[qid] = {"anotada": anot, "evidencia": ev, "filas": rows}
    return out


# ----------------------------------------------------------------------------- metricas por pregunta

def distinct_chunks(rec: dict, ev: EvidenceIndex) -> tuple[list[dict], int]:
    seen, out = set(), []
    for ch in rec["chunks"]:
        k = ev.chunk_key(ch)
        if k not in seen:
            seen.add(k)
            out.append(ch)
    return out, len(rec["chunks"]) - len(out)


def proxy_metrics(chunks: list[dict], q) -> dict:
    n_valid = sum(1 for kp in split_keypoints(q.puntos_clave) if significant_tokens(kp))
    if n_valid == 0:
        return {}
    union = " ".join(c["texto"] for c in chunks)
    cov = len(keypoint_hits(union, q.puntos_clave)) / n_valid
    need = max(1, math.ceil(0.5 * n_valid))
    mrr = 0.0
    for rank, c in enumerate(chunks, 1):
        if len(keypoint_hits(c["texto"], q.puntos_clave)) >= need:
            mrr = 1.0 / rank
            break
    return {"kp_cov": cov, "kp_mrr": mrr}


def human_metrics(chunks: list[dict], evid: set[str], ev: EvidenceIndex) -> dict:
    rel_flags = [any(ev.covered(c, sid) for sid in evid) for c in chunks]
    n = len(chunks)
    p5 = sum(rel_flags) / n if n else 0.0
    first = next((i for i, f in enumerate(rel_flags, 1) if f), None)
    covered = {sid for sid in evid if any(ev.covered(c, sid) for c in chunks)}
    # densidad: palabras de evidencia dentro de lo recuperado / palabras recuperadas (union)
    retrieved: dict[str, set] = {}
    for c in chunks:
        art, i0, i1 = ev.chunk_key(c)
        retrieved.setdefault(art, set()).update(range(i0, i1))
    ev_words: dict[str, set] = {}
    for sid in evid:
        s = ev.by_id[sid]
        ev_words.setdefault(s.articulo, set()).update(range(s.inicio, s.fin))
    n_ret = sum(len(v) for v in retrieved.values())
    n_hit = sum(len(retrieved.get(a, set()) & w) for a, w in ev_words.items())
    return {"p5": p5, "hit": 1.0 if first else 0.0, "mrr": 1.0 / first if first else 0.0,
            "recall": len(covered) / len(evid), "dens": n_hit / n_ret if n_ret else 0.0}


# ----------------------------------------------------------------------------- estadistica

def boot_ci(x: np.ndarray, rng) -> tuple[float, float]:
    idx = rng.integers(0, len(x), size=(B, len(x)))
    means = x[idx].mean(axis=1)
    return float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def sign_flip_p(d: np.ndarray, rng) -> float:
    """Prueba de permutacion por cambio de signo, bilateral, sobre la media de diferencias."""
    n = len(d)
    obs = abs(d.mean())
    if obs == 0:
        return 1.0
    if n <= 20:
        signs = np.array(list(product((-1, 1), repeat=n)), dtype=np.int8)
        stat = np.abs((signs * d).mean(axis=1))
    else:
        signs = rng.choice((-1, 1), size=(100_000, n))
        stat = np.abs((signs * d).mean(axis=1))
    return float((np.sum(stat >= obs - 1e-12) + (0 if n <= 20 else 1)) / (len(stat) + (0 if n <= 20 else 1)))


def holm(pvals: list[float]) -> list[float]:
    order = np.argsort(pvals)
    adj, running = [0.0] * len(pvals), 0.0
    for rank, i in enumerate(order):
        running = max(running, (len(pvals) - rank) * pvals[i])
        adj[i] = min(1.0, running)
    return adj


def aggregate(per_q: dict[str, dict[str, dict]], metrics, qids: list[str]) -> dict:
    rng = np.random.default_rng(SEED)
    out = {}
    for cfg in CONFIGS:
        for key, _ in metrics:
            x = np.array([per_q[cfg][q][key] for q in qids if q in per_q.get(cfg, {})
                          and key in per_q[cfg][q]], dtype=float)
            if len(x):
                lo, hi = boot_ci(x, rng)
                out[(cfg, key)] = (float(x.mean()), lo, hi, len(x))
    return out


def contrasts(per_q, key: str, qids: list[str]) -> list[dict]:
    rng = np.random.default_rng(SEED + 1)
    rows = []
    for cid, a, b, desc in CONTRASTS:
        common = [q for q in qids if q in per_q.get(a, {}) and q in per_q.get(b, {})]
        if len(common) < 3:
            continue
        d = np.array([per_q[a][q][key] - per_q[b][q][key] for q in common])
        lo, hi = boot_ci(d, rng)
        rows.append({"id": cid, "a": a, "b": b, "desc": desc, "n": len(common), "diff": float(d.mean()),
                     "lo": lo, "hi": hi, "p": sign_flip_p(d, rng),
                     "wins": int((d > 0).sum()), "losses": int((d < 0).sum()), "ties": int((d == 0).sum())})
    for r, padj in zip(rows, holm([r["p"] for r in rows])):
        r["p_holm"] = padj
    return rows


# ----------------------------------------------------------------------------- reporte

def f2(x):
    return f"{x:.2f}"


def table_aggregate(agg, metrics) -> list[str]:
    head = "| Configuración | " + " | ".join(l for _, l in metrics) + " | n |"
    lines = [head, "|---|" + "---|" * (len(metrics) + 1)]
    for cfg in CONFIGS:
        cells, n = [], 0
        for key, _ in metrics:
            if (cfg, key) in agg:
                m, lo, hi, n = agg[(cfg, key)]
                cells.append(f"{f2(m)} [{f2(lo)}, {f2(hi)}]")
            else:
                cells.append("—")
        lines.append(f"| {LABEL[cfg]} | " + " | ".join(cells) + f" | {n} |")
    return lines


def table_contrasts(rows) -> list[str]:
    lines = ["| Contraste | Diferencia (A−B) | IC 95 % | p (permutación) | p Holm | A gana / empata / pierde | n |",
             "|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| **{r['id']}** {LABEL[r['a']]} − {LABEL[r['b']]} | {r['diff']:+.3f} | "
                     f"[{r['lo']:+.3f}, {r['hi']:+.3f}] | {r['p']:.3f} | {r['p_holm']:.3f} | "
                     f"{r['wins']}/{r['ties']}/{r['losses']} | {r['n']} |")
    return lines


def by_type(per_q, metric_key, qids, qtype) -> list[str]:
    types = sorted({qtype[q] for q in qids})
    lines = ["| Configuración | " + " | ".join(f"{t} (n={sum(qtype[q] == t for q in qids)})" for t in types) + " |",
             "|---|" + "---|" * len(types)]
    for cfg in CONFIGS:
        cells = []
        for t in types:
            vals = [per_q[cfg][q][metric_key] for q in qids if qtype[q] == t and q in per_q.get(cfg, {})]
            cells.append(f2(float(np.mean(vals))) if vals else "—")
        lines.append(f"| {LABEL[cfg]} | " + " | ".join(cells) + " |")
    return lines


def descriptive(runs, ev: EvidenceIndex) -> list[str]:
    from src.config import CHUNKERS, load_chunks_for, load_config
    from sentence_transformers import SentenceTransformer
    tok = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2").tokenizer
    lines = ["| Configuración | Chunks | Palabras/chunk (mediana) | Chunks > 128 tokens | Huecos top-5 perdidos por duplicados | Retrieval mediana (ms) | Retrieval p90 (ms) |",
             "|---|---|---|---|---|---|---|"]
    cache: dict[tuple, tuple] = {}
    for cfg in CONFIGS:
        c = load_config(f"configs/{cfg}.yaml")
        key = (c.chunking, c.chunk_size, c.chunk_overlap, c.chunk_max_words)
        if key not in cache:
            chunks = load_chunks_for(c, CHUNKERS[c.chunking](c))
            ids = tok([ch.texto for ch in chunks], add_special_tokens=True, truncation=False)["input_ids"]
            trunc = sum(len(i) > 128 for i in ids) / len(ids)
            cache[key] = (len(chunks), int(np.median([ch.num_palabras for ch in chunks])), trunc)
        n_ch, med_w, trunc = cache[key]
        recs = list(runs[cfg].values())
        dups = sum(distinct_chunks(r, ev)[1] for r in recs)
        t = np.array([r["t_retrieval_s"] for r in recs]) * 1000
        t_warm = t[1:]  # la primera pregunta incluye arranque en frio
        if c.retriever == "bm25":
            n_ch_txt, trunc_txt = f"{n_ch}", "n/a (léxica)"
        elif c.retriever == "hybrid":
            n_ch_txt, trunc_txt = f"{n_ch}", f"{trunc:.0%} (parte densa)"
        else:
            n_ch_txt, trunc_txt = f"{n_ch}", f"{trunc:.0%}"
        lines.append(f"| {LABEL[cfg]} | {n_ch_txt} | {med_w} | {trunc_txt} | {dups}/100 | "
                     f"{np.median(t_warm):.1f} | {np.percentile(t_warm, 90):.1f} |")
    return lines


def determinism(runs_a, dir_b) -> list[str]:
    runs_b = load_runs(dir_b)
    lines = ["| Configuración | Preguntas con top-5 idéntico (ids y orden) |", "|---|---|"]
    for cfg in CONFIGS:
        if cfg not in runs_b:
            continue
        same = sum([c["chunk_id"] for c in runs_a[cfg][q]["chunks"]] == [c["chunk_id"] for c in runs_b[cfg][q]["chunks"]]
                   for q in runs_a[cfg])
        lines.append(f"| {LABEL[cfg]} | {same}/{len(runs_a[cfg])} |")
    return lines


def lexical_overlap_by_question(qs, annotation) -> dict[str, float]:
    """Fraccion de los lemas de contenido de la pregunta que aparecen en sus oraciones de evidencia."""
    from src.preprocessing import SpacyLemmaPreprocessor
    pre = SpacyLemmaPreprocessor()
    ev = EvidenceIndex()
    out = {}
    for q in qs:
        a = annotation.get(q.id)
        if not a or not a["anotada"] or not a["evidencia"] or q.is_trap:
            continue
        qt = set(pre.tokens(q.pregunta))
        if not qt:
            continue
        et = set(pre.tokens(" ".join(ev.by_id[s].texto for s in a["evidencia"])))
        out[q.id] = len(qt & et) / len(qt)
    return out


def union_words(chunks: list[dict], ev: EvidenceIndex) -> int:
    seen: dict[str, set] = {}
    for c in chunks:
        art, i0, i1 = ev.chunk_key(c)
        seen.setdefault(art, set()).update(range(i0, i1))
    return sum(len(v) for v in seen.values())


def budget_prefix(chunks: list[dict], budget: int, ev: EvidenceIndex) -> list[dict]:
    """Prefijo del ranking (chunks distintos) hasta acumular >= budget palabras distintas
    (incluye el chunk que cruza el umbral). Si no se alcanza, devuelve todo."""
    out = []
    for c in chunks:
        out.append(c)
        if union_words(out, ev) >= budget:
            break
    return out


def render_view(md, title, per_proxy, per_human, qids_p, n_annot, qtype, qs, annotation, human_ready, note):
    md += [f"## {title}", "", note, ""]
    agg_p = aggregate(per_proxy, METRICS_PROXY, qids_p)
    md += ["### Métrica PROXY (cobertura de puntos clave; sin anotación humana)", "",
           f"n = {len(qids_p)} preguntas no trampa. Heurística de coincidencia de tokens: puede contar como "
           "acierto un chunk que menciona un año sin ser evidencia; vale solo hasta tener la anotación humana.", ""]
    md += table_aggregate(agg_p, METRICS_PROXY) + ["", "IC 95 % entre corchetes (bootstrap sobre preguntas).", ""]
    md += [f"#### Contrastes planeados (primaria: {dict(METRICS_PROXY)[PRIMARY['proxy']]})", ""]
    md += table_contrasts(contrasts(per_proxy, PRIMARY["proxy"], qids_p)) + [""]
    md += ["#### Por tipo de pregunta (cobertura de puntos clave)", ""] + \
          by_type(per_proxy, "kp_cov", qids_p, qtype) + [""]

    md += ["### Métrica HUMANA (evidencia anotada por oración)", ""]
    if not human_ready:
        pend = sum(1 for v in annotation.values() if not v["anotada"])
        md += [f"_Sin anotación todavía ({len(annotation)} preguntas en la hoja, {pend} pendientes). Esta sección se "
               "llena sola al marcar preguntas como anotadas en `results/pln/anotacion_evidencia.md` y volver a "
               "correr `evaluation/pln_metrics.py`._", ""]
        return
    agg_h = aggregate(per_human, METRICS_HUMANO, n_annot)
    md += [f"n = {len(n_annot)} preguntas no trampa anotadas con ≥1 evidencia ({', '.join(n_annot)}).", ""]
    md += table_aggregate(agg_h, METRICS_HUMANO) + [""]
    md += [f"#### Contrastes planeados (primaria: {dict(METRICS_HUMANO)[PRIMARY['humano']]})", ""]
    md += table_contrasts(contrasts(per_human, PRIMARY["humano"], n_annot)) + [""]
    for key, label in METRICS_HUMANO:
        if key != PRIMARY["humano"]:
            md += [f"<details><summary>Contrastes en {label} (exploratorios)</summary>", ""] + \
                  table_contrasts(contrasts(per_human, key, n_annot)) + ["", "</details>", ""]
    md += ["#### Por tipo de pregunta (Recall de evidencia)", ""] + by_type(per_human, "recall", n_annot, qtype) + [""]

    ov = lexical_overlap_by_question(qs, annotation)
    if len(ov) >= 6:
        med = float(np.median(list(ov.values())))
        hi = [q for q in n_annot if ov.get(q, 0) > med]
        lo = [q for q in n_annot if q in ov and ov[q] <= med]
        md += ["#### H3 — según el solapamiento léxico entre la pregunta y su evidencia", "",
               f"Fracción de lemas de contenido de la pregunta presentes en sus oraciones de evidencia; corte en la "
               f"mediana ({med:.2f}). Alto = {len(hi)} preguntas, bajo = {len(lo)}.", "",
               "| Grupo | Contraste | Diferencia Recall | IC 95 % | n |", "|---|---|---|---|---|"]
        for name, grp in (("Alto solapamiento", hi), ("Bajo solapamiento", lo)):
            for r in contrasts(per_human, "recall", grp):
                if r["id"] in ("H3", "H1"):
                    md.append(f"| {name} | {LABEL[r['a']]} − {LABEL[r['b']]} | {r['diff']:+.3f} | "
                              f"[{r['lo']:+.3f}, {r['hi']:+.3f}] | {r['n']} |")
        md += [""]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", default=f"{OUT_DIR}/run1")
    ap.add_argument("--deep", default=f"{OUT_DIR}/run1_deep",
                    help="corridas con top_k=50 de las configs de chunks chicos (vista a presupuesto igual)")
    ap.add_argument("--annotation", default=f"{OUT_DIR}/anotacion_evidencia.md")
    ap.add_argument("--determinism", default=None, help="segunda corrida para verificar reproducibilidad")
    ap.add_argument("--questions", default="evaluation/questions.json")
    ap.add_argument("--out", default=f"{OUT_DIR}/analisis.md")
    args = ap.parse_args()

    qs = load_questions(args.questions)
    qtype = {q.id: q.tipo for q in qs}
    nontrap = [q for q in qs if not q.is_trap]
    ev = EvidenceIndex()
    runs = load_runs(args.runs)
    deep = load_runs(args.deep) if os.path.isdir(args.deep) else {}
    annotation = parse_annotation(args.annotation)
    n_annot = [q.id for q in nontrap if annotation.get(q.id, {}).get("anotada") and annotation[q.id]["evidencia"]]

    # Presupuesto de contexto: mediana de palabras distintas del top-5 del baseline.
    budget = int(np.median([union_words(distinct_chunks(runs["cosine"][q.id], ev)[0], ev) for q in nontrap]))

    views = {"k5": ("Vista A — k = 5 chunks por pregunta (protocolo de la tesis)", None),
             "presupuesto": (f"Vista B — presupuesto de contexto igual (≈ {budget} palabras recuperadas)", budget)}
    per_proxy = {v: {c: {} for c in runs} for v in views}
    per_human = {v: {c: {} for c in runs} for v in views}
    ctx = {v: {c: [] for c in runs} for v in views}
    for cfg, recs in runs.items():
        for q in nontrap:
            src = (deep.get(cfg) or recs)[q.id]
            all_chunks, _ = distinct_chunks(src, ev)
            for v, (_, bud) in views.items():
                chunks = (distinct_chunks(recs[q.id], ev)[0] if bud is None else budget_prefix(all_chunks, bud, ev))
                ctx[v][cfg].append((len(chunks), union_words(chunks, ev)))
                pm = proxy_metrics(chunks, q)
                if pm:
                    per_proxy[v][cfg][q.id] = pm
                if q.id in n_annot:
                    per_human[v][cfg][q.id] = human_metrics(chunks, annotation[q.id]["evidencia"], ev)

    md = ["# Experimento de PLN — análisis (recuperación léxica vs. densa)", "",
          f"_Generado por `evaluation/pln_metrics.py` a partir de `{args.runs}`. Semilla del bootstrap: {SEED}; "
          f"remuestreos: {B:,}. Solo recuperación (sin generación)._", ""]
    man = corpus_manifest()
    md += ["## 0. Corpus evaluado", "",
           f"- {len(man['articulos'])} archivos, **{man['articulos_unicos']} artículos únicos**, "
           f"{man['palabras_unicas']:,} palabras únicas.",
           "- Duplicados exactos (mismo SHA-256): " + "; ".join(" = ".join(d["titulos"]) for d in man["duplicados"]) +
           ". Se tratan como un solo artículo (canónico = título más largo): un chunk de la copia se proyecta al "
           "canónico y los chunks idénticos cuentan una vez en el top-5.",
           "- Artículos anómalos: " + (", ".join(f"{a['titulo']} ({a['palabras']} palabras)"
                                                for a in man["articulos"] if a["anomalia"]) or "ninguno") + ".", ""]

    md += ["## 1. Descripción de las configuraciones", ""] + descriptive(runs, ev) + [
        "", "_Huecos perdidos: posiciones del top-5 ocupadas por una copia exacta de otro resultado (artículo "
        "duplicado). Se reportan, pero la evaluación cuenta cada contenido una vez._", "",
        "**Contexto recuperado por pregunta (palabras distintas, mediana) en cada vista**", "",
        "| Configuración | Vista A: chunks / palabras | Vista B: chunks / palabras |", "|---|---|---|"]
    for cfg in runs:
        a, b = ctx["k5"][cfg], ctx["presupuesto"][cfg]
        md.append(f"| {LABEL[cfg]} | {np.median([x[0] for x in a]):.0f} / {np.median([x[1] for x in a]):.0f} | "
                  f"{np.median([x[0] for x in b]):.0f} / {np.median([x[1] for x in b]):.0f} |")
    md += ["", "_Con k = 5, los chunks de 300 palabras reciben ≈ 4–5 veces más contexto que los de ~65: la Vista A "
           "mezcla el efecto de **cómo se segmenta** con el de **cuánto texto se entrega**. La Vista B los separa._", ""]

    if args.determinism:
        md += ["## 2. Reproducibilidad de la recuperación", "",
               f"Dos corridas independientes (`{args.runs}` y `{args.determinism}`):", ""] + \
              determinism(runs, args.determinism) + [""]

    human_ready = bool(n_annot)
    notes = {"k5": "Cada configuración entrega sus 5 mejores chunks distintos. Responde «¿qué pasa con el protocolo "
                   "de la tesis?», pero NO aísla el efecto de la segmentación (ver Vista B).",
             "presupuesto": "Cada configuración entrega los mejores chunks distintos hasta acumular el mismo número de "
                            "palabras. Con chunks chicos esto significa más de 5 chunks, por lo que **P@5 deja de ser "
                            "comparable: se reporta P@n (n variable)**. Aísla el efecto de segmentar del de dar más texto."}
    for i, (v, (title, _)) in enumerate(views.items(), 3):
        qids_p = [q.id for q in nontrap if all(q.id in per_proxy[v][c] for c in runs)]
        render_view(md, f"{i}. {title}", per_proxy[v], per_human[v], qids_p, n_annot, qtype, qs, annotation,
                    human_ready, notes[v])

    if human_ready:
        md += ["## 5. Validez del proxy frente a la anotación humana", ""]
        xs, ys = [], []
        for cfg in runs:
            for q in n_annot:
                if q in per_proxy["k5"][cfg] and q in per_human["k5"][cfg]:
                    xs.append(per_proxy["k5"][cfg][q]["kp_cov"])
                    ys.append(per_human["k5"][cfg][q]["recall"])
        if len(xs) > 5 and np.std(xs) > 0 and np.std(ys) > 0:
            md += [f"Correlación de Pearson entre la cobertura de puntos clave y el Recall humano (Vista A; pares "
                   f"configuración × pregunta, n = {len(xs)}): **r = {np.corrcoef(xs, ys)[0, 1]:.2f}**. Si es baja, "
                   "los resultados con proxy no deben interpretarse.", ""]

    md += ["## 6. Preguntas trampa (análisis aparte, no entran en los promedios)", ""]
    traps = [q for q in qs if q.is_trap]
    md += ["| Pregunta | " + " | ".join(LABEL[c] for c in runs) + " |", "|---|" + "---|" * len(runs)]
    for q in traps:
        cells = []
        for cfg in runs:
            top = runs[cfg][q.id]["chunks"]
            cells.append(f"{top[0]['score']:.2f}" if top else "sin resultados")
        md.append(f"| {q.id}: {q.pregunta} | " + " | ".join(cells) + " |")
    md += ["", "Puntaje del primer resultado (no comparable entre métodos: coseno 0–1, BM25 sin cota, RRF ≈ 0.01). "
           "Ninguna configuración tiene un umbral de rechazo; el puntaje de una trampa solo se puede juzgar "
           "contra el de las preguntas con respuesta (tarea de la fase de generación/rechazo, fuera de este experimento).", ""]

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")
    with open(f"{OUT_DIR}/metricas.json", "w", encoding="utf-8") as f:
        json.dump({"presupuesto_palabras": budget, "proxy": per_proxy, "humano": per_human if human_ready else {},
                   "anotadas": n_annot}, f, ensure_ascii=False, indent=1)
    print(f"-> {args.out}  (presupuesto={budget} palabras, proxy n={len(nontrap)}, humano n={len(n_annot)})")


if __name__ == "__main__":
    main()
