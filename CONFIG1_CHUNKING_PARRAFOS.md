# Configuración 1 — chunking por párrafos

**Cronograma:** implementación y evaluación, 05/11/2026. **Estado:** implementada y corrida sobre las 20 preguntas (12/10/2026); la hoja de evaluación está en blanco, falta la anotación manual.

**Hipótesis del RFC:** dividir por párrafos en lugar de ventana fija mejora Precision@5 al preservar coherencia semántica. Es el único componente que cambia respecto al baseline: mismo embedding, mismo índice (FAISS, coseno), mismo `top_k=5`, mismo LLM.

## Qué se implementó

- `ParagraphChunker` (`src/chunkers.py`), una clase nueva que hereda de `BaseChunker`. Es la prueba de la arquitectura SoC: el pipeline y el evaluador no se modificaron para soportarlo, solo se registró en `CHUNKERS` (`src/config.py`).
- `configs/cosine_paragraph.yaml`, con `chunking: paragraph`, `chunk_max_words: 85` e `index_dir: embeddings/paragraph`.

**Cómo parte el texto.** Los párrafos del corpus vienen separados por un salto de línea y los títulos de sección son líneas cortas.
1. Un párrafo nunca se corta salvo que él solo pase de `max_words`; en ese caso se divide en límites de oración.
2. Los párrafos cortos se unen con los siguientes hasta llenar `max_words`.
3. Un título nunca queda solo: se pega al texto que introduce, aunque eso rebase `max_words` por unas pocas palabras.

## Por qué 85 palabras

El modelo de embeddings (`paraphrase-multilingual-MiniLM-L12-v2`) tiene un límite de **128 tokens** por texto, y en este corpus 1 palabra ≈ 1.5 tokens. Medido sobre una muestra de 200 chunks del baseline, **la mediana es de 446 tokens y el 100 % excede el límite**: el vector de cada chunk del baseline representa solo su primer cuarto aproximadamente. Con 85 palabras, la mediana baja a 103 tokens y solo el 14.1 % de los chunks se trunca.

## Resultados descriptivos (sin anotar todavía)

| | Baseline (ventana 300/50) | Config 1 (párrafos, 85) |
|---|---|---|
| Chunks | 1,334 | 5,239 |
| Palabras por chunk | 300 (fijo) | mediana 68, máx. 99 |
| Chunks que exceden 128 tokens | 100 % | 14.1 % |
| Contexto por pregunta (5 chunks) | 1,500 palabras | mediana 347 palabras |
| Prompt (caracteres, mediana) | 9,949 | 2,783 |
| Generación, mediana | 5.0 s | 4.8 s |
| Texto cubierto | todo | todo (verificado: 0 palabras perdidas en 19 artículos) |

Son datos descriptivos. **No dicen si la configuración mejora o empeora**: eso lo decide la anotación de la hoja `results/cosine_paragraph/eval_sheet.md`.

## Cosas a tener en cuenta al interpretar

1. **El efecto de "párrafos" está mezclado con el efecto del tamaño.** El baseline trunca todos sus chunks al embeber, y esta configuración casi no trunca. Si Precision@5 sube, no se puede atribuir solo a la coherencia semántica. Un control limpio sería una ventana fija de 85 palabras sin consciencia de párrafos (propuesta de "Config 1b"); no está implementado.
2. **El LLM recibe unas 4 veces menos contexto** (347 contra 1,500 palabras). Puede afectar a las preguntas causales y comparativas, que necesitan información de varias partes.
3. **Los chunks son distintos, así que la anotación empieza de cero.** Lo que cuenta como "chunk relevante" y el "total de chunks relevantes" para Recall@5 cambian respecto al baseline.
4. **El arranque en frío de Ollama contamina la latencia.** La primera pregunta de cada corrida tarda mucho más (212.9 s aquí, 55.2 s en el baseline). Conviene reportar la mediana y el arranque en frío por separado.
5. **La pregunta trampa T1 ya no es trampa.** La respuesta de esta configuración ("la actual presidenta es Claudia Sheinbaum") está respaldada por el contexto: el corpus menciona a Sheinbaum 2 veces y el chunk de rank 2 la contiene. El baseline recuperó otro chunk (un periodo 2018-2024) y no la encontró. Es decir, la premisa "fuera del corpus" de T1 no se sostiene, y hay que decidir si se cambia la pregunta o se documenta (ver decisiones pendientes con el director).

## Cómo reproducirlo

```bash
python evaluation/evaluador.py --config configs/cosine_paragraph.yaml
python evaluation/eval_sheet.py --results results/cosine_paragraph/results.jsonl
```

La primera corrida calcula los embeddings de los 5,239 chunks (~2 minutos) y guarda el índice en `embeddings/paragraph/`, que no se sube a git porque se regenera. Si el índice guardado no coincide con el número de chunks, `CosineFaissRetriever` lo reconstruye y avisa con un warning, en lugar de usarlo en silencio.
