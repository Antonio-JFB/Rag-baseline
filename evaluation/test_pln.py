"""
Pruebas con resultado conocido del experimento de PLN (segmentacion, cobertura, metricas, estadistica).

    python evaluation/test_pln.py
"""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from evaluation.evidence import EvidenceIndex, split_article
from evaluation.pln_metrics import (budget_prefix, distinct_chunks, holm, human_metrics, parse_annotation,
                                    sign_flip_p, union_words)

ev = EvidenceIndex()
fails = 0


def check(name, cond, detail=""):
    global fails
    print(("OK   " if cond else "FALLA"), name, detail)
    fails += 0 if cond else 1


# --- segmentacion -----------------------------------------------------------------
txt = "# Titulo\nEl Dr. Perez nació en 1810. Murió en 1870 a. C. Luego volvió.\nOtro párrafo sin punto final"
s = split_article(txt, "X")
check("titulo se detecta como encabezado", s[0].es_titulo and s[0].texto == "Titulo", str([x.texto for x in s]))
check("'Dr.' no corta la oracion", s[1].texto.startswith("El Dr. Perez nació en 1810."), s[1].texto)
check("salto de linea corta (parrafo sin punto)", s[-1].texto == "Otro párrafo sin punto final")
check("offsets contiguos y completos", all(a.fin == b.inicio for a, b in zip(s, s[1:])) and s[-1].fin == len(txt.split()))

# --- cobertura y metricas con evidencia conocida ---------------------------------------
art = "Guerra de Independencia de México"
dup = "Independencia de México"
sent = next(x for x in ev.by_article[art] if not x.es_titulo and x.fin - x.inicio >= 10)
other = next(x for x in ev.by_article["Porfiriato"] if not x.es_titulo)

def chunk(fuente, i0, i1, texto="t"):
    return {"fuente": fuente, "inicio_palabra": i0, "fin_palabra": i1, "texto": texto, "chunk_id": f"{fuente}{i0}"}

c_rel = chunk(art, sent.inicio - 5, sent.fin + 5)
c_dup = chunk(dup, sent.inicio - 5, sent.fin + 5)                  # misma posicion, articulo duplicado
c_half = chunk(art, sent.inicio, sent.inicio + (sent.fin - sent.inicio) // 2 - 1)   # < 50 % de la oracion
c_other = chunk("Porfiriato", other.inicio, other.fin)
check("chunk del duplicado cubre la oracion del canonico", ev.covered(c_dup, sent.sid))
check("chunk que cubre < 50 % no cuenta", not ev.covered(c_half, sent.sid))
check("misma clave para canonico y duplicado", ev.chunk_key(c_rel) == ev.chunk_key(c_dup))

rec = {"chunks": [c_other, c_rel, c_dup, c_half]}
dist, nd = distinct_chunks(rec, ev)
check("duplicado cuenta una vez", len(dist) == 3 and nd == 1, f"distintos={len(dist)} duplicados={nd}")
m = human_metrics(dist, {sent.sid}, ev)
check("P@n = 1/3, MRR = 1/2, Hit = 1, Recall = 1", abs(m["p5"] - 1 / 3) < 1e-9 and m["mrr"] == 0.5
      and m["hit"] == 1 and m["recall"] == 1.0, str(m))
n_ret = union_words(dist, ev)
check("densidad = palabras de evidencia / palabras recuperadas",
      abs(m["dens"] - (sent.fin - sent.inicio) / n_ret) < 1e-9, f"{m['dens']:.4f}")
m0 = human_metrics([c_other], {sent.sid}, ev)
check("sin acierto: todo en 0", m0 == {"p5": 0.0, "hit": 0.0, "mrr": 0.0, "recall": 0.0, "dens": 0.0}, str(m0))

pre = budget_prefix([c_other, c_rel, c_half], (other.fin - other.inicio) + 1, ev)
check("prefijo de presupuesto incluye el chunk que cruza el umbral", len(pre) == 2)

# --- estadistica ---------------------------------------------------------------------
rng = np.random.default_rng(0)
check("sign-flip: diferencias todas iguales y positivas -> p = 2/2^n",
      abs(sign_flip_p(np.ones(10), rng) - 2 / 2 ** 10) < 1e-12)
check("sign-flip: media cero -> p = 1", sign_flip_p(np.array([1.0, -1.0, 2.0, -2.0]), rng) == 1.0)
check("Holm: [0.01, 0.04, 0.03] -> [0.03, 0.06, 0.06]",
      np.allclose(holm([0.01, 0.04, 0.03]), [0.03, 0.06, 0.06]))

# --- parser de anotacion -----------------------------------------------------------------
tmp = os.path.join(os.environ.get("TEMP", "."), "anot_test.md")
with open(tmp, "w", encoding="utf-8") as f:
    f.write("## Q1 (factual)\n**Anotada:** [x] sí\n| # | Evidencia | Artículo | Oración | Pista | Ref |\n|---|---|---|---|---|---|\n"
            "| 1 | [x] | A | texto ¦ con barra | — | A#1-5 |\n| 2 | [ ] | A | otra | — | A#6-9 |\n"
            "## Q2 (factual)\n**Anotada:** [ ] sí\n| 1 | [x] | A | x | — | A#1-5 |\n")
a = parse_annotation(tmp)
check("parser: Q1 anotada con 1 evidencia de 2 filas", a["Q1"]["anotada"] and a["Q1"]["evidencia"] == {"A#1-5"} and a["Q1"]["filas"] == 2)
check("parser: Q2 sin marca de anotada", not a["Q2"]["anotada"])
os.remove(tmp)

print("\nTODO OK" if not fails else f"\n{fails} PRUEBAS FALLARON")
sys.exit(1 if fails else 0)
