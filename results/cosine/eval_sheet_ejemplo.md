# Hoja de evaluación manual -- EJEMPLO ANOTADO (validación del protocolo)

Este archivo contiene solo 2 de las 20 preguntas (F1 y T1), anotadas a mano
para validar que el protocolo de evaluación manual y `metrics.py` funcionan
de punta a punta. La evaluación manual completa de las 20 preguntas es el
siguiente milestone del cronograma (15/10/2026) y se hace sobre
`results/cosine/eval_sheet.md` (generado en blanco).

---

## F1 — ¿En qué año cayó Tenochtitlan?

**Tipo:** factual
**Puntos clave esperados:** 1521; Cuauhtémoc; tlaxcaltecas
**Tiempos:** retrieval=6.830s · generación=72.027s · total=78.858s

**Respuesta del sistema:**
> Según el Fragmento 5, el fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españoles derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco. El Fragmento 4 indica que la ciudad debió rendirse el 13 de agosto, marcando así el inicio del dominio español.

Fuentes: Fragmento 4, Fragmento 5.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** 2

### Chunks recuperados
| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.6877 | Historia de México — _Lago de Texcoco y sitiar la ciudad..._ | [x] |
| 2 | 0.6643 | Moctezuma II — _llegada a Tenochtitlán, 8 de noviembre..._ | [ ] |
| 3 | 0.6383 | Tenochtitlan — _artículo de desambiguación, sin información útil_ | [ ] |
| 4 | 0.6242 | Virreinato de Nueva España — _muerte del emperador..._ | [ ] |
| 5 | 0.6129 | Imperio azteca — _"El fin del Imperio azteca ocurrió el 13 de agosto de 1521..."_ | [x] |

**Nota:** rank 3 es el falso positivo ya documentado en Fase 0 (artículo de desambiguación de Tenochtitlan, 51 palabras, sin información útil) -- se repite aquí de forma consistente.

### Faithfulness — afirmaciones de la respuesta
| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Según el Fragmento 5, el fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españoles derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco. | [x] |
| 2 | El Fragmento 4 indica que la ciudad debió rendirse el 13 de agosto, marcando así el inicio del dominio español. | [ ] |
| 3 | Fuentes: Fragmento 4, Fragmento 5. | [x] |

**Nota:** la afirmación 2 le atribuye al Fragmento 4 algo que ese chunk no dice (habla de la muerte del emperador, no de una rendición el 13 de agosto) -- es una afirmación no respaldada por el contexto, un caso real de imprecisión en el mapeo fuente-afirmación que Faithfulness está diseñada para detectar.

---

## T1 — ¿Quién es el presidente actual de México?

**Tipo:** trampa (pregunta trampa)
**Tiempos:** retrieval=0.020s · generación=4.955s · total=4.974s

**Respuesta del sistema:**
> El presidente de México desde el 1 de diciembre de 2018 hasta el 30 de septiembre de 2024.

Fuentes: Fragmento 3

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___ (no aplica -- pregunta trampa, no existe respuesta correcta que recuperar)

### Chunks recuperados
| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.6917 | Revolución mexicana — _Carranza, «Ejército Constitucionalista»..._ | [ ] |
| 2 | 0.6749 | Benito Juárez — _biografía, nacimiento en Guelatao..._ | [ ] |
| 3 | 0.6722 | Historia de México — _"Presidente de México desde el 1 de diciembre de 2018 hasta el 30 de septiembre de 2024..."_ | [ ] |
| 4 | 0.6651 | Benito Juárez — _ceremonia masónica..._ | [ ] |
| 5 | 0.6642 | Benito Juárez — _elecciones, Porfirio Díaz..._ | [ ] |

**Nota:** ninguno de los 5 chunks responde correctamente "quién es el presidente actual". El rank 3 contiene un dato desactualizado (un periodo presidencial 2018-2024) que el corpus incluye incidentalmente dentro del artículo "Historia de México" -- no es la respuesta correcta a una pregunta sobre el presente, así que se marca como no relevante a propósito: es un falso positivo de retrieval sobre una pregunta trampa, no una respuesta válida. El comportamiento esperado (declarar que no se encontró la información) **no ocurrió** -- falla real, documentada para la Fase 2.

### Faithfulness — afirmaciones de la respuesta
| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El presidente de México desde el 1 de diciembre de 2018 hasta el 30 de septiembre de 2024. | [x] |
| 2 | Fuentes: Fragmento 3 | [x] |

**Nota:** aunque la respuesta es incorrecta para el propósito de la pregunta, sí es *fiel* al chunk que recuperó -- no inventó la fecha, la copió del contexto. Esto separa claramente las dos capas de falla del RAG: aquí falló el **retrieval** (trajo un chunk que no debía), no la **generación** (que fue fiel a lo que recibió).

---
