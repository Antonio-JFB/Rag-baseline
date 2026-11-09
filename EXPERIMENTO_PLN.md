# Experimento de PLN — recuperación léxica vs. densa en español

**Efecto del preprocesamiento y la segmentación.** Bloque experimental para el proyecto del curso de PLN, diseñado para reutilizarse en la Fase 2 de la tesis (ver §9).

**Estado (08/11/2026):** corridas hechas y verificadas (reproducibles), herramientas de evaluación probadas, resultados provisionales con métrica automática (proxy). **Falta la anotación humana de evidencia** (§6), que es lo que convierte los resultados provisionales en resultados.

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

## 6. Qué te toca hacer: la anotación

Archivo: **`results/pln/anotacion_evidencia.md`** — 741 oraciones candidatas en 20 preguntas (30–43 por pregunta). Marca `[x]` en *Evidencia* y marca **Anotada** al terminar cada pregunta. Las reglas están en el encabezado de la hoja.

- Orden sugerido: primero las 17 preguntas con respuesta (todo el análisis principal se calcula con esas), después T1–T3.
- Estimación: ~10 s por oración → 1.5–2 h en total.
- Se pueden analizar avances parciales: `pln_metrics.py` solo usa las preguntas marcadas como anotadas.
- Las oraciones están ordenadas por artículo y posición, **sin indicar de qué método salieron**, para no sesgarte.
- **Después de anotar:** `python evaluation/pln_metrics.py` llena la sección humana sola.

El pool se armó con: top-8 por búsqueda densa, BM25 simple y BM25 lematizado sobre las **oraciones** del corpus, oraciones con puntos clave, y la mejor oración de cada chunk que alguna configuración recuperó. Lo que no aparece en la hoja se asume no relevante (supuesto estándar de *pooling*); si ves evidencia faltante, añade una fila con su `Ref`.

## 7. Resultados provisionales (proxy, sin anotación humana)

Métrica proxy = cobertura de los puntos clave de `questions.json` en el texto recuperado. **Es heurística** (coincidencia de tokens): sirve para probar el pipeline y orientar, no para concluir. Tabla completa en `results/pln/analisis.md`.

**Lo que ya se puede afirmar (descriptivo, no depende de la anotación):**
- Chunks que exceden los 128 tokens del modelo de embeddings: **100 %** en el baseline, 14 % con párrafos, 1 % con ventana 64.
- Recuperación determinista en las seis configuraciones.
- Lematizar cambia mucho qué se recupera: el top-5 de BM25 simple y BM25 lematizado es **idéntico en 0/20 preguntas** (Jaccard medio 0.35).
- La lista estándar de palabras vacías elimina «último» de «¿Quién fue el último emperador azteca?» (F5), que queda como «emperador azteca»; el efecto sobre F5 solo se sabe con la anotación.
- Latencia de recuperación (mediana, sin la primera pregunta): densas 18–22 ms, BM25 2.5 ms, BM25 lematizado 4 ms (incluye lematizar la consulta), híbrida 24 ms.

**Resultados con el proxy (n = 17):**

| | Cobertura Vista A (k = 5) | Cobertura Vista B (presupuesto igual) |
|---|---|---|
| Densa baseline | 0.59 | 0.59 |
| Densa + párrafos | 0.26 | 0.56 |
| Densa + ventana 64 | 0.29 | 0.65 |
| BM25 simple | 0.54 | 0.54 |
| BM25 + lemas + stopwords | 0.58 | 0.58 |
| Híbrida RRF | 0.62 | 0.62 |

- **El «castigo» de los chunks chicos en la Vista A (−0.33 y −0.31, significativo tras Holm) desaparece en la Vista B** (párrafos − baseline = −0.03, IC [−0.18, +0.10]). La pérdida en k = 5 se explica por entregar ≈ 4.5 veces menos texto, no por segmentar. Esto confirma por qué H2 necesita el control y la vista a presupuesto igual.
- H1 (lemas): +0.04, IC [−0.05, +0.14]; 4 mejoras, 11 empates, 2 empeoramientos. El proxy no detecta efecto. No se concluye nada hasta tener la métrica humana.
- Híbrida ≥ las demás en el valor puntual, pero ninguna diferencia es distinguible de cero.
- El MRR del proxy (≥ 50 % de los puntos clave en un solo chunk) **penaliza estructuralmente a los chunks chicos** (un chunk de 64 palabras casi nunca contiene la mitad de los puntos clave); no lo interpretes entre tamaños distintos.

## 8. Amenazas a la validez

1. **n = 17** y 5 tipos de pregunta con 2–5 casos cada uno: el análisis por tipo es ilustrativo.
2. **Un solo anotador** (tú). No hay acuerdo entre anotadores. Mitigación posible: que otra persona anote 5–6 preguntas y reportar acuerdo (κ).
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

1. **Anotar** (§6): bloquea todos los resultados definitivos.
2. Re-correr `pln_metrics.py`, revisar el proxy contra el gold humano (correlación, §5 de `analisis.md`) y decidir si el proxy se descarta.
3. Análisis de sensibilidad del umbral de cobertura; opcionalmente acuerdo entre anotadores en un subconjunto.
4. Análisis cualitativo de errores (qué preguntas pierde cada método y por qué).
5. Redactar el reporte del curso con las tablas de `analisis.md`.
6. **Commit (lo haces tú):** `.gitignore`, `evaluation/{evaluador,evidence,pln_pool,pln_metrics,test_pln}.py`, `EXPERIMENTO_PLN.md`, `results/pln/` (sin `cache/`, ya ignorado).
