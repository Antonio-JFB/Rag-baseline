# Hoja de evaluación manual

Protocolo: para cada pregunta, (1) marca qué chunks recuperados son genuinamente relevantes para responderla -- usa los **puntos clave esperados** como referencia, no tu propio conocimiento de historia; (2) marca qué afirmaciones de la respuesta están respaldadas por el texto de los chunks recuperados (Faithfulness) -- si una afirmación es correcta históricamente pero no aparece en los chunks, cuenta como **no respaldada**, porque el sistema no la pudo haber sacado del contexto. Para preguntas trampa, la respuesta correcta es que el sistema declare que no encontró la información -- marca eso como relevante/respaldado si ocurre así. Al terminar cada pregunta, marca la casilla **Anotada** (así `metrics.py` sabe cuáles ya revisaste y no confunde una pregunta pendiente con una donde todo resultó irrelevante).

Total de preguntas: 20

---

## F1 — ¿En qué año cayó Tenochtitlan?

**Tipo:** factual
**Puntos clave esperados:** 1521; Cuauhtémoc; tlaxcaltecas
**Tiempos:** retrieval=0.020s · generación=212.870s · total=212.890s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Tenochtitlan cayó en 1521.

Fuentes:
* Fragmento 3: Historia de México
* Fragmento 4: Virreinato de Nueva España
* Fragmento 5: Tenochtitlan

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.6815 | Hernán Cortés — _Sitio y caída de Tenochtitlan Después de su derrota de la Noche Triste, los españoles y sus aliados..._ | [ ] |
| 2 | 0.6645 | Historia de México — _A inicios de siglo XVI, se empezó a notar la intransigencia del imperio y el odio que México Tenocht..._ | [ ] |
| 3 | 0.6558 | Historia de México — _Fue la primera vez desde la conquista de Tenochtitlán en 1521, que la Ciudad de México volvió a ver..._ | [ ] |
| 4 | 0.6459 | Virreinato de Nueva España — _Se originó tras la caída de México-Tenochtitlan, acontecimiento principal de la conquista, la que pr..._ | [ ] |
| 5 | 0.6383 | Tenochtitlan — _# Tenochtitlan Tenochtitlan puede hacer referencia a: México-Tenochtitlan, ciudad principal de los m..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Tenochtitlan cayó en 1521. | [ ] |
| 2 | Fuentes:
* Fragmento 3: Historia de México
* Fragmento 4: Virreinato de Nueva España
* Fragmento 5: Tenochtitlan | [ ] |

---

## F2 — ¿Quién dio el Grito de Independencia?

**Tipo:** factual
**Puntos clave esperados:** Miguel Hidalgo; Dolores Hidalgo; 16 septiembre 1810
**Tiempos:** retrieval=0.024s · generación=3.958s · total=3.982s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

Fuentes:
* Historia de México
* Independencia de México
* Guerra de Independencia de México
* Miguel Hidalgo y Costilla

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.6622 | Historia de México — _Así, tras 10 días de intenso debate y acuerdos entre ambos, el 24 de febero de 1821 proclaman el Pla..._ | [ ] |
| 2 | 0.6480 | Historia de México — _La profundización y radicalización del movimiento insurgente llevó a la convocatoria, de parte de Mo..._ | [ ] |
| 3 | 0.6196 | Independencia de México — _Este fue un punto de discordia con López Rayón quien manifestó no estar de acuerdo con el primer pun..._ | [ ] |
| 4 | 0.6196 | Guerra de Independencia de México — _Este fue un punto de discordia con López Rayón quien manifestó no estar de acuerdo con el primer pun..._ | [ ] |
| 5 | 0.5881 | Miguel Hidalgo y Costilla — _perdiendo en la derrota gran cantidad de dinero, armas y tropas, y quedando herida de muerte la prim..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |
| 2 | Fuentes:
* Historia de México
* Independencia de México
* Guerra de Independencia de México
* Miguel Hidalgo y Costilla | [ ] |

---

## F3 — ¿Cuándo comenzó el Porfiriato?

**Tipo:** factual
**Puntos clave esperados:** 1876; Porfirio Díaz; reelección continua
**Tiempos:** retrieval=0.016s · generación=4.609s · total=4.625s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> El Porfiriato comenzó el 28 de noviembre de 1876 y duró hasta el 27 de mayo de 1911.

Fuentes:
* Fragmento 3: Porfiriato
* Fragmento 2: Historia de México

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.6303 | Porfiriato — _La primera etapa del porfiriato empieza en 1877 y termina en el inicio de tercer periodo presidencia..._ | [ ] |
| 2 | 0.6150 | Historia de México — _El ascenso de Porfirio Díaz al poder en 1876 empezó un periodo conocido como el Porfiriato, mismo qu..._ | [ ] |
| 3 | 0.5923 | Porfiriato — _# Porfiriato El porfiriato o porfirismo​ fue un período de la historia de México en el que el gobier..._ | [ ] |
| 4 | 0.5495 | Historia de México — _El periodo formativo sería el equivalente a la protohistoria. Este periodo es comprendido entre el 1..._ | [ ] |
| 5 | 0.5345 | Historia de México — _En abril mientras el empresario ferrocarrilero Weetman Pearson trabajaba en el Istmo de Tehuantepec,..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El Porfiriato comenzó el 28 de noviembre de 1876 y duró hasta el 27 de mayo de 1911. | [ ] |
| 2 | Fuentes:
* Fragmento 3: Porfiriato
* Fragmento 2: Historia de México | [ ] |

---

## F4 — ¿Qué civilización construyó Teotihuacán?

**Tipo:** factual
**Puntos clave esperados:** Cultura teotihuacana; nombre propio desconocido; periodo clásico
**Tiempos:** retrieval=0.018s · generación=6.220s · total=6.238s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus. Los fragmentos indican que Teotihuacán fue motivo de interés para los toltecas y los mexicas, pero no mencionan quién construyó la ciudad.

Fuentes:
* Cultura teotihuacana (Fragmento 1)
* Cultura teotihuacana (Fragmento 2)
* Cultura teotihuacana (Fragmento 3)
* Cultura teotihuacana (Fragmento 4)
* Cultura teotihuacana (Fragmento 5)

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.8132 | Cultura teotihuacana — _C.​ Primeros asentamientos en la región de Teotihuacán (antes del 300 a. C.)..._ | [ ] |
| 2 | 0.8077 | Cultura teotihuacana — _La historia de Teotihuacán se puede entender como parte de un largo proceso civilizatorio que comenz..._ | [ ] |
| 3 | 0.7983 | Cultura teotihuacana — _Teotihuacán fue ya motivo de interés para las sociedades posteriores al declive de la cultura teotih..._ | [ ] |
| 4 | 0.7876 | Cultura teotihuacana — _Hay poca información sobre el proceso que llevó a la fundación de Teotihuacán. A partir del Preclási..._ | [ ] |
| 5 | 0.7808 | Cultura teotihuacana — _Sin embargo, Teotihuacán habría influenciado mucho al área mesoamericana. Todas las civilizaciones a..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |
| 2 | Los fragmentos indican que Teotihuacán fue motivo de interés para los toltecas y los mexicas, pero no mencionan quién construyó la ciudad. | [ ] |
| 3 | Fuentes:
* Cultura teotihuacana (Fragmento 1)
* Cultura teotihuacana (Fragmento 2)
* Cultura teotihuacana (Fragmento 3)
* Cultura teotihuacana (Fragmento 4)
* Cultura teotihuacana (Fragmento 5) | [ ] |

---

## F5 — ¿Quién fue el último emperador azteca?

**Tipo:** factual
**Puntos clave esperados:** Cuauhtémoc; sobrino de Moctezuma II; capturado 1521
**Tiempos:** retrieval=0.016s · generación=4.862s · total=4.879s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

Fuentes usadas:
* Fragmento 1: Hernán Cortés
* Fragmento 2: Imperio azteca
* Fragmento 3: Imperio azteca
* Fragmento 4: Hernán Cortés
* Fragmento 5: Cultura teotihuacana

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.7134 | Hernán Cortés — _# Hernán Cortés Hernán Cortés de Monroy y Pizarro Altamirano, primer marqués del Valle de Oaxaca (Me..._ | [ ] |
| 2 | 0.6911 | Imperio azteca — _A partir de entonces, los territorios del Imperio azteca se fueron ampliando hasta llegar a ocupar e..._ | [ ] |
| 3 | 0.6569 | Imperio azteca — _# Imperio azteca El Imperio mexica o Triple Alianza (del náhuatl: Exkan Tlahtoloyan​ o Ēxcān Tlahtōl..._ | [ ] |
| 4 | 0.6489 | Hernán Cortés — _El fin de ciclo era inevitable y llegaría con el retorno de Quetzalcóatl un año como aquel desde don..._ | [ ] |
| 5 | 0.6483 | Cultura teotihuacana — _En enero de 378, en tiempos en que Búho Lanzadardos gobernaba en Teotihuacán, el guerrero teotihuaca..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |
| 2 | Fuentes usadas:
* Fragmento 1: Hernán Cortés
* Fragmento 2: Imperio azteca
* Fragmento 3: Imperio azteca
* Fragmento 4: Hernán Cortés
* Fragmento 5: Cultura teotihuacana | [ ] |

---

## C1 — ¿Cuáles fueron las causas de la Revolución Mexicana?

**Tipo:** causalidad
**Puntos clave esperados:** Reelección de Díaz; desigualdad agraria; Plan de San Luis; crisis de 1907; Madero
**Tiempos:** retrieval=0.023s · generación=4.636s · total=4.659s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Los antecedentes de la Revolución Mexicana se remontan a la situación de México bajo la dictadura conocida como el porfiriato. Porfirio Díaz Mori ejerció el poder en el país de manera dictatorial desde 1876 hasta 1911.

Fuentes: Fragmento 1

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.8326 | Revolución mexicana — _# Revolución mexicana La Revolución mexicana fue un conflicto armado en México que se inició el 20 d..._ | [ ] |
| 2 | 0.7998 | Revolución mexicana — _La Revolución mexicana conllevó varios cambios sociales. En primer lugar, los dirigentes porfiristas..._ | [ ] |
| 3 | 0.7572 | Historia de México — _Y gracias al impulso nacionalista que habían dado los emperadores por el interés del pasado mexicano..._ | [ ] |
| 4 | 0.7486 | Independencia de México — _El movimiento de la independencia de México tiene como marco la Ilustración y las revoluciones liber..._ | [ ] |
| 5 | 0.7486 | Guerra de Independencia de México — _El movimiento de la independencia de México tiene como marco la Ilustración y las revoluciones liber..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Los antecedentes de la Revolución Mexicana se remontan a la situación de México bajo la dictadura conocida como el porfiriato. | [ ] |
| 2 | Porfirio Díaz Mori ejerció el poder en el país de manera dictatorial desde 1876 hasta 1911. | [ ] |
| 3 | Fuentes: Fragmento 1 | [ ] |

---

## C2 — ¿Por qué cayó el Imperio Azteca?

**Tipo:** causalidad
**Puntos clave esperados:** Alianzas con tlaxcaltecas; enfermedades; superioridad militar española; muerte de Moctezuma
**Tiempos:** retrieval=0.021s · generación=5.151s · total=5.172s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> El fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españoles —en alianza con los tlaxcaltecas y totonacas, entre otros pueblos indígenas— derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco.

Fuentes:
* Fragmento 1 | Fuente: Imperio azteca

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.7354 | Imperio azteca — _A partir de entonces, los territorios del Imperio azteca se fueron ampliando hasta llegar a ocupar e..._ | [ ] |
| 2 | 0.6686 | Virreinato de Nueva España — _La conquista de Yucatán fue la más tardía de las que finalmente integraron el virreinato de la Nueva..._ | [ ] |
| 3 | 0.6680 | Hernán Cortés — _Estos regalos, en lugar de disuadir a Cortés, le animaron a continuar y conquistar México.​ Los azte..._ | [ ] |
| 4 | 0.6663 | Imperio azteca — _# Imperio azteca El Imperio mexica o Triple Alianza (del náhuatl: Exkan Tlahtoloyan​ o Ēxcān Tlahtōl..._ | [ ] |
| 5 | 0.6410 | Virreinato de Nueva España — _Las estrategias indígenas con la ayuda de los tlatelolcas lograron echar de la ciudad a los conquist..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españoles —en alianza con los tlaxcaltecas y totonacas, entre otros pueblos indígenas— derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco. | [ ] |
| 2 | Fuentes:
* Fragmento 1 | Fuente: Imperio azteca | [ ] |

---

## C3 — ¿Qué provocó la Guerra de Reforma?

**Tipo:** causalidad
**Puntos clave esperados:** Constitución de 1857; liberales vs conservadores; Ley Juárez; Ley Lerdo
**Tiempos:** retrieval=0.018s · generación=5.024s · total=5.042s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> La Guerra de Reforma, también conocida como la guerra de los tres años, fue provocada por la promulgación de la Constitución de 1857 y en especial de las llamadas Leyes de Reforma. El país estaba dividido en dos grandes grupos: liberales (a favor de las Leyes de Reforma) y los conservadores (en contra).

Fuentes: Fragmento 1.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.7463 | Guerra de Reforma — _# Guerra de Reforma La Guerra de Reforma, también conocida como la guerra de los tres años, fue una..._ | [ ] |
| 2 | 0.6383 | Civilización maya — _debido a una proliferación de la guerra...._ | [ ] |
| 3 | 0.6012 | Historia de México — _Quizá aquel tiempo marcó el inicio del desgaste del régimen. Mientras se inauguraban obras y recinto..._ | [ ] |
| 4 | 0.5959 | Historia de México — _Si en la guerra de Reforma había surgido para que la Iglesia dejara de meterse en asuntos del Estado..._ | [ ] |
| 5 | 0.5803 | Revolución mexicana — _Tras el triunfo de la revolución constitucionalista en agosto de 1914 y el posterior exilio de Victo..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | La Guerra de Reforma, también conocida como la guerra de los tres años, fue provocada por la promulgación de la Constitución de 1857 y en especial de las llamadas Leyes de Reforma. | [ ] |
| 2 | El país estaba dividido en dos grandes grupos: liberales (a favor de las Leyes de Reforma) y los conservadores (en contra). | [ ] |
| 3 | Fuentes: Fragmento 1. | [ ] |

---

## C4 — ¿Por qué terminó el Porfiriato?

**Tipo:** causalidad
**Puntos clave esperados:** Revolución Mexicana; renuncia de Díaz en 1911; Plan de San Luis; descontento social
**Tiempos:** retrieval=0.018s · generación=4.133s · total=4.151s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> El Porfiriato terminó el 27 de mayo de 1911 con el exilio de Porfirio Díaz.

Fuentes:
* Fragmento 5 | Fuente: Historia de México

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.5558 | Porfiriato — _La primera etapa del porfiriato empieza en 1877 y termina en el inicio de tercer periodo presidencia..._ | [ ] |
| 2 | 0.5515 | Historia de México — _Don Porfirio es militar de carrera y político de trayectoria, lidió con el país casi 30 años. Las nu..._ | [ ] |
| 3 | 0.5512 | Porfiriato — _# Porfiriato El porfiriato o porfirismo​ fue un período de la historia de México en el que el gobier..._ | [ ] |
| 4 | 0.5289 | Moctezuma II — _Los datos ofrecidos en el Códice Florentino sobre esta leyenda fueron escritos décadas después de la..._ | [ ] |
| 5 | 0.5257 | Historia de México — _El ascenso de Porfirio Díaz al poder en 1876 empezó un periodo conocido como el Porfiriato, mismo qu..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El Porfiriato terminó el 27 de mayo de 1911 con el exilio de Porfirio Díaz. | [ ] |
| 2 | Fuentes:
* Fragmento 5 | Fuente: Historia de México | [ ] |

---

## V1 — ¿En qué se diferencian los mayas y los olmecas?

**Tipo:** comparativa
**Puntos clave esperados:** Olmecas: civilización madre, cabezas colosales, zona costera; Mayas: escritura, calendario, ciudades-estado
**Tiempos:** retrieval=0.020s · generación=4.790s · total=4.810s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

Fuentes usadas:
* Fragmento 1: Civilización maya
* Fragmento 2: Civilización maya
* Fragmento 3: Cultura teotihuacana
* Fragmento 4: Civilización maya
* Fragmento 5: Civilización maya

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.6418 | Civilización maya — _El territorio de los mayas​ y los mayas mantuvieron una relación dinámica con las culturas vecinas,..._ | [ ] |
| 2 | 0.6090 | Civilización maya — _sido la lengua de prestigio de la élite maya del Clásico, utilizado en la comunicación entre las ent..._ | [ ] |
| 3 | 0.6035 | Cultura teotihuacana — _C.) y más tarde.​ Asimismo, los autores señalan que existe una estrecha relación entre reglas comune..._ | [ ] |
| 4 | 0.5899 | Civilización maya — _El mundo maya estaba poblado por una gran variedad de deidades, entidades sobrenaturales y poderes s..._ | [ ] |
| 5 | 0.5779 | Civilización maya — _# Cultura maya La cultura maya fue una civilización mesoamericana que se desarrolló en lo que actual..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |
| 2 | Fuentes usadas:
* Fragmento 1: Civilización maya
* Fragmento 2: Civilización maya
* Fragmento 3: Cultura teotihuacana
* Fragmento 4: Civilización maya
* Fragmento 5: Civilización maya | [ ] |

---

## V2 — ¿Qué diferencias hay entre Zapata y Villa?

**Tipo:** comparativa
**Puntos clave esperados:** Zapata: agrarismo, sur, Plan de Ayala; Villa: norte, División del Norte, carácter militar
**Tiempos:** retrieval=0.018s · generación=5.825s · total=5.843s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Villa aceptó el Plan de Ayala, a excepción de sus acusaciones a Francisco I. Madero, quien había sido su redentor, y se obligó a dar armas a Zapata. Zapata insistió en que la devolución de tierras fuese constitucional. Tras las discrepancias que Carranza había tenido con Villa, firmaron el Pacto de Torreón, donde Villa presentaba disculpas a Carranza.

Fuentes: Fragmento 1, Fragmento 2, Fragmento 5.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.6032 | Emiliano Zapata — _Alcanzó así fama nacional el movimiento zapatista como la otra cara de la moneda entre los campesino..._ | [ ] |
| 2 | 0.5638 | Pancho Villa — _Tuvo entonces lugar el Pacto de Xochimilco, en el que Pancho Villa aceptó el Plan de Ayala en lo rel..._ | [ ] |
| 3 | 0.5593 | Pancho Villa — _un bandido que cometió crímenes haciéndose pasar por villista. Es sabido que Pancho Villa y Emiliano..._ | [ ] |
| 4 | 0.5527 | Revolución mexicana — _Cuando Viva Villa Es La Muerte (del año 1960), con Pedro Armendariz en el papel de Pancho Villa. Viv..._ | [ ] |
| 5 | 0.5506 | Historia de México — _Tras las discrepancias que Carranza había tenido con Villa, el 8 de julio firmaron el Pacto de Torre..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Villa aceptó el Plan de Ayala, a excepción de sus acusaciones a Francisco I. | [ ] |
| 2 | Madero, quien había sido su redentor, y se obligó a dar armas a Zapata. | [ ] |
| 3 | Zapata insistió en que la devolución de tierras fuese constitucional. | [ ] |
| 4 | Tras las discrepancias que Carranza había tenido con Villa, firmaron el Pacto de Torreón, donde Villa presentaba disculpas a Carranza. | [ ] |
| 5 | Fuentes: Fragmento 1, Fragmento 2, Fragmento 5. | [ ] |

---

## V3 — ¿En qué se parecen el Virreinato y el Imperio Azteca?

**Tipo:** comparativa
**Puntos clave esperados:** Control centralizado; tributo; dominio territorial; jerarquía religiosa ligada al poder
**Tiempos:** retrieval=0.023s · generación=4.956s · total=4.979s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

Fuentes usadas:
* Fragmento 1: Imperio azteca
* Fragmento 2: Virreinato de Nueva España
* Fragmento 3: Imperio azteca
* Fragmento 4: Imperio azteca
* Fragmento 5: Imperio azteca

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.7202 | Imperio azteca — _# Imperio azteca El Imperio mexica o Triple Alianza (del náhuatl: Exkan Tlahtoloyan​ o Ēxcān Tlahtōl..._ | [ ] |
| 2 | 0.6782 | Virreinato de Nueva España — _Filipinas y Oceanía.​​ Situación de los pueblos prehispánicos Cuando los españoles llegaron al Nuevo..._ | [ ] |
| 3 | 0.6610 | Imperio azteca — _A partir de entonces, los territorios del Imperio azteca se fueron ampliando hasta llegar a ocupar e..._ | [ ] |
| 4 | 0.6380 | Imperio azteca — _Smith, Michael E.; Berdan, Frances F. (2021). Everyday Life in the Aztec World (en inglés). Cambridg..._ | [ ] |
| 5 | 0.6251 | Imperio azteca — _Originalmente, el imperio azteca era una alianza suelta entre tres ciudades: Tenochtitlan, Texcoco y..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |
| 2 | Fuentes usadas:
* Fragmento 1: Imperio azteca
* Fragmento 2: Virreinato de Nueva España
* Fragmento 3: Imperio azteca
* Fragmento 4: Imperio azteca
* Fragmento 5: Imperio azteca | [ ] |

---

## R1 — ¿Qué relación tuvo Juárez con la Guerra de Reforma?

**Tipo:** relacional
**Puntos clave esperados:** Juárez lideró el bando liberal; promulgó las Leyes de Reforma; fue presidente durante el conflicto
**Tiempos:** retrieval=0.019s · generación=5.518s · total=5.538s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Juárez fue una figura clave tanto en la Guerra de Reforma como en la segunda intervención francesa, a pesar de no tener antecedentes militares. Fue el círculo cercano a Juárez quien le hizo ver que la guerra ya no era por defensa de las leyes liberales o la reforma, sino por soberanía nacional.

Fuentes:
* Fragmento 1: Benito Juárez
* Fragmento 2: Historia de México

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.7746 | Benito Juárez — _Benito Juárez vivió una época crucial en la formación del Estado mexicano, considerada por muchos hi..._ | [ ] |
| 2 | 0.7139 | Historia de México — _Con la idea de poner fin a los levantamientos, Maximiliano decretó amnistía a quienes se unieran a s..._ | [ ] |
| 3 | 0.7138 | Historia de México — _Pero la estrategia jugó en su contra. Si bien la idea era introducir gobernantes de pensamiento libe..._ | [ ] |
| 4 | 0.7000 | Historia de México — _Rompiendo las líneas defensivas en Veracruz y luego Córdoba, Zaragoza se apresuba a preparar un ejér..._ | [ ] |
| 5 | 0.6986 | Benito Juárez — _Luego de pasar por el paseo de la Reforma, Juárez y su comitiva se dirigen hacia el Palacio de Miner..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Juárez fue una figura clave tanto en la Guerra de Reforma como en la segunda intervención francesa, a pesar de no tener antecedentes militares. | [ ] |
| 2 | Fue el círculo cercano a Juárez quien le hizo ver que la guerra ya no era por defensa de las leyes liberales o la reforma, sino por soberanía nacional. | [ ] |
| 3 | Fuentes:
* Fragmento 1: Benito Juárez
* Fragmento 2: Historia de México | [ ] |

---

## R2 — ¿Cómo se relacionan Hernán Cortés y Moctezuma II?

**Tipo:** relacional
**Puntos clave esperados:** Encuentro en Tenochtitlan en 1519; Moctezuma tomado como rehén; su muerte; destrucción del imperio
**Tiempos:** retrieval=0.020s · generación=6.020s · total=6.040s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Hernán Cortés y Moctezuma II intercambiaron regalos cuando se conocieron y los españoles fueron alojados en el Palacio de Axayácatl. Cortés reportó que Moctezuma le había ofrecido todas sus tierras al rey de España, aunque algunos historiadores cuestionan esto. Cortés también envió mensajes a Moctezuma a través de calpixques.

Fuentes: Fragmento 1, Fragmento 2, Fragmento 3, Fragmento 5.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.7540 | Moctezuma II — _Según se describió en la segunda carta de relación de Hernán Cortés al emperador Carlos V: ​..._ | [ ] |
| 2 | 0.6652 | Hernán Cortés — _Hernán Cortés: Página de relación Historia de los restos de Cortés Portal dedicado a Hernán Cortés e..._ | [ ] |
| 3 | 0.6570 | Moctezuma II — _Cortés y Moctezuma intercambiaron regalos cuando se conocieron y los españoles fueron alojados en el..._ | [ ] |
| 4 | 0.6452 | Moctezuma II — _La ortografía Moctezuma es la más frecuente y moderna; no obstante, Hernán Cortés transcribió su nom..._ | [ ] |
| 5 | 0.6376 | Hernán Cortés — _Cortés encargó que dos de los calpixques fuesen a su presencia, se mostró ajeno a lo ocurrido y les..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Hernán Cortés y Moctezuma II intercambiaron regalos cuando se conocieron y los españoles fueron alojados en el Palacio de Axayácatl. | [ ] |
| 2 | Cortés reportó que Moctezuma le había ofrecido todas sus tierras al rey de España, aunque algunos historiadores cuestionan esto. | [ ] |
| 3 | Cortés también envió mensajes a Moctezuma a través de calpixques. | [ ] |
| 4 | Fuentes: Fragmento 1, Fragmento 2, Fragmento 3, Fragmento 5. | [ ] |

---

## R3 — ¿Qué papel jugó el Virreinato en la Independencia?

**Tipo:** relacional
**Puntos clave esperados:** Agravios acumulados; criollos excluidos del poder; influencia ilustrada; debilitamiento de España
**Tiempos:** retrieval=0.020s · generación=4.452s · total=4.472s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

Fuentes usadas:
* Independencia de México
* Guerra de Independencia de México
* Independencia de México
* Guerra de Independencia de México
* Historia de México

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.6324 | Independencia de México — _Este fue un punto de discordia con López Rayón quien manifestó no estar de acuerdo con el primer pun..._ | [ ] |
| 2 | 0.6324 | Guerra de Independencia de México — _Este fue un punto de discordia con López Rayón quien manifestó no estar de acuerdo con el primer pun..._ | [ ] |
| 3 | 0.6303 | Independencia de México — _Durante esta época, el movimiento independentista no solo realizó acciones bélicas, sino que se dotó..._ | [ ] |
| 4 | 0.6303 | Guerra de Independencia de México — _Durante esta época, el movimiento independentista no solo realizó acciones bélicas, sino que se dotó..._ | [ ] |
| 5 | 0.6275 | Historia de México — _Así, tras 10 días de intenso debate y acuerdos entre ambos, el 24 de febero de 1821 proclaman el Pla..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |
| 2 | Fuentes usadas:
* Independencia de México
* Guerra de Independencia de México
* Independencia de México
* Guerra de Independencia de México
* Historia de México | [ ] |

---

## M1 — ¿Qué civilizaciones existían antes de los españoles y cuál dominaba en 1519?

**Tipo:** multihop
**Puntos clave esperados:** Olmecas; mayas; teotihuacanos; aztecas; el Imperio Azteca dominaba en 1519
**Tiempos:** retrieval=0.023s · generación=4.676s · total=4.699s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Antes de la llegada de los españoles, existían civilizaciones como el imperio teocrático de los incas, la confederación de los mexicas y la cultura maya. El imperio teocrático de los incas estaba en su apogeo en 1519.

Fuentes: Fragmento 2.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.7850 | Historia de México — _El periodo prehispánico se refiere a todo lo acontecido antes de la llegada de los españoles en 1519..._ | [ ] |
| 2 | 0.7140 | Virreinato de Nueva España — _Filipinas y Oceanía.​​ Situación de los pueblos prehispánicos Cuando los españoles llegaron al Nuevo..._ | [ ] |
| 3 | 0.6832 | Virreinato de Nueva España — _Los dominicos fueron la otra orden importante que se estableció en el virreinato, con poco tiempo de..._ | [ ] |
| 4 | 0.6803 | Virreinato de Nueva España — _En la literatura virreinal novohispana es posible distinguir varios periodos. En el primero, la lite..._ | [ ] |
| 5 | 0.6716 | Historia de México — _A partir de la institución del Virreinato, entre 1521 y 1535 en distintas zonas de México, empezaría..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Antes de la llegada de los españoles, existían civilizaciones como el imperio teocrático de los incas, la confederación de los mexicas y la cultura maya. | [ ] |
| 2 | El imperio teocrático de los incas estaba en su apogeo en 1519. | [ ] |
| 3 | Fuentes: Fragmento 2. | [ ] |

---

## M2 — ¿Cómo influyeron las reformas de Juárez en la Revolución décadas después?

**Tipo:** multihop
**Puntos clave esperados:** Constitución de 1857; separación Iglesia-Estado; antecedente liberal que Díaz traicionó
**Tiempos:** retrieval=0.020s · generación=3.797s · total=3.816s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

Fuentes usadas:
* Historia de México
* Benito Juárez
* Guerra de Independencia de México

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.7401 | Historia de México — _Fue paradójico que quien mayor impulso dio al poder liberal, fuese la corona de Maximiliano, y eso l..._ | [ ] |
| 2 | 0.7386 | Benito Juárez — _Benito Juárez vivió una época crucial en la formación del Estado mexicano, considerada por muchos hi..._ | [ ] |
| 3 | 0.7015 | Historia de México — _El día 11 de enero de 1861, Benito Juárez hizo su entrada triunfal en la capital mexicana celebrada..._ | [ ] |
| 4 | 0.6979 | Historia de México — _Temiendo que el Congreso tuviese más poder como había ocurrido toda la primera mitad del siglo XIX,..._ | [ ] |
| 5 | 0.6945 | Guerra de Independencia de México — _Este grupo estaba concentrado en los consulados de México y Guadalajara, que constituyeron la pieza..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |
| 2 | Fuentes usadas:
* Historia de México
* Benito Juárez
* Guerra de Independencia de México | [ ] |

---

## T1 — ¿Quién es el presidente actual de México?

**Tipo:** trampa  (pregunta trampa)
**Tiempos:** retrieval=0.018s · generación=4.865s · total=4.883s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> La actual presidenta de México es Claudia Sheinbaum, quien ganó las elecciones presidenciales de 2024 y asumió el cargo el 1 de octubre de 2024, convirtiéndose en la primera mujer en dirigir el país en la historia de México.

Fuentes: Fragmento 2.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.7447 | Historia de México — _antes del México moderno, definido por la llegada de caudillos militares como jefes de Gobierno. El..._ | [ ] |
| 2 | 0.7208 | Historia de México — _Claudia Sheinbaum, sucesora política del presidente López Obrador, ganó las elecciones presidenciale..._ | [ ] |
| 3 | 0.6884 | Historia de México — _El 2 de julio de 2000 se llevaron a cabo las elecciones presidenciales; México vivió por primera vez..._ | [ ] |
| 4 | 0.6876 | Historia de México — _Así, el 2 de septiembre de 1932, Pascual Ortiz Rubio se presentó ante el congreso diciendo: Salgo co..._ | [ ] |
| 5 | 0.6749 | Benito Juárez — _# Benito Juárez Benito Pablo Juárez García (San Pablo Guelatao, Intendencia de Oaxaca; 21 de marzo d..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | La actual presidenta de México es Claudia Sheinbaum, quien ganó las elecciones presidenciales de 2024 y asumió el cargo el 1 de octubre de 2024, convirtiéndose en la primera mujer en dirigir el país en la historia de México. | [ ] |
| 2 | Fuentes: Fragmento 2. | [ ] |

---

## T2 — ¿Cuál es el PIB actual de México?

**Tipo:** trampa  (pregunta trampa)
**Tiempos:** retrieval=0.020s · generación=3.896s · total=3.916s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

Fuentes usadas:
* Historia de México
* Porfiriato
* Revolución mexicana
* Independencia de México

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.6469 | Historia de México — _antes del México moderno, definido por la llegada de caudillos militares como jefes de Gobierno. El..._ | [ ] |
| 2 | 0.6258 | Porfiriato — _Así, la administración de los recursos nacionales se hacía con participación pública y privada. El B..._ | [ ] |
| 3 | 0.6256 | Revolución mexicana — _Durante estos 35 años, México experimentó un notable crecimiento económico y tuvo estabilidad políti..._ | [ ] |
| 4 | 0.6115 | Historia de México — _la burguesía mexicana, tasada en ese momento en 40 000 millones de dólares, no obstante dicha cifra..._ | [ ] |
| 5 | 0.5970 | Independencia de México — _La pérdida de esta posesión tuvo una importancia decisiva para la economía del Imperio español, ya q..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |
| 2 | Fuentes usadas:
* Historia de México
* Porfiriato
* Revolución mexicana
* Independencia de México | [ ] |

---

## T3 — ¿Qué equipos jugaron la final del fútbol mexicano en 2024?

**Tipo:** trampa  (pregunta trampa)
**Tiempos:** retrieval=0.021s · generación=4.049s · total=4.069s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

Fuentes:
* Historia de México
* Independencia de México
* Guerra de Independencia de México
* Revolución mexicana

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.6401 | Historia de México — _antes del México moderno, definido por la llegada de caudillos militares como jefes de Gobierno. El..._ | [ ] |
| 2 | 0.6061 | Independencia de México — _Ese mismo año, la República mexicana se integró por diecinueve estados (Yucatán argumentaría más tar..._ | [ ] |
| 3 | 0.6061 | Guerra de Independencia de México — _Ese mismo año, la República mexicana se integró por diecinueve estados (Yucatán argumentaría más tar..._ | [ ] |
| 4 | 0.5681 | Historia de México — _Así, mientras el resto del mundo se ocupaba en librar la Gran Guerra que estaba por marcar el fin de..._ | [ ] |
| 5 | 0.5663 | Revolución mexicana — _Las fuentes disponibles no concuerdan en cuanto al fin de la Revolución mexicana. Algunas fuentes lo..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |
| 2 | Fuentes:
* Historia de México
* Independencia de México
* Guerra de Independencia de México
* Revolución mexicana | [ ] |

---
