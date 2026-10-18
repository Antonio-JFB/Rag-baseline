# Hoja de evaluación manual

Protocolo: para cada pregunta, (1) marca qué chunks recuperados son genuinamente relevantes para responderla -- usa los **puntos clave esperados** como referencia, no tu propio conocimiento de historia; (2) marca qué afirmaciones de la respuesta están respaldadas por el texto de los chunks recuperados (Faithfulness) -- si una afirmación es correcta históricamente pero no aparece en los chunks, cuenta como **no respaldada**, porque el sistema no la pudo haber sacado del contexto. Para preguntas trampa, la respuesta correcta es que el sistema declare que no encontró la información. Al terminar cada pregunta, marca la casilla **Anotada**.

Reglas de la herramienta (para que `metrics.py` cuente igual en todas las configuraciones):
- La vista previa de cada chunk es parcial (300 caracteres). Si la decisión depende del resto del texto, léelo completo en `results.jsonl` antes de marcar.
- «Puntos clave presentes» es una ayuda automática, no decide la relevancia: un chunk puede mencionar un punto clave sin ayudar a responder, o ayudar sin mencionarlo literalmente.
- Los chunks con texto idéntico (copias) cuentan una sola vez; no hace falta marcar la copia.
- El bloque «Fuentes:» de la respuesta no es una afirmación y no se evalúa.
- El «Total de chunks relevantes en el corpus» debe contar chunks distintos. Usa la línea de ayuda de cada pregunta y `python evaluation/candidates.py` en lugar de estimarlo solo con el top-5.

Total de preguntas: 20

---

## F1 — ¿En qué año cayó Tenochtitlan?

**Tipo:** factual
**Puntos clave esperados:** 1521; Cuauhtémoc; tlaxcaltecas
**Tiempos:** retrieval=0.020s · generación=212.870s · total=212.890s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Tenochtitlan cayó en 1521.
>
> Fuentes:
> * Fragmento 3: Historia de México
> * Fragmento 4: Virreinato de Nueva España
> * Fragmento 5: Tenochtitlan

_Ayuda para Recall: 144 chunks distintos del corpus mencionan al menos un punto clave (11 mencionan 2 o más); detalle con `python evaluation/candidates.py --question F1`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.6815 | Hernán Cortés — _Sitio y caída de Tenochtitlan Después de su derrota de la Noche Triste, los españoles y sus aliados tlaxcaltecas se replegaron en Tlaxcala; se reorganizaron y atacaron Tenochtitlan, poniendo en sitio a la ciudad. Cabe meditar si en este punto la alianza de los tlaxcaltecas podría o no considerarse l..._ | tlaxcaltecas | [ ] |
| 2 | 0.6645 | Historia de México — _A inicios de siglo XVI, se empezó a notar la intransigencia del imperio y el odio que México Tenochtitlán empezó a cultivar en su contra por todos los pueblos prehispánicos de la época. Sus ataques e invasiones provocaron el éxodo masivo de matlatzincas rumbo al Imperio Purepecha, que los acogió com..._ | ninguno | [ ] |
| 3 | 0.6558 | Historia de México — _Fue la primera vez desde la conquista de Tenochtitlán en 1521, que la Ciudad de México volvió a ver una guerra sangrienta y destructiva en su suelo. Dictadura militar de Victoriano Huerta De 1913 a 1914..._ | 1521 | [ ] |
| 4 | 0.6459 | Virreinato de Nueva España — _Se originó tras la caída de México-Tenochtitlan, acontecimiento principal de la conquista, la que propiamente no concluyó sino hasta mucho después, pues su territorio siguió creciendo hacia el norte...._ | ninguno | [ ] |
| 5 | 0.6383 | Tenochtitlan — _# Tenochtitlan Tenochtitlan puede hacer referencia a: México-Tenochtitlan, ciudad principal de los mexicas. Municipio de Tenochtitlán, municipio del estado de Veracruz. Tenochtitlán (Veracruz), localidad del estado de Veracruz, cabecera del municipio anterior. San Miguel Tenochtitlán, localidad del ..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Tenochtitlan cayó en 1521. | [ ] |

---

## F2 — ¿Quién dio el Grito de Independencia?

**Tipo:** factual
**Puntos clave esperados:** Miguel Hidalgo; Dolores Hidalgo; 16 septiembre 1810
**Tiempos:** retrieval=0.024s · generación=3.958s · total=3.982s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.
>
> Fuentes:
> * Historia de México
> * Independencia de México
> * Guerra de Independencia de México
> * Miguel Hidalgo y Costilla

_Ayuda para Recall: 49 chunks distintos del corpus mencionan al menos un punto clave (9 mencionan 2 o más); detalle con `python evaluation/candidates.py --question F2`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.6622 | Historia de México — _Así, tras 10 días de intenso debate y acuerdos entre ambos, el 24 de febero de 1821 proclaman el Plan de Iguala que proclamaba la Independencia de la América Septentrional bajo tres garantías: independencia, unión y religión. Se propuso un gobierno monárquico templado por una constitución que solici..._ | ninguno | [ ] |
| 2 | 0.6480 | Historia de México — _La profundización y radicalización del movimiento insurgente llevó a la convocatoria, de parte de Morelos de una asamblea nacional para gestar la independencia absoluta. Por eso el 13 de septiembre de 1813 el Congreso de Anáhuac se reunió en Chilpancingo, y abrió al día siguiente con la lectura de u..._ | ninguno | [ ] |
| 3 | 0.6196 | Independencia de México — _Este fue un punto de discordia con López Rayón quien manifestó no estar de acuerdo con el primer punto mencionado en los Sentimientos de la Nación, pues defendía que la tesis que había abrazado el movimiento autonomista de 1808, debería seguir subsistiendo, es decir, América era dependiente del rey ..._ | ninguno | [ ] |
| 4 | 0.6196 | Guerra de Independencia de México **(copia exacta del rank 3: cuenta una sola vez)** — _Este fue un punto de discordia con López Rayón quien manifestó no estar de acuerdo con el primer punto mencionado en los Sentimientos de la Nación, pues defendía que la tesis que había abrazado el movimiento autonomista de 1808, debería seguir subsistiendo, es decir, América era dependiente del rey ..._ | ninguno | [ ] |
| 5 | 0.5881 | Miguel Hidalgo y Costilla — _perdiendo en la derrota gran cantidad de dinero, armas y tropas, y quedando herida de muerte la primera etapa de la guerra de Independencia. Captura de Hidalgo..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---

## F3 — ¿Cuándo comenzó el Porfiriato?

**Tipo:** factual
**Puntos clave esperados:** 1876; Porfirio Díaz; reelección continua
**Tiempos:** retrieval=0.016s · generación=4.609s · total=4.625s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> El Porfiriato comenzó el 28 de noviembre de 1876 y duró hasta el 27 de mayo de 1911.
>
> Fuentes:
> * Fragmento 3: Porfiriato
> * Fragmento 2: Historia de México

_Ayuda para Recall: 73 chunks distintos del corpus mencionan al menos un punto clave (7 mencionan 2 o más); detalle con `python evaluation/candidates.py --question F3`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.6303 | Porfiriato — _La primera etapa del porfiriato empieza en 1877 y termina en el inicio de tercer periodo presidencial de Porfirio Díaz (1888) o cuando se eliminó toda restricción legal a la reelección indefinida (1890). Se trata de una fase de construcción, pacificación, unificación, conciliación y negociación, per..._ | Porfirio Díaz | [ ] |
| 2 | 0.6150 | Historia de México — _El ascenso de Porfirio Díaz al poder en 1876 empezó un periodo conocido como el Porfiriato, mismo que duró hasta 1911 con su exilio. En 1910 inició la Revolución Mexicana, un periodo de grandes conflictos entre múltiples facciones y con distintos principios durante el transcurso de la misma: su fech..._ | 1876, Porfirio Díaz | [ ] |
| 3 | 0.5923 | Porfiriato — _# Porfiriato El porfiriato o porfirismo fue un período de la historia de México en el que el gobierno estuvo bajo el control (total o mayoritario) del militar, político y dictador Porfirio Díaz, entre el 28 de noviembre de 1876 y el 27 de mayo de 1911. En el porfiriato la política se aplicó de tal m..._ | 1876, Porfirio Díaz | [ ] |
| 4 | 0.5495 | Historia de México — _El periodo formativo sería el equivalente a la protohistoria. Este periodo es comprendido entre el 1500 a. n. e. y el 292, descrito por Gordon Willey y Philip Phillips, antes del periodo clásico en el que se desarrolló el primer sistema de escritura americano por el pueblo Olmeca...._ | ninguno | [ ] |
| 5 | 0.5345 | Historia de México — _En abril mientras el empresario ferrocarrilero Weetman Pearson trabajaba en el Istmo de Tehuantepec, descubrió petróleo. De la noche a la mañana, envuelto en la locura del petróleo fundó la Compañía El Águila de extracción petrolera y refinamiento que iniciaría sus labores oficiales hasta 1908. Fue ..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El Porfiriato comenzó el 28 de noviembre de 1876 y duró hasta el 27 de mayo de 1911. | [ ] |

---

## F4 — ¿Qué civilización construyó Teotihuacán?

**Tipo:** factual
**Puntos clave esperados:** Cultura teotihuacana; nombre propio desconocido; periodo clásico
**Tiempos:** retrieval=0.018s · generación=6.220s · total=6.238s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus. Los fragmentos indican que Teotihuacán fue motivo de interés para los toltecas y los mexicas, pero no mencionan quién construyó la ciudad.
>
> Fuentes:
> * Cultura teotihuacana (Fragmento 1)
> * Cultura teotihuacana (Fragmento 2)
> * Cultura teotihuacana (Fragmento 3)
> * Cultura teotihuacana (Fragmento 4)
> * Cultura teotihuacana (Fragmento 5)

_Ayuda para Recall: 75 chunks distintos del corpus mencionan al menos un punto clave (0 mencionan 2 o más); detalle con `python evaluation/candidates.py --question F4`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.8132 | Cultura teotihuacana — _C. Primeros asentamientos en la región de Teotihuacán (antes del 300 a. C.)..._ | ninguno | [ ] |
| 2 | 0.8077 | Cultura teotihuacana — _La historia de Teotihuacán se puede entender como parte de un largo proceso civilizatorio que comenzó con la llegada de los seres humanos al Anáhuac. Esto pudo ocurrir aproximadamente hace 20 mil años, época en la que han sido fechados los descubrimientos en Tequixquiac, y más tardíamente en Tocuila..._ | ninguno | [ ] |
| 3 | 0.7983 | Cultura teotihuacana — _Teotihuacán fue ya motivo de interés para las sociedades posteriores al declive de la cultura teotihuacana en Mesoamérica. Sus ruinas se han explorado desde la época prehispánica, entre otros, por los toltecas y los mexicas. El descubrimiento de objetos teotihuacanos en los yacimientos arqueológicos..._ | Cultura teotihuacana | [ ] |
| 4 | 0.7876 | Cultura teotihuacana — _Hay poca información sobre el proceso que llevó a la fundación de Teotihuacán. A partir del Preclásico Medio se desarrolló en el valle de Teotihuacán un pequeño grupo de aldeas dedicadas a la agricultura. Estas aldeas eran contemporáneas a Terremote Tlaltenco, Tlatilco y Cuicuilco, y su desarrollo c..._ | ninguno | [ ] |
| 5 | 0.7808 | Cultura teotihuacana — _Sin embargo, Teotihuacán habría influenciado mucho al área mesoamericana. Todas las civilizaciones avanzadas de la región incorporaron el estilo Teotihuacán a su arquitectura, como testimonian las representaciones de Quetzalcoatl, la famosa "serpiente emplumada" que se encuentra prácticamente en tod..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |
| 2 | Los fragmentos indican que Teotihuacán fue motivo de interés para los toltecas y los mexicas, pero no mencionan quién construyó la ciudad. | [ ] |

---

## F5 — ¿Quién fue el último emperador azteca?

**Tipo:** factual
**Puntos clave esperados:** Cuauhtémoc; sobrino de Moctezuma II; capturado 1521
**Tiempos:** retrieval=0.016s · generación=4.862s · total=4.879s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.
>
> Fuentes usadas:
> * Fragmento 1: Hernán Cortés
> * Fragmento 2: Imperio azteca
> * Fragmento 3: Imperio azteca
> * Fragmento 4: Hernán Cortés
> * Fragmento 5: Cultura teotihuacana

_Ayuda para Recall: 40 chunks distintos del corpus mencionan al menos un punto clave (2 mencionan 2 o más); detalle con `python evaluation/candidates.py --question F5`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.7134 | Hernán Cortés — _# Hernán Cortés Hernán Cortés de Monroy y Pizarro Altamirano, primer marqués del Valle de Oaxaca (Medellín, 1485-Castilleja de la Cuesta, 2 de diciembre de 1547), fue un militar, conquistador, explorador, fundador, capitán general y escritor español que, a principios del siglo XVI, lideró la conquis..._ | ninguno | [ ] |
| 2 | 0.6911 | Imperio azteca — _A partir de entonces, los territorios del Imperio azteca se fueron ampliando hasta llegar a ocupar el centro de México, la zona central de Oaxaca, la costa del golfo de México, Guerrero y el Soconusco. El fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españoles —en alianza con lo..._ | ninguno | [ ] |
| 3 | 0.6569 | Imperio azteca — _# Imperio azteca El Imperio mexica o Triple Alianza (del náhuatl: Exkan Tlahtoloyan o Ēxcān Tlahtōlōyān ‘Los tres lugares donde se dan órdenes’), llamado también Imperio azteca y —con más precisión— Imperio tenochca, fue un imperio organizado en una confederación compleja, multiétnica y flexible de ..._ | ninguno | [ ] |
| 4 | 0.6489 | Hernán Cortés — _El fin de ciclo era inevitable y llegaría con el retorno de Quetzalcóatl un año como aquel desde donde sale el sol. Según la obra del fraile Bernardino de Sahagún y sus colaboradores nahuas, según un discurso de Moctezuma recogido en la segunda carta de Cortés a Carlos I y según otras fuentes redact..._ | ninguno | [ ] |
| 5 | 0.6483 | Cultura teotihuacana — _En enero de 378, en tiempos en que Búho Lanzadardos gobernaba en Teotihuacán, el guerrero teotihuacano Siyah K'ak' (Nace el Fuego) "conquistó" Tikal, asesinando y reemplazando al rey Chak Tok Ich'aak II, con apoyo de El Perú-Waká y Naachtún, lo que fue registrado en la Estela 31 de Tikal y otros mon..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---

## C1 — ¿Cuáles fueron las causas de la Revolución Mexicana?

**Tipo:** causalidad
**Puntos clave esperados:** Reelección de Díaz; desigualdad agraria; Plan de San Luis; crisis de 1907; Madero
**Tiempos:** retrieval=0.023s · generación=4.636s · total=4.659s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Los antecedentes de la Revolución Mexicana se remontan a la situación de México bajo la dictadura conocida como el porfiriato. Porfirio Díaz Mori ejerció el poder en el país de manera dictatorial desde 1876 hasta 1911.
>
> Fuentes: Fragmento 1

_Ayuda para Recall: 161 chunks distintos del corpus mencionan al menos un punto clave (15 mencionan 2 o más); detalle con `python evaluation/candidates.py --question C1`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.8326 | Revolución mexicana — _# Revolución mexicana La Revolución mexicana fue un conflicto armado en México que se inició el 20 de noviembre de 1910 y terminó el 5 de febrero de 1917. Los antecedentes del conflicto se remontan a la situación de México bajo la dictadura conocida como el porfiriato. Porfirio Díaz Mori ejerció el ..._ | ninguno | [ ] |
| 2 | 0.7998 | Revolución mexicana — _La Revolución mexicana conllevó varios cambios sociales. En primer lugar, los dirigentes porfiristas perdieron el poder político, aunque mantuvieron poderío económico, y las clases medias accedieron a la administración pública. “Es el momento en el que nacen el burócrata, el funcionario, el líder […..._ | ninguno | [ ] |
| 3 | 0.7572 | Historia de México — _Y gracias al impulso nacionalista que habían dado los emperadores por el interés del pasado mexicano que los intelectuales comienzan a escribir sobre la historia de México y el mundo prehispánico para hallar la identidad mexicana. Pero mantener ese nuevo orden exigía aplacar cualquier rebelión desde..._ | ninguno | [ ] |
| 4 | 0.7486 | Independencia de México — _El movimiento de la independencia de México tiene como marco la Ilustración y las revoluciones liberales de la última parte del siglo XVIII. Por esa época la élite ilustrada comenzaba a reflexionar acerca de la ideas de soberanía popular y las relaciones entre la España peninsular y el resto del imp..._ | ninguno | [ ] |
| 5 | 0.7486 | Guerra de Independencia de México **(copia exacta del rank 4: cuenta una sola vez)** — _El movimiento de la independencia de México tiene como marco la Ilustración y las revoluciones liberales de la última parte del siglo XVIII. Por esa época la élite ilustrada comenzaba a reflexionar acerca de la ideas de soberanía popular y las relaciones entre la España peninsular y el resto del imp..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Los antecedentes de la Revolución Mexicana se remontan a la situación de México bajo la dictadura conocida como el porfiriato. | [ ] |
| 2 | Porfirio Díaz Mori ejerció el poder en el país de manera dictatorial desde 1876 hasta 1911. | [ ] |

---

## C2 — ¿Por qué cayó el Imperio Azteca?

**Tipo:** causalidad
**Puntos clave esperados:** Alianzas con tlaxcaltecas; enfermedades; superioridad militar española; muerte de Moctezuma
**Tiempos:** retrieval=0.021s · generación=5.151s · total=5.172s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> El fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españoles —en alianza con los tlaxcaltecas y totonacas, entre otros pueblos indígenas— derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco.
>
> Fuentes:
> * Fragmento 1 | Fuente: Imperio azteca

_Ayuda para Recall: 34 chunks distintos del corpus mencionan al menos un punto clave (0 mencionan 2 o más); detalle con `python evaluation/candidates.py --question C2`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.7354 | Imperio azteca — _A partir de entonces, los territorios del Imperio azteca se fueron ampliando hasta llegar a ocupar el centro de México, la zona central de Oaxaca, la costa del golfo de México, Guerrero y el Soconusco. El fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españoles —en alianza con lo..._ | ninguno | [ ] |
| 2 | 0.6686 | Virreinato de Nueva España — _La conquista de Yucatán fue la más tardía de las que finalmente integraron el virreinato de la Nueva España, ya que los últimos reductos mayas no fueron dominados íntegramente hasta el año de 1697 —es decir, más de siglo y medio después de la conquista de México—, con la conquista de Tayasal. Histor..._ | ninguno | [ ] |
| 3 | 0.6680 | Hernán Cortés — _Estos regalos, en lugar de disuadir a Cortés, le animaron a continuar y conquistar México. Los aztecas creían en un mito de origen tolteca, según el cual el mundo en que vivían debía desaparecer. El dios Quetzalcóatl, una serpiente emplumada, se había marchado con cincuenta y tres años de vida en un..._ | ninguno | [ ] |
| 4 | 0.6663 | Imperio azteca — _# Imperio azteca El Imperio mexica o Triple Alianza (del náhuatl: Exkan Tlahtoloyan o Ēxcān Tlahtōlōyān ‘Los tres lugares donde se dan órdenes’), llamado también Imperio azteca y —con más precisión— Imperio tenochca, fue un imperio organizado en una confederación compleja, multiétnica y flexible de ..._ | ninguno | [ ] |
| 5 | 0.6410 | Virreinato de Nueva España — _Las estrategias indígenas con la ayuda de los tlatelolcas lograron echar de la ciudad a los conquistadores, que en el acto perdieron cerca de mil soldados y varios caudales de dinero y oro. Supuestamente, Cortés lloró derrotado al pie de un ahuehuete, por lo que se le conoce a este hecho como Noche ..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españoles —en alianza con los tlaxcaltecas y totonacas, entre otros pueblos indígenas— derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco. | [ ] |

---

## C3 — ¿Qué provocó la Guerra de Reforma?

**Tipo:** causalidad
**Puntos clave esperados:** Constitución de 1857; liberales vs conservadores; Ley Juárez; Ley Lerdo
**Tiempos:** retrieval=0.018s · generación=5.024s · total=5.042s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> La Guerra de Reforma, también conocida como la guerra de los tres años, fue provocada por la promulgación de la Constitución de 1857 y en especial de las llamadas Leyes de Reforma. El país estaba dividido en dos grandes grupos: liberales (a favor de las Leyes de Reforma) y los conservadores (en contra).
>
> Fuentes: Fragmento 1.

_Ayuda para Recall: 294 chunks distintos del corpus mencionan al menos un punto clave (42 mencionan 2 o más); detalle con `python evaluation/candidates.py --question C3`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.7463 | Guerra de Reforma — _# Guerra de Reforma La Guerra de Reforma, también conocida como la guerra de los tres años, fue una guerra civil que aconteció en México desde el 17 de diciembre de 1857 al 11 de enero de 1861, como consecuencia de la promulgación de la Constitución de 1857 y en especial de las llamadas Leyes de Ref..._ | Constitución de 1857, liberales vs conservadores | [ ] |
| 2 | 0.6383 | Civilización maya — _debido a una proliferación de la guerra...._ | ninguno | [ ] |
| 3 | 0.6012 | Historia de México — _Quizá aquel tiempo marcó el inicio del desgaste del régimen. Mientras se inauguraban obras y recintos cada vez más grandes y opulentos se empezaron a sumar represiones y mascares cada vez más violentas y sangrientas. Eso sumado a los aires de lucha obrera y social que se daban en todo el mundo, marc..._ | ninguno | [ ] |
| 4 | 0.5959 | Historia de México — _Si en la guerra de Reforma había surgido para que la Iglesia dejara de meterse en asuntos del Estado, ahora el Estado quería meterse en los asuntos de la Iglesia. A 7 años de la creación de la Constitución, el artículo no solo era violado por la Iglesia católica, sino que la construcción del Cristo ..._ | ninguno | [ ] |
| 5 | 0.5803 | Revolución mexicana — _Tras el triunfo de la revolución constitucionalista en agosto de 1914 y el posterior exilio de Victoriano Huerta, Obregón reabrió la COM. Sin embargo, la lucha entre las facciones carrancistas y convencionistas causó debates sobre el camino que debía de seguir la organización. Los argumentos del pin..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | La Guerra de Reforma, también conocida como la guerra de los tres años, fue provocada por la promulgación de la Constitución de 1857 y en especial de las llamadas Leyes de Reforma. | [ ] |
| 2 | El país estaba dividido en dos grandes grupos: liberales (a favor de las Leyes de Reforma) y los conservadores (en contra). | [ ] |

---

## C4 — ¿Por qué terminó el Porfiriato?

**Tipo:** causalidad
**Puntos clave esperados:** Revolución Mexicana; renuncia de Díaz en 1911; Plan de San Luis; descontento social
**Tiempos:** retrieval=0.018s · generación=4.133s · total=4.151s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> El Porfiriato terminó el 27 de mayo de 1911 con el exilio de Porfirio Díaz.
>
> Fuentes:
> * Fragmento 5 | Fuente: Historia de México

_Ayuda para Recall: 94 chunks distintos del corpus mencionan al menos un punto clave (6 mencionan 2 o más); detalle con `python evaluation/candidates.py --question C4`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.5558 | Porfiriato — _La primera etapa del porfiriato empieza en 1877 y termina en el inicio de tercer periodo presidencial de Porfirio Díaz (1888) o cuando se eliminó toda restricción legal a la reelección indefinida (1890). Se trata de una fase de construcción, pacificación, unificación, conciliación y negociación, per..._ | ninguno | [ ] |
| 2 | 0.5515 | Historia de México — _Don Porfirio es militar de carrera y político de trayectoria, lidió con el país casi 30 años. Las nuevas generaciones que llegaban a la política no conocían de guerras, levantamientos, ni golpes de Estado como él los había visto en su niñez y juventud. Antes de tomar su decisión final dice: Madero h..._ | ninguno | [ ] |
| 3 | 0.5512 | Porfiriato — _# Porfiriato El porfiriato o porfirismo fue un período de la historia de México en el que el gobierno estuvo bajo el control (total o mayoritario) del militar, político y dictador Porfirio Díaz, entre el 28 de noviembre de 1876 y el 27 de mayo de 1911. En el porfiriato la política se aplicó de tal m..._ | renuncia de Díaz en 1911 | [ ] |
| 4 | 0.5289 | Moctezuma II — _Los datos ofrecidos en el Códice Florentino sobre esta leyenda fueron escritos décadas después de la conquista, aproximadamente en 1555. Historiadores modernos, como Matthew Restall, por lo tanto, han llegado a la conclusión de que es posible que algunos de los eventos descritos hayan sucedido, pero..._ | ninguno | [ ] |
| 5 | 0.5257 | Historia de México — _El ascenso de Porfirio Díaz al poder en 1876 empezó un periodo conocido como el Porfiriato, mismo que duró hasta 1911 con su exilio. En 1910 inició la Revolución Mexicana, un periodo de grandes conflictos entre múltiples facciones y con distintos principios durante el transcurso de la misma: su fech..._ | Revolución Mexicana, renuncia de Díaz en 1911 | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El Porfiriato terminó el 27 de mayo de 1911 con el exilio de Porfirio Díaz. | [ ] |

---

## V1 — ¿En qué se diferencian los mayas y los olmecas?

**Tipo:** comparativa
**Puntos clave esperados:** Olmecas: civilización madre, cabezas colosales, zona costera; Mayas: escritura, calendario, ciudades-estado
**Tiempos:** retrieval=0.020s · generación=4.790s · total=4.810s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.
>
> Fuentes usadas:
> * Fragmento 1: Civilización maya
> * Fragmento 2: Civilización maya
> * Fragmento 3: Cultura teotihuacana
> * Fragmento 4: Civilización maya
> * Fragmento 5: Civilización maya

_Ayuda para Recall: 247 chunks distintos del corpus mencionan al menos un punto clave (31 mencionan 2 o más); detalle con `python evaluation/candidates.py --question V1`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.6418 | Civilización maya — _El territorio de los mayas y los mayas mantuvieron una relación dinámica con las culturas vecinas, incluyendo los olmecas, los mixtecos, los de Teotihuacán, los aztecas, y otros. Durante el periodo Clásico Temprano, las ciudades mayas de Tikal y Kaminaljuyú fueron focos claves en una red que se exte..._ | Olmecas, Mayas | [ ] |
| 2 | 0.6090 | Civilización maya — _sido la lengua de prestigio de la élite maya del Clásico, utilizado en la comunicación entre las entidades políticas, como la diplomacia y el comercio. Por el período Posclásico, se utilizó también el yucateco en los códices mayas, junto al choltí clásico. Escritura maya..._ | Mayas, escritura | [ ] |
| 3 | 0.6035 | Cultura teotihuacana — _C.) y más tarde. Asimismo, los autores señalan que existe una estrecha relación entre reglas comunes de representación gráfica del sistema teotihuacano, los del zapoteco, el epi-olmeca y el maya para crear un sistema totalmente autóctono empleado por los habitantes de la ciudad, siendo el mismo comp..._ | ninguno | [ ] |
| 4 | 0.5899 | Civilización maya — _El mundo maya estaba poblado por una gran variedad de deidades, entidades sobrenaturales y poderes sagrados. Los mayas tenían una tan amplia interpretación de lo que era sagrado, que la identificación de deidades con diferentes funciones específicas sería incorrecta. La interpretación maya de las de..._ | Mayas, calendario | [ ] |
| 5 | 0.5779 | Civilización maya — _# Cultura maya La cultura maya fue una civilización mesoamericana que se desarrolló en lo que actualmente comprenden los territorios de Guatemala y México (en la península de Yucatán, Chiapas y Tabasco) principalmente, así como en Belice, y la parte occidental de Honduras y El Salvador (Correspondie..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---

## V2 — ¿Qué diferencias hay entre Zapata y Villa?

**Tipo:** comparativa
**Puntos clave esperados:** Zapata: agrarismo, sur, Plan de Ayala; Villa: norte, División del Norte, carácter militar
**Tiempos:** retrieval=0.018s · generación=5.825s · total=5.843s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Villa aceptó el Plan de Ayala, a excepción de sus acusaciones a Francisco I. Madero, quien había sido su redentor, y se obligó a dar armas a Zapata. Zapata insistió en que la devolución de tierras fuese constitucional. Tras las discrepancias que Carranza había tenido con Villa, firmaron el Pacto de Torreón, donde Villa presentaba disculpas a Carranza.
>
> Fuentes: Fragmento 1, Fragmento 2, Fragmento 5.

_Ayuda para Recall: 593 chunks distintos del corpus mencionan al menos un punto clave (88 mencionan 2 o más); detalle con `python evaluation/candidates.py --question V2`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.6032 | Emiliano Zapata — _Alcanzó así fama nacional el movimiento zapatista como la otra cara de la moneda entre los campesinos surianos y los del norte. El 4 de diciembre de ese año Villa y Zapata tuvieron la célebre entrevista de Xochimilco, lográndose una alianza militar entre ambos ejércitos. Villa aceptó en cambio el pl..._ | Zapata, Plan de Ayala, Villa, norte | [ ] |
| 2 | 0.5638 | Pancho Villa — _Tuvo entonces lugar el Pacto de Xochimilco, en el que Pancho Villa aceptó el Plan de Ayala en lo relativo al problema de la tierra y en el que convenían llevar a la presidencia a un civil identificado con la Revolución. Villa y Zapata entraron juntos al Palacio Nacional con el presidente convencioni..._ | Zapata, Plan de Ayala, Villa | [ ] |
| 3 | 0.5593 | Pancho Villa — _un bandido que cometió crímenes haciéndose pasar por villista. Es sabido que Pancho Villa y Emiliano Zapata son figuras históricas que han sido denostadas, calumniadas por la prensa de la época y hasta han querido borrarlos de la historia de México. El mismo Venustiano Carranza llegó a utilizar a la..._ | Zapata, Villa | [ ] |
| 4 | 0.5527 | Revolución mexicana — _Cuando Viva Villa Es La Muerte (del año 1960), con Pedro Armendariz en el papel de Pancho Villa. Viva Villa (del año 1935), con Wallace Beery en el papel de Villa. Vámonos con Pancho Villa (1935) de Fernando de Fuentes. La Adelita (1937) de Guillermo Hernández G.. Con los Dorados de Villa (1939) de ..._ | Zapata, Villa | [ ] |
| 5 | 0.5506 | Historia de México — _Tras las discrepancias que Carranza había tenido con Villa, el 8 de julio firmaron el Pacto de Torreón, donde Villa presentaba disculpas a Carranza que seguiría como primer jefe a cambio de convocar una convención de generales que crearan un nuevo programa de gobierno que satisficiera a todos. Mient..._ | Zapata, Plan de Ayala, Villa | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Villa aceptó el Plan de Ayala, a excepción de sus acusaciones a Francisco I. Madero, quien había sido su redentor, y se obligó a dar armas a Zapata. | [ ] |
| 2 | Zapata insistió en que la devolución de tierras fuese constitucional. | [ ] |
| 3 | Tras las discrepancias que Carranza había tenido con Villa, firmaron el Pacto de Torreón, donde Villa presentaba disculpas a Carranza. | [ ] |

---

## V3 — ¿En qué se parecen el Virreinato y el Imperio Azteca?

**Tipo:** comparativa
**Puntos clave esperados:** Control centralizado; tributo; dominio territorial; jerarquía religiosa ligada al poder
**Tiempos:** retrieval=0.023s · generación=4.956s · total=4.979s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.
>
> Fuentes usadas:
> * Fragmento 1: Imperio azteca
> * Fragmento 2: Virreinato de Nueva España
> * Fragmento 3: Imperio azteca
> * Fragmento 4: Imperio azteca
> * Fragmento 5: Imperio azteca

_Ayuda para Recall: 63 chunks distintos del corpus mencionan al menos un punto clave (0 mencionan 2 o más); detalle con `python evaluation/candidates.py --question V3`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.7202 | Imperio azteca — _# Imperio azteca El Imperio mexica o Triple Alianza (del náhuatl: Exkan Tlahtoloyan o Ēxcān Tlahtōlōyān ‘Los tres lugares donde se dan órdenes’), llamado también Imperio azteca y —con más precisión— Imperio tenochca, fue un imperio organizado en una confederación compleja, multiétnica y flexible de ..._ | ninguno | [ ] |
| 2 | 0.6782 | Virreinato de Nueva España — _Filipinas y Oceanía. Situación de los pueblos prehispánicos Cuando los españoles llegaron al Nuevo Mundo, se encontraron con civilizaciones muy bien constituidas: el imperio teocrático de los incas que estaba en su apogeo, la confederación de los mexicas y la cultura maya. Los conflictos entre los d..._ | ninguno | [ ] |
| 3 | 0.6610 | Imperio azteca — _A partir de entonces, los territorios del Imperio azteca se fueron ampliando hasta llegar a ocupar el centro de México, la zona central de Oaxaca, la costa del golfo de México, Guerrero y el Soconusco. El fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españoles —en alianza con lo..._ | ninguno | [ ] |
| 4 | 0.6380 | Imperio azteca — _Smith, Michael E.; Berdan, Frances F. (2021). Everyday Life in the Aztec World (en inglés). Cambridge University Press. ISBN 978-0-521-51636-5. LCCN 2019052441. doi:10.1017/9781139031844. Enlaces externos Wikimedia Commons alberga una categoría multimedia sobre Imperio azteca...._ | ninguno | [ ] |
| 5 | 0.6251 | Imperio azteca — _Originalmente, el imperio azteca era una alianza suelta entre tres ciudades: Tenochtitlan, Texcoco y el socio menor, Tlacopan. Como tales, eran conocidos como la 'Triple Alianza'. Esta forma política era muy común en Mesoamérica, donde las alianzas de ciudades-estado fluctuaban siempre...._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---

## R1 — ¿Qué relación tuvo Juárez con la Guerra de Reforma?

**Tipo:** relacional
**Puntos clave esperados:** Juárez lideró el bando liberal; promulgó las Leyes de Reforma; fue presidente durante el conflicto
**Tiempos:** retrieval=0.019s · generación=5.518s · total=5.538s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Juárez fue una figura clave tanto en la Guerra de Reforma como en la segunda intervención francesa, a pesar de no tener antecedentes militares. Fue el círculo cercano a Juárez quien le hizo ver que la guerra ya no era por defensa de las leyes liberales o la reforma, sino por soberanía nacional.
>
> Fuentes:
> * Fragmento 1: Benito Juárez
> * Fragmento 2: Historia de México

_Ayuda para Recall: 49 chunks distintos del corpus mencionan al menos un punto clave (1 mencionan 2 o más); detalle con `python evaluation/candidates.py --question R1`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.7746 | Benito Juárez — _Benito Juárez vivió una época crucial en la formación del Estado mexicano, considerada por muchos historiadores como la consolidación de la nación como república. Juárez marcó un parteaguas en la historia nacional y fue protagonista de primer nivel de esta época. A pesar de tratarse de un presidente..._ | ninguno | [ ] |
| 2 | 0.7139 | Historia de México — _Con la idea de poner fin a los levantamientos, Maximiliano decretó amnistía a quienes se unieran a su causa y envió una carta a Juárez para reunirse en la Ciudad de México y llegar a un acuerdo de paz, pero Juárez, temiendo una traición o una emboscada, se negó a pactar con él cualquier acuerdo. Fue..._ | promulgó las Leyes de Reforma | [ ] |
| 3 | 0.7138 | Historia de México — _Pero la estrategia jugó en su contra. Si bien la idea era introducir gobernantes de pensamiento liberal en estas ciudades, los verdaderos liberales le eran fiel a Juárez. De hecho Pedro Escudo y José María Cortés y Esparza, que habían participado en el Congreso Constituyente para la Constitución del..._ | ninguno | [ ] |
| 4 | 0.7000 | Historia de México — _Rompiendo las líneas defensivas en Veracruz y luego Córdoba, Zaragoza se apresuba a preparar un ejército en Puebla. Ante el avance victorioso de Charles Ferdinand Latrille, conde de Lorencez, este, escribió a Napoleón III:"Somos tan superiores a los mexicanos en organización, disciplina, raza, moral..._ | ninguno | [ ] |
| 5 | 0.6986 | Benito Juárez — _Luego de pasar por el paseo de la Reforma, Juárez y su comitiva se dirigen hacia el Palacio de Minería por la que hoy es la avenida Juárez. Juárez había decretado que se dejara en libertad a todos los presos que apoyaron la causa imperial. Iniciaba la reconciliación nacional. En el Palacio de Minerí..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Juárez fue una figura clave tanto en la Guerra de Reforma como en la segunda intervención francesa, a pesar de no tener antecedentes militares. | [ ] |
| 2 | Fue el círculo cercano a Juárez quien le hizo ver que la guerra ya no era por defensa de las leyes liberales o la reforma, sino por soberanía nacional. | [ ] |

---

## R2 — ¿Cómo se relacionan Hernán Cortés y Moctezuma II?

**Tipo:** relacional
**Puntos clave esperados:** Encuentro en Tenochtitlan en 1519; Moctezuma tomado como rehén; su muerte; destrucción del imperio
**Tiempos:** retrieval=0.020s · generación=6.020s · total=6.040s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Hernán Cortés y Moctezuma II intercambiaron regalos cuando se conocieron y los españoles fueron alojados en el Palacio de Axayácatl. Cortés reportó que Moctezuma le había ofrecido todas sus tierras al rey de España, aunque algunos historiadores cuestionan esto. Cortés también envió mensajes a Moctezuma a través de calpixques.
>
> Fuentes: Fragmento 1, Fragmento 2, Fragmento 3, Fragmento 5.

_Ayuda para Recall: 145 chunks distintos del corpus mencionan al menos un punto clave (1 mencionan 2 o más); detalle con `python evaluation/candidates.py --question R2`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.7540 | Moctezuma II — _Según se describió en la segunda carta de relación de Hernán Cortés al emperador Carlos V:..._ | ninguno | [ ] |
| 2 | 0.6652 | Hernán Cortés — _Hernán Cortés: Página de relación Historia de los restos de Cortés Portal dedicado a Hernán Cortés en la Biblioteca Virtual Miguel de Cervantes...._ | ninguno | [ ] |
| 3 | 0.6570 | Moctezuma II — _Cortés y Moctezuma intercambiaron regalos cuando se conocieron y los españoles fueron alojados en el Palacio de Axayácatl, donde actualmente está el edificio del Nacional Monte de Piedad. Cortés reportó que Moctezuma le había entonces ofrecido inmediatamente todas sus tierras al rey de España, aunqu..._ | ninguno | [ ] |
| 4 | 0.6452 | Moctezuma II — _La ortografía Moctezuma es la más frecuente y moderna; no obstante, Hernán Cortés transcribió su nombre como Mutecçuma o Muteçuma y la mayoría de las fuentes de los siglos xvi y xvii refieren que su nombre fue Moteucçoma, incluido fray Bernardino de Sahagún que usó una forma más próxima al náhuatl: ..._ | ninguno | [ ] |
| 5 | 0.6376 | Hernán Cortés — _Cortés encargó que dos de los calpixques fuesen a su presencia, se mostró ajeno a lo ocurrido y les dio un mensaje para Moctezuma, indicando que quería ser su amigo e ir a visitarlo. Posteriormente, repitió la operación con los otros tres. Tras esto, un pueblo vecino, por instigación de los aztecas,..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Hernán Cortés y Moctezuma II intercambiaron regalos cuando se conocieron y los españoles fueron alojados en el Palacio de Axayácatl. | [ ] |
| 2 | Cortés reportó que Moctezuma le había ofrecido todas sus tierras al rey de España, aunque algunos historiadores cuestionan esto. | [ ] |
| 3 | Cortés también envió mensajes a Moctezuma a través de calpixques. | [ ] |

---

## R3 — ¿Qué papel jugó el Virreinato en la Independencia?

**Tipo:** relacional
**Puntos clave esperados:** Agravios acumulados; criollos excluidos del poder; influencia ilustrada; debilitamiento de España
**Tiempos:** retrieval=0.020s · generación=4.452s · total=4.472s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.
>
> Fuentes usadas:
> * Independencia de México
> * Guerra de Independencia de México
> * Independencia de México
> * Guerra de Independencia de México
> * Historia de México

_Ayuda para Recall: 2 chunks distintos del corpus mencionan al menos un punto clave (0 mencionan 2 o más); detalle con `python evaluation/candidates.py --question R3`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.6324 | Independencia de México — _Este fue un punto de discordia con López Rayón quien manifestó no estar de acuerdo con el primer punto mencionado en los Sentimientos de la Nación, pues defendía que la tesis que había abrazado el movimiento autonomista de 1808, debería seguir subsistiendo, es decir, América era dependiente del rey ..._ | ninguno | [ ] |
| 2 | 0.6324 | Guerra de Independencia de México **(copia exacta del rank 1: cuenta una sola vez)** — _Este fue un punto de discordia con López Rayón quien manifestó no estar de acuerdo con el primer punto mencionado en los Sentimientos de la Nación, pues defendía que la tesis que había abrazado el movimiento autonomista de 1808, debería seguir subsistiendo, es decir, América era dependiente del rey ..._ | ninguno | [ ] |
| 3 | 0.6303 | Independencia de México — _Durante esta época, el movimiento independentista no solo realizó acciones bélicas, sino que se dotó a sí mismo de una estructura y un cuerpo jurídico. Durante este período cobra importancia el posicionamiento ideológico de la causa insurgente. Composición social del movimiento..._ | ninguno | [ ] |
| 4 | 0.6303 | Guerra de Independencia de México **(copia exacta del rank 3: cuenta una sola vez)** — _Durante esta época, el movimiento independentista no solo realizó acciones bélicas, sino que se dotó a sí mismo de una estructura y un cuerpo jurídico. Durante este período cobra importancia el posicionamiento ideológico de la causa insurgente. Composición social del movimiento..._ | ninguno | [ ] |
| 5 | 0.6275 | Historia de México — _Así, tras 10 días de intenso debate y acuerdos entre ambos, el 24 de febero de 1821 proclaman el Plan de Iguala que proclamaba la Independencia de la América Septentrional bajo tres garantías: independencia, unión y religión. Se propuso un gobierno monárquico templado por una constitución que solici..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---

## M1 — ¿Qué civilizaciones existían antes de los españoles y cuál dominaba en 1519?

**Tipo:** multihop
**Puntos clave esperados:** Olmecas; mayas; teotihuacanos; aztecas; el Imperio Azteca dominaba en 1519
**Tiempos:** retrieval=0.023s · generación=4.676s · total=4.699s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Antes de la llegada de los españoles, existían civilizaciones como el imperio teocrático de los incas, la confederación de los mexicas y la cultura maya. El imperio teocrático de los incas estaba en su apogeo en 1519.
>
> Fuentes: Fragmento 2.

_Ayuda para Recall: 222 chunks distintos del corpus mencionan al menos un punto clave (4 mencionan 2 o más); detalle con `python evaluation/candidates.py --question M1`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.7850 | Historia de México — _El periodo prehispánico se refiere a todo lo acontecido antes de la llegada de los españoles en 1519. En dicho periodo ocurrió el poblamiento del territorio, el inicio de la agricultura y la conformación del sedentarismo en tres grandes áreas culturales: Aridoamérica, Oasisamérica y Mesoamérica. La ..._ | ninguno | [ ] |
| 2 | 0.7140 | Virreinato de Nueva España — _Filipinas y Oceanía. Situación de los pueblos prehispánicos Cuando los españoles llegaron al Nuevo Mundo, se encontraron con civilizaciones muy bien constituidas: el imperio teocrático de los incas que estaba en su apogeo, la confederación de los mexicas y la cultura maya. Los conflictos entre los d..._ | ninguno | [ ] |
| 3 | 0.6832 | Virreinato de Nueva España — _Los dominicos fueron la otra orden importante que se estableció en el virreinato, con poco tiempo de diferencia de los franciscanos. Llegaron hacia 1526 y establecieron sus misiones en Oaxaca y Chiapas. Bartolomé de las Casas presidió esta organización religiosa durante su estancia en Nueva España, ..._ | ninguno | [ ] |
| 4 | 0.6803 | Virreinato de Nueva España — _En la literatura virreinal novohispana es posible distinguir varios periodos. En el primero, la literatura está vinculada con el momento histórico de la conquista, y en él abundan las cartas y crónicas. Relación breve de la conquista de la Nueva España, de Francisco de Aguilar (1479-1571). Itinerari..._ | ninguno | [ ] |
| 5 | 0.6716 | Historia de México — _A partir de la institución del Virreinato, entre 1521 y 1535 en distintas zonas de México, empezaría una Edad Media, mezcla de feudalismo con despotismo tributario. En sus inicios, este feudalismo se caracterizaba como una copia del español peninsular a través de la figura de la encomienda indiana. ..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Antes de la llegada de los españoles, existían civilizaciones como el imperio teocrático de los incas, la confederación de los mexicas y la cultura maya. | [ ] |
| 2 | El imperio teocrático de los incas estaba en su apogeo en 1519. | [ ] |

---

## M2 — ¿Cómo influyeron las reformas de Juárez en la Revolución décadas después?

**Tipo:** multihop
**Puntos clave esperados:** Constitución de 1857; separación Iglesia-Estado; antecedente liberal que Díaz traicionó
**Tiempos:** retrieval=0.020s · generación=3.797s · total=3.816s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.
>
> Fuentes usadas:
> * Historia de México
> * Benito Juárez
> * Guerra de Independencia de México

_Ayuda para Recall: 32 chunks distintos del corpus mencionan al menos un punto clave (0 mencionan 2 o más); detalle con `python evaluation/candidates.py --question M2`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.7401 | Historia de México — _Fue paradójico que quien mayor impulso dio al poder liberal, fuese la corona de Maximiliano, y eso lo sabía Juárez. Por eso cuando Juárez retornó triunfal como presidente a la Ciudad de México en julio de 1867, la mejor forma en que pudo legitimar el poder republicano fue restablecer la Constitución..._ | Constitución de 1857 | [ ] |
| 2 | 0.7386 | Benito Juárez — _Benito Juárez vivió una época crucial en la formación del Estado mexicano, considerada por muchos historiadores como la consolidación de la nación como república. Juárez marcó un parteaguas en la historia nacional y fue protagonista de primer nivel de esta época. A pesar de tratarse de un presidente..._ | ninguno | [ ] |
| 3 | 0.7015 | Historia de México — _El día 11 de enero de 1861, Benito Juárez hizo su entrada triunfal en la capital mexicana celebrada por un pueblo cansado de la guerra y organizó un nuevo gabinete. Tras proclamar elecciones, el apoyo a los liberales se hizo rotundamente evidente y Juárez se convirtió en el presidente del país. Al r..._ | ninguno | [ ] |
| 4 | 0.6979 | Historia de México — _Temiendo que el Congreso tuviese más poder como había ocurrido toda la primera mitad del siglo XIX, Juárez dividió al poder legislativo en cámara alta y baja, Senadores y Diputados. Reorganizó al ejército para disminuir su poder, permitió que el presidente pudiese vetar disposiciones del Congreso y ..._ | ninguno | [ ] |
| 5 | 0.6945 | Guerra de Independencia de México — _Este grupo estaba concentrado en los consulados de México y Guadalajara, que constituyeron la pieza fundamental en la circulación de capitales en el territorio novohispano. El poder económico de los consulados respaldaba su capacidad de representación política, gestión y cabildeo. La economía novohi..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---

## T1 — ¿Quién es el presidente actual de México?

**Tipo:** trampa  (pregunta trampa)
**Tiempos:** retrieval=0.018s · generación=4.865s · total=4.883s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> La actual presidenta de México es Claudia Sheinbaum, quien ganó las elecciones presidenciales de 2024 y asumió el cargo el 1 de octubre de 2024, convirtiéndose en la primera mujer en dirigir el país en la historia de México.
>
> Fuentes: Fragmento 2.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.7447 | Historia de México — _antes del México moderno, definido por la llegada de caudillos militares como jefes de Gobierno. El México moderno abarca la consolidación del presidencialismo (y los sexenios), la estabilidad de los partidos políticos y culmina con el inicio de cambio de régimen en 1994. Se le denomina México conte..._ | — | [ ] |
| 2 | 0.7208 | Historia de México — _Claudia Sheinbaum, sucesora política del presidente López Obrador, ganó las elecciones presidenciales de 2024 y al asumir el cargo, se convirtió en la primera mujer en dirigir el país en la historia de México. Fue juramentada como presidenta de México el 1 de octubre de 2024. Véase también Portal:Hi..._ | — | [ ] |
| 3 | 0.6884 | Historia de México — _El 2 de julio de 2000 se llevaron a cabo las elecciones presidenciales; México vivió por primera vez, tras 71 años de gobiernos priistas, la alternancia política cuando Vicente Fox candidato de la Alianza por el cambio (de los partidos Acción Nacional y Verde Ecologista de México), con el 43.5 % de ..._ | — | [ ] |
| 4 | 0.6876 | Historia de México — _Así, el 2 de septiembre de 1932, Pascual Ortiz Rubio se presentó ante el congreso diciendo: Salgo con las manos limpias de sangre y dinero, y prefiero irme, y no quedarme aquí sostenido por las bayonetas del ejército mexicano. Fue el primer y único presidente en la historia de México en renunciar al..._ | — | [ ] |
| 5 | 0.6749 | Benito Juárez — _# Benito Juárez Benito Pablo Juárez García (San Pablo Guelatao, Intendencia de Oaxaca; 21 de marzo de 1806 - Ciudad de México, 18 de julio de 1872), conocido como El Benemérito de las Américas, fue un abogado, jurista y político mexicano de origen indígena de la etnia zapoteca que se desempeñó como ..._ | — | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | La actual presidenta de México es Claudia Sheinbaum, quien ganó las elecciones presidenciales de 2024 y asumió el cargo el 1 de octubre de 2024, convirtiéndose en la primera mujer en dirigir el país en la historia de México. | [ ] |

---

## T2 — ¿Cuál es el PIB actual de México?

**Tipo:** trampa  (pregunta trampa)
**Tiempos:** retrieval=0.020s · generación=3.896s · total=3.916s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.
>
> Fuentes usadas:
> * Historia de México
> * Porfiriato
> * Revolución mexicana
> * Independencia de México

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.6469 | Historia de México — _antes del México moderno, definido por la llegada de caudillos militares como jefes de Gobierno. El México moderno abarca la consolidación del presidencialismo (y los sexenios), la estabilidad de los partidos políticos y culmina con el inicio de cambio de régimen en 1994. Se le denomina México conte..._ | — | [ ] |
| 2 | 0.6258 | Porfiriato — _Así, la administración de los recursos nacionales se hacía con participación pública y privada. El Banco Nacional Mexicano, fundado en 1882, se fusionó con el Banco Mercantil Mexicano y dio origen al Banco Nacional de México en 1884. En este banco participaba capital mexicano y español, y tenía las ..._ | — | [ ] |
| 3 | 0.6256 | Revolución mexicana — _Durante estos 35 años, México experimentó un notable crecimiento económico y tuvo estabilidad política, pero estos logros se realizaron con altos costos sociales, que pagaron los estratos menos favorecidos de la sociedad y la oposición política al régimen de Díaz. Durante la primera década del siglo..._ | — | [ ] |
| 4 | 0.6115 | Historia de México — _la burguesía mexicana, tasada en ese momento en 40 000 millones de dólares, no obstante dicha cifra se siguió incrementando por los altas tasas de interés a pagar. El gobierno inició una diversificación de los mercados receptores de productos mexicanos, para disminuir la dependencia con Estados Unid..._ | — | [ ] |
| 5 | 0.5970 | Independencia de México — _La pérdida de esta posesión tuvo una importancia decisiva para la economía del Imperio español, ya que los ingresos mexicanos representaban el ochenta por ciento del total de los caudales americanos al final del periodo colonial. La guerra por la independencia mexicana comenzó el día 16 de septiembr..._ | — | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---

## T3 — ¿Qué equipos jugaron la final del fútbol mexicano en 2024?

**Tipo:** trampa  (pregunta trampa)
**Tiempos:** retrieval=0.021s · generación=4.049s · total=4.069s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.
>
> Fuentes:
> * Historia de México
> * Independencia de México
> * Guerra de Independencia de México
> * Revolución mexicana

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.6401 | Historia de México — _antes del México moderno, definido por la llegada de caudillos militares como jefes de Gobierno. El México moderno abarca la consolidación del presidencialismo (y los sexenios), la estabilidad de los partidos políticos y culmina con el inicio de cambio de régimen en 1994. Se le denomina México conte..._ | — | [ ] |
| 2 | 0.6061 | Independencia de México — _Ese mismo año, la República mexicana se integró por diecinueve estados (Yucatán argumentaría más tarde su incorporación como república federada), cinco territorios y un distrito federal. Galería de imágenes Véase también Grito de Dolores Nueva España Batallas de la Guerra de Independencia de México ..._ | — | [ ] |
| 3 | 0.6061 | Guerra de Independencia de México **(copia exacta del rank 2: cuenta una sola vez)** — _Ese mismo año, la República mexicana se integró por diecinueve estados (Yucatán argumentaría más tarde su incorporación como república federada), cinco territorios y un distrito federal. Galería de imágenes Véase también Grito de Dolores Nueva España Batallas de la Guerra de Independencia de México ..._ | — | [ ] |
| 4 | 0.5681 | Historia de México — _Así, mientras el resto del mundo se ocupaba en librar la Gran Guerra que estaba por marcar el fin de la era imperialista del siglo XIX, finalmente el 5 de febrero, se promulgó la Constitución de 1917. Ese día se retiró el último norteamericano de México tras la fracasada expedición punitiva y con ca..._ | — | [ ] |
| 5 | 0.5663 | Revolución mexicana — _Las fuentes disponibles no concuerdan en cuanto al fin de la Revolución mexicana. Algunas fuentes lo sitúan en el año de 1917, con la proclamación de la Constitución mexicana, o 1924 con la de Plutarco Elías Calles. Por otro lado, el historiador Alan Knight, de la Universidad de Oxford, incluso aseg..._ | — | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---
