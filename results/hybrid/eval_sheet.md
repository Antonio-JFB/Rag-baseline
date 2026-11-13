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
**Tiempos:** retrieval=8.117s · generación=92.795s · total=100.911s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Según el Fragmento 1, la ciudad cayó el 21 de julio de 1521. El Fragmento 3 indica que el 13 de agosto de 1521, heroicamente defendido por Cuauhtémoc, cayó Tlatelolco en poder de Hernán Cortés.
>
> Fuentes:
> * Fragmento 1 | Fuente: Historia de México
> * Fragmento 3 | Fuente: Moctezuma II

_Ayuda para Recall: 105 chunks distintos del corpus mencionan al menos un punto clave (24 mencionan 2 o más); detalle con `python evaluation/candidates.py --question F1`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.0082 | Historia de México — _Lago de Texcoco y sitiar la ciudad. La inestabilidad del imperio apresuró los planes y el 28 de abril de 1521 inició el asedio. Ganada la batalla, comenzó el sitio de Tenochtitlán destruyendo sus puentes y acueductos dejando completamente incomunicada la isla en mayo de 1521, lo que fue devastador e..._ | 1521, Cuauhtémoc, tlaxcaltecas | [ ] |
| 2 | 0.0082 | Moctezuma II — _cabello largo, muy llano, sentado con mucha mesura». Actualmente la mayoría de investigadores opinan que Ce Ácatl Topiltzin fue un personaje histórico que habrá vivido en Tollan-Xicocotitlan o en Teotihuacán, aunque es tomado por hecho que la historia contada por las fuentes de los siglos XVI y XVII..._ | ninguno | [ ] |
| 3 | 0.0081 | Moctezuma II — _había existido por años entre los mexicas y tarascos. Llegada a Tenochtitlán El día 8 de noviembre de 1519, después de una ceremonia de bienvenida que duró más de una hora, los españoles finalmente llegaron a Tenochtitlán, donde conocieron a Moctezuma y también a su hermano y futuro huey tlatoani Cu..._ | ninguno | [ ] |
| 4 | 0.0081 | Hernán Cortés — _a la salida de Tenochtitlán. Ya no les faltaba mucho para completar la retirada cuando fueron descubiertos por una anciana, que dio la alarma, y en unos momentos, miles de guerreros mexicas atacaron en tromba a los españoles; les acosaron a lo largo de la calzada, mientras otros atacaban desde sus c..._ | tlaxcaltecas | [ ] |
| 5 | 0.0079 | Tenochtitlan — _# Tenochtitlan Tenochtitlan puede hacer referencia a: México-Tenochtitlan, ciudad principal de los mexicas. Municipio de Tenochtitlán, municipio del estado de Veracruz. Tenochtitlán (Veracruz), localidad del estado de Veracruz, cabecera del municipio anterior. San Miguel Tenochtitlán, localidad del ..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Según el Fragmento 1, la ciudad cayó el 21 de julio de 1521. | [ ] |
| 2 | El Fragmento 3 indica que el 13 de agosto de 1521, heroicamente defendido por Cuauhtémoc, cayó Tlatelolco en poder de Hernán Cortés. | [ ] |

---

## F2 — ¿Quién dio el Grito de Independencia?

**Tipo:** factual
**Puntos clave esperados:** Miguel Hidalgo; Dolores Hidalgo; 16 septiembre 1810
**Tiempos:** retrieval=0.021s · generación=5.396s · total=5.416s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Miguel Hidalgo convocó al pueblo de Dolores a sublevarse en contra de las autoridades españolas el 16 de septiembre de 1810, lo que se conoce como el Grito de Dolores.
>
> Fuentes:
> * Fragmento 3: Guerra de Independencia de México
> * Fragmento 5: Independencia de México

_Ayuda para Recall: 53 chunks distintos del corpus mencionan al menos un punto clave (22 mencionan 2 o más); detalle con `python evaluation/candidates.py --question F2`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.0145 | Guerra de Independencia de México — _hizo leer a su secretario Juan Nepomuceno Rosáins los Sentimientos de la Nación. Este documento declaraba la independencia de la nación, la soberanía popular, la religión católica como única, la supresión de obvenciones, la división de poderes, la igualdad ante la ley, la abolición de las castas, la..._ | Miguel Hidalgo | [ ] |
| 2 | 0.0143 | Independencia de México **(copia exacta del rank 1: cuenta una sola vez)** — _hizo leer a su secretario Juan Nepomuceno Rosáins los Sentimientos de la Nación. Este documento declaraba la independencia de la nación, la soberanía popular, la religión católica como única, la supresión de obvenciones, la división de poderes, la igualdad ante la ley, la abolición de las castas, la..._ | Miguel Hidalgo | [ ] |
| 3 | 0.0082 | Guerra de Independencia de México — _presentó ante el pleno, una memoria titulada Exposición de motivos de la guerra de independencia, en la que protestaba contra las autoridades virreinales por la situación de marginación y pobreza en que se encontraban los indígenas y mestizos novohispanos, y mostraba las posibles soluciones. Entre s..._ | Miguel Hidalgo, Dolores Hidalgo, 16 septiembre 1810 | [ ] |
| 4 | 0.0082 | Virreinato de Nueva España — _sublevó y proclamó a Fernando de Borbón, como rey de España. Napoleón a través de las abdicaciones de Bayona entregó la corona de España a su hermano José Bonaparte y dio inicio a la guerra de la Independencia Española. Sin los fondos enviados desde América, los gobiernos de España habrían colapsado..._ | Miguel Hidalgo, Dolores Hidalgo | [ ] |
| 5 | 0.0081 | Independencia de México **(copia exacta del rank 3: cuenta una sola vez)** — _presentó ante el pleno, una memoria titulada Exposición de motivos de la guerra de independencia, en la que protestaba contra las autoridades virreinales por la situación de marginación y pobreza en que se encontraban los indígenas y mestizos novohispanos, y mostraba las posibles soluciones. Entre s..._ | Miguel Hidalgo, Dolores Hidalgo, 16 septiembre 1810 | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Miguel Hidalgo convocó al pueblo de Dolores a sublevarse en contra de las autoridades españolas el 16 de septiembre de 1810, lo que se conoce como el Grito de Dolores. | [ ] |

---

## F3 — ¿Cuándo comenzó el Porfiriato?

**Tipo:** factual
**Puntos clave esperados:** 1876; Porfirio Díaz; reelección continua
**Tiempos:** retrieval=0.024s · generación=5.281s · total=5.305s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> El Porfiriato comenzó el 28 de noviembre de 1876.
>
> Fuentes:
> * Fragmento 1 | Fuente: Porfiriato

_Ayuda para Recall: 68 chunks distintos del corpus mencionan al menos un punto clave (12 mencionan 2 o más); detalle con `python evaluation/candidates.py --question F3`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.0158 | Porfiriato — _# Porfiriato El porfiriato o porfirismo fue un período de la historia de México en el que el gobierno estuvo bajo el control (total o mayoritario) del militar, político y dictador Porfirio Díaz, entre el 28 de noviembre de 1876 y el 27 de mayo de 1911. En el porfiriato la política se aplicó de tal m..._ | 1876, Porfirio Díaz | [ ] |
| 2 | 0.0145 | Historia de México — _la Compañía El Águila de extracción petrolera y refinamiento que iniciaría sus labores oficiales hasta 1908. Fue el 8 de abril de 1902 cuando también se puso fin a la guerra yaqui con la masacre de Mazatlán. Un grupo de yaquis hartos de los maltratos en las haciendas, huyeron por el cañón de Uvalama..._ | ninguno | [ ] |
| 3 | 0.0082 | Historia de México — _ascenso de Porfirio Díaz al poder en 1876 empezó un periodo conocido como el Porfiriato, mismo que duró hasta 1911 con su exilio. En 1910 inició la Revolución Mexicana, un periodo de grandes conflictos entre múltiples facciones y con distintos principios durante el transcurso de la misma: su fecha d..._ | 1876, Porfirio Díaz | [ ] |
| 4 | 0.0082 | Revolución mexicana — _las diferencias entre las facciones que habían luchado contra Huerta, lo que desencadenó nuevos conflictos. Carranza, jefe de la Revolución, de acuerdo con el Plan de Guadalupe, convocó a todas las fuerzas a la Convención de Aguascalientes para nombrar un líder único. En esa reunión Eulalio Gutiérre..._ | 1876, Porfirio Díaz | [ ] |
| 5 | 0.0081 | Porfiriato — _fuese por medio de sobornos o bien por torturas y desapariciones. Las represiones que Díaz ejercía sobre las personas que exigían una mejor calidad de vida fueron justificadas con una doctrina filosófica: el Positivismo, la cual proponía "Orden y progreso". Así, el "Orden" lo mantenía con represione..._ | Porfirio Díaz | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El Porfiriato comenzó el 28 de noviembre de 1876. | [ ] |

---

## F4 — ¿Qué civilización construyó Teotihuacán?

**Tipo:** factual
**Puntos clave esperados:** Cultura teotihuacana; nombre propio desconocido; periodo clásico
**Tiempos:** retrieval=0.023s · generación=6.861s · total=6.885s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Según los fragmentos proporcionados, los orígenes de la ciudad de Teotihuacán todavía son objeto de investigación entre los especialistas. Se sabe que los mexicas excavaron la ciudad en busca de objetos preciosos y que los nahuas pensaban que Teotihuacán fue construida por los quinametzin, una raza de gigantes. Sin embargo, la identidad de los fundadores de Teotihuacán es desconocida.
>
> Fuentes: Fragmento 2, Fragmento 3, Fragmento 5.

_Ayuda para Recall: 84 chunks distintos del corpus mencionan al menos un punto clave (2 mencionan 2 o más); detalle con `python evaluation/candidates.py --question F4`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.0151 | Cultura teotihuacana — _de arqueólogos donde se estableció que la Tollan mitológica fue Tollan-Xicocotitlan, y es compartida por Stuart, Uriarte, y Duverger. René Millon, uno de los más reconocidos especialistas en el tema de Teotihuacán, opina que efectivamente Teotihuacán es la legendaria Tollan, pero no acepta que este ..._ | nombre propio desconocido | [ ] |
| 2 | 0.0143 | Cultura teotihuacana — _sido construido por dioses. Pero no sabemos casi nada de los hombres que poblaron esta ciudad en el siglo II de nuestra era. La ciudad contaba con más de 100.000 habitantes en su apogeo. Teotihuacán fue destruida en el siglo VII, sin que se sepan las razones. La ciudad estaba desprovista de fortific..._ | ninguno | [ ] |
| 3 | 0.0141 | Cultura teotihuacana — _# Teotihuacán Teotihuacan o Teotihuacán (del náhuatl: Teōtīhuacān o Teotiwakan ‘lugar donde los hombres se convierten en dioses’ [‘lugar de la apoteosis’]; ‘lugar de los dioses’) (pronunciación: /teoːtiːˈwakãː/; ), y, según nuevas investigaciones, también pudo haber sido conocida como Teohuacan (del..._ | ninguno | [ ] |
| 4 | 0.0134 | Cultura teotihuacana — _Carr, D. C. (2005). Los otomíes: cultura, lengua y escritura (Vol. I, 2 vols.). Tesis de doctorado. Zamora: COLMICH. 06/07/2022, http://dx.doi.org/10.13140/2.1.5100.1280. Enlaces externos Wikimedia Commons alberga una categoría multimedia sobre Teotihuacán. Wikiviajes alberga guías de viajes de o so..._ | Cultura teotihuacana | [ ] |
| 5 | 0.0128 | Cultura teotihuacana — _textos mayas es efectivamente Teotihuacán. Esta hipótesis podría ser reforzada por el descubrimiento de varias representaciones del glifo puh en la pintura mural del conjunto residencial de Tepantitla, dentro de Teotihuacán. Aunque se identificó originalmente a esta Tollan legendaria con Tollan-Xico..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Según los fragmentos proporcionados, los orígenes de la ciudad de Teotihuacán todavía son objeto de investigación entre los especialistas. | [ ] |
| 2 | Se sabe que los mexicas excavaron la ciudad en busca de objetos preciosos y que los nahuas pensaban que Teotihuacán fue construida por los quinametzin, una raza de gigantes. | [ ] |
| 3 | Sin embargo, la identidad de los fundadores de Teotihuacán es desconocida. | [ ] |

---

## F5 — ¿Quién fue el último emperador azteca?

**Tipo:** factual
**Puntos clave esperados:** Cuauhtémoc; sobrino de Moctezuma II; capturado 1521
**Tiempos:** retrieval=0.021s · generación=6.716s · total=6.737s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> El último emperador azteca fue Cuitláhuac, hermano de Moctezuma, quien fue elegido tlatoani de Tenochtitlan tras la muerte de este último en junio de 1520.
>
> Fuentes:
> * Fragmento 4: "Cuitláhuac, hermano de Moctezuma y señor de Iztapalapa fue elegido tlatoani de Tenochtitlan en respuesta a la Matanza del Templo Mayor."

_Ayuda para Recall: 36 chunks distintos del corpus mencionan al menos un punto clave (3 mencionan 2 o más); detalle con `python evaluation/candidates.py --question F5`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.0159 | Imperio azteca — _# Imperio azteca El Imperio mexica o Triple Alianza (del náhuatl: Exkan Tlahtoloyan o Ēxcān Tlahtōlōyān ‘Los tres lugares donde se dan órdenes’), llamado también Imperio azteca y —con más precisión— Imperio tenochca, fue un imperio organizado en una confederación compleja, multiétnica y flexible de ..._ | ninguno | [ ] |
| 2 | 0.0149 | Historia de México — _de Tenochtitlán, Chimalpopoca, permaneció en silencio, lo que propició un descontento entre los mexicas. Fue el sacerdote Tlacaelél quien, desde las sombras, convenció al sacerdote Izcóatl de realizar un golpe de Estado en Tenochtitlán, logrando imponerse como gobernante el 16 de octubre de 1427. Aq..._ | ninguno | [ ] |
| 3 | 0.0146 | Imperio azteca — _Guerrero y el Soconusco. El fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españoles —en alianza con los tlaxcaltecas y totonacas, entre otros pueblos indígenas— derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco. Etimología, nombres y definiciones La palabra «azteca» ..._ | ninguno | [ ] |
| 4 | 0.0143 | Virreinato de Nueva España — _con el cacique o gobernador maya Tabscoob y escuchó acerca de una ciudad poderosa, capital del imperio más grande de Mesoamérica, la Gran Tenochtitlan, culminando su viaje en Veracruz. En 1519, bajo la designación de Diego Velázquez de Cuéllar, gobernador de Cuba (llamada entonces Fernandina, en hon..._ | ninguno | [ ] |
| 5 | 0.0141 | Historia de México — _completo. El siguiente líder al trono fue Tízoc en el año 1481, quien inició una campaña para atrapar cautivos para su ceremonia de investidura en Itzmiquilpan y Meztitlán. Esto supuso el comienzo del expansionismo azteca pues ordenó ataques contra tarascos, matlatzincas, chontales y cuitlatecos. Co..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El último emperador azteca fue Cuitláhuac, hermano de Moctezuma, quien fue elegido tlatoani de Tenochtitlan tras la muerte de este último en junio de 1520. | [ ] |

---

## C1 — ¿Cuáles fueron las causas de la Revolución Mexicana?

**Tipo:** causalidad
**Puntos clave esperados:** Reelección de Díaz; desigualdad agraria; Plan de San Luis; crisis de 1907; Madero
**Tiempos:** retrieval=0.027s · generación=7.781s · total=7.809s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Las causas de la Revolución Mexicana se remontan a la situación de México bajo la dictadura del porfiriato, donde Porfirio Díaz Mori ejerció el poder de manera dictatorial desde 1876 hasta 1911. Durante este periodo, México experimentó crecimiento económico y estabilidad política, pero a un alto costo social para los estratos menos favorecidos de la sociedad y la oposición política. También se mencionan varias crisis en diversas esferas de la vida nacional durante la primera década del siglo XX, que reflejaban el creciente descontento con el porfiriato.
>
> Fuentes: Fragmento 1, Fragmento 3.

_Ayuda para Recall: 124 chunks distintos del corpus mencionan al menos un punto clave (27 mencionan 2 o más); detalle con `python evaluation/candidates.py --question C1`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.0151 | Revolución mexicana — _# Revolución mexicana La Revolución mexicana fue un conflicto armado en México que se inició el 20 de noviembre de 1910 y terminó el 5 de febrero de 1917. Los antecedentes del conflicto se remontan a la situación de México bajo la dictadura conocida como el porfiriato. Porfirio Díaz Mori ejerció el ..._ | Reelección de Díaz, Madero | [ ] |
| 2 | 0.0151 | Revolución mexicana — _el cual se ubica en el paseo de la Reforma. La «primera piedra» fue colocada por el presidente Felipe Calderón Hinojosa. La Revolución mexicana en la cultura Novelas Existe una serie de novelas que reproducen este movimiento suscitado entre 1910 y 1917, las cuales, mediante cuadros sucesivos o fotog..._ | Plan de San Luis, Madero | [ ] |
| 3 | 0.0146 | Historia de México — _ascenso de Porfirio Díaz al poder en 1876 empezó un periodo conocido como el Porfiriato, mismo que duró hasta 1911 con su exilio. En 1910 inició la Revolución Mexicana, un periodo de grandes conflictos entre múltiples facciones y con distintos principios durante el transcurso de la misma: su fecha d..._ | ninguno | [ ] |
| 4 | 0.0140 | Emiliano Zapata — _como presidente y se reconocía a Pascual Orozco como jefe legítimo de la Revolución mexicana. Este documento sería transformado después del levantamiento de Victoriano Huerta por los diferentes ideología (muchos de ellos influenciados por Ricardo Flores Magón), y posteriormente defendido por Zapata ..._ | Madero | [ ] |
| 5 | 0.0127 | Historia de México — _contaban con ritos, ceremonias y un código jurídico y económico propio. Sin embargo, este proceso de creación de la burguesía mesoamericana fue interrumpido por la conquista. A partir de la institución del Virreinato, entre 1521 y 1535 en distintas zonas de México, empezaría una Edad Media, mezcla d..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Las causas de la Revolución Mexicana se remontan a la situación de México bajo la dictadura del porfiriato, donde Porfirio Díaz Mori ejerció el poder de manera dictatorial desde 1876 hasta 1911. | [ ] |
| 2 | Durante este periodo, México experimentó crecimiento económico y estabilidad política, pero a un alto costo social para los estratos menos favorecidos de la sociedad y la oposición política. | [ ] |
| 3 | También se mencionan varias crisis en diversas esferas de la vida nacional durante la primera década del siglo XX, que reflejaban el creciente descontento con el porfiriato. | [ ] |

---

## C2 — ¿Por qué cayó el Imperio Azteca?

**Tipo:** causalidad
**Puntos clave esperados:** Alianzas con tlaxcaltecas; enfermedades; superioridad militar española; muerte de Moctezuma
**Tiempos:** retrieval=0.021s · generación=5.856s · total=5.877s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> El Imperio azteca cayó el 13 de agosto de 1521, cuando los españoles —en alianza con los tlaxcaltecas y totonacas, entre otros pueblos indígenas— derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco.
>
> Fuentes:
> * Fragmento 1
> * Fragmento 2
> * Fragmento 3

_Ayuda para Recall: 73 chunks distintos del corpus mencionan al menos un punto clave (1 mencionan 2 o más); detalle con `python evaluation/candidates.py --question C2`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.0160 | Imperio azteca — _# Imperio azteca El Imperio mexica o Triple Alianza (del náhuatl: Exkan Tlahtoloyan o Ēxcān Tlahtōlōyān ‘Los tres lugares donde se dan órdenes’), llamado también Imperio azteca y —con más precisión— Imperio tenochca, fue un imperio organizado en una confederación compleja, multiétnica y flexible de ..._ | superioridad militar española | [ ] |
| 2 | 0.0157 | Imperio azteca — _Guerrero y el Soconusco. El fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españoles —en alianza con los tlaxcaltecas y totonacas, entre otros pueblos indígenas— derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco. Etimología, nombres y definiciones La palabra «azteca» ..._ | Alianzas con tlaxcaltecas | [ ] |
| 3 | 0.0144 | Historia de México — _Lago de Texcoco y sitiar la ciudad. La inestabilidad del imperio apresuró los planes y el 28 de abril de 1521 inició el asedio. Ganada la batalla, comenzó el sitio de Tenochtitlán destruyendo sus puentes y acueductos dejando completamente incomunicada la isla en mayo de 1521, lo que fue devastador e..._ | ninguno | [ ] |
| 4 | 0.0081 | Hernán Cortés — _contenido astral). Estos regalos, en lugar de disuadir a Cortés, le animaron a continuar y conquistar México. Los aztecas creían en un mito de origen tolteca, según el cual el mundo en que vivían debía desaparecer. El dios Quetzalcóatl, una serpiente emplumada, se había marchado con cincuenta y tres..._ | ninguno | [ ] |
| 5 | 0.0081 | Historia de México — _de Tenochtitlán, Chimalpopoca, permaneció en silencio, lo que propició un descontento entre los mexicas. Fue el sacerdote Tlacaelél quien, desde las sombras, convenció al sacerdote Izcóatl de realizar un golpe de Estado en Tenochtitlán, logrando imponerse como gobernante el 16 de octubre de 1427. Aq..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El Imperio azteca cayó el 13 de agosto de 1521, cuando los españoles —en alianza con los tlaxcaltecas y totonacas, entre otros pueblos indígenas— derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco. | [ ] |

---

## C3 — ¿Qué provocó la Guerra de Reforma?

**Tipo:** causalidad
**Puntos clave esperados:** Constitución de 1857; liberales vs conservadores; Ley Juárez; Ley Lerdo
**Tiempos:** retrieval=0.021s · generación=5.296s · total=5.317s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> La Guerra de Reforma, también conocida como la guerra de los tres años, fue provocada por la promulgación de la Constitución de 1857 y en especial de las llamadas Leyes de Reforma.
>
> Fuentes: Fragmento 1

_Ayuda para Recall: 143 chunks distintos del corpus mencionan al menos un punto clave (55 mencionan 2 o más); detalle con `python evaluation/candidates.py --question C3`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.0161 | Guerra de Reforma — _# Guerra de Reforma La Guerra de Reforma, también conocida como la guerra de los tres años, fue una guerra civil que aconteció en México desde el 17 de diciembre de 1857 al 11 de enero de 1861, como consecuencia de la promulgación de la Constitución de 1857 y en especial de las llamadas Leyes de Ref..._ | Constitución de 1857, liberales vs conservadores, Ley Juárez | [ ] |
| 2 | 0.0141 | Moctezuma II — _que tenía un profundo odio hacia los mexicas. La intención de las guerras floridas ha sido interpretada a lo largo de la mayoría de los años como guerras puramente religiosas, con el único fin de facilitar la captura de prisioneros de guerra para sacrificio humano. Dicha interpretación es apoyada po..._ | ninguno | [ ] |
| 3 | 0.0082 | Benito Juárez — _y Pepito, pero hay quienes solamente piensan en bienes materiales. ¡Vea estos precios! ¡Hasta 4 veces más caro está el cuarterón de maíz! y créame no se si por ser indio o por qué, pero no los entiendo, no entiendo a quienes se quieren enriquecer de la miseria, de las masas, del dolor y del sufrimie..._ | Ley Juárez | [ ] |
| 4 | 0.0081 | Revolución mexicana — _Tras el triunfo de la revolución constitucionalista en agosto de 1914 y el posterior exilio de Victoriano Huerta, Obregón reabrió la COM. Sin embargo, la lucha entre las facciones carrancistas y convencionistas causó debates sobre el camino que debía de seguir la organización. Los argumentos del pin..._ | ninguno | [ ] |
| 5 | 0.0081 | Benito Juárez — _gobierno conservador,como consecuencia de la guerra de reforma, el puerto de Veracruz fue invadido el 15 de diciembre de 1861 por una fuerza española de 6000 hombres que no encontró resistencia. El 9 de enero de 1862, se les unieron 3000 franceses y 800 ingleses. Los invasores ingleses y españoles s..._ | Ley Juárez | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | La Guerra de Reforma, también conocida como la guerra de los tres años, fue provocada por la promulgación de la Constitución de 1857 y en especial de las llamadas Leyes de Reforma. | [ ] |

---

## C4 — ¿Por qué terminó el Porfiriato?

**Tipo:** causalidad
**Puntos clave esperados:** Revolución Mexicana; renuncia de Díaz en 1911; Plan de San Luis; descontento social
**Tiempos:** retrieval=0.025s · generación=6.393s · total=6.418s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> El Porfiriato terminó el 27 de mayo de 1911, cuando Porfirio Díaz renunció a la presidencia y salió rumbo a Francia en exilio. Esto ocurrió meses después de haber estallado la Revolución.
>
> Fuentes:
> * Fragmento 1: Porfiriato
> * Fragmento 3: Historia de México

_Ayuda para Recall: 129 chunks distintos del corpus mencionan al menos un punto clave (22 mencionan 2 o más); detalle con `python evaluation/candidates.py --question C4`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.0155 | Porfiriato — _# Porfiriato El porfiriato o porfirismo fue un período de la historia de México en el que el gobierno estuvo bajo el control (total o mayoritario) del militar, político y dictador Porfirio Díaz, entre el 28 de noviembre de 1876 y el 27 de mayo de 1911. En el porfiriato la política se aplicó de tal m..._ | renuncia de Díaz en 1911 | [ ] |
| 2 | 0.0082 | Revolución mexicana — _# Revolución mexicana La Revolución mexicana fue un conflicto armado en México que se inició el 20 de noviembre de 1910 y terminó el 5 de febrero de 1917. Los antecedentes del conflicto se remontan a la situación de México bajo la dictadura conocida como el porfiriato. Porfirio Díaz Mori ejerció el ..._ | Revolución Mexicana, renuncia de Díaz en 1911, descontento social | [ ] |
| 3 | 0.0081 | Historia de México — _ascenso de Porfirio Díaz al poder en 1876 empezó un periodo conocido como el Porfiriato, mismo que duró hasta 1911 con su exilio. En 1910 inició la Revolución Mexicana, un periodo de grandes conflictos entre múltiples facciones y con distintos principios durante el transcurso de la misma: su fecha d..._ | Revolución Mexicana, renuncia de Díaz en 1911 | [ ] |
| 4 | 0.0081 | Porfiriato — _fuese por medio de sobornos o bien por torturas y desapariciones. Las represiones que Díaz ejercía sobre las personas que exigían una mejor calidad de vida fueron justificadas con una doctrina filosófica: el Positivismo, la cual proponía "Orden y progreso". Así, el "Orden" lo mantenía con represione..._ | Revolución Mexicana | [ ] |
| 5 | 0.0079 | Historia de México — _abril, cuando Obregón aprovechó las debilidades de Villa retirándolos hasta el norte. Desconectadas las fuerzas villistas de sus aliados zapatistas al sur, iniciaron un repliegue que los redujo a una guerrilla regional en Chihuahua. Aquella fue la Batalla de Celaya. Frente a un gobierno inestable, l..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El Porfiriato terminó el 27 de mayo de 1911, cuando Porfirio Díaz renunció a la presidencia y salió rumbo a Francia en exilio. | [ ] |
| 2 | Esto ocurrió meses después de haber estallado la Revolución. | [ ] |

---

## V1 — ¿En qué se diferencian los mayas y los olmecas?

**Tipo:** comparativa
**Puntos clave esperados:** Olmecas: civilización madre, cabezas colosales, zona costera; Mayas: escritura, calendario, ciudades-estado
**Tiempos:** retrieval=0.033s · generación=8.188s · total=8.221s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Los mayas desarrollaron su primera civilización en el período Preclásico, y la ocupación maya de Aguada Fénix en México ha sido fechada en el 1,000 a. C., marcando el paso de la civilización maya del nomadismo a un estilo de vida sedentario. Los olmecas surgieron alrededor de los años 1200 a. n. e. y 500 a. n. e. en la región costera del Golfo de México (actualmente Veracruz y Tabasco), marcando la tendencia del resto de los pueblos prehispánicos en cuanto a organización, economía, desarrollo, creencias, etc.
>
> Fuentes: Fragmento 2, Fragmento 3.

_Ayuda para Recall: 192 chunks distintos del corpus mencionan al menos un punto clave (40 mencionan 2 o más); detalle con `python evaluation/candidates.py --question V1`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.0156 | Cultura olmeca — _# Cultura olmeca La cultura olmeca fue una civilización que se desarrolló durante el periodo preclásico de Mesoamérica, en parte de los territorios actuales de México. Aunque se han encontrado vestigios de su presencia en amplias zonas de Mesoamérica, se considera que el área cultural olmeca —zona m..._ | Olmecas, civilización madre | [ ] |
| 2 | 0.0152 | Historia de México — _de ciudades, poblaciones y demarcaciones diferentes que convivieron o provocaron conflictos entre ellas e incluso dentro de ellas. Para entender la historia del México Prehispánico es necesario dejar de lado la diferenciación cultural como punto predominante para su definición. Preclásico Del 2500 a..._ | Olmecas, civilización madre, Mayas, ciudades-estado | [ ] |
| 3 | 0.0131 | Civilización maya — _como el valle de Guatemala y Quetzaltenango en el altiplano del sur, dominado por un cinturón de conos volcánicos que corre paralela a la costa del Pacífico. El altiplano se extiende hacia el norte en Verapaz, y desciende gradualmente hacia el este. Historia Antecedentes La historia de la civilizaci..._ | Mayas, ciudades-estado | [ ] |
| 4 | 0.0082 | Imperio azteca — _en la asimilación de la herencia popular de la tradición nahua. Los aztecas intentaron combinar dos sistemas religiosos en conflicto: la tradición de los guerreros y cazadores chichimecas y la herencia de los agricultores sedentarios. Los chichimecas, un pueblo de guerreros y cazadores nómadas, ador..._ | ninguno | [ ] |
| 5 | 0.0082 | Cultura olmeca — _Guatemala (Takalik Abaj), Belice, El Salvador, Honduras y Nicaragua. Economía La economía de los olmecas estaba basada principalmente en los productos agrícolas, con los que comerciaban tanto entre ellos como con otros pueblos vecinos, sobre todo con los pueblos nómadas, principalmente los olmecas r..._ | Olmecas | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Los mayas desarrollaron su primera civilización en el período Preclásico, y la ocupación maya de Aguada Fénix en México ha sido fechada en el 1,000 a. C., marcando el paso de la civilización maya del nomadismo a un estilo de vida sedentario. | [ ] |
| 2 | Los olmecas surgieron alrededor de los años 1200 a. n. e. y 500 a. n. e. en la región costera del Golfo de México (actualmente Veracruz y Tabasco), marcando la tendencia del resto de los pueblos prehispánicos en cuanto a organización, economía, desarrollo, creencias, etc. | [ ] |

---

## V2 — ¿Qué diferencias hay entre Zapata y Villa?

**Tipo:** comparativa
**Puntos clave esperados:** Zapata: agrarismo, sur, Plan de Ayala; Villa: norte, División del Norte, carácter militar
**Tiempos:** retrieval=0.023s · generación=7.739s · total=7.763s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Según los fragmentos proporcionados, las diferencias entre Zapata y Villa incluyen:
>
> *   Villa aceptó el Plan de Ayala, a excepción de las acusaciones contra Francisco I. Madero, a quien consideraba su redentor. Zapata, por otro lado, se opuso a Madero y lo desconocía.
> *   Aunque se aliaron militarmente, nunca hubo una verdadera colaboración entre ellos debido a que Zapata quería mantener aislada su región y se mantenía a la defensiva.
> *   Después de la renuncia de Eulalio Gutiérrez, Villa intentó tomar Celaya, mientras que Zapata se mantenía a la defensiva.
>
> Fuentes: Fragmento 2, Fragmento 5.

_Ayuda para Recall: 422 chunks distintos del corpus mencionan al menos un punto clave (96 mencionan 2 o más); detalle con `python evaluation/candidates.py --question V2`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.0159 | Emiliano Zapata — _traicionado la revolución. El gobierno federal reiteró su decisión de imponer el orden por la violencia, y Zapata se desplegó con sus tropas a los límites entre Guerrero y Puebla, escondiéndose del gobierno y generando emboscadas a pequeños contingentes federales. En este periodo, Zapata se casó con..._ | Zapata, Plan de Ayala | [ ] |
| 2 | 0.0155 | Emiliano Zapata — _Emiliano Zapata a Aguascalientes, que desempeñó un papel importante de negociación para la asistencia de la delegación zapatista, negociaciones tanto con Lucio Blanco como con el mismo general Francisco Villa, Paulino Martínez, Manuel J. Santibáñez y Manuel Uriarte, quienes quedaron en calidad de ob..._ | Zapata, Plan de Ayala, Villa, norte, División del Norte | [ ] |
| 3 | 0.0153 | Emiliano Zapata — _y algunos lugares de Guerrero. Poco después tomó Cuernavaca y para junio ocupó Cuajimalpa, Xochimilco y Milpa Alta, con lo que amagaba a la Ciudad de México. La población de la capital del país, huía al saber la cercanía del ejército de Zapata. Las fuerzas constitucionalistas les cerraron el paso, a..._ | Zapata, Plan de Ayala, Villa | [ ] |
| 4 | 0.0145 | Historia de México — _fecha en que se había pactado la convención. El 1 de octubre de 1914 en la Ciudad de México se instaló la Soberana Convención Revolucionaria. Carranza presentó su renuncia pero los delegados se la negaron. Como Villa se negó a trasladarse a la capital y Zapata desconocía a Carranza como autoridad, l..._ | Zapata, Villa, norte | [ ] |
| 5 | 0.0132 | Revolución mexicana — _llegaron las fuerzas de Villa, reuniéndose ambos generales y firmando el Pacto de Xochimilco, el cual básicamente constituía una alianza contra Carranza. Presionado por Villa y Zapata, Gutiérrez no pudo gobernar, y el 16 de enero salió de la capital e intentó establecer su gobierno en San Luis Potos..._ | Zapata, Villa | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Villa aceptó el Plan de Ayala, a excepción de las acusaciones contra Francisco I. Madero, a quien consideraba su redentor. | [ ] |
| 2 | Zapata, por otro lado, se opuso a Madero y lo desconocía. | [ ] |
| 3 | Aunque se aliaron militarmente, nunca hubo una verdadera colaboración entre ellos debido a que Zapata quería mantener aislada su región y se mantenía a la defensiva. | [ ] |
| 4 | Después de la renuncia de Eulalio Gutiérrez, Villa intentó tomar Celaya, mientras que Zapata se mantenía a la defensiva. | [ ] |

---

## V3 — ¿En qué se parecen el Virreinato y el Imperio Azteca?

**Tipo:** comparativa
**Puntos clave esperados:** Control centralizado; tributo; dominio territorial; jerarquía religiosa ligada al poder
**Tiempos:** retrieval=0.026s · generación=4.903s · total=4.930s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

_Ayuda para Recall: 71 chunks distintos del corpus mencionan al menos un punto clave (1 mencionan 2 o más); detalle con `python evaluation/candidates.py --question V3`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.0164 | Imperio azteca — _# Imperio azteca El Imperio mexica o Triple Alianza (del náhuatl: Exkan Tlahtoloyan o Ēxcān Tlahtōlōyān ‘Los tres lugares donde se dan órdenes’), llamado también Imperio azteca y —con más precisión— Imperio tenochca, fue un imperio organizado en una confederación compleja, multiétnica y flexible de ..._ | ninguno | [ ] |
| 2 | 0.0159 | Imperio azteca — _Guerrero y el Soconusco. El fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españoles —en alianza con los tlaxcaltecas y totonacas, entre otros pueblos indígenas— derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco. Etimología, nombres y definiciones La palabra «azteca» ..._ | ninguno | [ ] |
| 3 | 0.0143 | Historia de México — _completo. El siguiente líder al trono fue Tízoc en el año 1481, quien inició una campaña para atrapar cautivos para su ceremonia de investidura en Itzmiquilpan y Meztitlán. Esto supuso el comienzo del expansionismo azteca pues ordenó ataques contra tarascos, matlatzincas, chontales y cuitlatecos. Co..._ | ninguno | [ ] |
| 4 | 0.0081 | Imperio azteca — _lenguaje artístico comunicó historias, deidades y ritos en los que coincidieron ancestrales mitos y tradiciones. Ubicación del Imperio mexica Los aztecas se establecieron en el centro del valle de México, expandiendo su control hacia ciudades-estado ubicadas en los actuales estados de México, Morelo..._ | tributo, dominio territorial | [ ] |
| 5 | 0.0081 | Historia de México — _de Tenochtitlán, Chimalpopoca, permaneció en silencio, lo que propició un descontento entre los mexicas. Fue el sacerdote Tlacaelél quien, desde las sombras, convenció al sacerdote Izcóatl de realizar un golpe de Estado en Tenochtitlán, logrando imponerse como gobernante el 16 de octubre de 1427. Aq..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---

## R1 — ¿Qué relación tuvo Juárez con la Guerra de Reforma?

**Tipo:** relacional
**Puntos clave esperados:** Juárez lideró el bando liberal; promulgó las Leyes de Reforma; fue presidente durante el conflicto
**Tiempos:** retrieval=0.024s · generación=8.424s · total=8.448s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Juárez se convirtió en presidente de la República por primera vez tras un autogolpe de estado de Ignacio Comonfort. Inicialmente, Juárez nunca se declaró abiertamente a favor o en contra del conflicto, pero luego organizó un golpe de estado junto al general Manuel Doblado. La guerra, conocida como la Guerra de Reforma, fue una consecuencia de la promulgación de la Constitución de 1857 y las Leyes de Reforma, y enfrentó a liberales y conservadores. Juárez mantuvo un gobierno itinerante y formó una milicia para defenderse. Finalmente, la guerra terminó con la derrota de los conservadores en la Batalla de Calpulalpan, y Juárez instaló su administración en Ciudad de México.
>
> Fuentes:
> * Fragmento 2: Benito Juárez
> * Fragmento 1: Guerra de Reforma

_Ayuda para Recall: 79 chunks distintos del corpus mencionan al menos un punto clave (6 mencionan 2 o más); detalle con `python evaluation/candidates.py --question R1`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.0152 | Guerra de Reforma — _# Guerra de Reforma La Guerra de Reforma, también conocida como la guerra de los tres años, fue una guerra civil que aconteció en México desde el 17 de diciembre de 1857 al 11 de enero de 1861, como consecuencia de la promulgación de la Constitución de 1857 y en especial de las llamadas Leyes de Ref..._ | promulgó las Leyes de Reforma | [ ] |
| 2 | 0.0146 | Benito Juárez — _apresado por las fuerzas del propio Comonfort. La razón fue la duda de los golpistas ante su posición, ya que Juárez nunca se declaró abiertamente en contra ni a favor del conflicto, irónicamente causado por la ley cuyas bases él mismo había ayudado a sentar. Sin embargo, el propio Comonfort, quien ..._ | promulgó las Leyes de Reforma, fue presidente durante el conflicto | [ ] |
| 3 | 0.0146 | Benito Juárez — _héroe de la independencia. Juárez le preguntó al hombre sobre cómo era Hidalgo, a lo que éste respondió que era un hombre extraordinario. Juárez le dijo que él luchaba por los mismos ideales que Hidalgo. Juárez llegó a San Luis Potosí, donde intentó rehacer su gobierno. Él había decretado una ley, e..._ | promulgó las Leyes de Reforma | [ ] |
| 4 | 0.0144 | Benito Juárez — _y tropa huyeron hacia el Ajusco. Existieron otros altercados militares durante 1871 que fueron controlados pero que reflejaban la inestabilidad política de Juárez y el apoyo armado a Porfirio Díaz. Fallecimiento Días antes de su fallecimiento, Juárez había visitado una tarde junto a sus hijas la tum..._ | ninguno | [ ] |
| 5 | 0.0139 | Historia de México — _de pensamiento liberal en estas ciudades, los verdaderos liberales le eran fiel a Juárez. De hecho Pedro Escudo y José María Cortés y Esparza, que habían participado en el Congreso Constituyente para la Constitución del 57, se unieron a su consejo de ministros. Sin quererlo, Maximiliano estaba dándo..._ | promulgó las Leyes de Reforma | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Juárez se convirtió en presidente de la República por primera vez tras un autogolpe de estado de Ignacio Comonfort. | [ ] |
| 2 | Inicialmente, Juárez nunca se declaró abiertamente a favor o en contra del conflicto, pero luego organizó un golpe de estado junto al general Manuel Doblado. | [ ] |
| 3 | La guerra, conocida como la Guerra de Reforma, fue una consecuencia de la promulgación de la Constitución de 1857 y las Leyes de Reforma, y enfrentó a liberales y conservadores. | [ ] |
| 4 | Juárez mantuvo un gobierno itinerante y formó una milicia para defenderse. | [ ] |
| 5 | Finalmente, la guerra terminó con la derrota de los conservadores en la Batalla de Calpulalpan, y Juárez instaló su administración en Ciudad de México. | [ ] |

---

## R2 — ¿Cómo se relacionan Hernán Cortés y Moctezuma II?

**Tipo:** relacional
**Puntos clave esperados:** Encuentro en Tenochtitlan en 1519; Moctezuma tomado como rehén; su muerte; destrucción del imperio
**Tiempos:** retrieval=0.027s · generación=7.329s · total=7.356s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Según los fragmentos, Hernán Cortés y Moctezuma II establecieron un vínculo de amistad. Antes de morir, Moctezuma pidió a Cortés que favoreciera a su hijo, Chimalpopoca. Cortés intentó que Moctezuma apaciguara a los mexicas rebeldes, y existe la versión de que Cortés ordenó la muerte de Moctezuma cuando vio que no podía calmar al pueblo, aunque esta versión es menos probable.
>
> Fuentes:
> * Fragmento 3
> * Fragmento 4

_Ayuda para Recall: 174 chunks distintos del corpus mencionan al menos un punto clave (5 mencionan 2 o más); detalle con `python evaluation/candidates.py --question R2`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.0152 | Moctezuma II — _con una ruptura de varonía de los de Moctezuma se instaló en Portugal en el siglo XIX, donde sus descendientes utilizan de Moctezuma o de Montezuma. Tesoro de Moctezuma En torno a la figura de Moctezuma existe una historia sobre un gran tesoro que los españoles intentaron robar pero que se perdió. C..._ | ninguno | [ ] |
| 2 | 0.0151 | Moctezuma II — _Coyoacán, Tlacopan, Iztapalapa y el pueblo matlatzinca. Sin embargo, Moctezuma no deseaba la posibilidad del inicio de una guerra civil a causa de esto a pesar de las circunstancias, por lo que advirtió a Cortés de lo que sucedía. Hernán Cortés, el capitán general de las fuerzas españolas que entrar..._ | ninguno | [ ] |
| 3 | 0.0141 | Conquista de México — _fue llevado al interior pero falleció tres días después a causa de la herida. Su cuerpo y el de Itzcuauhtzin, señor de Tlatelolco, fueron llevados fuera del palacio por dos sirvientes del tlatoani y arrojados a la acequia. La convivencia entre Cortés y Moctezuma había creado un vínculo de amistad y ..._ | ninguno | [ ] |
| 4 | 0.0128 | Hernán Cortés — _Al haber hecho esto los pobladores se rebelaron contra Moctezuma, no teniéndole nadie respeto. Los españoles se tuvieron que refugiar en los alojamientos del palacio. La rebelión y La Noche Triste El 24 de junio de 1520 el ejército de Cortés entraba nuevamente en la ciudad. El hermano de Moctezuma, ..._ | su muerte | [ ] |
| 5 | 0.0082 | Moctezuma II — _el cuerpo de Itzquauhtzin fue llevado en una canoa a Tlatelolco. Durante la huida de los españoles, 30 de junio de 1520, perdieron cerca de la mitad de los soldados castellanos y casi todo el oro que habían obtenido y tuvieron que refugiarse entre los tlaxcaltecas. Entretanto, Cuitláhuac fue elegido..._ | su muerte | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Según los fragmentos, Hernán Cortés y Moctezuma II establecieron un vínculo de amistad. | [ ] |
| 2 | Antes de morir, Moctezuma pidió a Cortés que favoreciera a su hijo, Chimalpopoca. | [ ] |
| 3 | Cortés intentó que Moctezuma apaciguara a los mexicas rebeldes, y existe la versión de que Cortés ordenó la muerte de Moctezuma cuando vio que no podía calmar al pueblo, aunque esta versión es menos probable. | [ ] |

---

## R3 — ¿Qué papel jugó el Virreinato en la Independencia?

**Tipo:** relacional
**Puntos clave esperados:** Agravios acumulados; criollos excluidos del poder; influencia ilustrada; debilitamiento de España
**Tiempos:** retrieval=0.021s · generación=9.613s · total=9.634s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> El Virreinato de Nueva España estaba dividido en varios estratos sociales, cuya posición estaba condicionada por cuestiones económicas, culturales y políticas. Había un grupo pequeño de personas que controlaban la mayor parte de la riqueza, mientras que la gran parte de la población era pobre. Los pueblos indígenas debían pagar un tributo al gobierno y estaban sujetos a un régimen de autoridad que provocaba numerosas confrontaciones entre españoles, criollos y mestizos. Esto llevó a una situación de marginación y pobreza para los indígenas y mestizos novohispanos, lo que se reflejó en una memoria presentada ante el pleno, titulada "Exposición de motivos de la guerra de independencia". Esta memoria protestaba contra las autoridades virreinales y proponía soluciones como la organización de la enseñanza gratuita, la creación de sociedades agrícolas de producción, la libertad de comercio, la creación de ayuntamientos por elección popular y la división del gobierno en tres poderes.
>
> Fuentes: Fragmento 1, Fragmento 2, Fragmento 3, Fragmento 5.

_Ayuda para Recall: 8 chunks distintos del corpus mencionan al menos un punto clave (0 mencionan 2 o más); detalle con `python evaluation/candidates.py --question R3`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.0137 | Independencia de México — _Ulúa, Veracruz, entre otros episodios de los intentos de reconquista, incluyendo la expedición de Isidro Barradas en 1829, España reconoció la independencia de México en 1836, tras el fallecimiento del monarca Fernando VII. Antecedentes Situación económica y social del virreinato de Nueva España La ..._ | ninguno | [ ] |
| 2 | 0.0137 | Guerra de Independencia de México **(copia exacta del rank 1: cuenta una sola vez)** — _Ulúa, Veracruz, entre otros episodios de los intentos de reconquista, incluyendo la expedición de Isidro Barradas en 1829, España reconoció la independencia de México en 1836, tras el fallecimiento del monarca Fernando VII. Antecedentes Situación económica y social del virreinato de Nueva España La ..._ | ninguno | [ ] |
| 3 | 0.0082 | Guerra de Independencia de México — _presentó ante el pleno, una memoria titulada Exposición de motivos de la guerra de independencia, en la que protestaba contra las autoridades virreinales por la situación de marginación y pobreza en que se encontraban los indígenas y mestizos novohispanos, y mostraba las posibles soluciones. Entre s..._ | ninguno | [ ] |
| 4 | 0.0082 | Virreinato de Nueva España — _I), Juan de Tecto y Juan de Aora, pertenecientes a la alta sociedad castellana. Aora y Tecto fueron llevados por Cortés a evangelizar las Hibueras, pero murieron en el trayecto. Gante, mientras tanto, siguió su labor en Nueva España, fundó hospitales y escuelas, estableció un convento y enseñó artes..._ | ninguno | [ ] |
| 5 | 0.0081 | Independencia de México **(copia exacta del rank 3: cuenta una sola vez)** — _presentó ante el pleno, una memoria titulada Exposición de motivos de la guerra de independencia, en la que protestaba contra las autoridades virreinales por la situación de marginación y pobreza en que se encontraban los indígenas y mestizos novohispanos, y mostraba las posibles soluciones. Entre s..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El Virreinato de Nueva España estaba dividido en varios estratos sociales, cuya posición estaba condicionada por cuestiones económicas, culturales y políticas. | [ ] |
| 2 | Había un grupo pequeño de personas que controlaban la mayor parte de la riqueza, mientras que la gran parte de la población era pobre. | [ ] |
| 3 | Los pueblos indígenas debían pagar un tributo al gobierno y estaban sujetos a un régimen de autoridad que provocaba numerosas confrontaciones entre españoles, criollos y mestizos. | [ ] |
| 4 | Esto llevó a una situación de marginación y pobreza para los indígenas y mestizos novohispanos, lo que se reflejó en una memoria presentada ante el pleno, titulada "Exposición de motivos de la guerra de independencia". | [ ] |
| 5 | Esta memoria protestaba contra las autoridades virreinales y proponía soluciones como la organización de la enseñanza gratuita, la creación de sociedades agrícolas de producción, la libertad de comercio, la creación de ayuntamientos por elección popular y la división del gobierno en tres poderes. | [ ] |

---

## M1 — ¿Qué civilizaciones existían antes de los españoles y cuál dominaba en 1519?

**Tipo:** multihop
**Puntos clave esperados:** Olmecas; mayas; teotihuacanos; aztecas; el Imperio Azteca dominaba en 1519
**Tiempos:** retrieval=0.029s · generación=6.687s · total=6.717s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> Antes de la llegada de los españoles, existían varias civilizaciones, incluyendo los quichés, quienes habían forjado un pequeño imperio en el altiplano occidental de Guatemala, y los kaqchikel. En 1519, Francisco Hernández de Córdoba llegó a la costa de Yucatán, y Juan de Grijalva llegó a Campeche y Tabasco.
>
> Fuentes: Fragmento 2, Fragmento 1.

_Ayuda para Recall: 157 chunks distintos del corpus mencionan al menos un punto clave (17 mencionan 2 o más); detalle con `python evaluation/candidates.py --question M1`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.0135 | Virreinato de Nueva España — _Montejo el Adelantado, que junto con su hijo y sobrino, homónimos, dominaron a los grupos mayas que habitaban la península de Yucatán a su llegada en los albores del siglo XVI. Estos grupos, que presentaron una aguerrida defensa de su territorio, eran los descendientes de los que integraron la coali..._ | mayas | [ ] |
| 2 | 0.0127 | Civilización maya — _en varias provincias independientes que compartían una cultura común, pero variaban en su organización sociopolítica interna. En vísperas de la conquista española, varios poderosos estados mayas dominaron las tierras altas de Guatemala. Los quichés habían forjado un pequeño imperio que cubría una gr..._ | mayas, el Imperio Azteca dominaba en 1519 | [ ] |
| 3 | 0.0082 | Conquista de México — _de estos acontecimientos, que modificaron drásticamente la geopolítica mundial en los albores del siglo XVI, discurrirían aproximadamente tres siglos de dominación territorial española y resistencia indígena. Las fuentes principales de información de las campañas de Cortés y sus capitanes son las cr..._ | ninguno | [ ] |
| 4 | 0.0082 | Historia de México — _# Historia de México La historia de México es la narración cronológica y demostrable de los acontecimientos del pasado relacionados con el actual territorio de México, país ubicado en América del Norte. Dicha narración puede dividirse de distintas maneras según la perspectiva historiográfica. La div..._ | ninguno | [ ] |
| 5 | 0.0081 | Virreinato de Nueva España — _posible distinguir varios periodos. En el primero, la literatura está vinculada con el momento histórico de la conquista, y en él abundan las cartas y crónicas. Relación breve de la conquista de la Nueva España, de Francisco de Aguilar (1479-1571). Itinerario de la armada del rey católico a la isla ..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | Antes de la llegada de los españoles, existían varias civilizaciones, incluyendo los quichés, quienes habían forjado un pequeño imperio en el altiplano occidental de Guatemala, y los kaqchikel. | [ ] |
| 2 | En 1519, Francisco Hernández de Córdoba llegó a la costa de Yucatán, y Juan de Grijalva llegó a Campeche y Tabasco. | [ ] |

---

## M2 — ¿Cómo influyeron las reformas de Juárez en la Revolución décadas después?

**Tipo:** multihop
**Puntos clave esperados:** Constitución de 1857; separación Iglesia-Estado; antecedente liberal que Díaz traicionó
**Tiempos:** retrieval=0.027s · generación=4.368s · total=4.395s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

_Ayuda para Recall: 53 chunks distintos del corpus mencionan al menos un punto clave (3 mencionan 2 o más); detalle con `python evaluation/candidates.py --question M2`. Cuenta solo los realmente relevantes y sin copias._

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.0154 | Historia de México — _movimientos de las tropas francesas para el funcionamiento del imperio. Maximiliano solicitó revisar las reformas políticas dejadas por el gobierno anterior; no las de Santa Anna, sino las de Juárez. Fue cuando los conservadores descubrieron que la verdadera cara de la monarquía europea, ya estaba m..._ | ninguno | [ ] |
| 2 | 0.0143 | Benito Juárez — _héroe de la independencia. Juárez le preguntó al hombre sobre cómo era Hidalgo, a lo que éste respondió que era un hombre extraordinario. Juárez le dijo que él luchaba por los mismos ideales que Hidalgo. Juárez llegó a San Luis Potosí, donde intentó rehacer su gobierno. Él había decretado una ley, e..._ | ninguno | [ ] |
| 3 | 0.0082 | Historia de México — _cuando Juárez retornó triunfal como presidente a la Ciudad de México en julio de 1867, la mejor forma en que pudo legitimar el poder republicano fue restablecer la Constitución de 1857, ejecutar de nuevo las Leyes de Reforma y llamar a elecciones el 22 de septiembre. Juaréz, Lerdo y Díaz, compitiero..._ | Constitución de 1857, separación Iglesia-Estado | [ ] |
| 4 | 0.0082 | Independencia de México — _la agricultura. Por ejemplo, la creciente importancia de Guadalajara y El Bajío se debía a su relación con los minerales de Zacatecas y Guanajuato. Dado que la exportación de plata y oro constituía el nodo de la economía novohispana, en torno a esta actividad creció un complejo sistema que consolidó..._ | ninguno | [ ] |
| 5 | 0.0081 | Benito Juárez — _vez en Ciudad de México los recibió una muchedumbre así como miembros del gabinete y del gobierno, la familia se alojó en el Hotel Iturbide conforme a lo planeado y después de unas horas Juárez y Margarita al fin pudieron estar solos luego de tantos años. Segundo mandato constitucional Luego de gana..._ | ninguno | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---

## T1 — ¿Quién es el presidente actual de México?

**Tipo:** trampa  (pregunta trampa)
**Tiempos:** retrieval=0.023s · generación=5.830s · total=5.852s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> El presidente de México desde el 1 de diciembre de 2018 hasta el 30 de septiembre de 2024 es el que implementó una política social para disminuir la pobreza y mantuvo la estabilidad macroeconómica.
>
> Fuente: Fragmento 5

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.0149 | Benito Juárez — _# Benito Juárez Benito Pablo Juárez García (San Pablo Guelatao, Intendencia de Oaxaca; 21 de marzo de 1806 - Ciudad de México, 18 de julio de 1872), conocido como El Benemérito de las Américas, fue un abogado, jurista y político mexicano de origen indígena de la etnia zapoteca que se desempeñó como ..._ | — | [ ] |
| 2 | 0.0082 | Revolución mexicana — _Carranza jefe del «Ejército Constitucionalista» y se le daba la facultad de ocupar interinamente la presidencia de México para convocar a elecciones. Movimientos en el norte del país Este movimiento se caracterizó por tener una naturaleza legalista, cuyos segundos mandos estaban compuestos por los p..._ | — | [ ] |
| 3 | 0.0082 | Historia de México — _comunistas decidieron volvar su apoyo a Vasconcelos que ya consolidaba el gusto universitario y el católico. En el PNR hubo polémica sobre quién sería el elegido candidato, pues al principio se había propuesto a Aarón Sáenz. En un cambio de último momento, impuesto por el poder de Calles, se decidió..._ | — | [ ] |
| 4 | 0.0081 | Conquista de México — _siglo XVII un grupo de tlaxcaltecas fue llevado para pacificar a los nativos de la región así como para enseñarles la agricultura; no obstante, los ataques a las ciudades eran constantes y causaron problemas a los colonizadores hasta principios del siglo XVIII, al grado que la producción minera y al..._ | — | [ ] |
| 5 | 0.0079 | Historia de México — _Presidente de México desde el 1 de diciembre de 2018 hasta el 30 de septiembre de 2024. Durante su gobierno se destacaron principalmente, la implementación de una política social que sentara las bases de un estado de bienestar, lo que dio como resultado la disminución, por primera vez en décadas, de..._ | — | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | El presidente de México desde el 1 de diciembre de 2018 hasta el 30 de septiembre de 2024 es el que implementó una política social para disminuir la pobreza y mantuvo la estabilidad macroeconómica. | [ ] |

---

## T2 — ¿Cuál es el PIB actual de México?

**Tipo:** trampa  (pregunta trampa)
**Tiempos:** retrieval=0.023s · generación=4.322s · total=4.345s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.0160 | Historia de México — _Presidente de México desde el 1 de diciembre de 2018 hasta el 30 de septiembre de 2024. Durante su gobierno se destacaron principalmente, la implementación de una política social que sentara las bases de un estado de bienestar, lo que dio como resultado la disminución, por primera vez en décadas, de..._ | — | [ ] |
| 2 | 0.0138 | Historia de México — _# Historia de México La historia de México es la narración cronológica y demostrable de los acontecimientos del pasado relacionados con el actual territorio de México, país ubicado en América del Norte. Dicha narración puede dividirse de distintas maneras según la perspectiva historiográfica. La div..._ | — | [ ] |
| 3 | 0.0082 | Cultura teotihuacana — _Mimosa biuncifera. A estos tipos de vegetación se suman los pastizales, la vegetación hidrófila estacional, asociada con la temporada de lluvia. Las condiciones del valle favorecieron la concentración demográfica por ser benéficas para el estilo de vida mesoamericano basado en la agricultura. Los pa..._ | — | [ ] |
| 4 | 0.0081 | Guerra de Independencia de México — _# Independencia de México La independencia de México fue la consecuencia de un proceso político y social resuelto por las armas, que puso fin al dominio español mediante una guerra civil multifacética. Tuvo lugar en la mayor parte de los territorios de Nueva España, y dio como resultado el surgimien..._ | — | [ ] |
| 5 | 0.0081 | Cultura teotihuacana — _cuál ha sido el impacto de la actividad humana sobre los suelos de Teotihuacán. Rivera Uria et al. advierten que en algunos sitios como el cerro San Lucas la composición de la superficie ha cambiado dramáticamente. En este caso encontraron que antes del establecimiento de las primeras comunidades de..._ | — | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---

## T3 — ¿Qué equipos jugaron la final del fútbol mexicano en 2024?

**Tipo:** trampa  (pregunta trampa)
**Tiempos:** retrieval=0.028s · generación=4.373s · total=4.400s

**Anotada:** [ ]  _(marca `[x]` cuando termines esta pregunta; las no marcadas no cuentan en las métricas)_

**Respuesta del sistema:**
> No encontré esta información en el corpus.

**Total de chunks relevantes en el corpus (estimado, para Recall@5):** ___

### Chunks recuperados
_Marca `[x]` si el chunk es genuinamente relevante para responder la pregunta. La vista previa es parcial: ante la duda, lee el texto completo en `results.jsonl`._

| Rank | Score | Fuente y vista previa | Puntos clave presentes | Relevante |
|------|-------|-----------------------|------------------------|-----------|
| 1 | 0.0153 | Guerra de Independencia de México — _# Independencia de México La independencia de México fue la consecuencia de un proceso político y social resuelto por las armas, que puso fin al dominio español mediante una guerra civil multifacética. Tuvo lugar en la mayor parte de los territorios de Nueva España, y dio como resultado el surgimien..._ | — | [ ] |
| 2 | 0.0151 | Independencia de México **(copia exacta del rank 1: cuenta una sola vez)** — _# Independencia de México La independencia de México fue la consecuencia de un proceso político y social resuelto por las armas, que puso fin al dominio español mediante una guerra civil multifacética. Tuvo lugar en la mayor parte de los territorios de Nueva España, y dio como resultado el surgimien..._ | — | [ ] |
| 3 | 0.0143 | Historia de México — _del presidente Manuel de la Peña y Peña, intentó huir para mantener estabilidad desde oro sitio, pero la derrota era inminente. El 2 de febrero de 1848, se firmó el Tratado de Guadalupe Hidalgo en donde México cedía Texas, Alta California, Nevada, Utah, Nuevo México, Colorado, Wyoming, Kansas y Okla..._ | — | [ ] |
| 4 | 0.0139 | Historia de México — _Presidente de México desde el 1 de diciembre de 2018 hasta el 30 de septiembre de 2024. Durante su gobierno se destacaron principalmente, la implementación de una política social que sentara las bases de un estado de bienestar, lo que dio como resultado la disminución, por primera vez en décadas, de..._ | — | [ ] |
| 5 | 0.0082 | Historia de México — _como estrategia de prevención y contención. La falta de capacidad en los sistemas de salud para atender directamente el padecimiento. En principio el gobierno implementó un programa de reconversión hospitalaria para cubrir la necesidad de camas y respiradores. El 23 de diciembre de 2020 se inició la..._ | — | [ ] |

### Faithfulness — afirmaciones de la respuesta
_Marca `[x]` si la afirmación está respaldada por el texto de los chunks recuperados. El bloque «Fuentes:» no se evalúa._

| # | Afirmación | Respaldada |
|---|------------|------------|
| 1 | No encontré esta información en el corpus. | [ ] |

---
