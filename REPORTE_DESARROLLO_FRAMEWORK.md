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

`eval_sheet.py` lee `results.jsonl` y produce `eval_sheet.md`: una sección por pregunta con la respuesta del sistema, los puntos clave esperados (como referencia para el evaluador, no como respuesta automática), una tabla de chunks recuperados con una casilla `[ ]` por chunk, y una tabla de afirmaciones de la respuesta (partida automáticamente por oración) con una casilla `[ ]` por afirmación.

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

### 4.3 Validación del protocolo

Se aplicó este protocolo a mano sobre 2 preguntas reales (F1 y T1) para confirmar que el criterio es aplicable sin ambigüedad y que `metrics.py` calcula correctamente a partir de la hoja anotada — ver sección 6.

## 5. `metrics.py` — cálculo de métricas

Lee una `eval_sheet.md` ya anotada (parseando las casillas `[x]`/`[ ]` de cada tabla) y la cruza con `results.jsonl` para los tiempos. Calcula, por pregunta y agregado:

- **Precision@5** = chunks marcados relevantes / chunks mostrados.
- **MRR** = 1 / posición del primer chunk relevante marcado (0 si ninguno).
- **Recall@5** = chunks relevantes recuperados / total de chunks relevantes estimado — solo en las preguntas donde el evaluador llenó ese campo opcional; se reporta la cobertura (cuántas preguntas lo tienen) en vez de forzar un promedio incompleto.
- **Faithfulness** = afirmaciones respaldadas / afirmaciones totales de la respuesta.
- **Latencia** = tiempos ya logueados por `evaluador.py` (no requiere anotación manual).

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
| F1 | 0.4 (2/5) | 1.0 | 1.0 (2/2 estimado) | 0.667 (2/3) |
| T1 | 0.0 (0/5) | 0.0 | N/A (pregunta trampa) | 1.0 (2/2) |
| **Promedio** | **0.2** | **0.5** | 1.0 (cobertura 1/2) | **0.833** |

Verificación manual: cada uno de estos valores se recalculó a mano contra las casillas marcadas y coincide exactamente con la salida del script.

**Un bug real encontrado y corregido durante esta validación:** la primera versión de `metrics.py` usaba una sola expresión regular multilínea para detectar las casillas `[x]` marcadas en las tablas Markdown. Esa expresión confundía la fila separadora de la tabla (`|------|-------|...`) con una fila de datos, porque `\S+` no se detiene en el carácter `|`. El resultado eran conteos de relevancia incorrectos (subestimados) sin ningún error visible -- el script corría "bien" pero calculaba mal. Se reescribió el parser para procesar la tabla línea por línea, separando cada fila en celdas explícitamente y validando que la primera celda sea numérica antes de contarla como dato. Tras el cambio, los 4 valores por pregunta coinciden exactamente con el cálculo manual de control. Se documenta aquí porque es precisamente el tipo de falla silenciosa que un framework de evaluación no se puede dar el lujo de tener sin detectar.

## 7. Estado y siguientes pasos

**Completo:** arquitectura SoC (`src/`, del milestone anterior), `questions.json` validado, `evaluador.py` corrido de punta a punta sobre el baseline, `eval_sheet.py` generando hojas correctamente, `metrics.py` validado contra anotación manual real, protocolo documentado y probado.

**Pendiente (milestone 15/10/2026):** evaluación manual humana de las 20 preguntas completas sobre el baseline, para obtener los valores de referencia (Precision@5, Recall@5, MRR, Faithfulness) que sirven de punto de comparación para las 4 configuraciones experimentales de la Fase 2. La maquinaria para hacerlo ya está lista; lo que falta es el trabajo de anotación en sí, que es deliberadamente manual y no se automatiza en esta fase.
