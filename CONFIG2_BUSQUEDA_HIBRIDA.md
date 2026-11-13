# Configuración 2 — búsqueda híbrida (BM25 + embeddings, fusión RRF)

**Cronograma:** implementación y evaluación, 19/11/2026. **Estado:** implementada y corrida sobre las 20 preguntas (25/10/2026); la hoja `results/hybrid/eval_sheet.md` está en blanco, falta la anotación manual.

**Qué cambia respecto al baseline:** solo el método de retrieval. Mismos chunks (ventana de 300 palabras, traslape de 50), mismos índices ya existentes (FAISS y BM25), mismo `top_k=5`, mismo LLM y mismo prompt.

## Cómo funciona

Se piden los 20 mejores resultados a cada recuperador (coseno sobre embeddings y BM25) y se fusionan con *Reciprocal Rank Fusion* (RRF) [Cormack, Clarke y Büttcher, SIGIR 2009]:

> puntaje(chunk) = Σ peso / (k + posición en ese ranking), sumado sobre los rankings donde aparece

- **RRF combina posiciones, no puntajes.** Eso resuelve el problema de que el coseno va de 0 a 1 y BM25 no está acotado (valores de 9 a 28 en el primer resultado de cada pregunta en este corpus), cuyos puntajes no se pueden sumar directamente.
- Un chunk que aparece en los dos rankings suma dos términos y sube; uno que solo aparece en uno suma uno solo.
- El puntaje que se guarda en los resultados es el fusionado (≈0.008 a 0.016). **No es comparable** con el del coseno ni con el de BM25.

**Parámetros** (`configs/hybrid.yaml`): `rrf_k: 60` (valor estándar de la literatura), pesos 0.5 / 0.5 (equivale a RRF sin ponderar), `fusion_depth: 20` (cuántos resultados de cada recuperador entran a la fusión).

**Decisión de diseño:** los chunks que BM25 puntúa en 0 (ningún término de la pregunta aparece en ellos) no entran a la fusión, porque su orden entre sí es arbitrario y solo agregarían ruido.

**Verificación:** la fusión se probó con rankings sintéticos de resultado conocido (fórmula exacta, filtro de puntaje cero, prioridad de los chunks presentes en ambos rankings, peso cero en un ranking, `top_k` mayor que la profundidad).

## Datos descriptivos de la corrida (sin anotar)

| | Valor |
|---|---|
| Solape del top-5 con coseno (Jaccard medio) | 0.33 |
| Solape del top-5 con BM25 | 0.25 |
| Solape entre coseno y BM25 | 0.05 |
| Preguntas con top-5 idéntico al de coseno / al de BM25 | 0 / 0 |
| Origen de los 100 chunks del top-5: en ambos top-5 / solo coseno / solo BM25 / ninguno de los dos top-5 | 9 / 41 / 28 / 22 |
| Latencia total, mediana | 6.6 s (primera pregunta, arranque en frío: 100.9 s) |
| Tiempo de retrieval | 0.025 s (coseno 0.021 s, BM25 0.005 s) |

Coseno y BM25 casi no coinciden entre sí (0.05), lo que hace razonable combinarlos: aportan información distinta. Estos datos no dicen si la fusión mejora algo; eso lo decide la anotación.

## A tener en cuenta al interpretar

1. **Desajuste en la numeración del RFC.** La tabla de configuraciones candidatas describe `busqueda-hibrida` como «reemplazar coseno por BM25» (hipótesis: BM25 supera a los embeddings en nombres propios y fechas) y `contextual-retrieval` como «BM25 + embeddings con fusión» (hipótesis: la híbrida supera a ambos por separado). En cambio el YAML de ejemplo del RFC llama `busqueda-hibrida` a BM25 + embeddings con RRF, que es lo que se implementó aquí. En la práctica ya hay datos para las dos hipótesis: **BM25 solo** (`results/bm25`) prueba la primera y **esta híbrida** prueba la segunda. Falta decidir cómo se nombran en el documento de la Fase 2.
2. **«Contextual retrieval» en sentido estricto no está implementado.** La referencia que cita el RFC (35 % menos de fallos de recuperación) se refiere a que un LLM añada contexto a cada chunk antes de indexarlo. Eso es preprocesamiento con LLM, es otra configuración y no es lo mismo que fusionar rankings. Conviene aclarar a cuál se refiere la Configuración 3 del cronograma.
3. **Para probar «la híbrida supera a ambos por separado» hay que anotar también BM25** (`results/bm25/eval_sheet.md`), además del baseline y esta hoja.
4. **La fusión no crea información y puede desplazar un acierto.** En F5 el coseno no trae ningún chunk que mencione a Cuauhtémoc en su top-5; BM25 trae uno (rank 4, de «Virreinato de Nueva España»), y el híbrido lo pierde porque un solo ranking no alcanza para ganarle a chunks que aparecen en los dos. Si el chunk bueno no está bien posicionado en ambos rankings, RRF no lo rescata. Que ese chunk sea relevante lo decide la anotación; aquí solo se observa que lo menciona.
5. **El componente léxico es débil.** BM25 aquí no usa raíces ni palabras vacías, y eso limita lo que puede aportar a la fusión.
6. **Hiperparámetros sin ajustar.** `k=60` y `fusion_depth=20` son valores por defecto. Si se ajustan, no debe hacerse sobre estas mismas 20 preguntas, porque se sobreajustaría la evaluación.
7. **El artículo duplicado también afecta aquí.** `metrics.py` cuenta las copias una sola vez, como en las demás configuraciones.

## Cómo reproducirlo

```bash
python evaluation/evaluador.py --config configs/hybrid.yaml
python evaluation/eval_sheet.py --results results/hybrid/results.jsonl
```

No hace falta recalcular embeddings: reutiliza `embeddings/faiss.index` y `bm25_index/bm25.pkl`.

## Cómo compararla cuando esté anotada

```bash
python evaluation/compare.py cosine hybrid
python evaluation/compare.py bm25 hybrid
```

Genera `results/comparacion_<A>_vs_<B>.md` con los agregados, el desglose por tipo de pregunta, el detalle por pregunta, las preguntas no comparables y la latencia (mediana).
