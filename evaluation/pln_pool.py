"""
pln_pool.py -- arma las oraciones candidatas a evidencia y la hoja de anotacion.

Para cada pregunta junta (pooling) oraciones del corpus que algun metodo considera
posible evidencia, de modo que lo que se anota NO dependa de un solo recuperador:

  a) top-N oraciones segun BUSQUEDA DENSA (embeddings, mismo modelo del experimento)
  b) top-N segun BM25 sin preprocesar
  c) top-N segun BM25 con lematizacion y palabras vacias
  d) oraciones que contienen puntos clave de la pregunta (questions.json)
  e) la mejor oracion (segun a) de cada chunk distinto recuperado en el top-5 por
     cualquiera de las 6 configuraciones -> todo chunk recuperado tiene al menos un
     candidato juzgado

Lo no juzgado se considera no relevante (supuesto estandar de pooling). La hoja NO
muestra de que metodo salio cada oracion, para no sesgar al anotador.

Uso:
    python evaluation/pln_pool.py                      # genera pool.json y la hoja
    python evaluation/pln_pool.py --runs results/pln/run1 --n 8
"""

import argparse
import json
import os
import re
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from evaluation.evidence import EvidenceIndex
from evaluation.keypoints import keypoint_hits
from evaluation.schema import load_questions

CONFIGS = ["cosine", "cosine_paragraph", "cosine_fixed64", "bm25", "bm25_lemma", "hybrid"]
OUT_DIR = "results/pln"
CACHE_DIR = f"{OUT_DIR}/cache"
MIN_WORDS = 4            # oraciones mas cortas no son candidatas a evidencia
EMBED_MODEL = "paraphrase-multilingual-MiniLM-L12-v2"


def load_runs(runs_dir: str) -> dict[str, dict[str, dict]]:
    """{config: {question_id: record}}"""
    out = {}
    for cfg in CONFIGS:
        path = f"{runs_dir}/{cfg}/results.jsonl"
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            out[cfg] = {r["question_id"]: r for r in map(json.loads, f)}
    return out


def sentence_embeddings(sents) -> np.ndarray:
    """Embeddings normalizados de las oraciones (con cache en disco; la clave es el conteo +
    el id de la ultima oracion, que cambia si cambia el corpus o la segmentacion)."""
    os.makedirs(CACHE_DIR, exist_ok=True)
    tag = f"{len(sents)}_{re.sub(r'[^A-Za-z0-9]+', '', sents[-1].sid)}"
    path = f"{CACHE_DIR}/sent_emb_{tag}.npy"
    if os.path.exists(path):
        return np.load(path)
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(EMBED_MODEL)
    emb = model.encode([s.texto for s in sents], batch_size=64, show_progress_bar=False,
                       convert_to_numpy=True, normalize_embeddings=True).astype(np.float32)
    np.save(path, emb)
    return emb


def clean(text: str, limit: int = 420) -> str:
    text = text.replace("|", "¦").replace("\n", " ").strip()
    return text if len(text) <= limit else text[:limit].rsplit(" ", 1)[0] + " …"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", default=f"{OUT_DIR}/run1", help="directorio con las corridas de recuperacion")
    ap.add_argument("--n", type=int, default=8, help="top-N por metodo")
    ap.add_argument("--questions", default="evaluation/questions.json")
    args = ap.parse_args()

    from rank_bm25 import BM25Okapi
    from sentence_transformers import SentenceTransformer
    from src.preprocessing import PlainPreprocessor, SpacyLemmaPreprocessor

    ev = EvidenceIndex()
    cand = [s for s in ev.sentences if not s.es_titulo and s.fin - s.inicio >= MIN_WORDS]
    idx_of = {s.sid: i for i, s in enumerate(cand)}
    print(f"{len(cand)} oraciones candidatas (>= {MIN_WORDS} palabras, sin titulos)")

    emb = sentence_embeddings(cand)
    model = SentenceTransformer(EMBED_MODEL)
    plain, lemma = PlainPreprocessor(), SpacyLemmaPreprocessor()
    bm_plain = BM25Okapi(plain.tokens_many([s.texto for s in cand]))
    bm_lemma = BM25Okapi(lemma.tokens_many([s.texto for s in cand]))

    questions = load_questions(args.questions)
    runs = load_runs(args.runs)
    pool: dict[str, dict[str, set]] = {}

    for q in questions:
        origins: dict[str, set] = {}
        add = lambda sid, tag: origins.setdefault(sid, set()).add(tag)

        qe = model.encode([q.pregunta], normalize_embeddings=True, convert_to_numpy=True)[0]
        dense = emb @ qe
        for i in np.argsort(-dense)[:args.n]:
            add(cand[i].sid, "denso")
        for tag, bm, pre in (("bm25", bm_plain, plain), ("bm25_lemma", bm_lemma, lemma)):
            toks = pre.tokens(q.pregunta)
            if toks:
                sc = bm.get_scores(toks)
                for i in np.argsort(-sc)[:args.n]:
                    if sc[i] > 0:
                        add(cand[i].sid, tag)

        kp = [(len(h), dense[i], s.sid) for i, s in enumerate(cand)
              if (h := keypoint_hits(s.texto, q.puntos_clave))]
        for _, _, sid in sorted(kp, reverse=True)[:args.n]:
            add(sid, "puntos_clave")

        seen = set()
        for cfg, recs in runs.items():
            for ch in recs[q.id]["chunks"]:
                key = ev.chunk_key(ch)
                if key in seen:
                    continue
                seen.add(key)
                inside = [s for s in ev.sentences_in(ch) if s.sid in idx_of]
                if inside:
                    best = max(inside, key=lambda s: dense[idx_of[s.sid]])
                    add(best.sid, "chunk_recuperado")
        pool[q.id] = origins

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(f"{OUT_DIR}/pool.json", "w", encoding="utf-8") as f:
        json.dump({qid: {sid: sorted(t) for sid, t in o.items()} for qid, o in pool.items()},
                  f, ensure_ascii=False, indent=1)

    # --- hoja de anotacion ---------------------------------------------------
    lines = [HEADER]
    total = 0
    for q in questions:
        sids = sorted(pool[q.id], key=lambda sid: (ev.by_id[sid].articulo, ev.by_id[sid].inicio))
        total += len(sids)
        lines += [
            f"\n---\n\n## {q.id} ({q.tipo}){' — PREGUNTA TRAMPA' if q.is_trap else ''}\n",
            f"**Pregunta:** {q.pregunta}",
            f"**Puntos clave (guía, no juez):** {'; '.join(q.puntos_clave)}",
            f"**Anotada:** [ ] sí   (marca esta casilla al terminar la pregunta)\n",
            "| # | Evidencia | Artículo | Oración | Puntos clave en la oración | Ref |",
            "|---|---|---|---|---|---|",
        ]
        for n, sid in enumerate(sids, 1):
            s = ev.by_id[sid]
            hits = ", ".join(keypoint_hits(s.texto, q.puntos_clave)) or "—"
            lines.append(f"| {n} | [ ] | {clean(s.articulo, 40)} | {clean(s.texto)} | {clean(hits, 80)} | {sid} |")
    with open(f"{OUT_DIR}/anotacion_evidencia.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    sizes = [len(pool[q.id]) for q in questions]
    print(f"Pool: {total} oraciones en {len(questions)} preguntas "
          f"(min {min(sizes)}, mediana {sorted(sizes)[len(sizes) // 2]}, max {max(sizes)})")
    print(f"-> {OUT_DIR}/pool.json  y  {OUT_DIR}/anotacion_evidencia.md")


HEADER = """# Anotación de evidencia — experimento de PLN

**Qué se anota:** para cada pregunta, marca con `[x]` en la columna *Evidencia* las **oraciones** del corpus que
aportan información necesaria para contestarla. Esta anotación es **independiente de cómo se parta el texto en
chunks**: las métricas de las seis configuraciones se calculan después a partir de ella.

**Criterio (usa el mismo para todas las preguntas):**
1. Marca la oración si **por sí sola** (o con el dato que introduce) afirma algo de la respuesta: el dato pedido,
   una causa, una consecuencia, un elemento de la comparación, un eslabón de la relación. Una oración que solo
   *menciona el tema* sin aportar el dato **no** es evidencia.
2. Si la respuesta tiene varias partes (causalidad, comparativa, multihop), marca **todas** las oraciones que
   aportan una parte; no hace falta que una sola contenga todo.
3. Oraciones repetidas con otras palabras (dos artículos que dicen lo mismo): marca **ambas**.
4. Pregunta trampa: si el corpus **sí** contiene la respuesta, marca la evidencia (p. ej. T1); si no hay nada,
   deja todo vacío y marca la pregunta como anotada.
5. La columna *Puntos clave* es solo una pista automática; una oración puede ser evidencia sin ella, y tenerla
   sin serlo (p. ej. un año suelto).
6. Las oraciones están ordenadas por artículo y posición, **no** por relevancia ni por método.
7. Al terminar una pregunta marca `[x]` en **Anotada**. Las no marcadas se excluyen de las métricas (no cuentan
   como ceros).

**Alcance:** las oraciones candidatas se reunieron con varios métodos (búsqueda densa, BM25, BM25 lematizado,
puntos clave y los chunks recuperados por las seis configuraciones). Lo que no aparece aquí se asume no relevante.
Si notas una evidencia importante que falta, añádela al final de la tabla con su `Ref` o avísame.
"""

if __name__ == "__main__":
    main()
