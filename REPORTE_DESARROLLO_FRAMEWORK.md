# Reporte técnico — Desarrollo del framework de evaluación

**Milestone del cronograma:** "Desarrollo técnico del framework: `evaluador.py`, `metrics.py`, `questions.json` validado y protocolo de evaluación manual documentado" (30/09/2026).

Este documento reporta lo construido durante septiembre de 2026 para cerrar ese milestone, como continuación directa de la arquitectura SoC (Proposal 2 del RFC) implementada en `src/`. El objetivo del mes no era ejecutar la evaluación manual completa de las 20 preguntas — eso está agendado como el siguiente milestone del cronograma (15/10/2026) — sino dejar construida y **validada de punta a punta** la maquinaria que esa evaluación va a usar.

## 1. Qué se construyó

| Entregable | Archivo | Estado |
|---|---|---|
| Preguntas con *ground truth* | `evaluation/questions.json` | ✅ 20/20, validado con Pydantic |
| Corredor en batch | `evaluation/evaluador.py` | ✅ corrido de punta a punta sobre el baseline |
| Generador de hoja de evaluación | `evaluation/eval_sheet.py` | ✅ genera `eval_sheet.md` desde `results.jsonl` |
| Cálculo de métricas | `evaluation/metrics.py` | ✅ valida contra una hoja anotada de ejemplo |
| Protocolo de evaluación manual | Este documento, sección 4 | ✅ documentado y probado con 2 preguntas reales |

## 2. `questions.json` — preguntas y *ground truth*

Estructura (validada con Pydantic, `evaluation/schema.py`):

```python
class Question(BaseModel):
    id: str
    tipo: Literal["factual", "causalidad", "comparativa",
                  "relacional", "multihop", "trampa"]
    pregunta: str
    puntos_clave: list[str]
    is_trap: bool = False
    nota: str | None = None
```

Las 20 preguntas son las mismas que ya se definieron en el RFC (5 factuales, 4 causales, 3 comparativas, 3 relacionales, 2 multi-hop, 3 trampa) — este paso fue estructurarlas en JSON y confirmar que cargan y validan sin errores:

```
$ python -c "from evaluation.schema import load_questions; print(len(load_questions()))"
20 preguntas cargadas y validadas
```

## 3. `evaluador.py` — corredor en batch

Recibe un archivo de configuración (`configs/cosine.yaml` o `configs/bm25.yaml`), construye el `RAGPipeline` correspondiente reusando `src/config.build_pipeline`, indexa el corpus una sola vez, y corre las 20 preguntas en secuencia. Por cada una escribe una línea en `results/<config>/results.jsonl` con el mismo esquema que se definió en el RFC: `question_id`, `query`, `chunks` (rank, score, fuente, texto), `prompt` completo, `respuesta`, y tiempos de retrieval/generación/total.

Se corrió sobre el baseline (`configs/cosine.yaml`) el 29/09/2026:

```
$ python evaluation/evaluador.py --config configs/cosine.yaml
=== evaluador.py -- config: Cosine / FAISS (semántico) (configs/cosine.yaml) ===
20 preguntas cargadas desde evaluation/questions.json
Indexando 1334 chunks...
[1/20] F1 (factual): ¿En qué año cayó Tenochtitlan?
    retrieval=6.830s  generacion=72.027s  total=78.858s
...
[20/20] T3 (trampa): ¿Qué equipos jugaron la final del fútbol mexicano en 2024?
    retrieval=0.022s  generacion=4.142s  total=4.163s
=== Listo: 20 preguntas en 187.3s -> results/cosine/results.jsonl ===
```

Corrida real el 29/09/2026: **20/20 preguntas completadas en 187.3s** (~9.4s promedio por pregunta; la más lenta, F1, tomó 78.9s -- Ollama sin GPU es inconsistente entre corridas, ya documentado como limitación conocida). Las 3 preguntas trampa (T1-T3) respondieron en menos de 5s cada una. Esto confirma que el pipeline aguanta correr las 20 preguntas sin intervención manual, y que el archivo de resultados queda con todo lo necesario para las siguientes dos etapas.

## 4. Protocolo de evaluación manual

### 4.1 Cómo se genera la hoja

`eval_sheet.py` lee `results.jsonl` y produce `eval_sheet.md`: una sección por pregunta con la respuesta del sistema, los puntos clave esperados (como referencia para el evaluador, no como respuesta automática), una tabla de chunks recuperados con una casilla `[ ]` por chunk, y una tabla de afirmaciones de la respuesta (partida automáticamente por oración) con una casilla `[ ]` por afirmación. Cada pregunta incluye además una casilla `**Anotada:** [ ]` que el evaluador marca al terminarla (ver paso 6 de la sección 4.2).

```
$ python evaluation/eval_sheet.py --results results/cosine/results.jsonl
Generado: results/cosine/eval_sheet.md (20 preguntas)
```

### 4.2 Cómo la llena el evaluador humano (paso a paso)

Para que dos evaluadores distintos lleguen al mismo resultado dado el mismo `results.jsonl`, el procedimiento es:

1. **Lee la pregunta y los puntos clave esperados** antes de ver los chunks — evita el sesgo de "buscar" relevancia donde no la hay.
2. **Para cada chunk recuperado**, marca `[x]` únicamente si el chunk contiene información que efectivamente ayuda a responder la pregunta (no basta con que mencione el mismo tema general). El score del retriever **no** debe influir en esta decisión — es justo lo que la métrica va a evaluar.
3. **Para preguntas trampa**, si el sistema declaró correctamente que no encontró la información, no hay chunks "relevantes" que marcar (el criterio correcto es que ninguno lo sea) y la respuesta se considera fiel automáticamente.
4. **Para cada afirmación de la respuesta**, marca `[x]` solo si esa afirmación específica está respaldada por el texto de los chunks — una afirmación históricamente correcta pero ausente del contexto recuperado cuenta como **no respaldada**, porque el sistema no pudo haberla sacado de ahí (esto es lo que mide Faithfulness: fidelidad al contexto, no verdad absoluta).
5. **Campo opcional "Total de chunks relevantes en el corpus"**: si el evaluador reconoce, por conocimiento del corpus, que hay más chunks relevantes de los que aparecieron en el top-5 (p. ej. en preguntas comparativas que necesitan dos artículos), puede estimar ese total para habilitar el cálculo de Recall@5 en esa pregunta. Si se deja en blanco, esa pregunta simplemente no cuenta para el promedio de Recall@5 (se reporta la cobertura, no se inventa un valor).
6. **Al terminar cada pregunta, marcar la casilla `**Anotada:** [x]`.** Es lo que le dice a `metrics.py` que esa pregunta ya fue revisada. Sin la marca, la pregunta se excluye de los promedios; con ella, una pregunta donde ningún chunk resultó relevante cuenta como 0, que es un resultado real y distinto de "pendiente". El avance se consulta con `python evaluation/metrics.py --results ... --sheet ... --status`.

7. **Reglas que aplica `metrics.py`** (para que todas las configuraciones se cuenten igual): la fila «Fuentes:» de la respuesta no es una afirmación y no se evalúa; los chunks con texto idéntico (copias) cuentan una sola vez, y el distinto es relevante si alguna copia está marcada; y el «Total de chunks relevantes» debe contar chunks distintos. Para estimar ese total, la hoja incluye por pregunta una línea de ayuda y `python evaluation/candidates.py` lista los chunks del corpus que mencionan los puntos clave.

### 4.3 Validación del protocolo

Se aplicó este protocolo a mano sobre 2 preguntas reales (F1 y T1) para confirmar que el criterio es aplicable sin ambigüedad y que `metrics.py` calcula correctamente a partir de la hoja anotada — ver sección 6.

## 5. `metrics.py` — cálculo de métricas

Lee una `eval_sheet.md` ya anotada (parseando las casillas `[x]`/`[ ]` de cada tabla) y la cruza con `results.jsonl` para los tiempos. Calcula, por pregunta y agregado:

- **Precision@5** = chunks marcados relevantes / chunks mostrados.
- **MRR** = 1 / posición del primer chunk relevante marcado (0 si ninguno).
- **Recall@5** = chunks relevantes recuperados / total de chunks relevantes estimado — solo en las preguntas donde el evaluador llenó ese campo opcional; se reporta la cobertura (cuántas preguntas lo tienen) en vez de forzar un promedio incompleto.
- **Faithfulness** = afirmaciones respaldadas / afirmaciones totales de la respuesta.
- **Latencia** = tiempos ya logueados por `evaluador.py` (no requiere anotación manual; se calcula sobre todas las preguntas, estén o no anotadas).

**Preguntas anotadas vs. pendientes.** Solo cuentan para los promedios las preguntas con la casilla `**Anotada:** [x]`. El resultado reporta `n_preguntas_anotadas` sobre `n_preguntas_total` y la lista de `preguntas_pendientes`, y `--status` muestra solo ese avance. Esto evita que una pregunta sin revisar (todas sus casillas vacías) se lea como una pregunta revisada donde todo salió irrelevante. Si se le pasa una hoja generada antes de este cambio (sin el marcador), el script avisa y trata todas las preguntas como anotadas, en lugar de fallar en silencio.

## 6. Ejemplo real de punta a punta

`evaluador.py` se corrió sobre el baseline (`configs/cosine.yaml`) el 29/09/2026: **20/20 preguntas en 187.3s** (~9.4s promedio; el caso más lento, F1, tomó 78.9s con `gemma3:12b` en CPU). Los resultados quedaron en `results/cosine/results.jsonl` y `eval_sheet.py` generó `results/cosine/eval_sheet.md` correctamente (20 secciones).

Para validar que el protocolo de anotación y `metrics.py` funcionan de punta a punta -- sin adelantar la evaluación manual completa, agendada para el 15/10 -- se anotaron a mano 2 preguntas reales (`results/cosine/eval_sheet_ejemplo.md`):

**F1 — "¿En qué año cayó Tenochtitlan?"**
El sistema recuperó el chunk de "Tenochtitlan" (rank 3, score 0.6383) -- el mismo falso positivo por desambiguación ya documentado en la Fase 0, reproducido de forma consistente. Se marcaron relevantes los ranks 1 y 5 (contienen la fecha correcta, 13 de agosto de 1521). Al anotar Faithfulness se encontró que la respuesta le atribuye al "Fragmento 4" una afirmación ("la ciudad debió rendirse el 13 de agosto") que ese chunk en realidad no dice -- un caso real de mapeo incorrecto fuente→afirmación, exactamente el tipo de falla que Faithfulness está diseñada para detectar.

**T1 — "¿Quién es el presidente actual de México?" (trampa)**
El sistema **no** declaró que le faltaba información -- el comportamiento esperado para una pregunta trampa. En vez de eso, recuperó un chunk de "Historia de México" con un periodo presidencial desactualizado (2018-2024) y respondió con esa fecha, sin nombre. Los 5 chunks se marcaron como no relevantes (ninguno responde correctamente "quién es el presidente actual"). Sin embargo, Faithfulness = 1.0: la respuesta sí es fiel a lo que recuperó, solo que lo que recuperó era inadecuado. Este caso separa con claridad las dos capas de falla de un RAG que el RFC distingue: aquí falló el **retrieval** (trajo un chunk que no debía), no la **generación** (que no alucinó, fue fiel al contexto que recibió).

**Métricas calculadas por `metrics.py` sobre estas 2 preguntas** (`results/cosine/metrics_ejemplo.json`):

| Pregunta | Precision@5 | MRR | Recall@5 | Faithfulness |
|---|---|---|---|---|
| F1 | 0.4 (2/5) | 1.0 | 1.0 (2/2 estimado) | 0.5 (1/2) |
| T1 | 0.0 (0/5) | 0.0 | N/A (pregunta trampa) | 1.0 (1/1) |
| **Promedio** | **0.2** | **0.5** | 1.0 (cobertura 1/2) | **0.75** |

*(Faithfulness del ejemplo: en la primera versión del cálculo salía 0.667 y 0.833 porque la fila «Fuentes:» contaba como una afirmación respaldada; desde la corrección del 18/10/2026 esa fila se excluye, ver sección 8.)*

Verificación manual: cada uno de estos valores se recalculó a mano contra las casillas marcadas y coincide exactamente con la salida del script.

**Un bug real encontrado y corregido durante esta validación:** la primera versión de `metrics.py` usaba una sola expresión regular multilínea para detectar las casillas `[x]` marcadas en las tablas Markdown. Esa expresión confundía la fila separadora de la tabla (`|------|-------|...`) con una fila de datos, porque `\S+` no se detiene en el carácter `|`. El resultado eran conteos de relevancia incorrectos (subestimados) sin ningún error visible -- el script corría "bien" pero calculaba mal. Se reescribió el parser para procesar la tabla línea por línea, separando cada fila en celdas explícitamente y validando que la primera celda sea numérica antes de contarla como dato. Tras el cambio, los 4 valores por pregunta coinciden exactamente con el cálculo manual de control. Se documenta aquí porque es precisamente el tipo de falla silenciosa que un framework de evaluación no se puede dar el lujo de tener sin detectar.

**Una limitación de diseño detectada y corregida (07/10/2026):** al validar con solo 2 preguntas anotadas y 18 sin tocar, los promedios salían divididos entre 20 en lugar de entre 2. Las preguntas pendientes tienen todas sus casillas vacías, y el script no podía distinguirlas de preguntas revisadas donde nada resultó relevante, así que las contaba como ceros. En una prueba equivalente con una sola pregunta anotada (F1, Precision@5 = 0.4), el comportamiento anterior dio 0.02 (= 0.4 / 20) en lugar de 0.4. Se agregó la casilla `**Anotada:**` por pregunta: `metrics.py` excluye de los promedios las no marcadas, reporta el avance (`n_preguntas_anotadas` / `n_preguntas_total`) y ofrece `--status`. Se probó con cinco casos (el ejemplo F1+T1, una hoja en blanco, una hoja a medias con una sola pregunta anotada, la hoja en blanco sin `--status` y una hoja en formato anterior sin el marcador); los valores del ejemplo no cambiaron (Precision@5 0.2, MRR 0.5, Recall@5 1.0, Faithfulness 0.833).

**Nota sobre las corridas.** Las cifras de esta sección (187.3 s en total, F1 en 78.9 s) y las dos anotaciones de ejemplo corresponden a la corrida del 29/09/2026. El 05/10/2026 se volvió a correr el baseline (158.5 s) y `results/cosine/results.jsonl` y `eval_sheet.md` en el repositorio son de esa segunda corrida. Como `gemma3:12b` no es determinista, las respuestas pueden variar entre corridas; por eso `eval_sheet_ejemplo.md` se conserva como evidencia histórica de la corrida del 29/09 y no como anotación de la hoja vigente.

## 7. Estado y siguientes pasos

**Completo:** arquitectura SoC (`src/`, del milestone anterior), `questions.json` validado, `evaluador.py` corrido de punta a punta sobre el baseline, `eval_sheet.py` generando hojas correctamente, `metrics.py` validado contra anotación manual real (con control de preguntas anotadas vs. pendientes y `--status` para ver el avance), protocolo documentado y probado.

**Pendiente (milestone 15/10/2026):** evaluación manual humana de las 20 preguntas completas sobre el baseline, para obtener los valores de referencia (Precision@5, Recall@5, MRR, Faithfulness) que sirven de punto de comparación para las 4 configuraciones experimentales de la Fase 2. La maquinaria para hacerlo ya está lista; lo que falta es el trabajo de anotación en sí, que es deliberadamente manual y no se automatiza en esta fase.

## 8. Revisión de la primera anotación del baseline y correcciones (18/10/2026)

Con las 20 preguntas del baseline anotadas por primera vez, la revisión encontró problemas que afectaban a los números. Algunos eran de la herramienta y otros de datos o criterio:

| Hallazgo | Efecto | Qué se hizo |
|---|---|---|
| Filas de la tabla de afirmaciones de varias líneas (respuestas con viñetas) | `metrics.py` las descartaba **sin avisar**: se contaban menos afirmaciones de las que había (F3 contaba 1 en vez de 2, C1 y V2 contaban 4 en vez de 5) | `metrics.py` lee la fila completa y avisa (`filas_descartadas`) si alguna está mal formada |
| La línea «Fuentes:» contada como afirmación, y marcada de forma inconsistente (9 respaldadas, 5 sin marcar) | Faithfulness desfasada (p. ej. F2 salía 0.5 con su única afirmación factual respaldada) | Se excluye de Faithfulness; el generador de hojas ya no la incluye |
| El partidor de oraciones cortaba en abreviaturas («1200 a. \| n. e.») e iniciales («Francisco I. \| Madero») | Afirmaciones partidas a la mitad, denominador inflado | Partidor consciente de abreviaturas; una viñeta es una afirmación |
| Artículo duplicado en el corpus: `Independencia_de_México.txt` y `Guerra_de_Independencia_de_México.txt` son idénticos | 8 de las 100 posiciones del top-5 (20 preguntas) repiten un chunk (F2 y R3 tienen 2 de 5 duplicadas); infla o distorsiona Precision@5 | `metrics.py` cuenta los chunks idénticos una sola vez; la hoja marca las copias. El corpus **no** se modificó (ver decisión abajo) |
| Recall@5 estimado mirando solo el top-5 | Seis preguntas con Recall exactamente 1.0 por construcción. En F5, 31 chunks del corpus mencionan a Cuauhtémoc y el estimado era 3; en F1, 8 mencionan la fecha y el estimado era 3 | `candidates.py` lista los chunks distintos candidatos; la hoja trae una línea de ayuda por pregunta |
| Vista previa de 100 caracteres en la hoja | F2 se anotó con 0 chunks relevantes cuando el chunk 1 contenía la respuesta exacta (corregido por el evaluador) | La vista previa pasa a 300 caracteres y se muestran los puntos clave presentes en cada chunk (ayuda, no decide) |

**Efecto en los agregados del baseline** (anotaciones del evaluador sin cambios salvo la corrección de F2): Precision@5 0.53 → 0.55, MRR 0.754 → 0.804, Recall@5 0.73 → 0.73 (cobertura 18/20), Faithfulness 0.854 → 0.925. Siguen siendo **provisionales**: faltan las decisiones de abajo y la reestimación de Recall con la ayuda de candidatos.

**Decisiones pendientes**
1. **Artículo duplicado.** Quitarlo es lo más limpio, pero cambia los chunks del índice y obliga a re-correr las tres configuraciones, y con un modelo generativo no determinista las respuestas ya anotadas cambiarían. Por ahora se compensa en la métrica; conviene decidirlo antes de fijar los valores de referencia definitivos o, a más tardar, antes de la configuración de búsqueda híbrida.
2. **Regla para T1** (la pregunta sobre el presidente actual): ¿cuenta como relevante un chunk con información desactualizada? Además, el corpus sí contiene a la presidenta actual (la Configuración 1 la recuperó), así que la premisa de «fuera del corpus» no se sostiene.
3. **Criterio en preguntas multi-hop.** M2 tiene 5/5 chunks relevantes (incluido uno sobre tropas francesas) y el sistema rechazó responder; conviene releer qué chunks ayudan realmente.

Hallazgo de comportamiento: V3 y M2 son **rechazos excesivos** (el sistema dijo no encontrar la información con 5/5 chunks marcados relevantes), una falla de generación distinta de las de retrieval.
