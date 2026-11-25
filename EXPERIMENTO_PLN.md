# Experimento de PLN — recuperación léxica vs. densa en español

**Efecto del preprocesamiento y la segmentación.** Bloque experimental para el proyecto del curso de PLN, diseñado para reutilizarse en la Fase 2 de la tesis (ver §9).

**Estado (24/11/2026):** corridas hechas y verificadas (reproducibles), herramientas probadas y **anotación humana completa** (20 preguntas, 168 oraciones de evidencia). Resultados definitivos en §7 (n = 17, un solo anotador). Pendientes: sensibilidad al umbral de cobertura, análisis de errores, consistencia de la anotación y reporte (§10).

---

## 1. Qué se evalúa

Solo **recuperación** (sin generación): ¿qué texto entrega cada configuración para cada pregunta? Corpus: 19 archivos de Wikipedia sobre la historia de México; 20 preguntas de `evaluation/questions.json` (17 con respuesta + 3 trampa).

| Configuración | Archivo | Qué cambia respecto al baseline |
|---|---|---|
| Densa (baseline) | `configs/cosine.yaml` | — (ventana 300/50 palabras, MiniLM multilingüe, FAISS exacto) |
| Densa + párrafos | `configs/cosine_paragraph.yaml` | segmentación por párrafos, ≤ 85 palabras |
| Densa + ventana 64 | `configs/cosine_fixed64.yaml` | **control**: ventana fija de 64 palabras sin traslape |
| BM25 simple | `configs/bm25.yaml` | recuperador léxico (minúsculas + `\w+`) |
| BM25 + lemas + stopwords | `configs/bm25_lemma.yaml` | spaCy `es_core_news_sm`: lematización y lista estándar de palabras vacías |
| Híbrida RRF | `configs/hybrid.yaml` | densa + BM25 simple, fusión por rangos (k = 60, 0.5/0.5) |

**Hipótesis (fijadas antes de ver resultados con anotación humana):**
- **H1.** Lematizar y quitar palabras vacías mejora BM25 (BM25 + lemas − BM25 simple > 0).
- **H2.** Parte del efecto de segmentar por párrafos se explica solo por el **tamaño** del chunk. Se descompone con el control: tamaño (ventana 64 − baseline), estructura (párrafos − ventana 64) y total (párrafos − baseline).
- **H3.** La búsqueda léxica gana a la densa cuando la pregunta comparte vocabulario con su evidencia (datos, nombres, fechas) y pierde cuando la parafrasea.

## 2. Corpus fijado (versión de documentos)

`python evaluation/evidence.py` imprime el inventario; `analisis.md` §0 lo registra.

- **19 archivos, 18 artículos únicos** (298 638 palabras únicas). `Independencia_de_México.txt` y `Guerra_de_Independencia_de_México.txt` son idénticos byte a byte (mismo SHA-256).
- **Decisión:** el duplicado **no se borra** (para no invalidar las corridas ya hechas). Se trata como un solo artículo al evaluar: un chunk de la copia se proyecta al artículo canónico y los chunks idénticos cuentan una vez. El costo se reporta: 8/100 posiciones del top-5 del baseline las ocupa una copia exacta (5–8 en las densas, 1–2 en las léxicas).
- **Anomalía:** `Tenochtitlan.txt` tiene 51 palabras (artículo casi vacío). No se corrigió; está declarado.
- Se verificó que las **seis recuperaciones son deterministas**: dos corridas independientes dan el mismo top-5 (ids y orden) en 20/20 preguntas por configuración.

## 3. Protocolo de evaluación

### 3.1 Evidencia por oración, no por chunk
Cada oración del corpus tiene un id estable `articulo#inicio-fin` (offsets de palabra). La anotación marca **oraciones**; así no depende de cómo se parta el texto y vale para comparar chunkings distintos (y para configuraciones futuras como el reranking). Reglas en el encabezado de la hoja de anotación.

### 3.2 De oraciones a métricas de chunk
Un chunk **cubre** una oración si contiene ≥ 50 % de sus palabras. Por pregunta y configuración (chunks **distintos** del top-5):

| Métrica | Definición |
|---|---|
| P@n | chunks que cubren ≥ 1 oración de evidencia / chunks distintos |
| Hit@n | ¿algún chunk cubre evidencia? |
| MRR | 1 / posición del primer chunk relevante |
| **Recall (primaria)** | oraciones de evidencia cubiertas por la unión de los chunks / total de evidencia anotada |
| Densidad | palabras de evidencia recuperadas / palabras recuperadas |

A diferencia de las hojas por chunk de la tesis, el total de evidencia sale de la anotación y **no de una estimación**; eso resuelve el problema de Recall inflado del baseline.

### 3.3 Dos vistas, por una razón
Con k = 5, cinco chunks de 300 palabras entregan ≈ 1 450 palabras y cinco de ~65 entregan ≈ 320. Comparar así mezcla *cómo se segmenta* con *cuánto texto se entrega*.
- **Vista A (k = 5):** protocolo de la tesis.
- **Vista B (presupuesto igual, ≈ 1 450 palabras):** cada configuración entrega sus mejores chunks distintos hasta acumular el mismo texto (los chunks chicos entran con k ≈ 22–23; se corrió top-50 en `run1_deep`). Aquí P@5 deja de ser comparable y se usa P@n.

### 3.4 Estadística
n = 17 preguntas. Intervalos de confianza **bootstrap sobre preguntas** (10 000, semilla 12345); contrastes pareados con prueba de permutación por cambio de signo (exacta) y **corrección de Holm** sobre los 7 contrastes planeados, con una métrica primaria por tipo de gold (Recall con anotación humana; cobertura de puntos clave con el proxy). El resto de métricas son exploratorias. Con n = 17 solo se detectan diferencias grandes; los intervalos anchos son un resultado, no un defecto.

### 3.5 Preguntas trampa
Fuera de los promedios. Se reporta el puntaje del primer resultado (§6 de `analisis.md`). T1 («presidente actual») sí tiene respuesta en el corpus; la anotación lo decide.

## 4. Decisiones que tomé por defecto (cámbialas si no te convencen)

| Decisión | Elegí | Alternativa | Si la cambias |
|---|---|---|---|
| Unidad de anotación | Oración (opción B) | Chunk por familia de chunking | Habría que rehacer pool y métricas; la anotación sería válida solo para el curso |
| Duplicado | Tratarlo como uno al evaluar | Borrarlo del corpus | Hay que re-correr las 6 configs (~5 min) y reindexar; las hojas de tesis ya anotadas quedarían desalineadas |
| Híbrida | Incluida, con BM25 **simple** (como en la Config. 2 de la tesis) | Versión con BM25 lematizado | Es un contraste exploratorio extra; decidirlo después de ver resultados sería analizar con flexibilidad |
| Lista de stopwords | Estándar de spaCy, sin ajustar | Ajustada a las preguntas | Ajustarla con las mismas 20 preguntas sería sobreajustar |
| Umbral de cobertura | 50 % de palabras de la oración | 100 % / cualquier traslape | Se cambia en `EvidenceIndex(min_cover=...)`; conviene reportarlo como análisis de sensibilidad |

## 5. Cómo reproducirlo

```bash
# recuperación de las 6 configs (sin Ollama; ~1 min cada una por cargar modelos)
for c in cosine cosine_paragraph cosine_fixed64 bm25 bm25_lemma hybrid; do
  python evaluation/evaluador.py --config configs/$c.yaml --retrieval-only --out results/pln/run1/$c
done
# presupuesto igual: más profundidad para los chunks chicos
for c in cosine_paragraph cosine_fixed64; do
  python evaluation/evaluador.py --config configs/$c.yaml --retrieval-only --top-k 50 --out results/pln/run1_deep/$c
done
python evaluation/pln_pool.py                                  # oraciones candidatas + hoja de anotación
python evaluation/pln_metrics.py --determinism results/pln/run2  # métricas, estadística, results/pln/analisis.md
python evaluation/test_pln.py                                  # pruebas con resultado conocido
```

(`python` = `./venv/Scripts/python.exe`.) Los registros de recuperación ahora guardan `chunk_id` y offsets.

## 6. La anotación (hecha; instrucciones conservadas para repetirla)

> **Estado:** completa para las 20 preguntas. Para re-anotar un subconjunto (consistencia intra-anotador) se usa la misma hoja en una copia, sin consultar la anterior.

Archivo: **`results/pln/anotacion_evidencia.md`** — 741 oraciones candidatas en 20 preguntas (30–43 por pregunta). Marca `[x]` en *Evidencia* y marca **Anotada** al terminar cada pregunta. Las reglas están en el encabezado de la hoja.

- Orden sugerido: primero las 17 preguntas con respuesta (todo el análisis principal se calcula con esas), después T1–T3.
- Estimación: ~10 s por oración → 1.5–2 h en total.
- Se pueden analizar avances parciales: `pln_metrics.py` solo usa las preguntas marcadas como anotadas.
- Las oraciones están ordenadas por artículo y posición, **sin indicar de qué método salieron**, para no sesgarte.
- **Después de anotar:** `python evaluation/pln_metrics.py` llena la sección humana sola.

El pool se armó con: top-8 por búsqueda densa, BM25 simple y BM25 lematizado sobre las **oraciones** del corpus, oraciones con puntos clave, y la mejor oración de cada chunk que alguna configuración recuperó. Lo que no aparece en la hoja se asume no relevante (supuesto estándar de *pooling*); si ves evidencia faltante, añade una fila con su `Ref`.

## 7. Resultados (con anotación humana)

Evidencia anotada por oración sobre las 20 preguntas (única anotadora: Jesús). Las 17 preguntas con respuesta suman **168 oraciones de evidencia** (media 9.8, mediana 8, mín. 3, máx. 28; V1 = 23 y V2 = 28 son las extremas). T1 tiene 1 oración de evidencia en el corpus; T2 y T3 ninguna. Tablas completas con IC y contrastes en `results/pln/analisis.md` y `results/pln/metricas.json`.

**Qué se afirma sin depender de la anotación (descriptivo):**
- Chunks que exceden los 128 tokens del modelo de embeddings: **100 %** en el baseline, 14 % con párrafos, 1 % con ventana 64.
- Recuperación determinista en las seis configuraciones (20/20 preguntas con el mismo top-5 en dos corridas).
- Lematizar cambia mucho qué se recupera: el top-5 de BM25 simple y BM25 lematizado es **idéntico en 0/20 preguntas** (Jaccard medio 0.35).
- La lista estándar de palabras vacías elimina «último» de «¿Quién fue el último emperador azteca?» (F5). Con la anotación: BM25 simple y BM25 lematizado obtienen el mismo Recall en F5 (0.25), así que quitar «último» no la perjudicó; la densa y la híbrida obtienen 0.
- Latencia de recuperación (mediana, sin la primera pregunta): densas 18–22 ms, BM25 2.5 ms, BM25 lematizado 4 ms (incluye lematizar la consulta), híbrida 24 ms.

### 7.1 Métricas humanas (n = 17; media [IC 95 % bootstrap])

**Vista A (k = 5 chunks):**

| Configuración | P@5 | Hit@5 | MRR | Recall de evidencia (primaria) | Densidad |
|---|---|---|---|---|---|
| Densa baseline (300/50) | 0.33 | 0.94 | 0.66 | 0.19 [0.14, 0.25] | 0.04 |
| Densa + párrafos | 0.27 | 0.76 | 0.53 | 0.14 [0.09, 0.20] | 0.13 |
| Densa + ventana 64 | 0.27 | 0.71 | 0.51 | 0.16 [0.09, 0.25] | 0.14 |
| BM25 simple | 0.28 | 0.76 | 0.42 | 0.18 [0.10, 0.28] | 0.04 |
| BM25 + lemas + stopwords | 0.39 | 0.94 | 0.60 | 0.25 [0.18, 0.31] | 0.05 |
| Híbrida RRF | 0.38 | 0.88 | 0.68 | 0.22 [0.15, 0.31] | 0.05 |

**Vista B (mismo presupuesto de contexto, ≈ 1 450 palabras).** Solo cambian las dos configuraciones de chunks chicos; el resto coincide con la Vista A:

| Configuración | P@n | Hit | MRR | Recall de evidencia (primaria) | Densidad |
|---|---|---|---|---|---|
| Densa + párrafos (22 chunks) | 0.14 | 0.88 | 0.54 | **0.32** [0.23, 0.42] | 0.07 |
| Densa + ventana 64 (23 chunks) | 0.12 | 1.00 | 0.53 | **0.30** [0.23, 0.37] | 0.06 |

El Recall absoluto es bajo (0.14–0.32) porque cada pregunta tiene en promedio unas 10 oraciones de evidencia y solo se recupera una cantidad fija de texto; se interpreta en términos relativos.

### 7.2 Contrastes planeados sobre el Recall (p Holm sobre 7 contrastes)

| Contraste | Vista A | p Holm | Vista B | p Holm |
|---|---|---|---|---|
| **H1** BM25 lemas − BM25 simple | +0.063 [−0.006, +0.133] | 0.656 | igual | 0.547 |
| **H2a** párrafos − baseline (efecto total) | −0.052 [−0.104, −0.010] | 0.438 | **+0.132 [+0.052, +0.210]** | **0.047** |
| **H2b** ventana 64 − baseline (solo tamaño) | −0.032 [−0.106, +0.047] | 1.000 | **+0.107 [+0.046, +0.171]** | **0.041** |
| **H2c** párrafos − ventana 64 (estructura) | −0.020 [−0.125, +0.063] | 1.000 | +0.025 [−0.046, +0.101] | 1.000 |
| **H3** BM25 simple − densa | −0.009 [−0.088, +0.069] | 1.000 | igual | 1.000 |
| **Hy1** híbrida − densa | +0.032 [−0.021, +0.084] | 1.000 | igual | 1.000 |
| **Hy2** híbrida − BM25 simple | +0.041 [−0.036, +0.117] | 1.000 | igual | 1.000 |

### 7.3 Lectura por hipótesis

- **H2 (segmentación y tamaño): hay efecto y es de tamaño, no de estructura.** Con k = 5 los chunks chicos no ganan en Recall porque entregan ≈ 4.5 veces menos texto. A igual contexto recuperan más evidencia que el baseline (H2a +0.132, H2b +0.107; ganan 9, empatan 7, pierden 1), y párrafos frente a ventana de 64 no se distingue de cero (H2c). Respetar la estructura de párrafos no aporta más que usar chunks chicos. **Contrapartida:** a igual contexto la precisión cae (P@n 0.33 → 0.14 y 0.12, peor en 16 de 17 preguntas, exploratorio). La densidad por palabra recuperada mejora con k = 5 (0.04 → 0.13 y 0.14, Holm 0.006 y 0.017). Significativo por poco tras Holm y con n = 17: evidencia a favor, no resultado cerrado.
- **H1 (lemas): tendencia, no confirmada.** Recall +0.063 (6 gana, 9 empatan, 2 pierden). En Hit@5 mejora en 3 preguntas, empata en 14 y no empeora en ninguna; P@5 +0.109 [+0.009, +0.218]; MRR +0.18 (exploratorios). La dirección es consistente, pero n = 17 no alcanza tras Holm.
- **H3 (léxica vs. densa): no se sostiene.** El Recall es prácticamente igual (−0.009) y separar las preguntas por solapamiento léxico con su evidencia (alto n = 8, bajo n = 9; mediana 0.67) no cambia el resultado. La densa pone antes el primer resultado relevante (MRR −0.24 a favor de la densa, p = 0.027 sin corregir, Holm 0.19; exploratorio).
- **Híbrida:** sin diferencias significativas; MRR numéricamente más alto (0.68). BM25 lematizado tiene el mejor Recall con k = 5 (0.25).
- **Por tipo de pregunta (ilustrativo, 2–5 casos por tipo):** BM25 lematizado es mejor en relacionales (0.35) y factuales (0.32); la híbrida en causalidad (0.25) y comparativas (0.21).

### 7.4 Validez del proxy: descartado

La cobertura de puntos clave (proxy) correlaciona **r = 0.39** con el Recall humano (n = 102 pares configuración × pregunta). Además falla donde importa: a igual contexto el proxy daba H2a = −0.03 y la anotación humana da **+0.132**. Los resultados con proxy de versiones anteriores de este documento y de `presentacion_pln.html` quedan **retirados**; no deben citarse. El proxy solo se conserva como diagnóstico de pipeline.

### 7.5 Preguntas trampa

Ninguna configuración tiene umbral de rechazo y los puntajes del primer resultado no son comparables entre métodos (coseno 0–1, BM25 sin cota, RRF ≈ 0.01). T1 sí tiene una oración de evidencia en el corpus (juramentación de la presidenta, 1 de octubre de 2024), así que su estatus como «trampa» depende de la fecha de corte del corpus. El rechazo es tarea de la fase de generación (tesis).

## 8. Amenazas a la validez

1. **n = 17** y 5 tipos de pregunta con 2–5 casos cada uno: el análisis por tipo es ilustrativo.
2. **Un solo anotador** (tú). No hay acuerdo entre anotadores ni se ha medido la consistencia intra-anotador. Mitigación posible: re-anotar ~3 preguntas sin mirar la anotación previa, o que otra persona anote 5–6 y reportar acuerdo (κ).
3. **Sesgo del pooling:** la evidencia que ningún método propuso queda sin juzgar; favorece a métodos parecidos a los del pool.
4. **Un solo modelo de embeddings** (MiniLM, 128 tokens) y un lematizador pequeño (`es_core_news_sm`); no hay conclusiones sobre «lo denso» en general. No se revisó la calidad de la lematización más allá de ejemplos (p. ej. «tlaxcaltecas» → «tlaxcalteca», «mexicana» → «mexicano»).
5. **Un solo corpus** de dominio histórico-enciclopédico; fechas y nombres propios favorecen lo léxico.
6. **La segmentación en oraciones es heurística** (abreviaturas conocidas; «a. C.» seguido de mayúscula une dos oraciones). Probada con casos sintéticos, no auditada sobre todo el corpus.
7. **Supuestos de la métrica:** el umbral de cobertura (50 %) y la definición de densidad son decisiones del diseño; hace falta un análisis de sensibilidad.
8. **Hiperparámetros sin ajustar** (k de RRF, fusion_depth, 85 palabras): ajustarlos con estas 20 preguntas sería sobreajustar.

## 9. Relación con la tesis

| Pieza | Uso en el curso | Uso en la tesis |
|---|---|---|
| Configs párrafos, ventana 64, BM25, híbrida | contrastes H1–H3 | Config. 1 (chunking), control reconocido por el revisor, Config. 2 (híbrida) |
| BM25 + lemas | H1 | extiende el eje de representación; contenido nuevo para el comparativo de Fase 2 |
| Evidencia por oración | gold de este experimento | gold reutilizable para reranking y futuras configs; resuelve el Recall estimado |
| `evidence.py`, `pln_*.py`, `--retrieval-only`, corpus fijado | herramientas | framework de la Fase 1/2; corpus versionado pedido por el revisor |
| Generación, Faithfulness, juez LLM, producto | — | quedan solo en la tesis |

La reutilización debe **declararse por escrito** al profesor del curso y al director. El reporte del curso debe ser un artículo propio (introducción, método, resultados, discusión); este documento es el protocolo, no el reporte.

## 10. Pendiente

1. ~~Anotar (§6)~~ **Hecho.**
2. ~~Re-correr `pln_metrics.py` y validar el proxy~~ **Hecho:** r = 0.39, proxy descartado (§7.4).
3. Análisis de sensibilidad del umbral de cobertura (30 %, 50 %, 100 %); re-anotación de ~3 preguntas (consistencia) o acuerdo entre anotadores en un subconjunto.
4. Análisis cualitativo de errores (qué preguntas pierde cada método y por qué).
5. Redactar el reporte del curso con las tablas de `analisis.md`.
6. **Commit (lo haces tú):** `.gitignore`, `evaluation/{evaluador,evidence,pln_pool,pln_metrics,test_pln}.py`, `EXPERIMENTO_PLN.md`, `results/pln/` (sin `cache/`, ya ignorado).
