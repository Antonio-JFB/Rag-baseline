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

n = 17 preguntas no trampa anotadas con ≥1 evidencia (F1, F2, F3, F4, F5, C1, C2, C3, C4, V1, V2, V3, R1, R2, R3, M1, M2).

| Configuración | P@5 | Hit@5 | MRR | Recall@5 (evidencia) | Densidad de evidencia | n |
|---|---|---|---|---|---|---|
| Densa (baseline 300/50) | 0.33 [0.24, 0.43] | 0.94 [0.82, 1.00] | 0.66 [0.48, 0.84] | 0.19 [0.14, 0.25] | 0.04 [0.03, 0.05] | 17 |
| Densa + párrafos (≤85 pal.) | 0.27 [0.16, 0.38] | 0.76 [0.53, 0.94] | 0.53 [0.34, 0.72] | 0.14 [0.09, 0.20] | 0.13 [0.08, 0.18] | 17 |
| Densa + ventana 64 (control) | 0.27 [0.16, 0.39] | 0.71 [0.47, 0.88] | 0.51 [0.32, 0.71] | 0.16 [0.09, 0.25] | 0.14 [0.08, 0.22] | 17 |
| BM25 simple | 0.28 [0.18, 0.38] | 0.76 [0.53, 0.94] | 0.42 [0.26, 0.60] | 0.18 [0.10, 0.28] | 0.04 [0.02, 0.06] | 17 |
| BM25 + lemas + stopwords | 0.39 [0.28, 0.50] | 0.94 [0.82, 1.00] | 0.60 [0.45, 0.75] | 0.25 [0.18, 0.31] | 0.05 [0.03, 0.07] | 17 |
| Híbrida RRF (denso + BM25 simple) | 0.38 [0.26, 0.49] | 0.88 [0.71, 1.00] | 0.68 [0.50, 0.85] | 0.22 [0.15, 0.31] | 0.05 [0.03, 0.08] | 17 |

#### Contrastes planeados (primaria: Recall@5 (evidencia))

| Contraste | Diferencia (A−B) | IC 95 % | p (permutación) | p Holm | A gana / empata / pierde | n |
|---|---|---|---|---|---|---|
| **H1** BM25 + lemas + stopwords − BM25 simple | +0.063 | [-0.006, +0.133] | 0.109 | 0.656 | 6/9/2 | 17 |
| **H2a** Densa + párrafos (≤85 pal.) − Densa (baseline 300/50) | -0.052 | [-0.104, -0.010] | 0.062 | 0.438 | 1/11/5 | 17 |
| **H2b** Densa + ventana 64 (control) − Densa (baseline 300/50) | -0.032 | [-0.106, +0.047] | 0.435 | 1.000 | 5/4/8 | 17 |
| **H2c** Densa + párrafos (≤85 pal.) − Densa + ventana 64 (control) | -0.020 | [-0.125, +0.063] | 0.754 | 1.000 | 5/7/5 | 17 |
| **H3** BM25 simple − Densa (baseline 300/50) | -0.009 | [-0.088, +0.069] | 0.833 | 1.000 | 6/4/7 | 17 |
| **Hy1** Híbrida RRF (denso + BM25 simple) − Densa (baseline 300/50) | +0.032 | [-0.021, +0.084] | 0.260 | 1.000 | 7/7/3 | 17 |
| **Hy2** Híbrida RRF (denso + BM25 simple) − BM25 simple | +0.041 | [-0.036, +0.117] | 0.325 | 1.000 | 8/5/4 | 17 |

<details><summary>Contrastes en P@5 (exploratorios)</summary>

| Contraste | Diferencia (A−B) | IC 95 % | p (permutación) | p Holm | A gana / empata / pierde | n |
|---|---|---|---|---|---|---|
| **H1** BM25 + lemas + stopwords − BM25 simple | +0.109 | [+0.009, +0.218] | 0.090 | 0.539 | 7/7/3 | 17 |
| **H2a** Densa + párrafos (≤85 pal.) − Densa (baseline 300/50) | -0.067 | [-0.139, -0.000] | 0.125 | 0.625 | 2/9/6 | 17 |
| **H2b** Densa + ventana 64 (control) − Densa (baseline 300/50) | -0.065 | [-0.165, +0.042] | 0.264 | 0.951 | 4/3/10 | 17 |
| **H2c** Densa + párrafos (≤85 pal.) − Densa + ventana 64 (control) | -0.002 | [-0.106, +0.097] | 1.000 | 1.000 | 5/8/4 | 17 |
| **H3** BM25 simple − Densa (baseline 300/50) | -0.056 | [-0.138, +0.026] | 0.238 | 0.951 | 5/4/8 | 17 |
| **Hy1** Híbrida RRF (denso + BM25 simple) − Densa (baseline 300/50) | +0.044 | [-0.031, +0.117] | 0.281 | 0.951 | 6/9/2 | 17 |
| **Hy2** Híbrida RRF (denso + BM25 simple) − BM25 simple | +0.100 | [+0.016, +0.186] | 0.047 | 0.326 | 9/4/4 | 17 |

</details>

<details><summary>Contrastes en Hit@5 (exploratorios)</summary>

| Contraste | Diferencia (A−B) | IC 95 % | p (permutación) | p Holm | A gana / empata / pierde | n |
|---|---|---|---|---|---|---|
| **H1** BM25 + lemas + stopwords − BM25 simple | +0.176 | [+0.000, +0.353] | 0.250 | 1.000 | 3/14/0 | 17 |
| **H2a** Densa + párrafos (≤85 pal.) − Densa (baseline 300/50) | -0.176 | [-0.353, +0.000] | 0.250 | 1.000 | 0/14/3 | 17 |
| **H2b** Densa + ventana 64 (control) − Densa (baseline 300/50) | -0.235 | [-0.471, -0.059] | 0.125 | 0.875 | 0/13/4 | 17 |
| **H2c** Densa + párrafos (≤85 pal.) − Densa + ventana 64 (control) | +0.059 | [-0.118, +0.235] | 1.000 | 1.000 | 2/14/1 | 17 |
| **H3** BM25 simple − Densa (baseline 300/50) | -0.176 | [-0.412, +0.059] | 0.375 | 1.000 | 1/12/4 | 17 |
| **Hy1** Híbrida RRF (denso + BM25 simple) − Densa (baseline 300/50) | -0.059 | [-0.176, +0.000] | 1.000 | 1.000 | 0/16/1 | 17 |
| **Hy2** Híbrida RRF (denso + BM25 simple) − BM25 simple | +0.118 | [-0.176, +0.412] | 0.688 | 1.000 | 4/11/2 | 17 |

</details>

<details><summary>Contrastes en MRR (exploratorios)</summary>

| Contraste | Diferencia (A−B) | IC 95 % | p (permutación) | p Holm | A gana / empata / pierde | n |
|---|---|---|---|---|---|---|
| **H1** BM25 + lemas + stopwords − BM25 simple | +0.181 | [-0.001, +0.365] | 0.086 | 0.430 | 9/6/2 | 17 |
| **H2a** Densa + párrafos (≤85 pal.) − Densa (baseline 300/50) | -0.131 | [-0.332, +0.066] | 0.232 | 0.836 | 4/7/6 | 17 |
| **H2b** Densa + ventana 64 (control) − Densa (baseline 300/50) | -0.151 | [-0.364, +0.061] | 0.209 | 0.836 | 3/6/8 | 17 |
| **H2c** Densa + párrafos (≤85 pal.) − Densa + ventana 64 (control) | +0.020 | [-0.147, +0.157] | 1.000 | 1.000 | 3/13/1 | 17 |
| **H3** BM25 simple − Densa (baseline 300/50) | -0.237 | [-0.426, -0.058] | 0.027 | 0.191 | 4/4/9 | 17 |
| **Hy1** Híbrida RRF (denso + BM25 simple) − Densa (baseline 300/50) | +0.021 | [-0.164, +0.215] | 0.838 | 1.000 | 5/7/5 | 17 |
| **Hy2** Híbrida RRF (denso + BM25 simple) − BM25 simple | +0.258 | [+0.020, +0.490] | 0.057 | 0.343 | 10/2/5 | 17 |

</details>

<details><summary>Contrastes en Densidad de evidencia (exploratorios)</summary>

| Contraste | Diferencia (A−B) | IC 95 % | p (permutación) | p Holm | A gana / empata / pierde | n |
|---|---|---|---|---|---|---|
| **H1** BM25 + lemas + stopwords − BM25 simple | +0.011 | [-0.004, +0.025] | 0.178 | 0.712 | 8/2/7 | 17 |
| **H2a** Densa + párrafos (≤85 pal.) − Densa (baseline 300/50) | +0.090 | [+0.049, +0.131] | 0.001 | 0.006 | 13/1/3 | 17 |
| **H2b** Densa + ventana 64 (control) − Densa (baseline 300/50) | +0.103 | [+0.045, +0.173] | 0.003 | 0.017 | 12/1/4 | 17 |
| **H2c** Densa + párrafos (≤85 pal.) − Densa + ventana 64 (control) | -0.013 | [-0.064, +0.040] | 0.629 | 1.000 | 5/3/9 | 17 |
| **H3** BM25 simple − Densa (baseline 300/50) | +0.004 | [-0.013, +0.024] | 0.717 | 1.000 | 7/1/9 | 17 |
| **Hy1** Híbrida RRF (denso + BM25 simple) − Densa (baseline 300/50) | +0.016 | [+0.001, +0.033] | 0.073 | 0.365 | 8/4/5 | 17 |
| **Hy2** Híbrida RRF (denso + BM25 simple) − BM25 simple | +0.012 | [-0.010, +0.035] | 0.333 | 0.999 | 9/1/7 | 17 |

</details>

#### Por tipo de pregunta (Recall de evidencia)

| Configuración | causalidad (n=4) | comparativa (n=3) | factual (n=5) | multihop (n=2) | relacional (n=3) |
|---|---|---|---|---|---|
| Densa (baseline 300/50) | 0.20 | 0.13 | 0.25 | 0.18 | 0.16 |
| Densa + párrafos (≤85 pal.) | 0.20 | 0.10 | 0.14 | 0.12 | 0.11 |
| Densa + ventana 64 (control) | 0.20 | 0.11 | 0.18 | 0.17 | 0.11 |
| BM25 simple | 0.14 | 0.09 | 0.26 | 0.12 | 0.25 |
| BM25 + lemas + stopwords | 0.21 | 0.15 | 0.32 | 0.12 | 0.35 |
| Híbrida RRF (denso + BM25 simple) | 0.25 | 0.21 | 0.28 | 0.12 | 0.18 |

#### H3 — según el solapamiento léxico entre la pregunta y su evidencia

Fracción de lemas de contenido de la pregunta presentes en sus oraciones de evidencia; corte en la mediana (0.67). Alto = 8 preguntas, bajo = 9.

| Grupo | Contraste | Diferencia Recall | IC 95 % | n |
|---|---|---|---|---|
| Alto solapamiento | BM25 + lemas + stopwords − BM25 simple | +0.083 | [+0.000, +0.168] | 8 |
| Alto solapamiento | BM25 simple − Densa (baseline 300/50) | -0.004 | [-0.066, +0.069] | 8 |
| Bajo solapamiento | BM25 + lemas + stopwords − BM25 simple | +0.045 | [-0.065, +0.160] | 9 |
| Bajo solapamiento | BM25 simple − Densa (baseline 300/50) | -0.014 | [-0.155, +0.124] | 9 |

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

n = 17 preguntas no trampa anotadas con ≥1 evidencia (F1, F2, F3, F4, F5, C1, C2, C3, C4, V1, V2, V3, R1, R2, R3, M1, M2).

| Configuración | P@5 | Hit@5 | MRR | Recall@5 (evidencia) | Densidad de evidencia | n |
|---|---|---|---|---|---|---|
| Densa (baseline 300/50) | 0.33 [0.24, 0.43] | 0.94 [0.82, 1.00] | 0.66 [0.48, 0.84] | 0.19 [0.14, 0.25] | 0.04 [0.03, 0.05] | 17 |
| Densa + párrafos (≤85 pal.) | 0.14 [0.08, 0.21] | 0.88 [0.71, 1.00] | 0.54 [0.37, 0.72] | 0.32 [0.23, 0.42] | 0.07 [0.04, 0.10] | 17 |
| Densa + ventana 64 (control) | 0.12 [0.08, 0.18] | 1.00 [1.00, 1.00] | 0.53 [0.36, 0.71] | 0.30 [0.23, 0.37] | 0.06 [0.04, 0.09] | 17 |
| BM25 simple | 0.28 [0.18, 0.38] | 0.76 [0.53, 0.94] | 0.42 [0.26, 0.60] | 0.18 [0.10, 0.28] | 0.04 [0.02, 0.06] | 17 |
| BM25 + lemas + stopwords | 0.39 [0.28, 0.50] | 0.94 [0.82, 1.00] | 0.60 [0.45, 0.75] | 0.25 [0.18, 0.31] | 0.05 [0.03, 0.07] | 17 |
| Híbrida RRF (denso + BM25 simple) | 0.38 [0.26, 0.49] | 0.88 [0.71, 1.00] | 0.68 [0.50, 0.85] | 0.22 [0.15, 0.31] | 0.05 [0.03, 0.08] | 17 |

#### Contrastes planeados (primaria: Recall@5 (evidencia))

| Contraste | Diferencia (A−B) | IC 95 % | p (permutación) | p Holm | A gana / empata / pierde | n |
|---|---|---|---|---|---|---|
| **H1** BM25 + lemas + stopwords − BM25 simple | +0.063 | [-0.006, +0.133] | 0.109 | 0.547 | 6/9/2 | 17 |
| **H2a** Densa + párrafos (≤85 pal.) − Densa (baseline 300/50) | +0.132 | [+0.052, +0.210] | 0.008 | 0.047 | 9/7/1 | 17 |
| **H2b** Densa + ventana 64 (control) − Densa (baseline 300/50) | +0.107 | [+0.046, +0.171] | 0.006 | 0.041 | 9/7/1 | 17 |
| **H2c** Densa + párrafos (≤85 pal.) − Densa + ventana 64 (control) | +0.025 | [-0.046, +0.101] | 0.516 | 1.000 | 6/8/3 | 17 |
| **H3** BM25 simple − Densa (baseline 300/50) | -0.009 | [-0.088, +0.069] | 0.833 | 1.000 | 6/4/7 | 17 |
| **Hy1** Híbrida RRF (denso + BM25 simple) − Densa (baseline 300/50) | +0.032 | [-0.021, +0.084] | 0.260 | 1.000 | 7/7/3 | 17 |
| **Hy2** Híbrida RRF (denso + BM25 simple) − BM25 simple | +0.041 | [-0.036, +0.117] | 0.325 | 1.000 | 8/5/4 | 17 |

<details><summary>Contrastes en P@5 (exploratorios)</summary>

| Contraste | Diferencia (A−B) | IC 95 % | p (permutación) | p Holm | A gana / empata / pierde | n |
|---|---|---|---|---|---|---|
| **H1** BM25 + lemas + stopwords − BM25 simple | +0.109 | [+0.009, +0.218] | 0.090 | 0.359 | 7/7/3 | 17 |
| **H2a** Densa + párrafos (≤85 pal.) − Densa (baseline 300/50) | -0.193 | [-0.260, -0.127] | 0.000 | 0.000 | 0/1/16 | 17 |
| **H2b** Densa + ventana 64 (control) − Densa (baseline 300/50) | -0.208 | [-0.281, -0.140] | 0.000 | 0.000 | 1/0/16 | 17 |
| **H2c** Densa + párrafos (≤85 pal.) − Densa + ventana 64 (control) | +0.015 | [-0.011, +0.040] | 0.270 | 0.713 | 11/2/4 | 17 |
| **H3** BM25 simple − Densa (baseline 300/50) | -0.056 | [-0.138, +0.026] | 0.238 | 0.713 | 5/4/8 | 17 |
| **Hy1** Híbrida RRF (denso + BM25 simple) − Densa (baseline 300/50) | +0.044 | [-0.031, +0.117] | 0.281 | 0.713 | 6/9/2 | 17 |
| **Hy2** Híbrida RRF (denso + BM25 simple) − BM25 simple | +0.100 | [+0.016, +0.186] | 0.047 | 0.233 | 9/4/4 | 17 |

</details>

<details><summary>Contrastes en Hit@5 (exploratorios)</summary>

| Contraste | Diferencia (A−B) | IC 95 % | p (permutación) | p Holm | A gana / empata / pierde | n |
|---|---|---|---|---|---|---|
| **H1** BM25 + lemas + stopwords − BM25 simple | +0.176 | [+0.000, +0.353] | 0.250 | 1.000 | 3/14/0 | 17 |
| **H2a** Densa + párrafos (≤85 pal.) − Densa (baseline 300/50) | -0.059 | [-0.176, +0.000] | 1.000 | 1.000 | 0/16/1 | 17 |
| **H2b** Densa + ventana 64 (control) − Densa (baseline 300/50) | +0.059 | [+0.000, +0.176] | 1.000 | 1.000 | 1/16/0 | 17 |
| **H2c** Densa + párrafos (≤85 pal.) − Densa + ventana 64 (control) | -0.118 | [-0.294, +0.000] | 0.500 | 1.000 | 0/15/2 | 17 |
| **H3** BM25 simple − Densa (baseline 300/50) | -0.176 | [-0.412, +0.059] | 0.375 | 1.000 | 1/12/4 | 17 |
| **Hy1** Híbrida RRF (denso + BM25 simple) − Densa (baseline 300/50) | -0.059 | [-0.176, +0.000] | 1.000 | 1.000 | 0/16/1 | 17 |
| **Hy2** Híbrida RRF (denso + BM25 simple) − BM25 simple | +0.118 | [-0.176, +0.412] | 0.688 | 1.000 | 4/11/2 | 17 |

</details>

<details><summary>Contrastes en MRR (exploratorios)</summary>

| Contraste | Diferencia (A−B) | IC 95 % | p (permutación) | p Holm | A gana / empata / pierde | n |
|---|---|---|---|---|---|---|
| **H1** BM25 + lemas + stopwords − BM25 simple | +0.181 | [-0.001, +0.365] | 0.086 | 0.430 | 9/6/2 | 17 |
| **H2a** Densa + párrafos (≤85 pal.) − Densa (baseline 300/50) | -0.117 | [-0.316, +0.075] | 0.277 | 1.000 | 4/7/6 | 17 |
| **H2b** Densa + ventana 64 (control) − Densa (baseline 300/50) | -0.127 | [-0.335, +0.080] | 0.265 | 1.000 | 4/5/8 | 17 |
| **H2c** Densa + párrafos (≤85 pal.) − Densa + ventana 64 (control) | +0.010 | [-0.128, +0.127] | 0.969 | 1.000 | 3/10/4 | 17 |
| **H3** BM25 simple − Densa (baseline 300/50) | -0.237 | [-0.426, -0.058] | 0.027 | 0.191 | 4/4/9 | 17 |
| **Hy1** Híbrida RRF (denso + BM25 simple) − Densa (baseline 300/50) | +0.021 | [-0.164, +0.215] | 0.838 | 1.000 | 5/7/5 | 17 |
| **Hy2** Híbrida RRF (denso + BM25 simple) − BM25 simple | +0.258 | [+0.020, +0.490] | 0.057 | 0.343 | 10/2/5 | 17 |

</details>

<details><summary>Contrastes en Densidad de evidencia (exploratorios)</summary>

| Contraste | Diferencia (A−B) | IC 95 % | p (permutación) | p Holm | A gana / empata / pierde | n |
|---|---|---|---|---|---|---|
| **H1** BM25 + lemas + stopwords − BM25 simple | +0.011 | [-0.004, +0.025] | 0.178 | 0.712 | 8/2/7 | 17 |
| **H2a** Densa + párrafos (≤85 pal.) − Densa (baseline 300/50) | +0.033 | [+0.009, +0.060] | 0.027 | 0.191 | 11/1/5 | 17 |
| **H2b** Densa + ventana 64 (control) − Densa (baseline 300/50) | +0.025 | [+0.004, +0.050] | 0.045 | 0.271 | 11/0/6 | 17 |
| **H2c** Densa + párrafos (≤85 pal.) − Densa + ventana 64 (control) | +0.008 | [-0.005, +0.021] | 0.271 | 0.814 | 10/0/7 | 17 |
| **H3** BM25 simple − Densa (baseline 300/50) | +0.004 | [-0.013, +0.024] | 0.717 | 0.814 | 7/1/9 | 17 |
| **Hy1** Híbrida RRF (denso + BM25 simple) − Densa (baseline 300/50) | +0.016 | [+0.001, +0.033] | 0.073 | 0.365 | 8/4/5 | 17 |
| **Hy2** Híbrida RRF (denso + BM25 simple) − BM25 simple | +0.012 | [-0.010, +0.035] | 0.333 | 0.814 | 9/1/7 | 17 |

</details>

#### Por tipo de pregunta (Recall de evidencia)

| Configuración | causalidad (n=4) | comparativa (n=3) | factual (n=5) | multihop (n=2) | relacional (n=3) |
|---|---|---|---|---|---|
| Densa (baseline 300/50) | 0.20 | 0.13 | 0.25 | 0.18 | 0.16 |
| Densa + párrafos (≤85 pal.) | 0.24 | 0.33 | 0.35 | 0.31 | 0.40 |
| Densa + ventana 64 (control) | 0.24 | 0.31 | 0.32 | 0.35 | 0.30 |
| BM25 simple | 0.14 | 0.09 | 0.26 | 0.12 | 0.25 |
| BM25 + lemas + stopwords | 0.21 | 0.15 | 0.32 | 0.12 | 0.35 |
| Híbrida RRF (denso + BM25 simple) | 0.25 | 0.21 | 0.28 | 0.12 | 0.18 |

#### H3 — según el solapamiento léxico entre la pregunta y su evidencia

Fracción de lemas de contenido de la pregunta presentes en sus oraciones de evidencia; corte en la mediana (0.67). Alto = 8 preguntas, bajo = 9.

| Grupo | Contraste | Diferencia Recall | IC 95 % | n |
|---|---|---|---|---|
| Alto solapamiento | BM25 + lemas + stopwords − BM25 simple | +0.083 | [+0.000, +0.168] | 8 |
| Alto solapamiento | BM25 simple − Densa (baseline 300/50) | -0.004 | [-0.066, +0.069] | 8 |
| Bajo solapamiento | BM25 + lemas + stopwords − BM25 simple | +0.045 | [-0.065, +0.160] | 9 |
| Bajo solapamiento | BM25 simple − Densa (baseline 300/50) | -0.014 | [-0.155, +0.124] | 9 |

## 5. Validez del proxy frente a la anotación humana

Correlación de Pearson entre la cobertura de puntos clave y el Recall humano (Vista A; pares configuración × pregunta, n = 102): **r = 0.39**. Si es baja, los resultados con proxy no deben interpretarse.

## 6. Preguntas trampa (análisis aparte, no entran en los promedios)

| Pregunta | Densa (baseline 300/50) | Densa + párrafos (≤85 pal.) | Densa + ventana 64 (control) | BM25 simple | BM25 + lemas + stopwords | Híbrida RRF (denso + BM25 simple) |
|---|---|---|---|---|---|---|
| T1: ¿Quién es el presidente actual de México? | 0.69 | 0.74 | 0.70 | 16.29 | 8.28 | 0.01 |
| T2: ¿Cuál es el PIB actual de México? | 0.64 | 0.65 | 0.64 | 17.88 | 8.49 | 0.02 |
| T3: ¿Qué equipos jugaron la final del fútbol mexicano en 2024? | 0.58 | 0.64 | 0.69 | 19.83 | 8.10 | 0.02 |

Puntaje del primer resultado (no comparable entre métodos: coseno 0–1, BM25 sin cota, RRF ≈ 0.01). Ninguna configuración tiene un umbral de rechazo; el puntaje de una trampa solo se puede juzgar contra el de las preguntas con respuesta (tarea de la fase de generación/rechazo, fuera de este experimento).

