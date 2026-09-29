# Hoja de evaluación manual

Protocolo: para cada pregunta, (1) marca qué chunks recuperados son genuinamente relevantes para responderla -- usa los **puntos clave esperados** como referencia, no tu propio conocimiento de historia; (2) marca qué afirmaciones de la respuesta están respaldadas por el texto de los chunks recuperados (Faithfulness) -- si una afirmación es correcta históricamente pero no aparece en los chunks, cuenta como **no respaldada**, porque el sistema no la pudo haber sacado del contexto. Para preguntas trampa, la respuesta correcta es que el sistema declare que no encontró la información -- marca eso como relevante/respaldado si ocurre así.

Total de preguntas: 20

---

## F1 — ¿En qué año cayó Tenochtitlan?

**Tipo:** factual
**Puntos clave esperados:** 1521; Cuauhtémoc; tlaxcaltecas
**Tiempos:** retrieval=6.830s · generación=72.027s · total=78.858s

**Respuesta del sistema:**
> Según el Fragmento 5, el fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españoles derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco. El Fragmento 4 indica que la ciudad debió rendirse el 13 de agosto, marcando así el inicio del dominio español.

Fuentes: Fragmento 4, Fragmento 5.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.6877 | Historia de México — _Lago de Texcoco y sitiar la ciudad. La inestabilidad del imperio apresuró los planes y el 28 de abri..._ | [ ] |
| 2 | 0.6643 | Moctezuma II — _había existido por años entre los mexicas y tarascos.​ Llegada a Tenochtitlán El día 8 de noviembre..._ | [ ] |
| 3 | 0.6383 | Tenochtitlan — _# Tenochtitlan Tenochtitlan puede hacer referencia a: México-Tenochtitlan, ciudad principal de los m..._ | [ ] |
| 4 | 0.6242 | Virreinato de Nueva España — _quienes en lugar de obedecer a su monarca, comenzaron a apedrearlo. El emperador murió pocos días de..._ | [ ] |
| 5 | 0.6129 | Imperio azteca — _Guerrero y el Soconusco. El fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españ..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Según el Fragmento 5, el fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españoles derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco. | [ ] |
| 2 | El Fragmento 4 indica que la ciudad debió rendirse el 13 de agosto, marcando así el inicio del dominio español. | [ ] |
| 3 | Fuentes: Fragmento 4, Fragmento 5. | [ ] |

---

## F2 — ¿Quién dio el Grito de Independencia?

**Tipo:** factual
**Puntos clave esperados:** Miguel Hidalgo; Dolores Hidalgo; 16 septiembre 1810
**Tiempos:** retrieval=0.019s · generación=5.321s · total=5.341s

**Respuesta del sistema:**
> Miguel Hidalgo y Costilla convocó al pueblo de Dolores a sublevarse en contra de las autoridades españolas el 16 de septiembre de 1810, marcando el inicio de la Guerra de Independencia de México.

Fuentes: Fragmento 1, Fragmento 2.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.6657 | Guerra de Independencia de México — _presentó ante el pleno, una memoria titulada Exposición de motivos de la guerra de independencia,​​..._ | [ ] |
| 2 | 0.6657 | Independencia de México — _presentó ante el pleno, una memoria titulada Exposición de motivos de la guerra de independencia,​​..._ | [ ] |
| 3 | 0.6255 | Guerra de Independencia de México — _hizo leer a su secretario Juan Nepomuceno Rosáins los Sentimientos de la Nación.​ Este documento dec..._ | [ ] |
| 4 | 0.6255 | Independencia de México — _hizo leer a su secretario Juan Nepomuceno Rosáins los Sentimientos de la Nación.​ Este documento dec..._ | [ ] |
| 5 | 0.6209 | Historia de México — _a la miseria. El anuncio de una constitución con derechos sociales, nacida de una revolución con el..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Miguel Hidalgo y Costilla convocó al pueblo de Dolores a sublevarse en contra de las autoridades españolas el 16 de septiembre de 1810, marcando el inicio de la Guerra de Independencia de México. | [ ] |
| 2 | Fuentes: Fragmento 1, Fragmento 2. | [ ] |

---

## F3 — ¿Cuándo comenzó el Porfiriato?

**Tipo:** factual
**Puntos clave esperados:** 1876; Porfirio Díaz; reelección continua
**Tiempos:** retrieval=0.019s · generación=4.810s · total=4.829s

**Respuesta del sistema:**
> El Porfiriato comenzó el 28 de noviembre de 1876.

Fuentes:
* Fragmento 2: Porfiriato

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.6119 | Historia de México — _ascenso de Porfirio Díaz al poder en 1876 empezó un periodo conocido como el Porfiriato, mismo que d..._ | [ ] |
| 2 | 0.5910 | Porfiriato — _# Porfiriato El porfiriato o porfirismo​ fue un período de la historia de México en el que el gobier..._ | [ ] |
| 3 | 0.5588 | Historia de México — _mientras que la aleación de oro-plata es una aleación que se encuentra en estado nativo. De las alea..._ | [ ] |
| 4 | 0.5191 | Cultura teotihuacana — _la fundación de Teotihuacán, pero parece que las migraciones desde la ciudad al sur de los lagos com..._ | [ ] |
| 5 | 0.5126 | Historia de México — _e.), el hombre de Texcal (7800 a. n. e.) y la pareja de Aztahuacán (7400 a. n. e.).​ Todos ellos hal..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El Porfiriato comenzó el 28 de noviembre de 1876. | [ ] |
| 2 | Fuentes:
* Fragmento 2: Porfiriato | [ ] |

---

## F4 — ¿Qué civilización construyó Teotihuacán?

**Tipo:** factual
**Puntos clave esperados:** Cultura teotihuacana; nombre propio desconocido; periodo clásico
**Tiempos:** retrieval=0.019s · generación=6.318s · total=6.337s

**Respuesta del sistema:**
> De acuerdo con las fuentes, la identidad de los fundadores de Teotihuacán es desconocida. Los nahuas pensaban que Teotihuacán fue construida por los quinametzin, una raza de gigantes que pobló el mundo durante la era anterior. Aun así, la evidencia arqueológica sugiere que la urbe estuvo situada en un enclave regional donde a lo largo de siglos existió una fuerte convergencia de grupos étnicos y lingüísticos que influyeron en cantidad a sus habitantes.

Fuentes: Fragmento 3

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.7741 | Cultura teotihuacana — _probable que Cuicuilco hubiera declinado definitivamente antes de ese suceso.​ Inicios de la ciudad..._ | [ ] |
| 2 | 0.7368 | Cultura teotihuacana — _de otras regiones, y un caso muy notable es el de los zapotecos que se asentaron en Tlailotlacan en..._ | [ ] |
| 3 | 0.7347 | Cultura teotihuacana — _sido construido por dioses. Pero no sabemos casi nada de los hombres que poblaron esta ciudad en el..._ | [ ] |
| 4 | 0.7316 | Cultura teotihuacana — _yacimientos de diversas zonas. Otros opinan que Teotihuacán fue un estado militarista y que la expan..._ | [ ] |
| 5 | 0.7306 | Cultura teotihuacana — _vestigios de la cerámica maya hallados en Teotihuacán corresponden al tipo Tzakol y guardan semejanz..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | De acuerdo con las fuentes, la identidad de los fundadores de Teotihuacán es desconocida. | [ ] |
| 2 | Los nahuas pensaban que Teotihuacán fue construida por los quinametzin, una raza de gigantes que pobló el mundo durante la era anterior. | [ ] |
| 3 | Aun así, la evidencia arqueológica sugiere que la urbe estuvo situada en un enclave regional donde a lo largo de siglos existió una fuerte convergencia de grupos étnicos y lingüísticos que influyeron en cantidad a sus habitantes. | [ ] |
| 4 | Fuentes: Fragmento 3 | [ ] |

---

## F5 — ¿Quién fue el último emperador azteca?

**Tipo:** factual
**Puntos clave esperados:** Cuauhtémoc; sobrino de Moctezuma II; capturado 1521
**Tiempos:** retrieval=0.019s · generación=4.646s · total=4.665s

**Respuesta del sistema:**
> Moctezuma Xocoyotzin fue el último emperador azteca.

Fuentes: Fragmento 4.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.7134 | Hernán Cortés — _# Hernán Cortés Hernán Cortés de Monroy y Pizarro Altamirano, primer marqués del Valle de Oaxaca (Me..._ | [ ] |
| 2 | 0.6964 | Imperio azteca — _Guerrero y el Soconusco. El fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españ..._ | [ ] |
| 3 | 0.6559 | Imperio azteca — _# Imperio azteca El Imperio mexica o Triple Alianza (del náhuatl: Exkan Tlahtoloyan​ o Ēxcān Tlahtōl..._ | [ ] |
| 4 | 0.6479 | Historia de México — _completo. El siguiente líder al trono fue Tízoc en el año 1481, quien inició una campaña para atrapa..._ | [ ] |
| 5 | 0.6385 | Historia de México — _expandir sus dominios hasta Jaltepec y conquistar cerca de 100 señoríos de la zona de Oaxaca. Sin em..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Moctezuma Xocoyotzin fue el último emperador azteca. | [ ] |
| 2 | Fuentes: Fragmento 4. | [ ] |

---

## C1 — ¿Cuáles fueron las causas de la Revolución Mexicana?

**Tipo:** causalidad
**Puntos clave esperados:** Reelección de Díaz; desigualdad agraria; Plan de San Luis; crisis de 1907; Madero
**Tiempos:** retrieval=0.021s · generación=8.552s · total=8.573s

**Respuesta del sistema:**
> Las causas de la Revolución Mexicana se remontan a la situación de México bajo la dictadura del porfiriato, donde Porfirio Díaz Mori ejerció el poder de manera dictatorial desde 1876 hasta 1911. Durante este periodo, México experimentó crecimiento económico y estabilidad política, pero a altos costos sociales, que fueron pagados por los estratos menos favorecidos de la sociedad y la oposición política al régimen de Díaz. Además, varias crisis en diversas esferas de la vida nacional reflejaban el creciente descontento de algunos sectores con el porfiriato. Cuando Porfirio Díaz aseguró en una entrevista que se retiraría al finalizar su mandato sin buscar la reelección, la situación política comenzó a agitarse.

Fuentes:
*   Revolución mexicana (Fragmento 1)
*   Historia de México (Fragmento 2)
*   Revolución mexicana (Fragmento 3)
*   Historia de México (Fragmento 4)

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.8512 | Revolución mexicana — _# Revolución mexicana La Revolución mexicana fue un conflicto armado en México que se inició el 20 d..._ | [ ] |
| 2 | 0.7570 | Historia de México — _ascenso de Porfirio Díaz al poder en 1876 empezó un periodo conocido como el Porfiriato, mismo que d..._ | [ ] |
| 3 | 0.7505 | Revolución mexicana — _el cual se ubica en el paseo de la Reforma.​ La «primera piedra» fue colocada por el presidente Feli..._ | [ ] |
| 4 | 0.7488 | Historia de México — _de la modernidad, siendo la revolución de 1910 el primer hecho histórico mexicano con rasgos contemp..._ | [ ] |
| 5 | 0.7403 | Independencia de México — _# Independencia de México La independencia de México fue la consecuencia de un proceso político y so..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Las causas de la Revolución Mexicana se remontan a la situación de México bajo la dictadura del porfiriato, donde Porfirio Díaz Mori ejerció el poder de manera dictatorial desde 1876 hasta 1911. | [ ] |
| 2 | Durante este periodo, México experimentó crecimiento económico y estabilidad política, pero a altos costos sociales, que fueron pagados por los estratos menos favorecidos de la sociedad y la oposición política al régimen de Díaz. | [ ] |
| 3 | Además, varias crisis en diversas esferas de la vida nacional reflejaban el creciente descontento de algunos sectores con el porfiriato. | [ ] |
| 4 | Cuando Porfirio Díaz aseguró en una entrevista que se retiraría al finalizar su mandato sin buscar la reelección, la situación política comenzó a agitarse. | [ ] |
| 5 | Fuentes:
*   Revolución mexicana (Fragmento 1)
*   Historia de México (Fragmento 2)
*   Revolución mexicana (Fragmento 3)
*   Historia de México (Fragmento 4) | [ ] |

---

## C2 — ¿Por qué cayó el Imperio Azteca?

**Tipo:** causalidad
**Puntos clave esperados:** Alianzas con tlaxcaltecas; enfermedades; superioridad militar española; muerte de Moctezuma
**Tiempos:** retrieval=0.019s · generación=5.966s · total=5.985s

**Respuesta del sistema:**
> El Imperio azteca cayó el 13 de agosto de 1521, cuando los españoles —en alianza con los tlaxcaltecas y totonacas, entre otros pueblos indígenas— derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco.

Fuentes:
* Fragmento 1: Imperio azteca
* Fragmento 4: Imperio azteca

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.7110 | Imperio azteca — _Guerrero y el Soconusco. El fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españ..._ | [ ] |
| 2 | 0.6750 | Hernán Cortés — _contenido astral). Estos regalos, en lugar de disuadir a Cortés, le animaron a continuar y conquista..._ | [ ] |
| 3 | 0.6678 | Imperio azteca — _lenguaje artístico comunicó historias, deidades y ritos en los que coincidieron ancestrales mitos y..._ | [ ] |
| 4 | 0.6669 | Imperio azteca — _# Imperio azteca El Imperio mexica o Triple Alianza (del náhuatl: Exkan Tlahtoloyan​ o Ēxcān Tlahtōl..._ | [ ] |
| 5 | 0.6420 | Historia de México — _expandir sus dominios hasta Jaltepec y conquistar cerca de 100 señoríos de la zona de Oaxaca. Sin em..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El Imperio azteca cayó el 13 de agosto de 1521, cuando los españoles —en alianza con los tlaxcaltecas y totonacas, entre otros pueblos indígenas— derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco. | [ ] |
| 2 | Fuentes:
* Fragmento 1: Imperio azteca
* Fragmento 4: Imperio azteca | [ ] |

---

## C3 — ¿Qué provocó la Guerra de Reforma?

**Tipo:** causalidad
**Puntos clave esperados:** Constitución de 1857; liberales vs conservadores; Ley Juárez; Ley Lerdo
**Tiempos:** retrieval=0.018s · generación=5.722s · total=5.740s

**Respuesta del sistema:**
> La Guerra de Reforma, también conocida como la guerra de los tres años, fue provocada por la promulgación de la Constitución de 1857 y en especial de las llamadas Leyes de Reforma. El país estaba dividido en dos grandes grupos: liberales (a favor de las Leyes de Reforma) y los conservadores (en contra).

Fuentes: Fragmento 1

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.7316 | Guerra de Reforma — _# Guerra de Reforma La Guerra de Reforma, también conocida como la guerra de los tres años, fue una..._ | [ ] |
| 2 | 0.5995 | Revolución mexicana — _Tras el triunfo de la revolución constitucionalista en agosto de 1914 y el posterior exilio de Victo..._ | [ ] |
| 3 | 0.5898 | Guerra de Independencia de México — _Ecatepec el 22 de diciembre de 1815. Durante esta época, el movimiento independentista no solo reali..._ | [ ] |
| 4 | 0.5898 | Independencia de México — _Ecatepec el 22 de diciembre de 1815. Durante esta época, el movimiento independentista no solo reali..._ | [ ] |
| 5 | 0.5845 | Historia de México — _alto del Frontón México, el 14 de septiembre de 1939, junto con los grupos progresistas católicos, e..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | La Guerra de Reforma, también conocida como la guerra de los tres años, fue provocada por la promulgación de la Constitución de 1857 y en especial de las llamadas Leyes de Reforma. | [ ] |
| 2 | El país estaba dividido en dos grandes grupos: liberales (a favor de las Leyes de Reforma) y los conservadores (en contra). | [ ] |
| 3 | Fuentes: Fragmento 1 | [ ] |

---

## C4 — ¿Por qué terminó el Porfiriato?

**Tipo:** causalidad
**Puntos clave esperados:** Revolución Mexicana; renuncia de Díaz en 1911; Plan de San Luis; descontento social
**Tiempos:** retrieval=0.016s · generación=5.855s · total=5.872s

**Respuesta del sistema:**
> El Porfiriato terminó meses después de que Porfirio Díaz renunció a la presidencia y salió rumbo a Francia, esto ocurrió el 27 de mayo de 1911, después de que estallara la Revolución.

Fuentes:
*   [Fragmento 1 | Fuente: Porfiriato]
*   [Fragmento 2 | Fuente: Historia de México]

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.5607 | Porfiriato — _# Porfiriato El porfiriato o porfirismo​ fue un período de la historia de México en el que el gobier..._ | [ ] |
| 2 | 0.5194 | Historia de México — _ascenso de Porfirio Díaz al poder en 1876 empezó un periodo conocido como el Porfiriato, mismo que d..._ | [ ] |
| 3 | 0.5039 | Historia de México — _abril, cuando Obregón aprovechó las debilidades de Villa retirándolos hasta el norte. Desconectadas..._ | [ ] |
| 4 | 0.4991 | Cultura teotihuacana — _a la cronología propuesta por René Millon y su equipo de colaboradores.​ A pesar de esta aceptación..._ | [ ] |
| 5 | 0.4745 | Historia de México — _Nueva España y que concluyó con 12 personas quemadas en la hoguera (algo extraordinario y nunca vist..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El Porfiriato terminó meses después de que Porfirio Díaz renunció a la presidencia y salió rumbo a Francia, esto ocurrió el 27 de mayo de 1911, después de que estallara la Revolución. | [ ] |
| 2 | Fuentes:
*   [Fragmento 1 | Fuente: Porfiriato]
*   [Fragmento 2 | Fuente: Historia de México] | [ ] |

---

## V1 — ¿En qué se diferencian los mayas y los olmecas?

**Tipo:** comparativa
**Puntos clave esperados:** Olmecas: civilización madre, cabezas colosales, zona costera; Mayas: escritura, calendario, ciudades-estado
**Tiempos:** retrieval=0.024s · generación=6.839s · total=6.862s

**Respuesta del sistema:**
> Los olmecas se pueden definir como la cultura madre de la América precolombina, y surgieron alrededor de los años 1200 a. n. e. en la región costera del Golfo de México (actualmente Veracruz y Tabasco). Se cree que los sacerdotes eran la clase dirigente por poseer conocimientos astronómicos sobre los períodos de lluvia y la siembra. Los mayas, cuya estructura más antigua conocida es la de Aguada Fénix en Tabasco, datan de alrededor del año 1500 a. n. e.

Fuentes: Fragmento 4, Fragmento 5.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.5940 | Imperio azteca — _en la asimilación de la herencia popular de la tradición nahua. Los aztecas intentaron combinar dos..._ | [ ] |
| 2 | 0.5786 | Civilización maya — _pueden tener una longitud de hasta más de 30 cm.​ Su forma puede variar considerablemente, pero por..._ | [ ] |
| 3 | 0.5779 | Civilización maya — _# Cultura maya La cultura maya fue una civilización mesoamericana que se desarrolló en lo que actual..._ | [ ] |
| 4 | 0.5570 | Historia de México — _de ciudades, poblaciones y demarcaciones diferentes que convivieron o provocaron conflictos entre el..._ | [ ] |
| 5 | 0.5460 | Civilización maya — _Aunque es difícil de reconstruir el sistema de creencias a través de la arqueología, existen indicad..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Los olmecas se pueden definir como la cultura madre de la América precolombina, y surgieron alrededor de los años 1200 a. | [ ] |
| 2 | en la región costera del Golfo de México (actualmente Veracruz y Tabasco). | [ ] |
| 3 | Se cree que los sacerdotes eran la clase dirigente por poseer conocimientos astronómicos sobre los períodos de lluvia y la siembra. | [ ] |
| 4 | Los mayas, cuya estructura más antigua conocida es la de Aguada Fénix en Tabasco, datan de alrededor del año 1500 a. | [ ] |
| 5 | Fuentes: Fragmento 4, Fragmento 5. | [ ] |

---

## V2 — ¿Qué diferencias hay entre Zapata y Villa?

**Tipo:** comparativa
**Puntos clave esperados:** Zapata: agrarismo, sur, Plan de Ayala; Villa: norte, División del Norte, carácter militar
**Tiempos:** retrieval=0.019s · generación=7.545s · total=7.564s

**Respuesta del sistema:**
> Según los fragmentos proporcionados, las diferencias entre Zapata y Villa incluyen:

*   Zapata se unió con Francisco Villa y ambos reconocieron a Eulalio Gutiérrez como presidente provisional de México, mientras que no reconocieron a Venustiano Carranza, lo que provocó la continuación de la guerra civil.
*   Villa aceptó el plan de Ayala, a excepción de sus acusaciones a Francisco I. Madero, mientras que Zapata se enfureció al que Madero le ofreciera una hacienda como "pago a sus servicios a la Revolución".
*   Zapata se mantuvo a la defensiva para mantener aislada su región, mientras que Villa intentó tomar Celaya, pero sufrió derrotas significativas.

Fuentes: Fragmento 1, Fragmento 2, Fragmento 5.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.5152 | Emiliano Zapata — _Emiliano Zapata a Aguascalientes, que desempeñó un papel importante de negociación para la asistenci..._ | [ ] |
| 2 | 0.4891 | Emiliano Zapata — _traicionado la revolución. El gobierno federal reiteró su decisión de imponer el orden por la violen..._ | [ ] |
| 3 | 0.4836 | Historia de México — _noticias falsas sobre la participación de Pancho Villa que vivía tranquilamente en su hacienda. Al c..._ | [ ] |
| 4 | 0.4826 | Pancho Villa — _Francisco Villa, llamado Centauro del Norte.​ En 2023 se lanzó una serie biográfica sobre su vida ll..._ | [ ] |
| 5 | 0.4729 | Revolución mexicana — _y Zapata debido a que este último tenía por objetivo mantener aislada su región, por lo que se mante..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Según los fragmentos proporcionados, las diferencias entre Zapata y Villa incluyen:

*   Zapata se unió con Francisco Villa y ambos reconocieron a Eulalio Gutiérrez como presidente provisional de México, mientras que no reconocieron a Venustiano Carranza, lo que provocó la continuación de la guerra civil. | [ ] |
| 2 | *   Villa aceptó el plan de Ayala, a excepción de sus acusaciones a Francisco I. | [ ] |
| 3 | Madero, mientras que Zapata se enfureció al que Madero le ofreciera una hacienda como "pago a sus servicios a la Revolución". | [ ] |
| 4 | *   Zapata se mantuvo a la defensiva para mantener aislada su región, mientras que Villa intentó tomar Celaya, pero sufrió derrotas significativas. | [ ] |
| 5 | Fuentes: Fragmento 1, Fragmento 2, Fragmento 5. | [ ] |

---

## V3 — ¿En qué se parecen el Virreinato y el Imperio Azteca?

**Tipo:** comparativa
**Puntos clave esperados:** Control centralizado; tributo; dominio territorial; jerarquía religiosa ligada al poder
**Tiempos:** retrieval=0.035s · generación=4.275s · total=4.310s

**Respuesta del sistema:**
> No encontré esta información en el corpus.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.7241 | Imperio azteca — _# Imperio azteca El Imperio mexica o Triple Alianza (del náhuatl: Exkan Tlahtoloyan​ o Ēxcān Tlahtōl..._ | [ ] |
| 2 | 0.6951 | Imperio azteca — _lenguaje artístico comunicó historias, deidades y ritos en los que coincidieron ancestrales mitos y..._ | [ ] |
| 3 | 0.6660 | Imperio azteca — _Guerrero y el Soconusco. El fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españ..._ | [ ] |
| 4 | 0.6574 | Imperio azteca — _conocidos como aztecas—, un pueblo que, de acuerdo con algunos documentos históricos como la Tira de..._ | [ ] |
| 5 | 0.6184 | Imperio azteca — _en la asimilación de la herencia popular de la tradición nahua. Los aztecas intentaron combinar dos..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---

## R1 — ¿Qué relación tuvo Juárez con la Guerra de Reforma?

**Tipo:** relacional
**Puntos clave esperados:** Juárez lideró el bando liberal; promulgó las Leyes de Reforma; fue presidente durante el conflicto
**Tiempos:** retrieval=0.018s · generación=5.338s · total=5.356s

**Respuesta del sistema:**
> Benito Juárez volvió a entrar triunfante a la capital en julio de 1867 tras el triunfo sobre los invasores franceses y austríacos, aunque al poco tiempo después enfrentaría la rebelión de Porfirio Díaz.

Fuentes:
* Fragmento 4 | Fuente: Guerra de Reforma

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.7081 | Historia de México — _del universo, que por primera vez intruduce en la lucha las ideas socialistas para reformar la propi..._ | [ ] |
| 2 | 0.7059 | Benito Juárez — _héroe de la independencia. Juárez le preguntó al hombre sobre cómo era Hidalgo, a lo que éste respon..._ | [ ] |
| 3 | 0.7020 | Benito Juárez — _vez en Ciudad de México los recibió una muchedumbre así como miembros del gabinete y del gobierno, l..._ | [ ] |
| 4 | 0.6914 | Guerra de Reforma — _y lograr la pacificación del país, por lo que sobrevendría la segunda intervención francesa en Méxic..._ | [ ] |
| 5 | 0.6835 | Benito Juárez — _y tropa huyeron hacia el Ajusco. Existieron otros altercados militares durante 1871 que fueron contr..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Benito Juárez volvió a entrar triunfante a la capital en julio de 1867 tras el triunfo sobre los invasores franceses y austríacos, aunque al poco tiempo después enfrentaría la rebelión de Porfirio Díaz. | [ ] |
| 2 | Fuentes:
* Fragmento 4 | Fuente: Guerra de Reforma | [ ] |

---

## R2 — ¿Cómo se relacionan Hernán Cortés y Moctezuma II?

**Tipo:** relacional
**Puntos clave esperados:** Encuentro en Tenochtitlan en 1519; Moctezuma tomado como rehén; su muerte; destrucción del imperio
**Tiempos:** retrieval=0.023s · generación=6.666s · total=6.689s

**Respuesta del sistema:**
> Hernán Cortés le pidió a Moctezuma II que hiciera algo al respecto sobre Cacamatzin, quien amenazaba con iniciar una guerra civil. Moctezuma sugirió que Cacamatzin fuera arrestado y que Ixtlilxóchitl tomara su lugar en el trono. Además, la convivencia entre Cortés y Moctezuma había creado un vínculo de amistad y el tlatoani, antes de morir, pidió a Cortés que favoreciese a su hijo, Chimalpopoca.

Fuentes: Fragmento 1, Fragmento 4.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.6153 | Moctezuma II — _Coyoacán, Tlacopan, Iztapalapa y el pueblo matlatzinca. Sin embargo, Moctezuma no deseaba la posibil..._ | [ ] |
| 2 | 0.6091 | Conquista de México — _parte Cortés le entregó una carta o salvoconducto para mostrar a posibles futuras expediciones españ..._ | [ ] |
| 3 | 0.6032 | Moctezuma II — _con una ruptura de varonía de los de Moctezuma se instaló en Portugal en el siglo XIX, donde sus des..._ | [ ] |
| 4 | 0.6027 | Conquista de México — _fue llevado al interior pero falleció tres días después a causa de la herida.​ Su cuerpo y el de Itz..._ | [ ] |
| 5 | 0.5840 | Conquista de México — _Las primeras escalas de Cortés: de Cozumel a Centla Cortés se dirigió a la isla de Cozumel​ siguiend..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Hernán Cortés le pidió a Moctezuma II que hiciera algo al respecto sobre Cacamatzin, quien amenazaba con iniciar una guerra civil. | [ ] |
| 2 | Moctezuma sugirió que Cacamatzin fuera arrestado y que Ixtlilxóchitl tomara su lugar en el trono. | [ ] |
| 3 | Además, la convivencia entre Cortés y Moctezuma había creado un vínculo de amistad y el tlatoani, antes de morir, pidió a Cortés que favoreciese a su hijo, Chimalpopoca. | [ ] |
| 4 | Fuentes: Fragmento 1, Fragmento 4. | [ ] |

---

## R3 — ¿Qué papel jugó el Virreinato en la Independencia?

**Tipo:** relacional
**Puntos clave esperados:** Agravios acumulados; criollos excluidos del poder; influencia ilustrada; debilitamiento de España
**Tiempos:** retrieval=0.020s · generación=6.688s · total=6.709s

**Respuesta del sistema:**
> El Virreinato jugó un papel importante en la Independencia de México debido a que el gobierno de la metrópoli implementó medidas que restaron facultades autónomas a las autoridades civiles y eclesiásticas en Nueva España. El aumento de tributos causó un déficit en las finanzas de cada territorio, restringiendo su capacidad de desarrollarse. La ocupación de España por Napoleón Bonaparte fue el momento idóneo para que las ideas de independencia florecieran.

Fuentes: Fragmento 5, Fragmento 1, Fragmento 2, Fragmento 3, Fragmento 4.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.6640 | Guerra de Independencia de México — _presentó ante el pleno, una memoria titulada Exposición de motivos de la guerra de independencia,​​..._ | [ ] |
| 2 | 0.6640 | Independencia de México — _presentó ante el pleno, una memoria titulada Exposición de motivos de la guerra de independencia,​​..._ | [ ] |
| 3 | 0.6426 | Guerra de Independencia de México — _Ecatepec el 22 de diciembre de 1815. Durante esta época, el movimiento independentista no solo reali..._ | [ ] |
| 4 | 0.6426 | Independencia de México — _Ecatepec el 22 de diciembre de 1815. Durante esta época, el movimiento independentista no solo reali..._ | [ ] |
| 5 | 0.6174 | Historia de México — _gobierno de la metrópoli implementó en el Imperio español, sumado a la centralización del poder polí..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El Virreinato jugó un papel importante en la Independencia de México debido a que el gobierno de la metrópoli implementó medidas que restaron facultades autónomas a las autoridades civiles y eclesiásticas en Nueva España. | [ ] |
| 2 | El aumento de tributos causó un déficit en las finanzas de cada territorio, restringiendo su capacidad de desarrollarse. | [ ] |
| 3 | La ocupación de España por Napoleón Bonaparte fue el momento idóneo para que las ideas de independencia florecieran. | [ ] |
| 4 | Fuentes: Fragmento 5, Fragmento 1, Fragmento 2, Fragmento 3, Fragmento 4. | [ ] |

---

## M1 — ¿Qué civilizaciones existían antes de los españoles y cuál dominaba en 1519?

**Tipo:** multihop
**Puntos clave esperados:** Olmecas; mayas; teotihuacanos; aztecas; el Imperio Azteca dominaba en 1519
**Tiempos:** retrieval=0.024s · generación=5.736s · total=5.760s

**Respuesta del sistema:**
> Antes de la llegada de los españoles, existían civilizaciones como los mexicas, acolhuas y tepanecas. La Triple Alianza, comúnmente llamada Imperio mexica, dominaba en 1519.

Fuentes:
* Fragmento 5: Imperio azteca
* Fragmento 1: Conquista de México

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.6539 | Conquista de México — _de estos acontecimientos, que modificaron drásticamente la geopolítica mundial en los albores del si..._ | [ ] |
| 2 | 0.6536 | Virreinato de Nueva España — _posible distinguir varios periodos. En el primero, la literatura está vinculada con el momento histó..._ | [ ] |
| 3 | 0.6529 | Historia de México — _contaban con ritos, ceremonias y un código jurídico y económico propio.​ Sin embargo, este proceso d..._ | [ ] |
| 4 | 0.6367 | Virreinato de Nueva España — _siglo XVII, cuando fueron casi exterminadas. En ese mismo siglo, la labor de los frailes llegados a..._ | [ ] |
| 5 | 0.6365 | Imperio azteca — _lenguaje artístico comunicó historias, deidades y ritos en los que coincidieron ancestrales mitos y..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Antes de la llegada de los españoles, existían civilizaciones como los mexicas, acolhuas y tepanecas. | [ ] |
| 2 | La Triple Alianza, comúnmente llamada Imperio mexica, dominaba en 1519. | [ ] |
| 3 | Fuentes:
* Fragmento 5: Imperio azteca
* Fragmento 1: Conquista de México | [ ] |

---

## M2 — ¿Cómo influyeron las reformas de Juárez en la Revolución décadas después?

**Tipo:** multihop
**Puntos clave esperados:** Constitución de 1857; separación Iglesia-Estado; antecedente liberal que Díaz traicionó
**Tiempos:** retrieval=0.021s · generación=4.125s · total=4.147s

**Respuesta del sistema:**
> No encontré esta información en el corpus.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.7539 | Historia de México — _cuando Juárez retornó triunfal como presidente a la Ciudad de México en julio de 1867, la mejor form..._ | [ ] |
| 2 | 0.7352 | Benito Juárez — _vez en Ciudad de México los recibió una muchedumbre así como miembros del gabinete y del gobierno, l..._ | [ ] |
| 3 | 0.6982 | Guerra de Reforma — _y lograr la pacificación del país, por lo que sobrevendría la segunda intervención francesa en Méxic..._ | [ ] |
| 4 | 0.6863 | Revolución mexicana — _# Revolución mexicana La Revolución mexicana fue un conflicto armado en México que se inició el 20 d..._ | [ ] |
| 5 | 0.6833 | Historia de México — _movimientos de las tropas francesas para el funcionamiento del imperio.​ Maximiliano solicitó revisa..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---

## T1 — ¿Quién es el presidente actual de México?

**Tipo:** trampa  (pregunta trampa)
**Tiempos:** retrieval=0.020s · generación=4.955s · total=4.974s

**Respuesta del sistema:**
> El presidente de México desde el 1 de diciembre de 2018 hasta el 30 de septiembre de 2024.

Fuentes: Fragmento 3

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.6917 | Revolución mexicana — _Carranza jefe del «Ejército Constitucionalista» y se le daba la facultad de ocupar interinamente la..._ | [ ] |
| 2 | 0.6749 | Benito Juárez — _# Benito Juárez Benito Pablo Juárez García (San Pablo Guelatao, Intendencia de Oaxaca; 21 de marzo d..._ | [ ] |
| 3 | 0.6722 | Historia de México — _Presidente de México desde el 1 de diciembre de 2018 hasta el 30 de septiembre de 2024. Durante su g..._ | [ ] |
| 4 | 0.6651 | Benito Juárez — _como un símbolo sagrado.​​​ A la ceremonia de iniciación de Juárez concurrieron distinguidos masones..._ | [ ] |
| 5 | 0.6642 | Benito Juárez — _él se presentaría a las elecciones. Porfirio Díaz reclamaba también elecciones. Juárez instruyó a Se..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El presidente de México desde el 1 de diciembre de 2018 hasta el 30 de septiembre de 2024. | [ ] |
| 2 | Fuentes: Fragmento 3 | [ ] |

---

## T2 — ¿Cuál es el PIB actual de México?

**Tipo:** trampa  (pregunta trampa)
**Tiempos:** retrieval=0.022s · generación=4.471s · total=4.494s

**Respuesta del sistema:**
> No encontré esta información en el corpus.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.6443 | Historia de México — _Presidente de México desde el 1 de diciembre de 2018 hasta el 30 de septiembre de 2024. Durante su g..._ | [ ] |
| 2 | 0.6162 | Guerra de Independencia de México — _# Independencia de México La independencia de México fue la consecuencia de un proceso político y so..._ | [ ] |
| 3 | 0.6162 | Independencia de México — _# Independencia de México La independencia de México fue la consecuencia de un proceso político y so..._ | [ ] |
| 4 | 0.5930 | Guerra de Independencia de México — _de México: legado y pasado reciente. México: Pearson. ISBN 978-970-26-0523-2. Florescano, Enrique (2..._ | [ ] |
| 5 | 0.5930 | Independencia de México — _de México: legado y pasado reciente. México: Pearson. ISBN 978-970-26-0523-2. Florescano, Enrique (2..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---

## T3 — ¿Qué equipos jugaron la final del fútbol mexicano en 2024?

**Tipo:** trampa  (pregunta trampa)
**Tiempos:** retrieval=0.022s · generación=4.142s · total=4.163s

**Respuesta del sistema:**
> No encontré esta información en el corpus.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta._

| Rank | Score | Fuente | Relevante |
|------|-------|--------|-----------|
| 1 | 0.5793 | Guerra de Independencia de México — _# Independencia de México La independencia de México fue la consecuencia de un proceso político y so..._ | [ ] |
| 2 | 0.5793 | Independencia de México — _# Independencia de México La independencia de México fue la consecuencia de un proceso político y so..._ | [ ] |
| 3 | 0.5759 | Historia de México — _México para calmar el golpe de Estado contra su vicepresidente, el ejército norteamericano ya estaba..._ | [ ] |
| 4 | 0.5628 | Revolución mexicana — _# Revolución mexicana La Revolución mexicana fue un conflicto armado en México que se inició el 20 d..._ | [ ] |
| 5 | 0.5598 | Pancho Villa — _1966 su nombre fue inscrito en letras de oro en el muro de honor de la Cámara de Diputados en la Ciu..._ | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---
