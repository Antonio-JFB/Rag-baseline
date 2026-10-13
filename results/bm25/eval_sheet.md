# Hoja de evaluación manual

Protocolo: para cada pregunta, (1) marca qué chunks recuperados son genuinamente relevantes para responderla -- usa los **puntos clave esperados** como referencia, no tu propio conocimiento de historia; (2) marca qué afirmaciones de la respuesta están respaldadas por el texto de los chunks recuperados (Faithfulness) -- si una afirmación es correcta históricamente pero no aparece en los chunks, cuenta como **no respaldada**, porque el sistema no la pudo haber sacado del contexto. Para preguntas trampa, la respuesta correcta es que el sistema declare que no encontró la información -- marca eso como relevante/respaldado si ocurre así. Al terminar cada pregunta, marca la casilla **Anotada** (así `metrics.py` sabe cuáles ya revisaste y no confunde una pregunta pendiente con una donde todo resultó irrelevante).

Total de preguntas: 20

---

## F1 — ¿En qué año cayó Tenochtitlan?

**Tipo:** factual
**Puntos clave esperados:** 1521; Cuauhtémoc; tlaxcaltecas
**Tiempos:** retrieval=0.003s · generación=76.328s · total=76.331s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> El 13 de agosto de 1521, correspondiente al día "1 coatl" del año "3 calli" del mes Xocotlhuetzi, Cuauhtémoc salió de Tenochtitlan en una canoa. Al final del sitio, que duró tres meses, Pedro de Alvarado tomó la plaza de Tlatelolco.

Fuentes:
* Fragmento 3: Conquista de México
* Fragmento 4: Historia de México

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 12.3673 | Moctezuma II — _cabello largo, muy llano, sentado con mucha mesura».​ Actualmente la mayoría de investigadores opina..._ | [ ] |
| 2 | 11.0866 | Hernán Cortés — _a la salida de Tenochtitlán. Ya no les faltaba mucho para completar la retirada cuando fueron descub..._ | [ ] |
| 3 | 10.9279 | Conquista de México — _leales a los mexicas provenía de los malinalcas, matlatzincas y cohuixcas. Cortés envió fuerzas a ca..._ | [ ] |
| 4 | 10.7487 | Historia de México — _es muy utilizada ya que suele ser complicado determinar los respectivos períodos en México sin recur..._ | [ ] |
| 5 | 9.8362 | Moctezuma II — _eventos más importantes que llevarían a la colonización del resto del continente americano por nacio..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El 13 de agosto de 1521, correspondiente al día "1 coatl" del año "3 calli" del mes Xocotlhuetzi, Cuauhtémoc salió de Tenochtitlan en una canoa. | [ ] |
| 2 | Al final del sitio, que duró tres meses, Pedro de Alvarado tomó la plaza de Tlatelolco. | [ ] |
| 3 | Fuentes:
* Fragmento 3: Conquista de México
* Fragmento 4: Historia de México | [ ] |

---

## F2 — ¿Quién dio el Grito de Independencia?

**Tipo:** factual
**Puntos clave esperados:** Miguel Hidalgo; Dolores Hidalgo; 16 septiembre 1810
**Tiempos:** retrieval=0.004s · generación=5.219s · total=5.223s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Según los fragmentos proporcionados, Miguel Hidalgo dio el Grito de Independencia.

Fuentes:
* Fragmento 1
* Fragmento 3
* Fragmento 4
* Fragmento 5

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 14.6425 | Virreinato de Nueva España — _sublevó y proclamó a Fernando de Borbón, como rey de España. Napoleón a través de las abdicaciones d..._ | [ ] |
| 2 | 14.1124 | Benito Juárez — _la República y en contra del imperialismo francés. Abraham Lincoln, presidente estadounidense en ese..._ | [ ] |
| 3 | 13.6065 | Guerra de Independencia de México — _se adhirieron al nuevo plan. El 19 de marzo de 1823, el efímero imperio terminó con la abdicación a..._ | [ ] |
| 4 | 13.6065 | Independencia de México — _se adhirieron al nuevo plan. El 19 de marzo de 1823, el efímero imperio terminó con la abdicación a..._ | [ ] |
| 5 | 13.0446 | Independencia de México — _de México: legado y pasado reciente. México: Pearson. ISBN 978-970-26-0523-2. Florescano, Enrique (2..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Según los fragmentos proporcionados, Miguel Hidalgo dio el Grito de Independencia. | [ ] |
| 2 | Fuentes:
* Fragmento 1
* Fragmento 3
* Fragmento 4
* Fragmento 5 | [ ] |

---

## F3 — ¿Cuándo comenzó el Porfiriato?

**Tipo:** factual
**Puntos clave esperados:** 1876; Porfirio Díaz; reelección continua
**Tiempos:** retrieval=0.003s · generación=4.612s · total=4.615s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> El Porfiriato comenzó el 28 de noviembre de 1876.

Fuentes:
* Fragmento 5: Porfiriato

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 11.4375 | Revolución mexicana — _las diferencias entre las facciones que habían luchado contra Huerta, lo que desencadenó nuevos conf..._ | [ ] |
| 2 | 11.4225 | Porfiriato — _fuese por medio de sobornos o bien por torturas y desapariciones. Las represiones que Díaz ejercía s..._ | [ ] |
| 3 | 10.9125 | Revolución mexicana — _# Revolución mexicana La Revolución mexicana fue un conflicto armado en México que se inició el 20 d..._ | [ ] |
| 4 | 9.7498 | Porfiriato — _porfiriato Entrevista Díaz - Creelman Crisis del Porfiriato Revolución Mexicana Revolución de la Nor..._ | [ ] |
| 5 | 9.4779 | Porfiriato — _# Porfiriato El porfiriato o porfirismo​ fue un período de la historia de México en el que el gobier..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El Porfiriato comenzó el 28 de noviembre de 1876. | [ ] |
| 2 | Fuentes:
* Fragmento 5: Porfiriato | [ ] |

---

## F4 — ¿Qué civilización construyó Teotihuacán?

**Tipo:** factual
**Puntos clave esperados:** Cultura teotihuacana; nombre propio desconocido; periodo clásico
**Tiempos:** retrieval=0.004s · generación=4.129s · total=4.133s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 9.3916 | Cultura teotihuacana — _de arqueólogos donde se estableció que la Tollan mitológica fue Tollan-Xicocotitlan,​ y es compartid..._ | [ ] |
| 2 | 9.2150 | Cultura teotihuacana — _Nacional de Antropología e Historia enviaron un vehículo robot, llamado Tlaloque I y diseñado por el..._ | [ ] |
| 3 | 9.1922 | Cultura olmeca — _# Cultura olmeca La cultura olmeca fue una civilización que se desarrolló durante el periodo preclás..._ | [ ] |
| 4 | 8.9924 | Cultura teotihuacana — _Diccionario del náhuatl en el español de México, C. Montemayor menciona que proviene de los vocablos..._ | [ ] |
| 5 | 8.2633 | Civilización maya — _Mesoamérica carecía de animales de tiro, no utilizaba la rueda, y poseía pocos animales domésticos;..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---

## F5 — ¿Quién fue el último emperador azteca?

**Tipo:** factual
**Puntos clave esperados:** Cuauhtémoc; sobrino de Moctezuma II; capturado 1521
**Tiempos:** retrieval=0.004s · generación=4.634s · total=4.638s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Cuauhtémoc fue el último emperador azteca.

Fuentes:
* Fragmento 4

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 14.0979 | Hernán Cortés — _Zúñiga. Cortés mandó grabar una cruz en una ceiba de la ciudad y ordenó construir un altar a la Virg..._ | [ ] |
| 2 | 13.8620 | Virreinato de Nueva España — _con el cacique o gobernador maya Tabscoob y escuchó acerca de una ciudad poderosa, capital del imper..._ | [ ] |
| 3 | 13.0222 | Imperio azteca — _# Imperio azteca El Imperio mexica o Triple Alianza (del náhuatl: Exkan Tlahtoloyan​ o Ēxcān Tlahtōl..._ | [ ] |
| 4 | 12.4926 | Virreinato de Nueva España — _quienes en lugar de obedecer a su monarca, comenzaron a apedrearlo. El emperador murió pocos días de..._ | [ ] |
| 5 | 12.1676 | Historia de México — _de Tenochtitlán, Chimalpopoca, permaneció en silencio, lo que propició un descontento entre los mexi..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Cuauhtémoc fue el último emperador azteca. | [ ] |
| 2 | Fuentes:
* Fragmento 4 | [ ] |

---

## C1 — ¿Cuáles fueron las causas de la Revolución Mexicana?

**Tipo:** causalidad
**Puntos clave esperados:** Reelección de Díaz; desigualdad agraria; Plan de San Luis; crisis de 1907; Madero
**Tiempos:** retrieval=0.006s · generación=6.120s · total=6.126s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Según los fragmentos proporcionados, una de las causas de la Revolución Mexicana fue que Porfirio Díaz, quien había asumido la presidencia en 1876 y mantenido una dictadura para 1910, había perdido el poder político, aunque mantuvo poderío económico. Además, las diferencias entre las facciones que habían luchado contra Huerta desencadenaron nuevos conflictos.

Fuentes:
* Fragmento 1
* Fragmento 5

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 18.0360 | Revolución mexicana — _federal, como en las diferentes tropas revolucionarias como las de Villa, Zapata y Carranza.​ Oficia..._ | [ ] |
| 2 | 17.0212 | Revolución mexicana — _a 1.9 millones. Mientras, en un estudio estadounidense, Andrew Collver haría variar la estadística d..._ | [ ] |
| 3 | 16.5865 | Revolución mexicana — _encuentra en la ciudad de Torreón, Coahuila. Fue inaugurado en octubre de 2007 y se centra en la vid..._ | [ ] |
| 4 | 16.5042 | Conquista de México — _motivo principal de la controversia que surgió como resultado de la insurrección de Hernan Cortés. D..._ | [ ] |
| 5 | 16.3752 | Revolución mexicana — _las diferencias entre las facciones que habían luchado contra Huerta, lo que desencadenó nuevos conf..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Según los fragmentos proporcionados, una de las causas de la Revolución Mexicana fue que Porfirio Díaz, quien había asumido la presidencia en 1876 y mantenido una dictadura para 1910, había perdido el poder político, aunque mantuvo poderío económico. | [ ] |
| 2 | Además, las diferencias entre las facciones que habían luchado contra Huerta desencadenaron nuevos conflictos. | [ ] |
| 3 | Fuentes:
* Fragmento 1
* Fragmento 5 | [ ] |

---

## C2 — ¿Por qué cayó el Imperio Azteca?

**Tipo:** causalidad
**Puntos clave esperados:** Alianzas con tlaxcaltecas; enfermedades; superioridad militar española; muerte de Moctezuma
**Tiempos:** retrieval=0.005s · generación=6.059s · total=6.064s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> El Imperio azteca cayó el 13 de agosto de 1521, cuando los españoles —en alianza con los tlaxcaltecas y totonacas, entre otros pueblos indígenas— derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco.

Fuentes:
*   Fragmento 1: Imperio azteca
*   Fragmento 4: Virreinato de Nueva España

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 16.8865 | Imperio azteca — _# Imperio azteca El Imperio mexica o Triple Alianza (del náhuatl: Exkan Tlahtoloyan​ o Ēxcān Tlahtōl..._ | [ ] |
| 2 | 16.1682 | Historia de México — _de Tenochtitlán, Chimalpopoca, permaneció en silencio, lo que propició un descontento entre los mexi..._ | [ ] |
| 3 | 14.8396 | Historia de México — _del Lago de Texcoco que pretendía dividir el lago de agua salada para introducir agua dulce a la isl..._ | [ ] |
| 4 | 14.5261 | Virreinato de Nueva España — _con el cacique o gobernador maya Tabscoob y escuchó acerca de una ciudad poderosa, capital del imper..._ | [ ] |
| 5 | 13.8409 | Imperio azteca — _los reinos fragmentados de los mayas. En este campamento los antiguos comerciantes mexicas viajaban..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El Imperio azteca cayó el 13 de agosto de 1521, cuando los españoles —en alianza con los tlaxcaltecas y totonacas, entre otros pueblos indígenas— derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco. | [ ] |
| 2 | Fuentes:
*   Fragmento 1: Imperio azteca
*   Fragmento 4: Virreinato de Nueva España | [ ] |

---

## C3 — ¿Qué provocó la Guerra de Reforma?

**Tipo:** causalidad
**Puntos clave esperados:** Constitución de 1857; liberales vs conservadores; Ley Juárez; Ley Lerdo
**Tiempos:** retrieval=0.004s · generación=6.275s · total=6.280s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> La Guerra de Reforma, también conocida como la guerra de los tres años, fue provocada por la promulgación de la Constitución de 1857 y en especial de las llamadas Leyes de Reforma. El país estaba dividido en dos grandes grupos: liberales (a favor de las Leyes de Reforma) y los conservadores (en contra).

Fuentes: Fragmento 3

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 15.0663 | Benito Juárez — _y Pepito, pero hay quienes solamente piensan en bienes materiales. ¡Vea estos precios! ¡Hasta 4 vece..._ | [ ] |
| 2 | 14.9784 | Benito Juárez — _gobierno conservador,​como consecuencia de la guerra de reforma, el puerto de Veracruz fue invadido..._ | [ ] |
| 3 | 14.2995 | Guerra de Reforma — _# Guerra de Reforma La Guerra de Reforma, también conocida como la guerra de los tres años, fue una..._ | [ ] |
| 4 | 14.2690 | Historia de México — _no eran, ni acumulados en una reserva estratégica para el Banco de México, ni para la diversificació..._ | [ ] |
| 5 | 13.1997 | Benito Juárez — _"Virginia" y trasladarse junto con un gran arsenal al Puerto de Veracruz para buscar un golpe de Est..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | La Guerra de Reforma, también conocida como la guerra de los tres años, fue provocada por la promulgación de la Constitución de 1857 y en especial de las llamadas Leyes de Reforma. | [ ] |
| 2 | El país estaba dividido en dos grandes grupos: liberales (a favor de las Leyes de Reforma) y los conservadores (en contra). | [ ] |
| 3 | Fuentes: Fragmento 3 | [ ] |

---

## C4 — ¿Por qué terminó el Porfiriato?

**Tipo:** causalidad
**Puntos clave esperados:** Revolución Mexicana; renuncia de Díaz en 1911; Plan de San Luis; descontento social
**Tiempos:** retrieval=0.003s · generación=5.651s · total=5.654s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Cuando Porfirio Díaz aseguró en una entrevista que se retiraría al finalizar su mandato sin buscar la reelección, la situación política comenzó a agitarse. La oposición al Gobierno cobró relevancia ante la postura manifestada por Díaz. Díaz lanzó una nueva candidatura a la presidencia y Madero fue arrestado en San Luis Potosí por sedición.

Fuentes: Fragmento 1

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 13.6024 | Revolución mexicana — _# Revolución mexicana La Revolución mexicana fue un conflicto armado en México que se inició el 20 d..._ | [ ] |
| 2 | 13.5173 | Porfiriato — _fuese por medio de sobornos o bien por torturas y desapariciones. Las represiones que Díaz ejercía s..._ | [ ] |
| 3 | 13.1969 | Benito Juárez — _y Pepito, pero hay quienes solamente piensan en bienes materiales. ¡Vea estos precios! ¡Hasta 4 vece..._ | [ ] |
| 4 | 12.5537 | Historia de México — _instituciones de salubridad. Pero el principal detalle era que para lograrlo, no bastaban 4 años de..._ | [ ] |
| 5 | 12.0421 | Pancho Villa — _matarlo. Doroteo Arango (ahora bajo el nombre de Francisco Villa) acabó con la vida de su rival y lo..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Cuando Porfirio Díaz aseguró en una entrevista que se retiraría al finalizar su mandato sin buscar la reelección, la situación política comenzó a agitarse. | [ ] |
| 2 | La oposición al Gobierno cobró relevancia ante la postura manifestada por Díaz. | [ ] |
| 3 | Díaz lanzó una nueva candidatura a la presidencia y Madero fue arrestado en San Luis Potosí por sedición. | [ ] |
| 4 | Fuentes: Fragmento 1 | [ ] |

---

## V1 — ¿En qué se diferencian los mayas y los olmecas?

**Tipo:** comparativa
**Puntos clave esperados:** Olmecas: civilización madre, cabezas colosales, zona costera; Mayas: escritura, calendario, ciudades-estado
**Tiempos:** retrieval=0.004s · generación=8.014s · total=8.018s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Los mayas y los olmecas mantuvieron una relación dinámica y mantuvieron vínculos estrechos, como se evidencia en murales en Cacaxtla pintados en estilo maya y en la ciudad maya de Chichén Itzá y la capital tolteca de Tollan. Mesoamérica carecía de animales de tiro, no utilizaba la rueda, y poseía pocos animales domésticos; el principal medio de transporte era a pie o en canoa. Los mayas vieron el mundo como hostil y regido por deidades impredecibles.

Fuentes:
* Fragmento 3: Historia de México
* Fragmento 5: Civilización maya

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 28.1347 | Cultura olmeca — _Guatemala (Takalik Abaj), Belice, El Salvador, Honduras y Nicaragua. Economía La economía de los olm..._ | [ ] |
| 2 | 25.6426 | Cultura olmeca — _# Cultura olmeca La cultura olmeca fue una civilización que se desarrolló durante el periodo preclás..._ | [ ] |
| 3 | 24.4135 | Historia de México — _n. e.). Se considera que alrededor del año 1200 a. n. e. los olmecas crearon La Venta. Esta ciudad d..._ | [ ] |
| 4 | 23.0699 | Cultura olmeca — _descubierto en 1939 por Eulalia Guzmán.​ Es el más conocido porque fue el que sobrevivió hasta una é..._ | [ ] |
| 5 | 22.7352 | Civilización maya — _Mesoamérica carecía de animales de tiro, no utilizaba la rueda, y poseía pocos animales domésticos;..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Los mayas y los olmecas mantuvieron una relación dinámica y mantuvieron vínculos estrechos, como se evidencia en murales en Cacaxtla pintados en estilo maya y en la ciudad maya de Chichén Itzá y la capital tolteca de Tollan. | [ ] |
| 2 | Mesoamérica carecía de animales de tiro, no utilizaba la rueda, y poseía pocos animales domésticos; el principal medio de transporte era a pie o en canoa. | [ ] |
| 3 | Los mayas vieron el mundo como hostil y regido por deidades impredecibles. | [ ] |
| 4 | Fuentes:
* Fragmento 3: Historia de México
* Fragmento 5: Civilización maya | [ ] |

---

## V2 — ¿Qué diferencias hay entre Zapata y Villa?

**Tipo:** comparativa
**Puntos clave esperados:** Zapata: agrarismo, sur, Plan de Ayala; Villa: norte, División del Norte, carácter militar
**Tiempos:** retrieval=0.003s · generación=4.336s · total=4.341s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 15.7960 | Revolución mexicana — _las diferencias entre las facciones que habían luchado contra Huerta, lo que desencadenó nuevos conf..._ | [ ] |
| 2 | 15.2795 | Emiliano Zapata — _y algunos lugares de Guerrero. Poco después tomó Cuernavaca y para junio ocupó Cuajimalpa, Xochimilc..._ | [ ] |
| 3 | 14.3300 | Revolución mexicana — _fue arrestado en San Luis Potosí por sedición. Durante su estancia en la cárcel se llevaron a cabo l..._ | [ ] |
| 4 | 13.9600 | Emiliano Zapata — _traicionado la revolución. El gobierno federal reiteró su decisión de imponer el orden por la violen..._ | [ ] |
| 5 | 13.6576 | Benito Juárez — _y Pepito, pero hay quienes solamente piensan en bienes materiales. ¡Vea estos precios! ¡Hasta 4 vece..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---

## V3 — ¿En qué se parecen el Virreinato y el Imperio Azteca?

**Tipo:** comparativa
**Puntos clave esperados:** Control centralizado; tributo; dominio territorial; jerarquía religiosa ligada al poder
**Tiempos:** retrieval=0.007s · generación=4.510s · total=4.518s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 26.5953 | Imperio azteca — _# Imperio azteca El Imperio mexica o Triple Alianza (del náhuatl: Exkan Tlahtoloyan​ o Ēxcān Tlahtōl..._ | [ ] |
| 2 | 24.8574 | Historia de México — _de Tenochtitlán, Chimalpopoca, permaneció en silencio, lo que propició un descontento entre los mexi..._ | [ ] |
| 3 | 23.6682 | Imperio azteca — _Guerrero y el Soconusco. El fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españ..._ | [ ] |
| 4 | 23.4209 | Imperio azteca — _los reinos fragmentados de los mayas. En este campamento los antiguos comerciantes mexicas viajaban..._ | [ ] |
| 5 | 23.3804 | Historia de México — _del Lago de Texcoco que pretendía dividir el lago de agua salada para introducir agua dulce a la isl..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---

## R1 — ¿Qué relación tuvo Juárez con la Guerra de Reforma?

**Tipo:** relacional
**Puntos clave esperados:** Juárez lideró el bando liberal; promulgó las Leyes de Reforma; fue presidente durante el conflicto
**Tiempos:** retrieval=0.006s · generación=7.648s · total=7.654s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Benito Juárez fue una figura central en la Guerra de Reforma, que ocurrió entre 1857 y 1861. La guerra fue una consecuencia de la promulgación de la Constitución de 1857 y las Leyes de Reforma, y dividió al país en liberales (a favor de las Leyes de Reforma) y conservadores (en contra). Los liberales, liderados por Juárez, finalmente derrotaron a los conservadores, y Juárez instaló su administración en Ciudad de México.

Fuentes: Fragmento 2, Fragmento 3, Fragmento 5.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 20.8266 | Historia de México — _Mori fue capturado en Juchitán de Zaragoza (Oaxaca) cuando intentaba huir hacia Panamá; ahí mismo fu..._ | [ ] |
| 2 | 20.5725 | Benito Juárez — _quien finalmente levantó el sitio sobre el puerto, el 30 de marzo de 1859.​ El 6 de abril recibió al..._ | [ ] |
| 3 | 20.3752 | Benito Juárez — _quien decide que un cañonero estadounidense que estaba cerca del puerto de Veracruz bombardease el b..._ | [ ] |
| 4 | 19.9611 | Benito Juárez — _"Virginia" y trasladarse junto con un gran arsenal al Puerto de Veracruz para buscar un golpe de Est..._ | [ ] |
| 5 | 19.6994 | Guerra de Reforma — _# Guerra de Reforma La Guerra de Reforma, también conocida como la guerra de los tres años, fue una..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Benito Juárez fue una figura central en la Guerra de Reforma, que ocurrió entre 1857 y 1861. | [ ] |
| 2 | La guerra fue una consecuencia de la promulgación de la Constitución de 1857 y las Leyes de Reforma, y dividió al país en liberales (a favor de las Leyes de Reforma) y conservadores (en contra). | [ ] |
| 3 | Los liberales, liderados por Juárez, finalmente derrotaron a los conservadores, y Juárez instaló su administración en Ciudad de México. | [ ] |
| 4 | Fuentes: Fragmento 2, Fragmento 3, Fragmento 5. | [ ] |

---

## R2 — ¿Cómo se relacionan Hernán Cortés y Moctezuma II?

**Tipo:** relacional
**Puntos clave esperados:** Encuentro en Tenochtitlan en 1519; Moctezuma tomado como rehén; su muerte; destrucción del imperio
**Tiempos:** retrieval=0.007s · generación=7.600s · total=7.607s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Hernán Cortés y Moctezuma II se relacionaron porque Cortés y su ejército fueron hospedados por Moctezuma II en el templo de su antecesor Axayácatl en Tenochtitlán. Moctezuma II creyó que los españoles eran enviados del dios Quetzalcóatl y los obsequió con regalos, incluyendo el Tocado del Dios Quetzalcóatl. Posteriormente, Moctezuma fue hecho prisionero por Cortés en su propio palacio en noviembre de 1519.

Fuentes: Fragmento 3, Fragmento 4.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 19.2886 | Moctezuma II — _el cuerpo de Itzquauhtzin fue llevado en una canoa a Tlatelolco.​ Durante la huida de los españoles,..._ | [ ] |
| 2 | 18.1326 | Moctezuma II — _más exclusivos. Uno de sus hijos fue Jerónimo Girón y Moctezuma. Este hombre fue III marqués de las..._ | [ ] |
| 3 | 17.8108 | Hernán Cortés — _otro lado, avistó por primera vez el lago de Texcoco aproximándose a ella por el rumbo de Xochimilco..._ | [ ] |
| 4 | 17.1820 | Moctezuma II — _# Moctezuma Xocoyotzin Moctezuma Xocoyotzin (en náhuatl clásico: Motēcuzōmah Xōcoyōtzin;​ AFI [moteː..._ | [ ] |
| 5 | 17.0408 | Moctezuma II — _Una breve batalla sucedió después en la que Xóchitl fue capturado y posteriormente ejecutado pública..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Hernán Cortés y Moctezuma II se relacionaron porque Cortés y su ejército fueron hospedados por Moctezuma II en el templo de su antecesor Axayácatl en Tenochtitlán. | [ ] |
| 2 | Moctezuma II creyó que los españoles eran enviados del dios Quetzalcóatl y los obsequió con regalos, incluyendo el Tocado del Dios Quetzalcóatl. | [ ] |
| 3 | Posteriormente, Moctezuma fue hecho prisionero por Cortés en su propio palacio en noviembre de 1519. | [ ] |
| 4 | Fuentes: Fragmento 3, Fragmento 4. | [ ] |

---

## R3 — ¿Qué papel jugó el Virreinato en la Independencia?

**Tipo:** relacional
**Puntos clave esperados:** Agravios acumulados; criollos excluidos del poder; influencia ilustrada; debilitamiento de España
**Tiempos:** retrieval=0.005s · generación=4.142s · total=4.147s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 21.9497 | Virreinato de Nueva España — _I), Juan de Tecto y Juan de Aora, pertenecientes a la alta sociedad castellana. Aora y Tecto fueron..._ | [ ] |
| 2 | 19.1400 | Virreinato de Nueva España — _la primera actividad lingüística del Nuevo Mundo.​ A finales del siglo, el intelectual nahua Antonio..._ | [ ] |
| 3 | 18.6458 | Civilización maya — _internos.​ El panorama político maya era muy complejo, y las élites mayas se sirvieron de intriga po..._ | [ ] |
| 4 | 18.5825 | Virreinato de Nueva España — _aliciente para el contrabando. Veracruz era el puerto donde se realizaba el comercio con España, y l..._ | [ ] |
| 5 | 17.4988 | Virreinato de Nueva España — _el primer virreinato erigido, y por lo tanto, donde se puso en práctica el modelo español de goberna..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---

## M1 — ¿Qué civilizaciones existían antes de los españoles y cuál dominaba en 1519?

**Tipo:** multihop
**Puntos clave esperados:** Olmecas; mayas; teotihuacanos; aztecas; el Imperio Azteca dominaba en 1519
**Tiempos:** retrieval=0.006s · generación=5.283s · total=5.289s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Según el contexto proporcionado, antes de la llegada de los españoles existían el imperio teocrático de los incas, la confederación de los mexicas y la cultura maya. En 1519, los mexicas dominaban.

Fuentes:
* Fragmento 3
* Fragmento 4
* Fragmento 5

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 25.4849 | Historia de México — _# Historia de México La historia de México es la narración cronológica y demostrable de los aconteci..._ | [ ] |
| 2 | 24.1826 | Moctezuma II — _eventos más importantes que llevarían a la colonización del resto del continente americano por nacio..._ | [ ] |
| 3 | 24.0433 | Virreinato de Nueva España — _En el caso de las Islas Filipinas, predominaban lenguas indígenas como el tagalo y el cebuano, que j..._ | [ ] |
| 4 | 22.7927 | Hernán Cortés — _con los otros tres.​ Tras esto, un pueblo vecino, por instigación de los aztecas, se dispuso a ataca..._ | [ ] |
| 5 | 21.9762 | Conquista de México — _el hedor era insoportable. Organizaron un banquete con vino, carne de cerdo, carne de pavo y tortill..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Según el contexto proporcionado, antes de la llegada de los españoles existían el imperio teocrático de los incas, la confederación de los mexicas y la cultura maya. | [ ] |
| 2 | En 1519, los mexicas dominaban. | [ ] |
| 3 | Fuentes:
* Fragmento 3
* Fragmento 4
* Fragmento 5 | [ ] |

---

## M2 — ¿Cómo influyeron las reformas de Juárez en la Revolución décadas después?

**Tipo:** multihop
**Puntos clave esperados:** Constitución de 1857; separación Iglesia-Estado; antecedente liberal que Díaz traicionó
**Tiempos:** retrieval=0.004s · generación=4.071s · total=4.076s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 22.3380 | Independencia de México — _la agricultura. Por ejemplo, la creciente importancia de Guadalajara y El Bajío se debía a su relaci..._ | [ ] |
| 2 | 22.3380 | Guerra de Independencia de México — _la agricultura. Por ejemplo, la creciente importancia de Guadalajara y El Bajío se debía a su relaci..._ | [ ] |
| 3 | 21.6954 | Guerra de Reforma — _punto de vista, atacaba a la religión católica, que era la creencia de la mayoría del país, además d..._ | [ ] |
| 4 | 21.3385 | Imperio azteca — _masa o cera para engañar a vendedores. La calidad y tipo del cacao era tomada en cuenta; el «buen tr..._ | [ ] |
| 5 | 21.2930 | Historia de México — _movimientos de las tropas francesas para el funcionamiento del imperio.​ Maximiliano solicitó revisa..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---

## T1 — ¿Quién es el presidente actual de México?

**Tipo:** trampa  (pregunta trampa)
**Tiempos:** retrieval=0.004s · generación=4.160s · total=4.165s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 16.2886 | Historia de México — _comunistas decidieron volvar su apoyo a Vasconcelos que ya consolidaba el gusto universitario y el c..._ | [ ] |
| 2 | 15.3470 | Conquista de México — _siglo XVII un grupo de tlaxcaltecas fue llevado para pacificar a los nativos de la región así como p..._ | [ ] |
| 3 | 14.9132 | Conquista de México — _del río Usumacinta y fundó la villa de San Pedro Tanoche. Cuando «el Mozo» se enteró de este evento..._ | [ ] |
| 4 | 14.8003 | Conquista de México — _Carlos I de España también nombró a Nuño de Guzmán como gobernador de la provincia de Pánuco y como..._ | [ ] |
| 5 | 14.6491 | Imperio azteca — _consideraba representante de los dioses.​ Otros altos funcionarios eran: El Cihuacóatl del Imperio M..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---

## T2 — ¿Cuál es el PIB actual de México?

**Tipo:** trampa  (pregunta trampa)
**Tiempos:** retrieval=0.008s · generación=4.520s · total=4.529s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 17.8849 | Cultura teotihuacana — _Mimosa biuncifera. A estos tipos de vegetación se suman los pastizales, la vegetación hidrófila esta..._ | [ ] |
| 2 | 16.6111 | Cultura teotihuacana — _cuál ha sido el impacto de la actividad humana sobre los suelos de Teotihuacán. Rivera Uria et al. a..._ | [ ] |
| 3 | 15.3470 | Conquista de México — _siglo XVII un grupo de tlaxcaltecas fue llevado para pacificar a los nativos de la región así como p..._ | [ ] |
| 4 | 15.1297 | Historia de México — _Presidente de México desde el 1 de diciembre de 2018 hasta el 30 de septiembre de 2024. Durante su g..._ | [ ] |
| 5 | 15.0667 | Cultura teotihuacana — _la ciudad se dispersó por diversas localidades en la cuenca de México. Se desconoce cuál era la iden..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---

## T3 — ¿Qué equipos jugaron la final del fútbol mexicano en 2024?

**Tipo:** trampa  (pregunta trampa)
**Tiempos:** retrieval=0.008s · generación=4.307s · total=4.315s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 19.8305 | Historia de México — _como estrategia de prevención y contención. La falta de capacidad en los sistemas de salud para aten..._ | [ ] |
| 2 | 18.2531 | Historia de México — _que los países de Latinoamérica se comprometían a no fabricar, poseer o utilizar armas nucleares. El..._ | [ ] |
| 3 | 17.5745 | Historia de México — _del presidente Manuel de la Peña y Peña, intentó huir para mantener estabilidad desde oro sitio, per..._ | [ ] |
| 4 | 17.3102 | Historia de México — _volcán Popocatépetl y el sureste del estado presentó los mayores daños; Jojutla fue una de las local..._ | [ ] |
| 5 | 15.4567 | Cultura olmeca — _# Cultura olmeca La cultura olmeca fue una civilización que se desarrolló durante el periodo preclás..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---
