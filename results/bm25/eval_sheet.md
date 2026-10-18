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
**Tiempos:** retrieval=0.003s · generación=76.328s · total=76.331s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> El 13 de agosto de 1521, correspondiente al día "1 coatl" del año "3 calli" del mes Xocotlhuetzi, Cuauhtémoc salió de Tenochtitlan en una canoa. Al final del sitio, que duró tres meses, Pedro de Alvarado tomó la plaza de Tlatelolco.
>
> Fuentes:
> * Fragmento 3: Conquista de México
> * Fragmento 4: Historia de México

_Ayuda para Recall: 105 chunks distintos del corpus mencionan al menos un punto clave (24 mencionan 2 o más); detalle con `python evaluation/candidates.py --question F1`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 12.3673 | Moctezuma II — _cabello largo, muy llano, sentado con mucha mesura». Actualmente la mayoría de investigadores opinan que Ce Ácatl Topiltzin fue un personaje histórico que habrá vivido en Tollan-Xicocotitlan o en Teotihuacán, aunque es tomado por hecho que la historia contada por las fuentes de los siglos XVI y XVII..._ | ninguno | [ ] |
| 2 | 11.0866 | Hernán Cortés — _a la salida de Tenochtitlán. Ya no les faltaba mucho para completar la retirada cuando fueron descubiertos por una anciana, que dio la alarma, y en unos momentos, miles de guerreros mexicas atacaron en tromba a los españoles; les acosaron a lo largo de la calzada, mientras otros atacaban desde sus c..._ | tlaxcaltecas | [ ] |
| 3 | 10.9279 | Conquista de México — _leales a los mexicas provenía de los malinalcas, matlatzincas y cohuixcas. Cortés envió fuerzas a cargo de Andrés de Tapia y Gonzalo de Sandoval para detener su avance. Los conquistadores españoles pensaron que los mexicas estaban totalmente debilitados y realizaron una incursión general a la ciudad..._ | 1521, Cuauhtémoc | [ ] |
| 4 | 10.7487 | Historia de México — _es muy utilizada ya que suele ser complicado determinar los respectivos períodos en México sin recurrir a explicaciones eurocentristas. Periodización La periodización es la división del tiempo histórico en períodos. El objetivo de una periodización comúnmente es darle orden a la narración de los hec..._ | ninguno | [ ] |
| 5 | 9.8362 | Moctezuma II — _eventos más importantes que llevarían a la colonización del resto del continente americano por naciones europeas. Antecedentes La primera vez que Moctezuma oyó de la llegada de extranjeros nunca antes vistos, de piel blanca y grandes barbas desde las playas del este, sucedió en el año 13 Tochtli del..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El 13 de agosto de 1521, correspondiente al día "1 coatl" del año "3 calli" del mes Xocotlhuetzi, Cuauhtémoc salió de Tenochtitlan en una canoa. | [ ] |
| 2 | Al final del sitio, que duró tres meses, Pedro de Alvarado tomó la plaza de Tlatelolco. | [ ] |

---

## F2 — ¿Quién dio el Grito de Independencia?

**Tipo:** factual
**Puntos clave esperados:** Miguel Hidalgo; Dolores Hidalgo; 16 septiembre 1810
**Tiempos:** retrieval=0.004s · generación=5.219s · total=5.223s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Según los fragmentos proporcionados, Miguel Hidalgo dio el Grito de Independencia.
>
> Fuentes:
> * Fragmento 1
> * Fragmento 3
> * Fragmento 4
> * Fragmento 5

_Ayuda para Recall: 53 chunks distintos del corpus mencionan al menos un punto clave (22 mencionan 2 o más); detalle con `python evaluation/candidates.py --question F2`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 14.6425 | Virreinato de Nueva España — _sublevó y proclamó a Fernando de Borbón, como rey de España. Napoleón a través de las abdicaciones de Bayona entregó la corona de España a su hermano José Bonaparte y dio inicio a la guerra de la Independencia Española. Sin los fondos enviados desde América, los gobiernos de España habrían colapsado..._ | Miguel Hidalgo, Dolores Hidalgo | [ ] |
| 2 | 14.1124 | Benito Juárez — _la República y en contra del imperialismo francés. Abraham Lincoln, presidente estadounidense en ese entonces, tenía grandes problemas en medio de la guerra de Secesión, que se entablaba entre el Norte y el Sur del país. Matías Romero consiguió que el secretario de Estado estadounidense pidiera a su..._ | ninguno | [ ] |
| 3 | 13.6065 | Guerra de Independencia de México — _se adhirieron al nuevo plan. El 19 de marzo de 1823, el efímero imperio terminó con la abdicación a la corona y el exilio de Iturbide. Se estableció un triunvirato conformado por Guadalupe Victoria, Nicolás Bravo y Pedro Celestino Negrete, cuyos suplentes fueron José Mariano de Michelena, Miguel Dom..._ | ninguno | [ ] |
| 4 | 13.6065 | Independencia de México **(copia exacta del rank 3: cuenta una sola vez)** — _se adhirieron al nuevo plan. El 19 de marzo de 1823, el efímero imperio terminó con la abdicación a la corona y el exilio de Iturbide. Se estableció un triunvirato conformado por Guadalupe Victoria, Nicolás Bravo y Pedro Celestino Negrete, cuyos suplentes fueron José Mariano de Michelena, Miguel Dom..._ | ninguno | [ ] |
| 5 | 13.0446 | Independencia de México — _de México: legado y pasado reciente. México: Pearson. ISBN 978-970-26-0523-2. Florescano, Enrique (2002). Memoria mexicana. México: Fondo de Cultura Económica. ISBN 978-968-16-6526-5. Consultado el 25 de abril de 2010. González, Luis (1973). «Siglo de las Luces». Historia mínima de México. Daniel Co..._ | Miguel Hidalgo, Dolores Hidalgo | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Según los fragmentos proporcionados, Miguel Hidalgo dio el Grito de Independencia. | [ ] |

---

## F3 — ¿Cuándo comenzó el Porfiriato?

**Tipo:** factual
**Puntos clave esperados:** 1876; Porfirio Díaz; reelección continua
**Tiempos:** retrieval=0.003s · generación=4.612s · total=4.615s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> El Porfiriato comenzó el 28 de noviembre de 1876.
>
> Fuentes:
> * Fragmento 5: Porfiriato

_Ayuda para Recall: 68 chunks distintos del corpus mencionan al menos un punto clave (12 mencionan 2 o más); detalle con `python evaluation/candidates.py --question F3`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 11.4375 | Revolución mexicana — _las diferencias entre las facciones que habían luchado contra Huerta, lo que desencadenó nuevos conflictos. Carranza, jefe de la Revolución, de acuerdo con el Plan de Guadalupe, convocó a todas las fuerzas a la Convención de Aguascalientes para nombrar un líder único. En esa reunión Eulalio Gutiérre..._ | 1876, Porfirio Díaz | [ ] |
| 2 | 11.4225 | Porfiriato — _fuese por medio de sobornos o bien por torturas y desapariciones. Las represiones que Díaz ejercía sobre las personas que exigían una mejor calidad de vida fueron justificadas con una doctrina filosófica: el Positivismo, la cual proponía "Orden y progreso". Así, el "Orden" lo mantenía con represione..._ | Porfirio Díaz | [ ] |
| 3 | 10.9125 | Revolución mexicana — _# Revolución mexicana La Revolución mexicana fue un conflicto armado en México que se inició el 20 de noviembre de 1910 y terminó el 5 de febrero de 1917. Los antecedentes del conflicto se remontan a la situación de México bajo la dictadura conocida como el porfiriato. Porfirio Díaz Mori ejerció el ..._ | 1876, Porfirio Díaz | [ ] |
| 4 | 9.7498 | Porfiriato — _porfiriato Entrevista Díaz - Creelman Crisis del Porfiriato Revolución Mexicana Revolución de la Noria Referencias Bibliografía Bazant, Jan: Breve historia de México México: Eds Coyoacán (2003) ISBN 970-633-057-7. Cosío Villegas, Daniel. Estados Unidos contra Julio Hernández Jalili Arriba el cultura..._ | 1876, Porfirio Díaz | [ ] |
| 5 | 9.4779 | Porfiriato — _# Porfiriato El porfiriato o porfirismo fue un período de la historia de México en el que el gobierno estuvo bajo el control (total o mayoritario) del militar, político y dictador Porfirio Díaz, entre el 28 de noviembre de 1876 y el 27 de mayo de 1911. En el porfiriato la política se aplicó de tal m..._ | 1876, Porfirio Díaz | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El Porfiriato comenzó el 28 de noviembre de 1876. | [ ] |

---

## F4 — ¿Qué civilización construyó Teotihuacán?

**Tipo:** factual
**Puntos clave esperados:** Cultura teotihuacana; nombre propio desconocido; periodo clásico
**Tiempos:** retrieval=0.004s · generación=4.129s · total=4.133s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

_Ayuda para Recall: 84 chunks distintos del corpus mencionan al menos un punto clave (2 mencionan 2 o más); detalle con `python evaluation/candidates.py --question F4`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 9.3916 | Cultura teotihuacana — _de arqueólogos donde se estableció que la Tollan mitológica fue Tollan-Xicocotitlan, y es compartida por Stuart, Uriarte, y Duverger. René Millon, uno de los más reconocidos especialistas en el tema de Teotihuacán, opina que efectivamente Teotihuacán es la legendaria Tollan, pero no acepta que este ..._ | nombre propio desconocido | [ ] |
| 2 | 9.2150 | Cultura teotihuacana — _Nacional de Antropología e Historia enviaron un vehículo robot, llamado Tlaloque I y diseñado por el Instituto Politécnico Nacional, para explorar un túnel estrecho, a 8 metros de profundidad y de aproximadamente 100 metros lineales de fondo, ubicado justo debajo del templo. Al hacer uso de un georr..._ | Cultura teotihuacana | [ ] |
| 3 | 9.1922 | Cultura olmeca — _# Cultura olmeca La cultura olmeca fue una civilización que se desarrolló durante el periodo preclásico de Mesoamérica, en parte de los territorios actuales de México. Aunque se han encontrado vestigios de su presencia en amplias zonas de Mesoamérica, se considera que el área cultural olmeca —zona m..._ | periodo clásico | [ ] |
| 4 | 8.9924 | Cultura teotihuacana — _Diccionario del náhuatl en el español de México, C. Montemayor menciona que proviene de los vocablos teō[tl] ‘Dios’, -ti (ligadura eufónica), -huah (posesivo) y -cān (locativo que indica el sitio donde se realiza una acción), de modo que lo traduce como «Lugar de los que tienen dioses». Hay que acla..._ | ninguno | [ ] |
| 5 | 8.2633 | Civilización maya — _Mesoamérica carecía de animales de tiro, no utilizaba la rueda, y poseía pocos animales domésticos; el principal medio de transporte era a pie o en canoa. Los mesoamericanos vieron el mundo como hostil y regido por deidades impredecibles. El juego ritual de pelota mesoamericano fue ampliamente pract..._ | periodo clásico | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

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
>
> Fuentes:
> * Fragmento 4

_Ayuda para Recall: 36 chunks distintos del corpus mencionan al menos un punto clave (3 mencionan 2 o más); detalle con `python evaluation/candidates.py --question F5`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 14.0979 | Hernán Cortés — _Zúñiga. Cortés mandó grabar una cruz en una ceiba de la ciudad y ordenó construir un altar a la Virgen María y poner una cruz de madera. El fraile Bartolomé de Omedo predicó a los nativos contra la idolatría. Cortés celebró el Domingo de Ramos, 17 de abril, con los jefes indígenas y les encargó que ..._ | ninguno | [ ] |
| 2 | 13.8620 | Virreinato de Nueva España — _con el cacique o gobernador maya Tabscoob y escuchó acerca de una ciudad poderosa, capital del imperio más grande de Mesoamérica, la Gran Tenochtitlan, culminando su viaje en Veracruz. En 1519, bajo la designación de Diego Velázquez de Cuéllar, gobernador de Cuba (llamada entonces Fernandina, en hon..._ | ninguno | [ ] |
| 3 | 13.0222 | Imperio azteca — _# Imperio azteca El Imperio mexica o Triple Alianza (del náhuatl: Exkan Tlahtoloyan o Ēxcān Tlahtōlōyān ‘Los tres lugares donde se dan órdenes’), llamado también Imperio azteca y —con más precisión— Imperio tenochca, fue un imperio organizado en una confederación compleja, multiétnica y flexible de ..._ | ninguno | [ ] |
| 4 | 12.4926 | Virreinato de Nueva España — _quienes en lugar de obedecer a su monarca, comenzaron a apedrearlo. El emperador murió pocos días después. Cuitláhuac, hermano de Moctezuma y señor de Iztapalapa fue elegido tlatoani de Tenochtitlan y en respuesta a la Matanza del Templo Mayor, decidió lanzar al pueblo contra los españoles el 30 de ..._ | Cuauhtémoc | [ ] |
| 5 | 12.1676 | Historia de México — _de Tenochtitlán, Chimalpopoca, permaneció en silencio, lo que propició un descontento entre los mexicas. Fue el sacerdote Tlacaelél quien, desde las sombras, convenció al sacerdote Izcóatl de realizar un golpe de Estado en Tenochtitlán, logrando imponerse como gobernante el 16 de octubre de 1427. Aq..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Cuauhtémoc fue el último emperador azteca. | [ ] |

---

## C1 — ¿Cuáles fueron las causas de la Revolución Mexicana?

**Tipo:** causalidad
**Puntos clave esperados:** Reelección de Díaz; desigualdad agraria; Plan de San Luis; crisis de 1907; Madero
**Tiempos:** retrieval=0.006s · generación=6.120s · total=6.126s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Según los fragmentos proporcionados, una de las causas de la Revolución Mexicana fue que Porfirio Díaz, quien había asumido la presidencia en 1876 y mantenido una dictadura para 1910, había perdido el poder político, aunque mantuvo poderío económico. Además, las diferencias entre las facciones que habían luchado contra Huerta desencadenaron nuevos conflictos.
>
> Fuentes:
> * Fragmento 1
> * Fragmento 5

_Ayuda para Recall: 124 chunks distintos del corpus mencionan al menos un punto clave (27 mencionan 2 o más); detalle con `python evaluation/candidates.py --question C1`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 18.0360 | Revolución mexicana — _federal, como en las diferentes tropas revolucionarias como las de Villa, Zapata y Carranza. Oficialmente las adelitas no tenían deberes militares, sino más bien domésticos: conseguir alimentos, cocinar y cargar bultos y armas, entre otras cosas, aunque hubo algunas que combatieron, incluso algunas ..._ | ninguno | [ ] |
| 2 | 17.0212 | Revolución mexicana — _a 1.9 millones. Mientras, en un estudio estadounidense, Andrew Collver haría variar la estadística de este dato entre 2.5 y 3.1 millones. Sin embargo, el análisis más reconocido es el de 1993, cuando Manuel Ordorica y José Luis Lezama realizaron un análisis demográfico de México, auspiciado por el C..._ | Plan de San Luis | [ ] |
| 3 | 16.5865 | Revolución mexicana — _encuentra en la ciudad de Torreón, Coahuila. Fue inaugurado en octubre de 2007 y se centra en la vida de Francisco Villa y Francisco I. Madero. Museo de la Revolución.- Este museo se encuentra también en el estado de Coahuila, en la ciudad de Saltillo, y se centra en la vida de Francisco I. Madero. ..._ | Madero | [ ] |
| 4 | 16.5042 | Conquista de México — _motivo principal de la controversia que surgió como resultado de la insurrección de Hernan Cortés. Diego de Velázquez firmó como adjunto del almirante y comandante en jefe Diego Colón y Moniz Perestrello, pues todavía no había recibido nombramiento por parte del rey de España. El gobernador de Cuba ..._ | ninguno | [ ] |
| 5 | 16.3752 | Revolución mexicana — _las diferencias entre las facciones que habían luchado contra Huerta, lo que desencadenó nuevos conflictos. Carranza, jefe de la Revolución, de acuerdo con el Plan de Guadalupe, convocó a todas las fuerzas a la Convención de Aguascalientes para nombrar un líder único. En esa reunión Eulalio Gutiérre..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Según los fragmentos proporcionados, una de las causas de la Revolución Mexicana fue que Porfirio Díaz, quien había asumido la presidencia en 1876 y mantenido una dictadura para 1910, había perdido el poder político, aunque mantuvo poderío económico. | [ ] |
| 2 | Además, las diferencias entre las facciones que habían luchado contra Huerta desencadenaron nuevos conflictos. | [ ] |

---

## C2 — ¿Por qué cayó el Imperio Azteca?

**Tipo:** causalidad
**Puntos clave esperados:** Alianzas con tlaxcaltecas; enfermedades; superioridad militar española; muerte de Moctezuma
**Tiempos:** retrieval=0.005s · generación=6.059s · total=6.064s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> El Imperio azteca cayó el 13 de agosto de 1521, cuando los españoles —en alianza con los tlaxcaltecas y totonacas, entre otros pueblos indígenas— derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco.
>
> Fuentes:
> *   Fragmento 1: Imperio azteca
> *   Fragmento 4: Virreinato de Nueva España

_Ayuda para Recall: 73 chunks distintos del corpus mencionan al menos un punto clave (1 mencionan 2 o más); detalle con `python evaluation/candidates.py --question C2`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 16.8865 | Imperio azteca — _# Imperio azteca El Imperio mexica o Triple Alianza (del náhuatl: Exkan Tlahtoloyan o Ēxcān Tlahtōlōyān ‘Los tres lugares donde se dan órdenes’), llamado también Imperio azteca y —con más precisión— Imperio tenochca, fue un imperio organizado en una confederación compleja, multiétnica y flexible de ..._ | superioridad militar española | [ ] |
| 2 | 16.1682 | Historia de México — _de Tenochtitlán, Chimalpopoca, permaneció en silencio, lo que propició un descontento entre los mexicas. Fue el sacerdote Tlacaelél quien, desde las sombras, convenció al sacerdote Izcóatl de realizar un golpe de Estado en Tenochtitlán, logrando imponerse como gobernante el 16 de octubre de 1427. Aq..._ | ninguno | [ ] |
| 3 | 14.8396 | Historia de México — _del Lago de Texcoco que pretendía dividir el lago de agua salada para introducir agua dulce a la isla por medio de su segunda obra, el Acueducto de Chapultepec, iniciado en 1449. A su muerte, Nezahualpilli recibió el trono de Texcoco y el Imperio Azteca le envió a Chalchiunenetzin como concubina par..._ | ninguno | [ ] |
| 4 | 14.5261 | Virreinato de Nueva España — _con el cacique o gobernador maya Tabscoob y escuchó acerca de una ciudad poderosa, capital del imperio más grande de Mesoamérica, la Gran Tenochtitlan, culminando su viaje en Veracruz. En 1519, bajo la designación de Diego Velázquez de Cuéllar, gobernador de Cuba (llamada entonces Fernandina, en hon..._ | ninguno | [ ] |
| 5 | 13.8409 | Imperio azteca — _los reinos fragmentados de los mayas. En este campamento los antiguos comerciantes mexicas viajaban para obtener algunas de las materias más valoradas, por la lejanía desde donde se traían y la dificultad. El campamento tenía solo una pequeña guarnición de soldados que eran para proteger a los mexic..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El Imperio azteca cayó el 13 de agosto de 1521, cuando los españoles —en alianza con los tlaxcaltecas y totonacas, entre otros pueblos indígenas— derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco. | [ ] |

---

## C3 — ¿Qué provocó la Guerra de Reforma?

**Tipo:** causalidad
**Puntos clave esperados:** Constitución de 1857; liberales vs conservadores; Ley Juárez; Ley Lerdo
**Tiempos:** retrieval=0.004s · generación=6.275s · total=6.280s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> La Guerra de Reforma, también conocida como la guerra de los tres años, fue provocada por la promulgación de la Constitución de 1857 y en especial de las llamadas Leyes de Reforma. El país estaba dividido en dos grandes grupos: liberales (a favor de las Leyes de Reforma) y los conservadores (en contra).
>
> Fuentes: Fragmento 3

_Ayuda para Recall: 143 chunks distintos del corpus mencionan al menos un punto clave (55 mencionan 2 o más); detalle con `python evaluation/candidates.py --question C3`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 15.0663 | Benito Juárez — _y Pepito, pero hay quienes solamente piensan en bienes materiales. ¡Vea estos precios! ¡Hasta 4 veces más caro está el cuarterón de maíz! y créame no se si por ser indio o por qué, pero no los entiendo, no entiendo a quienes se quieren enriquecer de la miseria, de las masas, del dolor y del sufrimie..._ | Ley Juárez | [ ] |
| 2 | 14.9784 | Benito Juárez — _gobierno conservador,como consecuencia de la guerra de reforma, el puerto de Veracruz fue invadido el 15 de diciembre de 1861 por una fuerza española de 6000 hombres que no encontró resistencia. El 9 de enero de 1862, se les unieron 3000 franceses y 800 ingleses. Los invasores ingleses y españoles s..._ | Ley Juárez | [ ] |
| 3 | 14.2995 | Guerra de Reforma — _# Guerra de Reforma La Guerra de Reforma, también conocida como la guerra de los tres años, fue una guerra civil que aconteció en México desde el 17 de diciembre de 1857 al 11 de enero de 1861, como consecuencia de la promulgación de la Constitución de 1857 y en especial de las llamadas Leyes de Ref..._ | Constitución de 1857, liberales vs conservadores, Ley Juárez | [ ] |
| 4 | 14.2690 | Historia de México — _no eran, ni acumulados en una reserva estratégica para el Banco de México, ni para la diversificación de las fuentes de ingresos, pero tampoco en un aumento sustancial del gasto social. La corrupción, presente en el sistema político desde tiempos del alemanismo en los años 1940, tuvo un auge signifi..._ | ninguno | [ ] |
| 5 | 13.1997 | Benito Juárez — _"Virginia" y trasladarse junto con un gran arsenal al Puerto de Veracruz para buscar un golpe de Estado con el apoyo de sus paisanos los veracruzanos. Sebastián Lerdo y Juárez veían que el ejército republicano tuviera todo para salir avante en su empresa. En eso llegó al Palacio Nacional provisional..._ | Ley Juárez, Ley Lerdo | [ ] |

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
**Tiempos:** retrieval=0.003s · generación=5.651s · total=5.654s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Cuando Porfirio Díaz aseguró en una entrevista que se retiraría al finalizar su mandato sin buscar la reelección, la situación política comenzó a agitarse. La oposición al Gobierno cobró relevancia ante la postura manifestada por Díaz. Díaz lanzó una nueva candidatura a la presidencia y Madero fue arrestado en San Luis Potosí por sedición.
>
> Fuentes: Fragmento 1

_Ayuda para Recall: 129 chunks distintos del corpus mencionan al menos un punto clave (22 mencionan 2 o más); detalle con `python evaluation/candidates.py --question C4`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 13.6024 | Revolución mexicana — _# Revolución mexicana La Revolución mexicana fue un conflicto armado en México que se inició el 20 de noviembre de 1910 y terminó el 5 de febrero de 1917. Los antecedentes del conflicto se remontan a la situación de México bajo la dictadura conocida como el porfiriato. Porfirio Díaz Mori ejerció el ..._ | Revolución Mexicana, renuncia de Díaz en 1911, descontento social | [ ] |
| 2 | 13.5173 | Porfiriato — _fuese por medio de sobornos o bien por torturas y desapariciones. Las represiones que Díaz ejercía sobre las personas que exigían una mejor calidad de vida fueron justificadas con una doctrina filosófica: el Positivismo, la cual proponía "Orden y progreso". Así, el "Orden" lo mantenía con represione..._ | Revolución Mexicana | [ ] |
| 3 | 13.1969 | Benito Juárez — _y Pepito, pero hay quienes solamente piensan en bienes materiales. ¡Vea estos precios! ¡Hasta 4 veces más caro está el cuarterón de maíz! y créame no se si por ser indio o por qué, pero no los entiendo, no entiendo a quienes se quieren enriquecer de la miseria, de las masas, del dolor y del sufrimie..._ | ninguno | [ ] |
| 4 | 12.5537 | Historia de México — _instituciones de salubridad. Pero el principal detalle era que para lograrlo, no bastaban 4 años de presidencia, sino al menos 6. A partir de ese momento y por orden de Calles, Rodríguez dedicaría su presidencia a nivelar el camino para la llegada del siguiente presidente que ahora tendría 6 años en..._ | ninguno | [ ] |
| 5 | 12.0421 | Pancho Villa — _matarlo. Doroteo Arango (ahora bajo el nombre de Francisco Villa) acabó con la vida de su rival y los hombres de este, empezando a seguir una causa en defensa de la clase popular que era fuertemente explotada, al punto de comparación con la esclavitud. Otra cuenta que su verdadero padre en realidad ..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Cuando Porfirio Díaz aseguró en una entrevista que se retiraría al finalizar su mandato sin buscar la reelección, la situación política comenzó a agitarse. | [ ] |
| 2 | La oposición al Gobierno cobró relevancia ante la postura manifestada por Díaz. | [ ] |
| 3 | Díaz lanzó una nueva candidatura a la presidencia y Madero fue arrestado en San Luis Potosí por sedición. | [ ] |

---

## V1 — ¿En qué se diferencian los mayas y los olmecas?

**Tipo:** comparativa
**Puntos clave esperados:** Olmecas: civilización madre, cabezas colosales, zona costera; Mayas: escritura, calendario, ciudades-estado
**Tiempos:** retrieval=0.004s · generación=8.014s · total=8.018s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Los mayas y los olmecas mantuvieron una relación dinámica y mantuvieron vínculos estrechos, como se evidencia en murales en Cacaxtla pintados en estilo maya y en la ciudad maya de Chichén Itzá y la capital tolteca de Tollan. Mesoamérica carecía de animales de tiro, no utilizaba la rueda, y poseía pocos animales domésticos; el principal medio de transporte era a pie o en canoa. Los mayas vieron el mundo como hostil y regido por deidades impredecibles.
>
> Fuentes:
> * Fragmento 3: Historia de México
> * Fragmento 5: Civilización maya

_Ayuda para Recall: 192 chunks distintos del corpus mencionan al menos un punto clave (40 mencionan 2 o más); detalle con `python evaluation/candidates.py --question V1`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 28.1347 | Cultura olmeca — _Guatemala (Takalik Abaj), Belice, El Salvador, Honduras y Nicaragua. Economía La economía de los olmecas estaba basada principalmente en los productos agrícolas, con los que comerciaban tanto entre ellos como con otros pueblos vecinos, sobre todo con los pueblos nómadas, principalmente los olmecas r..._ | Olmecas | [ ] |
| 2 | 25.6426 | Cultura olmeca — _# Cultura olmeca La cultura olmeca fue una civilización que se desarrolló durante el periodo preclásico de Mesoamérica, en parte de los territorios actuales de México. Aunque se han encontrado vestigios de su presencia en amplias zonas de Mesoamérica, se considera que el área cultural olmeca —zona m..._ | Olmecas, civilización madre | [ ] |
| 3 | 24.4135 | Historia de México — _n. e.). Se considera que alrededor del año 1200 a. n. e. los olmecas crearon La Venta. Esta ciudad destaca por la construcción simétrica de sus edificios, dispuestos en un eje largo que va de norte a sur; con monumentos colocados a los lados destinados a asemejar las montañas y el paisaje. Este cent..._ | Olmecas, cabezas colosales, Mayas, escritura | [ ] |
| 4 | 23.0699 | Cultura olmeca — _descubierto en 1939 por Eulalia Guzmán. Es el más conocido porque fue el que sobrevivió hasta una época más cercana, pero la civilización olmeca que se desarrolló aquí fue una cultura ya en decadencia, no el esplendor que vivió en los centros ceremoniales anteriores. Estos centros ceremoniales tenía..._ | Olmecas, zona costera | [ ] |
| 5 | 22.7352 | Civilización maya — _Mesoamérica carecía de animales de tiro, no utilizaba la rueda, y poseía pocos animales domésticos; el principal medio de transporte era a pie o en canoa. Los mesoamericanos vieron el mundo como hostil y regido por deidades impredecibles. El juego ritual de pelota mesoamericano fue ampliamente pract..._ | Olmecas, Mayas | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Los mayas y los olmecas mantuvieron una relación dinámica y mantuvieron vínculos estrechos, como se evidencia en murales en Cacaxtla pintados en estilo maya y en la ciudad maya de Chichén Itzá y la capital tolteca de Tollan. | [ ] |
| 2 | Mesoamérica carecía de animales de tiro, no utilizaba la rueda, y poseía pocos animales domésticos; el principal medio de transporte era a pie o en canoa. | [ ] |
| 3 | Los mayas vieron el mundo como hostil y regido por deidades impredecibles. | [ ] |

---

## V2 — ¿Qué diferencias hay entre Zapata y Villa?

**Tipo:** comparativa
**Puntos clave esperados:** Zapata: agrarismo, sur, Plan de Ayala; Villa: norte, División del Norte, carácter militar
**Tiempos:** retrieval=0.003s · generación=4.336s · total=4.341s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

_Ayuda para Recall: 422 chunks distintos del corpus mencionan al menos un punto clave (96 mencionan 2 o más); detalle con `python evaluation/candidates.py --question V2`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 15.7960 | Revolución mexicana — _las diferencias entre las facciones que habían luchado contra Huerta, lo que desencadenó nuevos conflictos. Carranza, jefe de la Revolución, de acuerdo con el Plan de Guadalupe, convocó a todas las fuerzas a la Convención de Aguascalientes para nombrar un líder único. En esa reunión Eulalio Gutiérre..._ | Zapata, Villa | [ ] |
| 2 | 15.2795 | Emiliano Zapata — _y algunos lugares de Guerrero. Poco después tomó Cuernavaca y para junio ocupó Cuajimalpa, Xochimilco y Milpa Alta, con lo que amagaba a la Ciudad de México. La población de la capital del país, huía al saber la cercanía del ejército de Zapata. Las fuerzas constitucionalistas les cerraron el paso, a..._ | Zapata, Plan de Ayala, Villa | [ ] |
| 3 | 14.3300 | Revolución mexicana — _fue arrestado en San Luis Potosí por sedición. Durante su estancia en la cárcel se llevaron a cabo las elecciones que dieron el triunfo a Díaz. Madero logró escapar de la prisión estatal y huyó a los Estados Unidos. Desde San Antonio (Texas), el 5 de octubre de 1910, proclamó el Plan de San Luis, qu..._ | Zapata, Villa, norte | [ ] |
| 4 | 13.9600 | Emiliano Zapata — _traicionado la revolución. El gobierno federal reiteró su decisión de imponer el orden por la violencia, y Zapata se desplegó con sus tropas a los límites entre Guerrero y Puebla, escondiéndose del gobierno y generando emboscadas a pequeños contingentes federales. En este periodo, Zapata se casó con..._ | Zapata, Plan de Ayala | [ ] |
| 5 | 13.6576 | Benito Juárez — _y Pepito, pero hay quienes solamente piensan en bienes materiales. ¡Vea estos precios! ¡Hasta 4 veces más caro está el cuarterón de maíz! y créame no se si por ser indio o por qué, pero no los entiendo, no entiendo a quienes se quieren enriquecer de la miseria, de las masas, del dolor y del sufrimie..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

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

_Ayuda para Recall: 71 chunks distintos del corpus mencionan al menos un punto clave (1 mencionan 2 o más); detalle con `python evaluation/candidates.py --question V3`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 26.5953 | Imperio azteca — _# Imperio azteca El Imperio mexica o Triple Alianza (del náhuatl: Exkan Tlahtoloyan o Ēxcān Tlahtōlōyān ‘Los tres lugares donde se dan órdenes’), llamado también Imperio azteca y —con más precisión— Imperio tenochca, fue un imperio organizado en una confederación compleja, multiétnica y flexible de ..._ | ninguno | [ ] |
| 2 | 24.8574 | Historia de México — _de Tenochtitlán, Chimalpopoca, permaneció en silencio, lo que propició un descontento entre los mexicas. Fue el sacerdote Tlacaelél quien, desde las sombras, convenció al sacerdote Izcóatl de realizar un golpe de Estado en Tenochtitlán, logrando imponerse como gobernante el 16 de octubre de 1427. Aq..._ | ninguno | [ ] |
| 3 | 23.6682 | Imperio azteca — _Guerrero y el Soconusco. El fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españoles —en alianza con los tlaxcaltecas y totonacas, entre otros pueblos indígenas— derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco. Etimología, nombres y definiciones La palabra «azteca» ..._ | ninguno | [ ] |
| 4 | 23.4209 | Imperio azteca — _los reinos fragmentados de los mayas. En este campamento los antiguos comerciantes mexicas viajaban para obtener algunas de las materias más valoradas, por la lejanía desde donde se traían y la dificultad. El campamento tenía solo una pequeña guarnición de soldados que eran para proteger a los mexic..._ | ninguno | [ ] |
| 5 | 23.3804 | Historia de México — _del Lago de Texcoco que pretendía dividir el lago de agua salada para introducir agua dulce a la isla por medio de su segunda obra, el Acueducto de Chapultepec, iniciado en 1449. A su muerte, Nezahualpilli recibió el trono de Texcoco y el Imperio Azteca le envió a Chalchiunenetzin como concubina par..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

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
>
> Fuentes: Fragmento 2, Fragmento 3, Fragmento 5.

_Ayuda para Recall: 79 chunks distintos del corpus mencionan al menos un punto clave (6 mencionan 2 o más); detalle con `python evaluation/candidates.py --question R1`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 20.8266 | Historia de México — _Mori fue capturado en Juchitán de Zaragoza (Oaxaca) cuando intentaba huir hacia Panamá; ahí mismo fue torturado, castrado y ejecutado por los habitantes del pueblo. Todo levantamiento era reprimido con fuerza. No duró mucho, cierto día, el 16 de julio de 1872 Juárez fue a visitar con su hija la tumb..._ | ninguno | [ ] |
| 2 | 20.5725 | Benito Juárez — _quien finalmente levantó el sitio sobre el puerto, el 30 de marzo de 1859. El 6 de abril recibió al representante diplomático de los Estados Unidos Robert MacLane. Nacionalización de los bienes del clero El 12 de julio de 1859, Juárez decretó la primera de las normas de reforma: la Ley de Nacionaliz..._ | ninguno | [ ] |
| 3 | 20.3752 | Benito Juárez — _quien decide que un cañonero estadounidense que estaba cerca del puerto de Veracruz bombardease el barco de Santa Anna para obligarlo a partir fuera de costas mexicanas y con esto evitar toda posibilidad de llevar a cabo su plan y con esto consolidar el gobierno de Juárez. Santa Anna, que en ese mom..._ | ninguno | [ ] |
| 4 | 19.9611 | Benito Juárez — _"Virginia" y trasladarse junto con un gran arsenal al Puerto de Veracruz para buscar un golpe de Estado con el apoyo de sus paisanos los veracruzanos. Sebastián Lerdo y Juárez veían que el ejército republicano tuviera todo para salir avante en su empresa. En eso llegó al Palacio Nacional provisional..._ | ninguno | [ ] |
| 5 | 19.6994 | Guerra de Reforma — _# Guerra de Reforma La Guerra de Reforma, también conocida como la guerra de los tres años, fue una guerra civil que aconteció en México desde el 17 de diciembre de 1857 al 11 de enero de 1861, como consecuencia de la promulgación de la Constitución de 1857 y en especial de las llamadas Leyes de Ref..._ | promulgó las Leyes de Reforma | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Benito Juárez fue una figura central en la Guerra de Reforma, que ocurrió entre 1857 y 1861. | [ ] |
| 2 | La guerra fue una consecuencia de la promulgación de la Constitución de 1857 y las Leyes de Reforma, y dividió al país en liberales (a favor de las Leyes de Reforma) y conservadores (en contra). | [ ] |
| 3 | Los liberales, liderados por Juárez, finalmente derrotaron a los conservadores, y Juárez instaló su administración en Ciudad de México. | [ ] |

---

## R2 — ¿Cómo se relacionan Hernán Cortés y Moctezuma II?

**Tipo:** relacional
**Puntos clave esperados:** Encuentro en Tenochtitlan en 1519; Moctezuma tomado como rehén; su muerte; destrucción del imperio
**Tiempos:** retrieval=0.007s · generación=7.600s · total=7.607s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Hernán Cortés y Moctezuma II se relacionaron porque Cortés y su ejército fueron hospedados por Moctezuma II en el templo de su antecesor Axayácatl en Tenochtitlán. Moctezuma II creyó que los españoles eran enviados del dios Quetzalcóatl y los obsequió con regalos, incluyendo el Tocado del Dios Quetzalcóatl. Posteriormente, Moctezuma fue hecho prisionero por Cortés en su propio palacio en noviembre de 1519.
>
> Fuentes: Fragmento 3, Fragmento 4.

_Ayuda para Recall: 174 chunks distintos del corpus mencionan al menos un punto clave (5 mencionan 2 o más); detalle con `python evaluation/candidates.py --question R2`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 19.2886 | Moctezuma II — _el cuerpo de Itzquauhtzin fue llevado en una canoa a Tlatelolco. Durante la huida de los españoles, 30 de junio de 1520, perdieron cerca de la mitad de los soldados castellanos y casi todo el oro que habían obtenido y tuvieron que refugiarse entre los tlaxcaltecas. Entretanto, Cuitláhuac fue elegido..._ | su muerte | [ ] |
| 2 | 18.1326 | Moctezuma II — _más exclusivos. Uno de sus hijos fue Jerónimo Girón y Moctezuma. Este hombre fue III marqués de las Amarillas y un general que participó en la guerra de Independencia de los Estados Unidos, teniendo un papel destacado en la victoria obtenida sobre los ingleses en la batalla del Fuerte Charlotte (Mob..._ | ninguno | [ ] |
| 3 | 17.8108 | Hernán Cortés — _otro lado, avistó por primera vez el lago de Texcoco aproximándose a ella por el rumbo de Xochimilco. Tenochtitlan Hernán Cortés, en su marcha hacia México-Tenochtitlan, el ejército de Cortés (unos trescientos españoles) y el apoyo de unos 3000 tlaxcaltecas avistó los volcanes Popocatépetl e Iztaccí..._ | Encuentro en Tenochtitlan en 1519 | [ ] |
| 4 | 17.1820 | Moctezuma II — _# Moctezuma Xocoyotzin Moctezuma Xocoyotzin (en náhuatl clásico: Motēcuzōmah Xōcoyōtzin; AFI [moteːkʷˈsoːmaḁ ʃoːkoˈjoːt͡sin̥] (): ‘Moctezuma el Joven’ (México-Tenochtitlan, c. 1466-México-Tenochtitlan, 29 de junio de 1520), también llamado Moctezuma II, fue el noveno Huey Tlatoani de México-Tenochti..._ | Encuentro en Tenochtitlan en 1519 | [ ] |
| 5 | 17.0408 | Moctezuma II — _Una breve batalla sucedió después en la que Xóchitl fue capturado y posteriormente ejecutado públicamente en la hoguera. Tras esto, Moctezuma ordenó que ningún otro enfrentamiento ocurriera, y que tenía planeado finalmente castigar a Ixtlilxóchitl por lo sucedido, pero en un momento más apropiado. L..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Hernán Cortés y Moctezuma II se relacionaron porque Cortés y su ejército fueron hospedados por Moctezuma II en el templo de su antecesor Axayácatl en Tenochtitlán. | [ ] |
| 2 | Moctezuma II creyó que los españoles eran enviados del dios Quetzalcóatl y los obsequió con regalos, incluyendo el Tocado del Dios Quetzalcóatl. | [ ] |
| 3 | Posteriormente, Moctezuma fue hecho prisionero por Cortés en su propio palacio en noviembre de 1519. | [ ] |

---

## R3 — ¿Qué papel jugó el Virreinato en la Independencia?

**Tipo:** relacional
**Puntos clave esperados:** Agravios acumulados; criollos excluidos del poder; influencia ilustrada; debilitamiento de España
**Tiempos:** retrieval=0.005s · generación=4.142s · total=4.147s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

_Ayuda para Recall: 8 chunks distintos del corpus mencionan al menos un punto clave (0 mencionan 2 o más); detalle con `python evaluation/candidates.py --question R3`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 21.9497 | Virreinato de Nueva España — _I), Juan de Tecto y Juan de Aora, pertenecientes a la alta sociedad castellana. Aora y Tecto fueron llevados por Cortés a evangelizar las Hibueras, pero murieron en el trayecto. Gante, mientras tanto, siguió su labor en Nueva España, fundó hospitales y escuelas, estableció un convento y enseñó artes..._ | ninguno | [ ] |
| 2 | 19.1400 | Virreinato de Nueva España — _la primera actividad lingüística del Nuevo Mundo. A finales del siglo, el intelectual nahua Antonio del Rincón escribió el Arte mexicana (1595), una gramática de su lengua materna más compleja que incluyó análisis fonológicos como la duración vocálica y la oclusión glotal. Es reconocido como el prim..._ | ninguno | [ ] |
| 3 | 18.6458 | Civilización maya — _internos. El panorama político maya era muy complejo, y las élites mayas se sirvieron de intriga política para obtener ventajas económicas y sociales sobre sus vecinos. En el Clásico Tardío, algunas entidades políticas alcanzaron un largo período de dominación sobre otras grandes entidades políticas..._ | ninguno | [ ] |
| 4 | 18.5825 | Virreinato de Nueva España — _aliciente para el contrabando. Veracruz era el puerto donde se realizaba el comercio con España, y las mercancías se descargaban en Cádiz, donde comisionados de la Casa de Contratación de Sevilla revisaban las mercancías. Por otro lado, Acapulco era la vía de comunicación con las Filipinas, y donde ..._ | ninguno | [ ] |
| 5 | 17.4988 | Virreinato de Nueva España — _el primer virreinato erigido, y por lo tanto, donde se puso en práctica el modelo español de gobernación. El virrey, cuyo término significa etimológicamente en lugar del rey, concentraba todo el poder público, como ya se ha dicho. Era nombrado y removido libremente por el rey, cuando el soberano qui..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

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
>
> Fuentes:
> * Fragmento 3
> * Fragmento 4
> * Fragmento 5

_Ayuda para Recall: 157 chunks distintos del corpus mencionan al menos un punto clave (17 mencionan 2 o más); detalle con `python evaluation/candidates.py --question M1`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 25.4849 | Historia de México — _# Historia de México La historia de México es la narración cronológica y demostrable de los acontecimientos del pasado relacionados con el actual territorio de México, país ubicado en América del Norte. Dicha narración puede dividirse de distintas maneras según la perspectiva historiográfica. La div..._ | ninguno | [ ] |
| 2 | 24.1826 | Moctezuma II — _eventos más importantes que llevarían a la colonización del resto del continente americano por naciones europeas. Antecedentes La primera vez que Moctezuma oyó de la llegada de extranjeros nunca antes vistos, de piel blanca y grandes barbas desde las playas del este, sucedió en el año 13 Tochtli del..._ | ninguno | [ ] |
| 3 | 24.0433 | Virreinato de Nueva España — _En el caso de las Islas Filipinas, predominaban lenguas indígenas como el tagalo y el cebuano, que juntas cubrían aproximadamente un cuarto de la población del archipiélago cada una. Lingüistas estiman que el ilocano, hiligaíno, bicol y samareño también eran hablados por 5-10 % de habitantes, y exis..._ | ninguno | [ ] |
| 4 | 22.7927 | Hernán Cortés — _con los otros tres. Tras esto, un pueblo vecino, por instigación de los aztecas, se dispuso a atacarlos. Cortés mandó a un vasco apellidado Heredia con una escopeta que pegó un tiro y aterrorizó a los enemigos, provocando una victoria. Cortés quiso formalizar su alianza con este pueblo. Malintzin le..._ | aztecas, el Imperio Azteca dominaba en 1519 | [ ] |
| 5 | 21.9762 | Conquista de México — _el hedor era insoportable. Organizaron un banquete con vino, carne de cerdo, carne de pavo y tortillas de maíz en abundancia. Al día siguiente celebraron misa y se cantó un tedeum. Los texcocanos en la conquista Tetzcoco (Texcoco) era una ciudad importante, la segunda del Valle de México, con el ant..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Según el contexto proporcionado, antes de la llegada de los españoles existían el imperio teocrático de los incas, la confederación de los mexicas y la cultura maya. | [ ] |
| 2 | En 1519, los mexicas dominaban. | [ ] |

---

## M2 — ¿Cómo influyeron las reformas de Juárez en la Revolución décadas después?

**Tipo:** multihop
**Puntos clave esperados:** Constitución de 1857; separación Iglesia-Estado; antecedente liberal que Díaz traicionó
**Tiempos:** retrieval=0.004s · generación=4.071s · total=4.076s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

_Ayuda para Recall: 53 chunks distintos del corpus mencionan al menos un punto clave (3 mencionan 2 o más); detalle con `python evaluation/candidates.py --question M2`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 22.3380 | Independencia de México — _la agricultura. Por ejemplo, la creciente importancia de Guadalajara y El Bajío se debía a su relación con los minerales de Zacatecas y Guanajuato. Dado que la exportación de plata y oro constituía el nodo de la economía novohispana, en torno a esta actividad creció un complejo sistema que consolidó..._ | ninguno | [ ] |
| 2 | 22.3380 | Guerra de Independencia de México **(copia exacta del rank 1: cuenta una sola vez)** — _la agricultura. Por ejemplo, la creciente importancia de Guadalajara y El Bajío se debía a su relación con los minerales de Zacatecas y Guanajuato. Dado que la exportación de plata y oro constituía el nodo de la economía novohispana, en torno a esta actividad creció un complejo sistema que consolidó..._ | ninguno | [ ] |
| 3 | 21.6954 | Guerra de Reforma — _punto de vista, atacaba a la religión católica, que era la creencia de la mayoría del país, además de afectar gravemente a los pueblos indígenas al despojarlos de sus tierras comunales y poner en riesgo su forma tradicional de vida. Con el Plan de Tacubaya, dirigido por Félix Zuloaga, se estipulaba ..._ | ninguno | [ ] |
| 4 | 21.3385 | Imperio azteca — _masa o cera para engañar a vendedores. La calidad y tipo del cacao era tomada en cuenta; el «buen tratante» vendía sus almendras «gordas, macizas y escogidas», y separadas por su tamaño, peso y conservación, y también por su lugar de origen, en caso de venir de alguna región lejana o extranjera. Al ..._ | ninguno | [ ] |
| 5 | 21.2930 | Historia de México — _movimientos de las tropas francesas para el funcionamiento del imperio. Maximiliano solicitó revisar las reformas políticas dejadas por el gobierno anterior; no las de Santa Anna, sino las de Juárez. Fue cuando los conservadores descubrieron que la verdadera cara de la monarquía europea, ya estaba m..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

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
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 16.2886 | Historia de México — _comunistas decidieron volvar su apoyo a Vasconcelos que ya consolidaba el gusto universitario y el católico. En el PNR hubo polémica sobre quién sería el elegido candidato, pues al principio se había propuesto a Aarón Sáenz. En un cambio de último momento, impuesto por el poder de Calles, se decidió..._ | — | [ ] |
| 2 | 15.3470 | Conquista de México — _siglo XVII un grupo de tlaxcaltecas fue llevado para pacificar a los nativos de la región así como para enseñarles la agricultura; no obstante, los ataques a las ciudades eran constantes y causaron problemas a los colonizadores hasta principios del siglo XVIII, al grado que la producción minera y al..._ | — | [ ] |
| 3 | 14.9132 | Conquista de México — _del río Usumacinta y fundó la villa de San Pedro Tanoche. Cuando «el Mozo» se enteró de este evento avanzó hacia la zona para defender los derechos de su padre. Debido a que la población se encontraba en medio de la selva, incomunicada, y muy apartada de los centros de abastecimiento, «el Mozo» dio ..._ | — | [ ] |
| 4 | 14.8003 | Conquista de México — _Carlos I de España también nombró a Nuño de Guzmán como gobernador de la provincia de Pánuco y como capitán general de la Nueva España en 1529. El nuevo gobernador se comportó como un acérrimo enemigo de Cortés, llegando al punto de arrestar a Pedro de Alvarado solo porque este hablaba bien del conq..._ | — | [ ] |
| 5 | 14.6491 | Imperio azteca — _consideraba representante de los dioses. Otros altos funcionarios eran: El Cihuacóatl del Imperio Mexica era una especie de "coemperador". Se encargaba de la administración tributaria, los asuntos religiosos y las apelaciones judiciales. En algunos aspectos ejercía ciertas facultades de jefe de Gobi..._ | — | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

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
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 17.8849 | Cultura teotihuacana — _Mimosa biuncifera. A estos tipos de vegetación se suman los pastizales, la vegetación hidrófila estacional, asociada con la temporada de lluvia. Las condiciones del valle favorecieron la concentración demográfica por ser benéficas para el estilo de vida mesoamericano basado en la agricultura. Los pa..._ | — | [ ] |
| 2 | 16.6111 | Cultura teotihuacana — _cuál ha sido el impacto de la actividad humana sobre los suelos de Teotihuacán. Rivera Uria et al. advierten que en algunos sitios como el cerro San Lucas la composición de la superficie ha cambiado dramáticamente. En este caso encontraron que antes del establecimiento de las primeras comunidades de..._ | — | [ ] |
| 3 | 15.3470 | Conquista de México — _siglo XVII un grupo de tlaxcaltecas fue llevado para pacificar a los nativos de la región así como para enseñarles la agricultura; no obstante, los ataques a las ciudades eran constantes y causaron problemas a los colonizadores hasta principios del siglo XVIII, al grado que la producción minera y al..._ | — | [ ] |
| 4 | 15.1297 | Historia de México — _Presidente de México desde el 1 de diciembre de 2018 hasta el 30 de septiembre de 2024. Durante su gobierno se destacaron principalmente, la implementación de una política social que sentara las bases de un estado de bienestar, lo que dio como resultado la disminución, por primera vez en décadas, de..._ | — | [ ] |
| 5 | 15.0667 | Cultura teotihuacana — _la ciudad se dispersó por diversas localidades en la cuenca de México. Se desconoce cuál era la identidad étnica de los primeros habitantes de Teotihuacán. Entre los candidatos se encuentran los totonacos, los nahuas y los pueblos de idioma otomangue, particularmente los otomíes. Las hipótesis más r..._ | — | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

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
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 19.8305 | Historia de México — _como estrategia de prevención y contención. La falta de capacidad en los sistemas de salud para atender directamente el padecimiento. En principio el gobierno implementó un programa de reconversión hospitalaria para cubrir la necesidad de camas y respiradores. El 23 de diciembre de 2020 se inició la..._ | — | [ ] |
| 2 | 18.2531 | Historia de México — _que los países de Latinoamérica se comprometían a no fabricar, poseer o utilizar armas nucleares. El 12 de octubre de 1968, nueve días después de ocurrir la Masacre de Tlatelolco, se inauguró la XIX Olimpiada, que tuvieron su sede en la Ciudad de México y el país se mantuvo en el ojo público. Se imp..._ | — | [ ] |
| 3 | 17.5745 | Historia de México — _del presidente Manuel de la Peña y Peña, intentó huir para mantener estabilidad desde oro sitio, pero la derrota era inminente. El 2 de febrero de 1848, se firmó el Tratado de Guadalupe Hidalgo en donde México cedía Texas, Alta California, Nevada, Utah, Nuevo México, Colorado, Wyoming, Kansas y Okla..._ | — | [ ] |
| 4 | 17.3102 | Historia de México — _volcán Popocatépetl y el sureste del estado presentó los mayores daños; Jojutla fue una de las localidades más afectadas. Por el lado de Puebla, la mixteca, la región de los valles de Izúcar y Atlixco, y el centro histórico de la ciudad de Puebla registraron importantes afectaciones. El 5 de octubre..._ | — | [ ] |
| 5 | 15.4567 | Cultura olmeca — _# Cultura olmeca La cultura olmeca fue una civilización que se desarrolló durante el periodo preclásico de Mesoamérica, en parte de los territorios actuales de México. Aunque se han encontrado vestigios de su presencia en amplias zonas de Mesoamérica, se considera que el área cultural olmeca —zona m..._ | — | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---
