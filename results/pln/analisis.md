# Experimento de PLN — análisis (recuperación léxica vs. densa)

_Generado por `evaluation/pln_metrics.py` a partir de `results/pln/run1`. Semilla del bootstrap: 12345; remuestreos: 10,000. Solo recuperación (sin generación)._

## 0. Corpus evaluado

- 19 archivos, **18 artículos únicos**, 298,638 palabras únicas.
- Duplicados exactos (mismo SHA-256): Guerra de Independencia de México = Independencia de México. Se tratan como un solo artículo (canónico = título más largo): un chunk de la copia se proyecta al canónico y los chunks idénticos cuentan una vez en el top-5.
- Artículos anómalos: Tenochtitlan (51 palabras).

## 1. Descripción de las configuraciones

| Configuración | Chunks | Palabras/chunk (mediana) | Chunks > 128 tokens | Huecos top-5 perdidos por duplicados | Retrieval mediana (ms) | Retrieval p90 (ms) |
|---|---|---|---|---|---|---|
| Densa (baseline 300/50) | 1334 | 300 | 100% | 8/100 | 21.6 | 23.5 |
| Densa + párrafos (≤85 pal.) | 5239 | 68 | 14% | 5/100 | 17.6 | 18.1 |
| Densa + ventana 64 (control) | 5197 | 64 | 1% | 5/100 | 18.2 | 21.6 |
| BM25 simple | 1334 | 300 | n/a (léxica) | 2/100 | 2.5 | 3.5 |
| BM25 + lemas + stopwords | 1334 | 300 | n/a (léxica) | 1/100 | 4.1 | 5.4 |
| Híbrida RRF (denso + BM25 simple) | 1334 | 300 | 100% (parte densa) | 5/100 | 23.6 | 28.0 |

_Huecos perdidos: posiciones del top-5 ocupadas por una copia exacta de otro resultado (artículo duplicado). Se reportan, pero la evaluación cuenta cada contenido una vez._

**Contexto recuperado por pregunta (palabras distintas, mediana) en cada vista**

| Configuración | Vista A: chunks / palabras | Vista B: chunks / palabras |
|---|---|---|
| Densa (baseline 300/50) | 5 / 1450 | 5 / 1450 |
| Densa + párrafos (≤85 pal.) | 5 / 322 | 22 / 1485 |
| Densa + ventana 64 (control) | 5 / 320 | 23 / 1472 |
| BM25 simple | 5 / 1450 | 5 / 1450 |
| BM25 + lemas + stopwords | 5 / 1450 | 5 / 1450 |
| Híbrida RRF (denso + BM25 simple) | 5 / 1500 | 5 / 1500 |

_Con k = 5, los chunks de 300 palabras reciben ≈ 4–5 veces más contexto que los de ~65: la Vista A mezcla el efecto de **cómo se segmenta** con el de **cuánto texto se entrega**. La Vista B los separa._

## 2. Reproducibilidad de la recuperación

Dos corridas independientes (`results/pln/run1` y `results/pln/run2`):

| Configuración | Preguntas con top-5 idéntico (ids y orden) |
|---|---|
| Densa (baseline 300/50) | 20/20 |
| Densa + párrafos (≤85 pal.) | 20/20 |
| Densa + ventana 64 (control) | 20/20 |
| BM25 simple | 20/20 |
| BM25 + lemas + stopwords | 20/20 |
| Híbrida RRF (denso + BM25 simple) | 20/20 |

## 3. Vista A — k = 5 chunks por pregunta (protocolo de la tesis)

Cada configuración entrega sus 5 mejores chunks distintos. Responde «¿qué pasa con el protocolo de la tesis?», pero NO aísla el efecto de la segmentación (ver Vista B).

### Métrica PROXY (cobertura de puntos clave; sin anotación humana)

n = 17 preguntas no trampa. Heurística de coincidencia de tokens: puede contar como acierto un chunk que menciona un año sin ser evidencia; vale solo hasta tener la anotación humana.

| Configuración | Cobertura de puntos clave | MRR (≥50 % puntos clave) | n |
|---|---|---|---|
| Densa (baseline 300/50) | 0.59 [0.44, 0.74] | 0.43 [0.22, 0.65] | 17 |
| Densa + párrafos (≤85 pal.) | 0.26 [0.14, 0.39] | 0.16 [0.02, 0.34] | 17 |
| Densa + ventana 64 (control) | 0.29 [0.16, 0.42] | 0.03 [0.00, 0.09] | 17 |
| BM25 simple | 0.54 [0.38, 0.71] | 0.24 [0.08, 0.43] | 17 |
| BM25 + lemas + stopwords | 0.58 [0.46, 0.71] | 0.21 [0.11, 0.32] | 17 |
| Híbrida RRF (denso + BM25 simple) | 0.62 [0.49, 0.74] | 0.36 [0.19, 0.53] | 17 |

IC 95 % entre corchetes (bootstrap sobre preguntas).

#### Contrastes planeados (primaria: Cobertura de puntos clave)

| Contraste | Diferencia (A−B) | IC 95 % | p (permutación) | p Holm | A gana / empata / pierde | n |
|---|---|---|---|---|---|---|
| **H1** BM25 + lemas + stopwords − BM25 simple | +0.040 | [-0.052, +0.137] | 0.438 | 1.000 | 4/11/2 | 17 |
| **H2a** Densa + párrafos (≤85 pal.) − Densa (baseline 300/50) | -0.334 | [-0.487, -0.197] | 0.000 | 0.003 | 0/5/12 | 17 |
| **H2b** Densa + ventana 64 (control) − Densa (baseline 300/50) | -0.305 | [-0.455, -0.166] | 0.001 | 0.006 | 0/6/11 | 17 |
| **H2c** Densa + párrafos (≤85 pal.) − Densa + ventana 64 (control) | -0.029 | [-0.119, +0.057] | 0.531 | 1.000 | 3/10/4 | 17 |
| **H3** BM25 simple − Densa (baseline 300/50) | -0.050 | [-0.247, +0.135] | 0.638 | 1.000 | 6/4/7 | 17 |
| **Hy1** Híbrida RRF (denso + BM25 simple) − Densa (baseline 300/50) | +0.025 | [-0.054, +0.113] | 0.750 | 1.000 | 3/12/2 | 17 |
| **Hy2** Híbrida RRF (denso + BM25 simple) − BM25 simple | +0.074 | [-0.058, +0.211] | 0.328 | 1.000 | 8/4/5 | 17 |

#### Por tipo de pregunta (cobertura de puntos clave)

| Configuración | causalidad (n=4) | comparativa (n=3) | factual (n=5) | multihop (n=2) | relacional (n=3) |
|---|---|---|---|---|---|
| Densa (baseline 300/50) | 0.65 | 0.70 | 0.67 | 0.70 | 0.22 |
| Densa + párrafos (≤85 pal.) | 0.25 | 0.36 | 0.33 | 0.17 | 0.11 |
| Densa + ventana 64 (control) | 0.29 | 0.36 | 0.33 | 0.33 | 0.11 |
| BM25 simple | 0.72 | 0.48 | 0.73 | 0.20 | 0.28 |
| BM25 + lemas + stopwords | 0.66 | 0.57 | 0.73 | 0.37 | 0.39 |
| Híbrida RRF (denso + BM25 simple) | 0.78 | 0.61 | 0.67 | 0.53 | 0.39 |

### Métrica HUMANA (evidencia anotada por oración)

_Sin anotación todavía (20 preguntas en la hoja, 20 pendientes). Esta sección se llena sola al marcar preguntas como anotadas en `results/pln/anotacion_evidencia.md` y volver a correr `evaluation/pln_metrics.py`._

## 4. Vista B — presupuesto de contexto igual (≈ 1450 palabras recuperadas)

Cada configuración entrega los mejores chunks distintos hasta acumular el mismo número de palabras. Con chunks chicos esto significa más de 5 chunks, por lo que **P@5 deja de ser comparable: se reporta P@n (n variable)**. Aísla el efecto de segmentar del de dar más texto.

### Métrica PROXY (cobertura de puntos clave; sin anotación humana)

n = 17 preguntas no trampa. Heurística de coincidencia de tokens: puede contar como acierto un chunk que menciona un año sin ser evidencia; vale solo hasta tener la anotación humana.

| Configuración | Cobertura de puntos clave | MRR (≥50 % puntos clave) | n |
|---|---|---|---|
| Densa (baseline 300/50) | 0.59 [0.44, 0.74] | 0.43 [0.22, 0.65] | 17 |
| Densa + párrafos (≤85 pal.) | 0.56 [0.42, 0.69] | 0.17 [0.03, 0.34] | 17 |
| Densa + ventana 64 (control) | 0.65 [0.54, 0.77] | 0.04 [0.00, 0.10] | 17 |
| BM25 simple | 0.54 [0.38, 0.71] | 0.24 [0.08, 0.43] | 17 |
| BM25 + lemas + stopwords | 0.58 [0.46, 0.71] | 0.21 [0.11, 0.32] | 17 |
| Híbrida RRF (denso + BM25 simple) | 0.62 [0.49, 0.74] | 0.36 [0.19, 0.53] | 17 |

IC 95 % entre corchetes (bootstrap sobre preguntas).

#### Contrastes planeados (primaria: Cobertura de puntos clave)

| Contraste | Diferencia (A−B) | IC 95 % | p (permutación) | p Holm | A gana / empata / pierde | n |
|---|---|---|---|---|---|---|
| **H1** BM25 + lemas + stopwords − BM25 simple | +0.040 | [-0.052, +0.137] | 0.438 | 1.000 | 4/11/2 | 17 |
| **H2a** Densa + párrafos (≤85 pal.) − Densa (baseline 300/50) | -0.032 | [-0.181, +0.103] | 0.719 | 1.000 | 4/10/3 | 17 |
| **H2b** Densa + ventana 64 (control) − Densa (baseline 300/50) | +0.059 | [-0.083, +0.201] | 0.488 | 1.000 | 6/7/4 | 17 |
| **H2c** Densa + párrafos (≤85 pal.) − Densa + ventana 64 (control) | -0.091 | [-0.225, +0.049] | 0.227 | 1.000 | 3/8/6 | 17 |
| **H3** BM25 simple − Densa (baseline 300/50) | -0.050 | [-0.247, +0.135] | 0.638 | 1.000 | 6/4/7 | 17 |
| **Hy1** Híbrida RRF (denso + BM25 simple) − Densa (baseline 300/50) | +0.025 | [-0.054, +0.113] | 0.750 | 1.000 | 3/12/2 | 17 |
| **Hy2** Híbrida RRF (denso + BM25 simple) − BM25 simple | +0.074 | [-0.058, +0.211] | 0.328 | 1.000 | 8/4/5 | 17 |

#### Por tipo de pregunta (cobertura de puntos clave)

| Configuración | causalidad (n=4) | comparativa (n=3) | factual (n=5) | multihop (n=2) | relacional (n=3) |
|---|---|---|---|---|---|
| Densa (baseline 300/50) | 0.65 | 0.70 | 0.67 | 0.70 | 0.22 |
| Densa + párrafos (≤85 pal.) | 0.46 | 0.74 | 0.60 | 0.53 | 0.47 |
| Densa + ventana 64 (control) | 0.59 | 0.53 | 0.80 | 0.70 | 0.58 |
| BM25 simple | 0.72 | 0.48 | 0.73 | 0.20 | 0.28 |
| BM25 + lemas + stopwords | 0.66 | 0.57 | 0.73 | 0.37 | 0.39 |
| Híbrida RRF (denso + BM25 simple) | 0.78 | 0.61 | 0.67 | 0.53 | 0.39 |

### Métrica HUMANA (evidencia anotada por oración)

_Sin anotación todavía (20 preguntas en la hoja, 20 pendientes). Esta sección se llena sola al marcar preguntas como anotadas en `results/pln/anotacion_evidencia.md` y volver a correr `evaluation/pln_metrics.py`._

## 6. Preguntas trampa (análisis aparte, no entran en los promedios)

| Pregunta | Densa (baseline 300/50) | Densa + párrafos (≤85 pal.) | Densa + ventana 64 (control) | BM25 simple | BM25 + lemas + stopwords | Híbrida RRF (denso + BM25 simple) |
|---|---|---|---|---|---|---|
| T1: ¿Quién es el presidente actual de México? | 0.69 | 0.74 | 0.70 | 16.29 | 8.28 | 0.01 |
| T2: ¿Cuál es el PIB actual de México? | 0.64 | 0.65 | 0.64 | 17.88 | 8.49 | 0.02 |
| T3: ¿Qué equipos jugaron la final del fútbol mexicano en 2024? | 0.58 | 0.64 | 0.69 | 19.83 | 8.10 | 0.02 |

Puntaje del primer resultado (no comparable entre métodos: coseno 0–1, BM25 sin cota, RRF ≈ 0.01). Ninguna configuración tiene un umbral de rechazo; el puntaje de una trampa solo se puede juzgar contra el de las preguntas con respuesta (tarea de la fase de generación/rechazo, fuera de este experimento).

