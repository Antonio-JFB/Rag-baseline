# Anotación de evidencia — experimento de PLN

**Qué se anota:** para cada pregunta, marca con `[x]` en la columna *Evidencia* las **oraciones** del corpus que
aportan información necesaria para contestarla. Esta anotación es **independiente de cómo se parta el texto en
chunks**: las métricas de las seis configuraciones se calculan después a partir de ella.

**Criterio (usa el mismo para todas las preguntas):**
1. Marca la oración si **por sí sola** (o con el dato que introduce) afirma algo de la respuesta: el dato pedido,
   una causa, una consecuencia, un elemento de la comparación, un eslabón de la relación. Una oración que solo
   *menciona el tema* sin aportar el dato **no** es evidencia.
2. Si la respuesta tiene varias partes (causalidad, comparativa, multihop), marca **todas** las oraciones que
   aportan una parte; no hace falta que una sola contenga todo.
3. Oraciones repetidas con otras palabras (dos artículos que dicen lo mismo): marca **ambas**.
4. Pregunta trampa: si el corpus **sí** contiene la respuesta, marca la evidencia (p. ej. T1); si no hay nada,
   deja todo vacío y marca la pregunta como anotada.
5. La columna *Puntos clave* es solo una pista automática; una oración puede ser evidencia sin ella, y tenerla
   sin serlo (p. ej. un año suelto).
6. Las oraciones están ordenadas por artículo y posición, **no** por relevancia ni por método.
7. Al terminar una pregunta marca `[x]` en **Anotada**. Las no marcadas se excluyen de las métricas (no cuentan
   como ceros).

**Alcance:** las oraciones candidatas se reunieron con varios métodos (búsqueda densa, BM25, BM25 lematizado,
puntos clave y los chunks recuperados por las seis configuraciones). Lo que no aparece aquí se asume no relevante.
Si notas una evidencia importante que falta, añádela al final de la tabla con su `Ref` o avísame.


---

## F1 (factual)

**Pregunta:** ¿En qué año cayó Tenochtitlan?
**Puntos clave (guía, no juez):** 1521; Cuauhtémoc; tlaxcaltecas
**Anotada:** [ ] sí   (marca esta casilla al terminar la pregunta)

| # | Evidencia | Artículo | Oración | Puntos clave en la oración | Ref |
|---|---|---|---|---|---|
| 1 | [ ] | Benito Juárez | Maximiliano decidió quedarse entonces en Orizaba por un mes, para pensar qué hacer. | — | Benito Juárez#7567-7580 |
| 2 | [ ] | Benito Juárez | Ardo en deseos de que esta guerra se acabe, ¿Por qué siempre es el pobre el que sufre más? | — | Benito Juárez#9846-9865 |
| 3 | [ ] | Conquista de México | Las fuerzas españolas comenzaron a reorganizarse, aunque tardaron más de un año para regresar a tomar la plaza de Tenochtitlan. | — | Conquista de México#12307-12327 |
| 4 | [ ] | Conquista de México | Esto implicaba situarse casi sobre las veredas de acceso a Tenochtitlán. | — | Conquista de México#13666-13677 |
| 5 | [ ] | Conquista de México | Cortés casi fue hecho prisionero al caer de su caballo. | — | Conquista de México#14955-14965 |
| 6 | [ ] | Conquista de México | La batalla se prolongó durante tres días más y finalmente, los hombres de Cuauhtémoc se replegaron a Tenochtitlan. | Cuauhtémoc | Conquista de México#14989-15007 |
| 7 | [ ] | Conquista de México | El 13 de agosto de 1521, correspondiente al día "1 coatl" del año "3 calli" del mes Xocotlhuetzi, Cuauhtémoc salió de Tenochtitlan en una canoa, probablemente con la intención de negociar la rendición, pero fue avistado y capturado por el capitán García Holguín, mientras la ciudad caía en manos de los españoles y de sus aliados. | 1521, Cuauhtémoc | Conquista de México#16021-16077 |
| 8 | [ ] | Conquista de México | Poco tiempo después la noticia de la caída de Tenochtitlan a manos de los españoles llegó a Tzintzuntzan, capital del pueblo purépecha. | — | Conquista de México#17851-17873 |
| 9 | [ ] | Hernán Cortés | Mientras, en Tenochtitlan, Alvarado, temeroso de una concentración masiva de guerreros en la Plaza Mayor de Tenochtitlán, y temiendo los posibles augurios de Cholula, había cometido una matanza de nativos, de nobles, caciques y jefes de ejército cuando estos estaban celebrando la fiesta de Tóxcatl (quinto mes de los 18 que tenía el calendario mexica) en honor a Tezcatlipoca. | — | Hernán Cortés#7408-7467 |
| 10 | [ ] | Hernán Cortés | Después de su derrota de la Noche Triste, los españoles y sus aliados tlaxcaltecas se replegaron en Tlaxcala; se reorganizaron y atacaron Tenochtitlan, poniendo en sitio a la ciudad. | tlaxcaltecas | Hernán Cortés#7890-7919 |
| 11 | [ ] | Historia de México | Se tiene registro de que existió la recolección indígena de pepitas de oro en la región de Zacatula, Guerrero, cerca de los límites con Michoacán, mediante la recolección y el colado del sedimento de los ríos cercanos. | — | Historia de México#525-562 |
| 12 | [ ] | Historia de México | A inicios de siglo XVI, se empezó a notar la intransigencia del imperio y el odio que México Tenochtitlán empezó a cultivar en su contra por todos los pueblos prehispánicos de la época. | — | Historia de México#6581-6614 |
| 13 | [ ] | Historia de México | Sumado al fracaso, la epidemia de viruela llegó a Tenochtitlán acabando en 4 meses con poco más de 8 millones de personas. | — | Historia de México#8410-8432 |
| 14 | [ ] | Historia de México | Ganada la batalla, comenzó el sitio de Tenochtitlán destruyendo sus puentes y acueductos dejando completamente incomunicada la isla en mayo de 1521, lo que fue devastador en una ciudad asediada por la enfermedad y con el agua del lago contaminada por los cadáveres. | 1521 | Historia de México#8524-8567 |
| 15 | [ ] | Historia de México | La ciudad cayó ese día dejando el último reducto en Tlatelolco. | — | Historia de México#8738-8749 |
| 16 | [ ] | Historia de México | En 1960 Jaime Torres Bodet escribió:El 13 de agosto de 1521, heroicamente defendido por Cuauhtémoc, cayó Tlatelolco en poder de Hernán Cortés. | 1521, Cuauhtémoc | Historia de México#8777-8799 |
| 17 | [ ] | Historia de México | Fue la primera vez desde la conquista de Tenochtitlán en 1521, que la Ciudad de México volvió a ver una guerra sangrienta y destructiva en su suelo. | 1521 | Historia de México#45330-45357 |
| 18 | [ ] | Historia de México | Emiliano Zapata cayó muerto de su caballo. | — | Historia de México#49007-49014 |
| 19 | [ ] | Imperio azteca | El fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españoles —en alianza con los tlaxcaltecas y totonacas, entre otros pueblos indígenas— derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco. | 1521, tlaxcaltecas | Imperio azteca#254-288 |
| 20 | [ ] | Miguel Hidalgo y Costilla | Cuando Andalucía cayó en manos de los franceses, en la primavera de 1810 toda España ya estaba en poder del ejército napoleónico. | — | Miguel Hidalgo y Costilla#1469-1491 |
| 21 | [ ] | Moctezuma II | Sin embargo, sus gobiernos no duraron mucho tiempo, pues el imperio caería bajo control español en agosto de 1521, un año después de su muerte. | 1521 | Moctezuma II#692-717 |
| 22 | [ ] | Moctezuma II | La mayoría de las reformas y políticas de Moctezuma no durarían mucho después de su muerte, pues tras pasar un año de su muerte, las fuerzas castellanas y tlaxcaltecas lograron derrotar a las fuerzas del Imperio mexica durante la conquista de México, cayendo bajo control europeo el 13 de agosto de 1521. | 1521, tlaxcaltecas | Moctezuma II#2633-2685 |
| 23 | [ ] | Moctezuma II | Otra construcción fue el acueducto de Chapultepec, que fue finalizado en el año 1506, el cual traía agua dulce directamente desde Chapultepec a Tenochtitlan y Tlatelolco. | — | Moctezuma II#3987-4013 |
| 24 | [ ] | Moctezuma II | Después de la conquista, el árbol supuestamente fue llevado a Tenochtitlan. | — | Moctezuma II#5508-5519 |
| 25 | [ ] | Moctezuma II | Esta no era la primera vez que los huexotzincas habían enviado una embajada a Tenochtitlan con un propósito como tal, la primera vez siendo en el año 1499 durante el reinado de Ahuízotl, pero ésta fue rechazada. | — | Moctezuma II#8860-8897 |
| 26 | [ ] | Moctezuma II | Un rayo cayó en el templo de Xiuhtecuhtli, en donde se llama Tzummulco, no se escuchó el trueno. | — | Moctezuma II#12369-12387 |
| 27 | [ ] | Moctezuma II | Cuando había aún sol, cayó un fuego. | — | Moctezuma II#12387-12394 |
| 28 | [ ] | Moctezuma II | Parte de Tenochtitlán se inundó. | — | Moctezuma II#12428-12433 |
| 29 | [ ] | Moctezuma II | Al día siguiente los vigilantes volvieron a Tenochtitlán para informar a Moctezuma del evento. | — | Moctezuma II#12904-12918 |
| 30 | [ ] | Moctezuma II | El día 8 de noviembre de 1519, después de una ceremonia de bienvenida que duró más de una hora, los españoles finalmente llegaron a Tenochtitlán, donde conocieron a Moctezuma y también a su hermano y futuro huey tlatoani Cuitláhuac en el sitio de Huitzillan, donde actualmente está el hospital de Jesús y la Iglesia de Jesús Nazareno, en la Calzada de Tlalpan, el camino que conecta la parte sur de la ciudad con la … | — | Moctezuma II#14262-14338 |
| 31 | [ ] | Moctezuma II | También es de notar que el año 1 carrizo cayó durante el reinado de Moctezuma en el año de 1519. | — | Moctezuma II#16467-16487 |
| 32 | [ ] | Moctezuma II | En 1521, con la caída de Tenochtitlán, Cortés intentó recuperar el tesoro; para hacerlo mandó torturar al último tlatoani, Cuauhtémoc, pues creían que lo había escondido en una laguna. | 1521, Cuauhtémoc | Moctezuma II#20352-20381 |
| 33 | [ ] | Tenochtitlan | Tenochtitlan puede hacer referencia a: | — | Tenochtitlan#2-7 |
| 34 | [ ] | Tenochtitlan | Municipio de Tenochtitlán, municipio del estado de Veracruz. | — | Tenochtitlan#13-21 |
| 35 | [ ] | Virreinato de Nueva España | Se originó tras la caída de México-Tenochtitlan, acontecimiento principal de la conquista, la que propiamente no concluyó sino hasta mucho después, pues su territorio siguió creciendo hacia el norte. | — | Virreinato de Nueva España#70-99 |
| 36 | [ ] | Virreinato de Nueva España | Cuitláhuac, hermano de Moctezuma y señor de Iztapalapa fue elegido tlatoani de Tenochtitlan y en respuesta a la Matanza del Templo Mayor, decidió lanzar al pueblo contra los españoles el 30 de junio. | — | Virreinato de Nueva España#1517-1550 |

---

## F2 (factual)

**Pregunta:** ¿Quién dio el Grito de Independencia?
**Puntos clave (guía, no juez):** Miguel Hidalgo; Dolores Hidalgo; 16 septiembre 1810
**Anotada:** [ ] sí   (marca esta casilla al terminar la pregunta)

| # | Evidencia | Artículo | Oración | Puntos clave en la oración | Ref |
|---|---|---|---|---|---|
| 1 | [ ] | Benito Juárez | Fue ahí donde Juárez dio el Grito de Independencia en 1864. | — | Benito Juárez#4727-4738 |
| 2 | [ ] | Guerra de Independencia de México | En 1810, los conspiradores de Querétaro estuvieron a punto de correr la misma suerte pero, al verse descubiertos, optaron por tomar las armas el 16 de septiembre en compañía de los habitantes indígenas y campesinos del pueblo de Dolores (Guanajuato), convocados por el cura Miguel Hidalgo y Costilla. | Miguel Hidalgo, Dolores Hidalgo, 16 septiembre 1810 | Guerra de Independencia de México#355-403 |
| 3 | [ ] | Guerra de Independencia de México | Uno fue la Revolución francesa, y el otro, la independencia de Estados Unidos. | — | Guerra de Independencia de México#2453-2466 |
| 4 | [ ] | Guerra de Independencia de México | Uno de los diputados electos para asistir a las Cortes de Cádiz, fue José Eduardo de Cárdenas, diputado por Tabasco, quien el 24 de julio de 1811 presentó ante el pleno, una memoria titulada Exposición de motivos de la guerra de independencia, en la que protestaba contra las autoridades virreinales por la situación de marginación y pobreza en que se encontraban los indígenas y mestizos novohispanos, y mostraba las … | — | Guerra de Independencia de México#5723-5794 |
| 5 | [ ] | Guerra de Independencia de México | Entre sus revolucionarias propuestas estaban: la organización de la enseñanza gratuita, sin ninguna distinción de clases sociales y sin la exclusión de los indios; crear sociedades agrícolas de producción; otorgar libertad de comercio; creación de ayuntamientos por elección popular; y división del gobierno en tres poderes: Legislativo, Ejecutivo y Judicial. | — | Guerra de Independencia de México#5794-5844 |
| 6 | [ ] | Guerra de Independencia de México | La etapa de inicio de la Guerra de Independencia de México corresponde al levantamiento popular encabezado por Miguel Hidalgo y Costilla. | Miguel Hidalgo | Guerra de Independencia de México#5849-5870 |
| 7 | [ ] | Guerra de Independencia de México | Los miembros de la conspiración se hallaban sin una base de apoyo en ese momento, por lo que Hidalgo tuvo que convocar al pueblo de Dolores a sublevarse en contra de las autoridades españolas el 16 de septiembre de 1810. | Dolores Hidalgo, 16 septiembre 1810 | Guerra de Independencia de México#5895-5935 |
| 8 | [ ] | Guerra de Independencia de México | En ese lugar, Hidalgo convocó a los asistentes a levantarse contra el mal gobierno, en un acto que es conocido como Grito de Dolores y se considera el inicio de la guerra por la independencia mexicana. | Dolores Hidalgo | Guerra de Independencia de México#6294-6330 |
| 9 | [ ] | Guerra de Independencia de México | Este documento declaraba la independencia de la nación, la soberanía popular, la religión católica como única, la supresión de obvenciones, la división de poderes, la igualdad ante la ley, la abolición de las castas, la abolición de la esclavitud, la eliminación de la tortura, e instituía la celebración del 12 de diciembre para la Virgen de Guadalupe y el 16 de septiembre para conmemorar el inicio de la guerra de … | Miguel Hidalgo | Guerra de Independencia de México#14013-14088 |
| 10 | [ ] | Guerra de Independencia de México | Este fue un punto de discordia con López Rayón quien manifestó no estar de acuerdo con el primer punto mencionado en los Sentimientos de la Nación, pues defendía que la tesis que había abrazado el movimiento autonomista de 1808, debería seguir subsistiendo, es decir, América era dependiente del rey de España, pero no de la nación española, por tanto, la independencia buscada no era con respecto a la Corona, sino del … | — | Guerra de Independencia de México#14157-14236 |
| 11 | [ ] | Guerra de Independencia de México | Durante el congreso se pronunciaron otros discursos políticos de mayor o menor importancia, pero el 6 de noviembre de 1813, día de la clausura, se leyó el Acta Solemne de la Declaración de Independencia de la América Septentrional, la cual fue redactada por Carlos María de Bustamante y Andrés Quintana Roo. | — | Guerra de Independencia de México#14242-14293 |
| 12 | [ ] | Guerra de Independencia de México | Historia de México, desde los primeros movimientos que depararon su independencia en 1808 hasta la época presente. | — | Guerra de Independencia de México#32241-32258 |
| 13 | [ ] | Guerra de Independencia de México | Cronología de la Independencia (1808-1821) (1a. edición). | — | Guerra de Independencia de México#32436-32443 |
| 14 | [ ] | Guerra de Independencia de México | «Versiones del grito de Dolores y algo más». | — | Guerra de Independencia de México#32699-32707 |
| 15 | [ ] | Guerra de Independencia de México | Memoria de las revoluciones en México. | — | Guerra de Independencia de México#32712-32718 |
| 16 | [ ] | Guerra de Independencia de México | Atlas de historia de la revolución de independencia. | — | Guerra de Independencia de México#33480-33488 |
| 17 | [ ] | Historia de México | La madrugada del 16 de septiembre de 1810, Miguel Hidalgo y Costilla, llamó a la insurgencia al pueblo de Dolores (Guanajuato). | Miguel Hidalgo, Dolores Hidalgo, 16 septiembre 1810 | Historia de México#15465-15486 |
| 18 | [ ] | Historia de México | La profundización y radicalización del movimiento insurgente llevó a la convocatoria, de parte de Morelos de una asamblea nacional para gestar la independencia absoluta. | — | Historia de México#16655-16679 |
| 19 | [ ] | Historia de México | Así, tras 10 días de intenso debate y acuerdos entre ambos, el 24 de febero de 1821 proclaman el Plan de Iguala que proclamaba la Independencia de la América Septentrional bajo tres garantías: independencia, unión y religión. | — | Historia de México#17714-17751 |
| 20 | [ ] | Historia de México | Esa noche, los amotinados destruyeron el mercado de El Parián, el más grande del país, al grito de Viva Guerrero. | — | Historia de México#21917-21937 |
| 21 | [ ] | Historia de México | El anuncio de una constitución con derechos sociales, nacida de una revolución con el fin de derrocar gobernantes y dictaduras, avivió más la llama de las revueltas sociales. | — | Historia de México#48503-48531 |
| 22 | [ ] | Historia de México | 130.º. Cerraron su sesión al grito de Viva Cristo Rey. | — | Historia de México#51986-51996 |
| 23 | [ ] | Historia de México | Con tanto apoyo y fiel a sus ideales socialistas, el 15 de septiembre de 1936 al dar el grito de independencia también gritó Viva la República Española. | — | Historia de México#57383-57410 |
| 24 | [ ] | Miguel Hidalgo y Costilla | Destacó iniciando la primera etapa de la Guerra de Independencia de México con un acto conocido en la historiografía mexicana como Grito de Dolores. | — | Miguel Hidalgo y Costilla#65-89 |
| 25 | [ ] | Miguel Hidalgo y Costilla | Dirigió militar y políticamente la primera parte del movimiento independentista pero, tras una serie de derrotas, fue capturado el 21 de marzo de 1811, después de casi seis meses de iniciada la revuelta, y llevado prisionero a la ciudad de Chihuahua, fue juzgado y fusilado el 30 de julio del mismo año en Chihuahua. | — | Miguel Hidalgo y Costilla#89-143 |
| 26 | [ ] | Miguel Hidalgo y Costilla | Reunida buena parte de la población en el atrio de la iglesia, Hidalgo lanzó el ya famoso Grito de Dolores, comenzando formalmente la guerra de Independencia. | Dolores Hidalgo | Miguel Hidalgo y Costilla#2202-2228 |
| 27 | [ ] | Miguel Hidalgo y Costilla | Ante ello, los caudillos se vieron obligados a escapar con rumbo a Aguascalientes, perdiendo en la derrota gran cantidad de dinero, armas y tropas, y quedando herida de muerte la primera etapa de la guerra de Independencia. | — | Miguel Hidalgo y Costilla#6008-6045 |
| 28 | [ ] | Miguel Hidalgo y Costilla | El 16 de septiembre de 1810, llevando como estandarte a la virgen de Guadalupe, lanzó el llamado grito de Dolores que inició la gesta independentista. | 16 septiembre 1810 | Miguel Hidalgo y Costilla#8873-8898 |
| 29 | [ ] | Miguel Hidalgo y Costilla | Historia de Méjico: desde los primeros movimientos que prepararon su independencia en el año de 1808 hasta la época presente.. | — | Miguel Hidalgo y Costilla#9095-9115 |
| 30 | [ ] | Miguel Hidalgo y Costilla | Historia de Méjico: desde los primeros movimientos que prepararon su independencia en el año de 1808 hasta la época presente (Edición Facsimilar). | — | Miguel Hidalgo y Costilla#9124-9146 |
| 31 | [ ] | Miguel Hidalgo y Costilla | Cronología de la Independencia (1808-1821) (Primera edición). | — | Miguel Hidalgo y Costilla#9173-9180 |
| 32 | [ ] | Miguel Hidalgo y Costilla | De la insurrección a la independencia. | — | Miguel Hidalgo y Costilla#9313-9319 |
| 33 | [ ] | Virreinato de Nueva España | Esta última fue el antecedente directo de la independencia de México, la que, al consumarse en 1821, desintegró el virreinato y dio paso al Primer Imperio mexicano, en el que finalmente se coronaría Agustín de Iturbide. | — | Virreinato de Nueva España#624-660 |
| 34 | [ ] | Virreinato de Nueva España | La conspiración fue descubierta e Hidalgo adelantó la insurrección para el 16 de septiembre, en la madrugada, cuando inició la guerra de la Independencia de México, con el hecho conocido como Grito de Dolores. | Dolores Hidalgo | Virreinato de Nueva España#5261-5295 |
| 35 | [ ] | Virreinato de Nueva España | Fue de esta planta que Miguel Hidalgo obtendría recursos en su época de párroco de Dolores. | Miguel Hidalgo, Dolores Hidalgo | Virreinato de Nueva España#14030-14046 |

---

## F3 (factual)

**Pregunta:** ¿Cuándo comenzó el Porfiriato?
**Puntos clave (guía, no juez):** 1876; Porfirio Díaz; reelección continua
**Anotada:** [ ] sí   (marca esta casilla al terminar la pregunta)

| # | Evidencia | Artículo | Oración | Puntos clave en la oración | Ref |
|---|---|---|---|---|---|
| 1 | [ ] | Benito Juárez | La fiesta porfiriana del 2 de abril (1900-1911)». | — | Benito Juárez#15705-15713 |
| 2 | [ ] | Benito Juárez | Cronología (1854-1876) (1.ª edición). | 1876 | Benito Juárez#15863-15867 |
| 3 | [ ] | Civilización maya | Posclásico (c. 950-1540 d. C.) | — | Civilización maya#3282-3287 |
| 4 | [ ] | Cultura teotihuacana | Primeros asentamientos en la región de Teotihuacán (antes del 300 a. C.) | — | Cultura teotihuacana#4330-4342 |
| 5 | [ ] | Emiliano Zapata | En él se exigía la redención de los indígenas y la repartición de los latifundios creados durante el porfiriato. | — | Emiliano Zapata#1725-1744 |
| 6 | [ ] | Guerra de Independencia de México | Durante estas campañas comenzó a destacar el insurgente Pedro Ascencio Alquisiras. | — | Guerra de Independencia de México#22004-22015 |
| 7 | [ ] | Historia de México | Este periodo es comprendido entre el 1500 a. n. e. y el 292, descrito por Gordon Willey y Philip Phillips, antes del periodo clásico en el que se desarrolló el primer sistema de escritura americano por el pueblo Olmeca. | — | Historia de México#786-825 |
| 8 | [ ] | Historia de México | El ascenso de Porfirio Díaz al poder en 1876 empezó un periodo conocido como el Porfiriato, mismo que duró hasta 1911 con su exilio. | 1876, Porfirio Díaz | Historia de México#1749-1773 |
| 9 | [ ] | Historia de México | No obstante, a partir de 1973 hubo descubrimientos de restos arqueológicos considerablemente más antiguos —incluso al sur de América, donde destaca Pedra Furada en Brasil—, que permitió desarrollar la teoría del poblamiento temprano, más aceptada hoy en día por la comunidad científica y descartando a los Clovis. | — | Historia de México#2581-2628 |
| 10 | [ ] | Historia de México | Al iniciar el año electoral de 1876, Porfirio Díaz volvió a criticar el plan de reelección, pero ahora de Lerdo de Tejada, argumentando violaciones a la soberanía proclamando el Plan de Tuxtepec. | 1876, Porfirio Díaz | Historia de México#36820-36852 |
| 11 | [ ] | Historia de México | En ese ámbito se celebraron las elecciones del 25 de junio de 1876 que, parar sorpresa de nadie, dieron como ganador por reelección inmediata a Sebastián Lerdo de Tejada con 90 % de los votos, contra el 4 % de Porfirio Díaz. | 1876, Porfirio Díaz | Historia de México#36919-36961 |
| 12 | [ ] | Historia de México | No fue un síntoma del porfiriato, sino un suceso a nivel mundial, donde se empezó a ver a la clase baja como la causa de todos los males. | — | Historia de México#39155-39183 |
| 13 | [ ] | Historia de México | Eso sumado a los aires de lucha obrera y social que se daban en todo el mundo, marcaron la última década del Porfiriato. | — | Historia de México#40333-40356 |
| 14 | [ ] | Historia de México | En abril mientras el empresario ferrocarrilero Weetman Pearson trabajaba en el Istmo de Tehuantepec, descubrió petróleo. | — | Historia de México#40471-40487 |
| 15 | [ ] | Historia de México | Fue el 8 de abril de 1902 cuando también se puso fin a la guerra yaqui con la masacre de Mazatlán. | — | Historia de México#40516-40537 |
| 16 | [ ] | Historia de México | Don Porfirio es militar de carrera y político de trayectoria, lidió con el país casi 30 años. | — | Historia de México#43095-43112 |
| 17 | [ ] | Historia de México | Aquel fue el fin del Porfiriato. | — | Historia de México#43232-43238 |
| 18 | [ ] | Historia de México | Del 9 de febrero de 1913 al 19 de febero de 1913 | — | Historia de México#44107-44119 |
| 19 | [ ] | Porfiriato | El porfiriato o porfirismo fue un período de la historia de México en el que el gobierno estuvo bajo el control (total o mayoritario) del militar, político y dictador Porfirio Díaz, entre el 28 de noviembre de 1876 y el 27 de mayo de 1911. | 1876, Porfirio Díaz | Porfiriato#2-47 |
| 20 | [ ] | Porfiriato | En el porfiriato la política se aplicó de tal manera que todo quedaba subordinado al presidente. | — | Porfiriato#47-63 |
| 21 | [ ] | Porfiriato | La literatura fue el campo cultural que más avances tuvo en el Porfiriato. | — | Porfiriato#1895-1908 |
| 22 | [ ] | Porfiriato | La primera etapa del porfiriato empieza en 1877 y termina en el inicio de tercer periodo presidencial de Porfirio Díaz (1888) o cuando se eliminó toda restricción legal a la reelección indefinida (1890). | Porfirio Díaz | Porfiriato#3204-3237 |
| 23 | [ ] | Porfiriato | Para impulsar el desarrollo económico y el progreso material, la política exterior del Porfiriato fue la piedra angular. | — | Porfiriato#3962-3980 |
| 24 | [ ] | Porfiriato | Bazant, Jan: Breve historia de México México: Eds Coyoacán (2003) ISBN 970-633-057-7. | — | Porfiriato#5016-5028 |
| 25 | [ ] | Porfiriato | El Porfiriato vida social México: Hermes (1972). | — | Porfiriato#5050-5057 |
| 26 | [ ] | Porfiriato | El Porfiriato Vida política interior 2.ª Parte México: Hermes (1972). | — | Porfiriato#5064-5074 |
| 27 | [ ] | Revolución mexicana | Los antecedentes del conflicto se remontan a la situación de México bajo la dictadura conocida como el porfiriato. | — | Revolución mexicana#29-47 |
| 28 | [ ] | Revolución mexicana | Porfirio Díaz Mori ejerció el poder en el país de manera dictatorial desde 1876 hasta 1911. | 1876, Porfirio Díaz | Revolución mexicana#47-63 |
| 29 | [ ] | Revolución mexicana | Actualmente no existe un consenso sobre cuándo terminó el proceso revolucionario. | — | Revolución mexicana#668-679 |
| 30 | [ ] | Revolución mexicana | Porfirio Díaz, un mestizo oaxaqueño de ascendencia mixteca que se destacó en los ejércitos liberales combatiendo contra grupos conservadores y que participó en la Intervención Francesa, había asumido la presidencia desde 1876 tras el triunfo de la rebelión de Tuxtepec, y para el final de su séptimo mandato, en 1910, había mantenido una dictadura de 34 años. | 1876, Porfirio Díaz | Revolución mexicana#746-803 |

---

## F4 (factual)

**Pregunta:** ¿Qué civilización construyó Teotihuacán?
**Puntos clave (guía, no juez):** Cultura teotihuacana; nombre propio desconocido; periodo clásico
**Anotada:** [ ] sí   (marca esta casilla al terminar la pregunta)

| # | Evidencia | Artículo | Oración | Puntos clave en la oración | Ref |
|---|---|---|---|---|---|
| 1 | [ ] | Benito Juárez | Maximiliano decidió quedarse entonces en Orizaba por un mes, para pensar qué hacer. | — | Benito Juárez#7567-7580 |
| 2 | [ ] | Civilización maya | Posteriormente se construyó la primera ciudad maya en el actual estado de Tabasco, que recibió el nombre de Aguada Fénix, la cual se ha convertido en la ciudad más antigua y grande descubierta, ya que los estudios de radiocarbono indican que esta ciudad maya fue construida en el año 1000 a. C., colocándola antes de Ceibal y Cuello; en el período Preclásico (c. 2000 a. C. hasta 250 d. C.) se desarrollaron las … | periodo clásico | Civilización maya#152-247 |
| 3 | [ ] | Civilización maya | Mesoamérica fue una de las seis cunas de la civilización en el mundo. | — | Civilización maya#819-832 |
| 4 | [ ] | Civilización maya | En esta misma época hubo una fuerte presencia maya en el recinto de Tetitla en Teotihuacán. | — | Civilización maya#1172-1188 |
| 5 | [ ] | Cultura olmeca | Sin embargo, no está claro el proceso que dio origen al estilo artístico identificado con esta sociedad, ni hasta qué punto los rasgos culturales que se revelan en la evidencia arqueológica son creación de los olmecas del área nuclear. | — | Cultura olmeca#129-168 |
| 6 | [ ] | Cultura olmeca | También construyeron edificaciones en torno a patios centrales, característicos de las civilizaciones posteriores en la zona. | — | Cultura olmeca#1589-1605 |
| 7 | [ ] | Cultura olmeca | No se sabe qué tipo de dios pudo ser. | — | Cultura olmeca#1914-1923 |
| 8 | [ ] | Cultura teotihuacana | Alrededor del inicio de la era cristiana, más precisamente en el s. ii a. C., Teotihuacán constituía una aldea que empezaba a cobrar importancia como centro de culto en el valle de México. | — | Cultura teotihuacana#192-225 |
| 9 | [ ] | Cultura teotihuacana | Teotihuacán fue ya motivo de interés para las sociedades posteriores al declive de la cultura teotihuacana en Mesoamérica. | Cultura teotihuacana | Cultura teotihuacana#702-720 |
| 10 | [ ] | Cultura teotihuacana | Esta hipótesis podría ser reforzada por el descubrimiento de varias representaciones del glifo puh en la pintura mural del conjunto residencial de Tepantitla, dentro de Teotihuacán. | — | Cultura teotihuacana#1505-1531 |
| 11 | [ ] | Cultura teotihuacana | Haciendo un análisis de las fuentes históricas, los hallazgos arqueológicos en el centro de México y en el área maya ―como el referido caso del glifo Puh en las Tierras Bajas―, Enrique Florescano hace una asociación del mito con la ciudad de Teotihuacán, de modo que la llama «Tollan-Teotihuacán» y atribuye a la llamada ciudad de los dioses la identidad de la Tula mitológica. | — | Cultura teotihuacana#1597-1661 |
| 12 | [ ] | Cultura teotihuacana | Teotihuacán fue fundada en una posición poco común en su época con respecto al patrón de asentamiento propio de la cuenca de México durante el Preclásico Medio. | — | Cultura teotihuacana#1804-1831 |
| 13 | [ ] | Cultura teotihuacana | Duverger afirma que la ubicación de Teotihuacán corresponde no solo a una frontera ecológica, sino a la frontera entre la civilización agrícola mesoamericana y el mundo cultural de los pueblos aridoamericanos nómadas. | — | Cultura teotihuacana#1912-1944 |
| 14 | [ ] | Cultura teotihuacana | Los totonacos son otros candidatos a ocupar el sitio como fundadores de Teotihuacán. | — | Cultura teotihuacana#2885-2898 |
| 15 | [ ] | Cultura teotihuacana | La época de mayor apogeo de Teotihuacán corresponde al periodo Clásico Temprano de Mesoamérica (ss. | periodo clásico | Cultura teotihuacana#3458-3473 |
| 16 | [ ] | Cultura teotihuacana | Por motivos que aún no han sido del todo dilucidados, Teotihuacán se colapsó hacia mediados del siglo VIII, dando lugar al Período Epiclásico mesoamericano. | periodo clásico | Cultura teotihuacana#3552-3576 |
| 17 | [ ] | Cultura teotihuacana | La historia de Teotihuacán se puede entender como parte de un largo proceso civilizatorio que comenzó con la llegada de los seres humanos al Anáhuac. | — | Cultura teotihuacana#3849-3874 |
| 18 | [ ] | Cultura teotihuacana | Primeros asentamientos en la región de Teotihuacán (antes del 300 a. C.) | — | Cultura teotihuacana#4330-4342 |
| 19 | [ ] | Cultura teotihuacana | Estas aldeas eran contemporáneas a Terremote Tlaltenco, Tlatilco y Cuicuilco, y su desarrollo corresponde a las fases Cuanalán y Tezoyuca (c. 500-100 a. C.). | — | Cultura teotihuacana#4376-4400 |
| 20 | [ ] | Cultura teotihuacana | El proceso urbano que llevó a la fundación de Teotihuacán recibió el aporte cultural de los cuicuilcas, poseedores de una organización social compleja y centralizada que fortaleció a la estructura de Teotihuacán. | — | Cultura teotihuacana#4715-4747 |
| 21 | [ ] | Cultura teotihuacana | Todos estos factores constituyen parte del escenario que llevó a la culminación del proyecto urbano de Teotihuacán y la consolidación del Estado teotihuacano como uno de los más poderosos en la historia prehispánica de Mesoamérica. | — | Cultura teotihuacana#4805-4840 |
| 22 | [ ] | Cultura teotihuacana | La fase Tzacualli de Teotihuacán (1-150 d. C.) es aquella en la que se establecen las bases de la planificación urbanística de la ciudad y se definen varios rasgos característicos de la cultura teotihuacana. | Cultura teotihuacana | Cultura teotihuacana#5062-5096 |
| 23 | [ ] | Cultura teotihuacana | La presencia de esta cerámica en los yacimientos mesoamericanos es considerada como un indicador de vinculación con el mundo teotihuacano, pero es importante aclarar que se trata de un producto extranjero en Teotihuacán. | — | Cultura teotihuacana#6023-6056 |
| 24 | [ ] | Cultura teotihuacana | Algunos de los vestigios de la cerámica maya hallados en Teotihuacán corresponden al tipo Tzakol y guardan semejanzas con las obras contemporáneas de ese tipo que se han encontrado en Tikal y Uaxactún. | — | Cultura teotihuacana#6247-6280 |
| 25 | [ ] | Cultura teotihuacana | El arte teotihuacano vive una de sus mejores épocas. | — | Cultura teotihuacana#6741-6750 |
| 26 | [ ] | Cultura teotihuacana | Algunos autores opinan que esta cultura es extranjera, producto de una migración que contribuyó a la ruina teotihuacana. | Cultura teotihuacana | Cultura teotihuacana#7107-7125 |
| 27 | [ ] | Cultura teotihuacana | De acuerdo con la arqueóloga Verónica Ortega: «Lo primero que hubo para hacer adoración en Teotihuacán fue este túnel y posteriormente pusieron un lugar ya sagrado, ahí se construyó la Pirámide del Sol [...] | — | Cultura teotihuacana#9575-9609 |
| 28 | [ ] | Cultura teotihuacana | No es asombroso que todas las civilizaciones de la meseta mexicana dijeran descender de la civilización de Teotihuacán. | — | Cultura teotihuacana#10721-10739 |
| 29 | [ ] | Cultura teotihuacana | Todas las civilizaciones avanzadas de la región incorporaron el estilo Teotihuacán a su arquitectura, como testimonian las representaciones de Quetzalcoatl, la famosa "serpiente emplumada" que se encuentra prácticamente en todos los sitios arqueológicos de México y Guatemala. | — | Cultura teotihuacana#10822-10859 |
| 30 | [ ] | Cultura teotihuacana | De acuerdo con las fuentes coloniales, los nahuas pensaban que Teotihuacán fue construida por los quinametzin, una raza de gigantes que pobló el mundo durante la era anterior y cuyos sobrevivientes se encontraban ocultos. | — | Cultura teotihuacana#10863-10897 |
| 31 | [ ] | Cultura teotihuacana | Teotihuacan, ciudad de dioses. | — | Cultura teotihuacana#12674-12678 |
| 32 | [ ] | Cultura teotihuacana | Teotihuacan, la Ciudad de los Dioses. | — | Cultura teotihuacana#12905-12911 |
| 33 | [ ] | Cultura teotihuacana | The Names of Teotihuacan. | — | Cultura teotihuacana#13740-13744 |
| 34 | [ ] | Cultura teotihuacana | Página oficial del Municipio de Teotihuacan (enlace roto disponible en Internet Archive; véase el historial, la primera versión y la última). | — | Cultura teotihuacana#13790-13811 |
| 35 | [ ] | Cultura teotihuacana | Cultura teotihuacana Archivado el 24 de agosto de 2017 en Wayback Machine. | Cultura teotihuacana | Cultura teotihuacana#13879-13891 |
| 36 | [ ] | Historia de México | La última mencionada fue en la que se desarrollaron las civilizaciones prehispánicas. | — | Historia de México#104-116 |
| 37 | [ ] | Historia de México | Los criterios sobre qué hechos considerarlos como coyuntura y el criterio para ver qué tan relevantes fueron pueden diferir enormemente entre historiadores. | — | Historia de México#317-339 |
| 38 | [ ] | Historia de México | Con sus enemigos vencidos y el resto de ciudades aledañas en su control, la ciudad de Teotihuacán empezó un rápido desarrollo que les permitió construir lo que hoy se conoce como la Pirámide de la Luna alrededor del año 100. | — | Historia de México#4176-4216 |
| 39 | [ ] | Historia de México | Este auge aceleró el florecimiento de los teotihuacanos poniendo fin al periodo preclásico y dando inicio al clásico. | periodo clásico | Historia de México#4216-4234 |
| 40 | [ ] | Historia de México | Con aquella muestra de poder, Teotihuacán inició un periodo de embellecimiento que le permitió crear en el año 426 los barrios de Tepantitla, Atetelco o Teopancaxco, además de la construcción del Palacio de Quetzpapalotl. | — | Historia de México#4412-4446 |
| 41 | [ ] | Moctezuma II | Moctezuma construyó su propio tecpan (palacio) durante su reinado, al igual que la mayoría de sus antecesores. | — | Moctezuma II#2996-3013 |
| 42 | [ ] | Pancho Villa | Aunque este se debió haber llamado Agustín Villa Arango, se desconocen las causas de por qué Jesús Villa no dio nombre a su hijo y de por qué este recibió el apellido de su madre. | — | Pancho Villa#644-679 |

---

## F5 (factual)

**Pregunta:** ¿Quién fue el último emperador azteca?
**Puntos clave (guía, no juez):** Cuauhtémoc; sobrino de Moctezuma II; capturado 1521
**Anotada:** [ ] sí   (marca esta casilla al terminar la pregunta)

| # | Evidencia | Artículo | Oración | Puntos clave en la oración | Ref |
|---|---|---|---|---|---|
| 1 | [ ] | Benito Juárez | Juárez dijo que Iturbide era un emperador, que si no había mejor hotel. | — | Benito Juárez#11740-11753 |
| 2 | [ ] | Conquista de México | Considerando que Cacama había muerto durante los hechos ocurridos el 30 de junio, la Triple Alianza tuvo nuevos sucesores, Coanácoch en Tetzcuco, Tetlepanquetzaltzin en Tlacopan y Cuauhtémoc (Águila que desciende), sobrino de Moctezuma Xocoyotzin, en Tenochtitlan. | Cuauhtémoc, sobrino de Moctezuma II | Conquista de México#12442-12478 |
| 3 | [ ] | Conquista de México | El 13 de agosto de 1521, correspondiente al día "1 coatl" del año "3 calli" del mes Xocotlhuetzi, Cuauhtémoc salió de Tenochtitlan en una canoa, probablemente con la intención de negociar la rendición, pero fue avistado y capturado por el capitán García Holguín, mientras la ciudad caía en manos de los españoles y de sus aliados. | Cuauhtémoc, capturado 1521 | Conquista de México#16021-16077 |
| 4 | [ ] | Conquista de México | En el lugar fue recibido por el batab o halach uinik de Acalán, llamado Apoxpalón, quién comerciaba cacao, algodón, sal y esclavos. | — | Conquista de México#20210-20232 |
| 5 | [ ] | Conquista de México | Por tal motivo, al sureste de Xicalango, aún dentro de la jurisdicción de Acalán de los mayas chontales, en un punto llamado “Itzamkanac” se realizó la sentencia y ejecución por ahorcamiento del último huey tlatoani Cuauhtémoc. | Cuauhtémoc | Conquista de México#20298-20334 |
| 6 | [ ] | Conquista de México | Quebrantó la paz con el cazonci purépecha Tangáxoan Tzíntzicha a quién asesinó. | — | Conquista de México#22404-22416 |
| 7 | [ ] | Cultura olmeca | El centro ceremonial de Tres Zapotes fue el último en desarrollarse, descubierto en 1939 por Eulalia Guzmán. | — | Cultura olmeca#1489-1506 |
| 8 | [ ] | Cultura teotihuacana | En enero de 378, en tiempos en que Búho Lanzadardos gobernaba en Teotihuacán, el guerrero teotihuacano Siyah K'ak' (Nace el Fuego) "conquistó" Tikal, asesinando y reemplazando al rey Chak Tok Ich'aak II, con apoyo de El Perú-Waká y Naachtún, lo que fue registrado en la Estela 31 de Tikal y otros monumentos de la región Maya. | — | Cultura teotihuacana#6321-6377 |
| 9 | [ ] | Cultura teotihuacana | De Teotihuacán a los aztecas: antología de fuentes e interpretaciones históricas, 123-129. | — | Cultura teotihuacana#13172-13184 |
| 10 | [ ] | Cultura teotihuacana | En Carrasco, David et al. (eds.), Mesoamerica's Classic Heritage: from Teotihuacán to the Aztecs, 465-513. | — | Cultura teotihuacana#13569-13584 |
| 11 | [ ] | Hernán Cortés | Hernán Cortés de Monroy y Pizarro Altamirano, primer marqués del Valle de Oaxaca (Medellín, 1485-Castilleja de la Cuesta, 2 de diciembre de 1547), fue un militar, conquistador, explorador, fundador, capitán general y escritor español que, a principios del siglo XVI, lideró la conquista del Imperio azteca, conocida como conquista de México-Tenochtitlan, que significó el fin de dicho imperio, poniéndolo bajo dominio … | — | Hernán Cortés#3-80 |
| 12 | [ ] | Hernán Cortés | El Domingo de Resurrección se personaron dos caciques, Cuitlalpitoc y Tehutile (Teuhtilli o Tendile para los españoles), quienes les entregaron obsequios y se sorprendieron de que Cortés quisiese ver a Moctezuma, el «tlatoani» o emperador del Imperio azteca, con capital en Tenochtitlán. | — | Hernán Cortés#4418-4460 |
| 13 | [ ] | Hernán Cortés | Según la obra del fraile Bernardino de Sahagún y sus colaboradores nahuas, según un discurso de Moctezuma recogido en la segunda carta de Cortés a Carlos I y según otras fuentes redactadas en español, el emperador azteca interpretó que Cortés era Quetzalcóatl. | — | Hernán Cortés#4600-4642 |
| 14 | [ ] | Hernán Cortés | El hermano de Moctezuma, Cuitláhuac, fue liberado para que gestionase la pacificación, pero en vez de eso, se puso al frente de los mexicas y se unió al jefe de los caciques, llamado Cuauhtémoc —y quien sería el siguiente tlatoani mexica—, para oponerse a la ocupación española. | Cuauhtémoc | Hernán Cortés#7546-7593 |
| 15 | [ ] | Hernán Cortés | Por tal motivo, al sureste de Xicalango, aún dentro de la jurisdicción de Acalán de los mayas chontales se realizó la sentencia y ejecución por ahorcamiento del último huey tlatoani Cuauhtémoc. | Cuauhtémoc | Hernán Cortés#8680-8711 |
| 16 | [ ] | Historia de México | Su muerte significó el fin de la Unidad Mixteca de Oaxaca. | — | Historia de México#5284-5295 |
| 17 | [ ] | Historia de México | Así estaba por iniciar el Imperio Azteca. | — | Historia de México#6060-6067 |
| 18 | [ ] | Historia de México | Esto supuso el comienzo del expansionismo azteca pues ordenó ataques contra tarascos, matlatzincas, chontales y cuitlatecos. | — | Historia de México#6528-6544 |
| 19 | [ ] | Historia de México | En 1960 Jaime Torres Bodet escribió:El 13 de agosto de 1521, heroicamente defendido por Cuauhtémoc, cayó Tlatelolco en poder de Hernán Cortés. | Cuauhtémoc | Historia de México#8777-8799 |
| 20 | [ ] | Historia de México | La ciudad lo recibió con ovaciones pues le era fiel al emperador. | — | Historia de México#34116-34128 |
| 21 | [ ] | Imperio azteca | El Imperio mexica o Triple Alianza (del náhuatl: Exkan Tlahtoloyan o Ēxcān Tlahtōlōyān ‘Los tres lugares donde se dan órdenes’), llamado también Imperio azteca y —con más precisión— Imperio tenochca, fue un imperio organizado en una confederación compleja, multiétnica y flexible de ciudades estado con situaciones políticas diversas, que existió en el área central de Mesoamérica durante el Posclásico Tardío hasta la … | — | Imperio azteca#3-67 |
| 22 | [ ] | Imperio azteca | El fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españoles —en alianza con los tlaxcaltecas y totonacas, entre otros pueblos indígenas— derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco. | — | Imperio azteca#254-288 |
| 23 | [ ] | Imperio azteca | Los mexicas fueron los últimos en llegar a Mesoamérica. | — | Imperio azteca#9794-9803 |
| 24 | [ ] | Imperio azteca | El actual territorio del estado México fue el principal y mayor tributario de maderas, carnes y vegetales del Imperio azteca. | — | Imperio azteca#10197-10217 |
| 25 | [ ] | Imperio azteca | Y de donde se obtuvo parte de lo que fue la cultura azteca. | — | Imperio azteca#10217-10230 |
| 26 | [ ] | Imperio azteca | Aztec Warfare: Imperial Expansion and Political Control (en inglés). | — | Imperio azteca#10716-10725 |
| 27 | [ ] | Imperio azteca | Santamarina Novillo, Carlos, El sistema de dominación azteca: el Imperio Tepaneca. | — | Imperio azteca#10875-10886 |
| 28 | [ ] | Moctezuma II | Tras su muerte, hubo otros dos monarcas quienes gobernaron el imperio, siendo su sucesor su hermano Cuitláhuac, y el último, su sobrino Cuauhtémoc. | Cuauhtémoc | Moctezuma II#669-692 |
| 29 | [ ] | Moctezuma II | Se escuchó a una plañidera dirigir un canto fúnebre a los aztecas. | — | Moctezuma II#12433-12445 |
| 30 | [ ] | Virreinato de Nueva España | La conquista de Yucatán fue la más tardía de las que finalmente integraron el virreinato de la Nueva España, ya que los últimos reductos mayas no fueron dominados íntegramente hasta el año de 1697 —es decir, más de siglo y medio después de la conquista de México—, con la conquista de Tayasal. | — | Virreinato de Nueva España#1074-1126 |
| 31 | [ ] | Virreinato de Nueva España | Varias premoniciones en años anteriores hicieron creer a Moctezuma Xocoyotzin, soberano azteca o tlatoani, que el fin de su imperio estaba cerca. | — | Virreinato de Nueva España#1396-1418 |
| 32 | [ ] | Virreinato de Nueva España | El emperador murió pocos días después. | — | Virreinato de Nueva España#1511-1517 |
| 33 | [ ] | Virreinato de Nueva España | Los aztecas eran ahora gobernados por Cuauhtémoc, pues Cuitláhuac había fallecido en noviembre, víctima de viruela, enfermedad de la que eran portadores algunos españoles y ante la cual los indígenas eran muy vulnerables. | Cuauhtémoc | Virreinato de Nueva España#1664-1697 |
| 34 | [ ] | Virreinato de Nueva España | Cuauhtémoc, caudillo azteca, intentó escapar en balsa por el Lago de Texcoco, pero fue arrestado. | Cuauhtémoc | Virreinato de Nueva España#1745-1760 |
| 35 | [ ] | Virreinato de Nueva España | Fue el último virrey que gobernó bajo la dinastía Habsburgo. | — | Virreinato de Nueva España#7982-7992 |
| 36 | [ ] | Virreinato de Nueva España | Maestro de capilla de Puebla desde 1629. | — | Virreinato de Nueva España#20854-20861 |

---

## C1 (causalidad)

**Pregunta:** ¿Cuáles fueron las causas de la Revolución Mexicana?
**Puntos clave (guía, no juez):** Reelección de Díaz; desigualdad agraria; Plan de San Luis; crisis de 1907; Madero
**Anotada:** [ ] sí   (marca esta casilla al terminar la pregunta)

| # | Evidencia | Artículo | Oración | Puntos clave en la oración | Ref |
|---|---|---|---|---|---|
| 1 | [ ] | Benito Juárez | Instituto Nacional de Estudios Históricos de las Revoluciones de México. | — | Benito Juárez#15867-15877 |
| 2 | [ ] | Conquista de México | Tales contradicciones fueron, y han sido a través de los siglos, el motivo principal de la controversia que surgió como resultado de la insurrección de Hernan Cortés. | — | Conquista de México#2738-2765 |
| 3 | [ ] | Emiliano Zapata | Al proclamar Francisco I. Madero el Plan de San Luis, que marcaba el inicio de la Revolución de 1910, Zapata leyó un ejemplar; llamándole la atención especialmente el artículo tercero, que ofrecía la restitución de las tierras a sus "antiguos poseedores". | Plan de San Luis, Madero | Emiliano Zapata#887-928 |
| 4 | [ ] | Emiliano Zapata | Los intelectuales que se dedicaron a modificar el plan de Ayala, en el que desconocían a Madero y Huerta, como presidentes; y Orozco, como líder de la revolución; se encargaron de dejar claro el carácter social del movimiento, y además rectificaron el concepto de ‘clase’ dentro de la sociedad mexicana. | Madero | Emiliano Zapata#1797-1847 |
| 5 | [ ] | Emiliano Zapata | «7.º En virtud de que la inmensa mayoría de los pueblos y ciudadanos mexicanos no son más dueños que del terreno que pisan sufriendo los horrores de la miseria sin poder mejorar en nada su condición social ni poder dedicarse a la industria o a la agricultura por estar monopolizados en unas cuantas manos las tierras, montes y aguas, por esta causa se expropiarán, previa indemnización de la tercera parte de esos … | — | Emiliano Zapata#2189-2382 |
| 6 | [ ] | Guerra de Independencia de México | El movimiento de la independencia de México tiene como marco la Ilustración y las revoluciones liberales de la última parte del siglo XVIII. | — | Guerra de Independencia de México#124-147 |
| 7 | [ ] | Guerra de Independencia de México | La etapa de inicio de la Guerra de Independencia de México corresponde al levantamiento popular encabezado por Miguel Hidalgo y Costilla. | — | Guerra de Independencia de México#5849-5870 |
| 8 | [ ] | Guerra de Independencia de México | A causa de la revolución, la minería suspendió labores y entró en un proceso de decadencia. | — | Guerra de Independencia de México#10144-10160 |
| 9 | [ ] | Guerra de Independencia de México | Instituto Nacional de Estudios Históricos de las Revoluciones de México. | — | Guerra de Independencia de México#32443-32453 |
| 10 | [ ] | Guerra de Independencia de México | Memoria de las revoluciones en México. | — | Guerra de Independencia de México#32712-32718 |
| 11 | [ ] | Guerra de Independencia de México | Cuadro histórico de la revolución de la América Mexicana, comenzada en quince de septiembre de mil ochocientos diez, por el ciudadano Miguel Hidalgo y Costilla. | — | Guerra de Independencia de México#33353-33378 |
| 12 | [ ] | Historia de México | La Edad Contemporánea se desarrollaría simultáneamente con el fin de la modernidad, siendo la revolución de 1910 el primer hecho histórico mexicano con rasgos contemporáneos, la Constitución de 1917 su fundamento ideológico, el Maximato permitiría su implementación y la industrialización impulsada por Lázaro Cárdenas desde 1940 su consolidación como etapa histórica que continuaría hasta la actualidad. | — | Historia de México#1241-1297 |
| 13 | [ ] | Historia de México | En 1910 inició la Revolución Mexicana, un periodo de grandes conflictos entre múltiples facciones y con distintos principios durante el transcurso de la misma: su fecha de terminación es actualmente objeto de debate entre distintos historiadores, pues la sitúan en 1917, 1920 o 1924. | — | Historia de México#1773-1817 |
| 14 | [ ] | Historia de México | Y gracias al impulso nacionalista que habían dado los emperadores por el interés del pasado mexicano que los intelectuales comienzan a escribir sobre la historia de México y el mundo prehispánico para hallar la identidad mexicana. | — | Historia de México#34914-34950 |
| 15 | [ ] | Historia de México | He esperado pacientemente el día en que el pueblo de la República Mexicana estuviera preparado para escoger y cambiar a sus gobernantes en cada elección, sin peligro de revoluciones armadas y sin daño para el crédito y el progreso nacionales. | — | Historia de México#41225-41265 |
| 16 | [ ] | Historia de México | Apenas terminó el mes patrio de septiembre con las festividades y el 5 de octubre, Madero publicó el Plan de San Luis. | Plan de San Luis, Madero | Historia de México#42155-42177 |
| 17 | [ ] | Historia de México | Al triunfo del Plan de San Luis, Madero permitió la llegada de un presidente interino porfiriano, Francisco León de la Barra, que organizara unas elecciones el 1 de octubre de 1911. | Plan de San Luis, Madero | Historia de México#43247-43278 |
| 18 | [ ] | Historia de México | Aquel sería para muchos el punto cumbre de la revolución mexicana. | — | Historia de México#48413-48424 |
| 19 | [ ] | Historia de México | Para legitimar su gobierno tras las luchas internas y golpes de estado, se creó el concepto de Revolución Mexicana como una sola revolución sin lucha de facciones. | — | Historia de México#49647-49674 |
| 20 | [ ] | Historia de México | En ese momento Cárdenas se encontraba reformando al partido de un mismo grupo político a un partido de sectores (campesino, obrero, militar y popular): el Partido de la Revolución Mexicana (PRM) | — | Historia de México#58503-58535 |
| 21 | [ ] | Historia de México | El 18 de enero de 1946 el Partido de la Revolución Mexicana (PRM) acordó su transformación al Partido Revolucionario Institucional (PRI) bajo los lemas de civismo y democracia. | — | Historia de México#64883-64911 |
| 22 | [ ] | Historia de México | La llamada “familia revolucionaria” logró controlar la política mexicana, había gobernado y establecido los lineamientos políticos que deberían seguir los gobiernos herederos de la Revolución. | — | Historia de México#66124-66149 |
| 23 | [ ] | Miguel Hidalgo y Costilla | En Ibarra Palafox, Francisco, ed. Juicios y causas procesales en la independencia mexicana (1ª edición). | — | Miguel Hidalgo y Costilla#9258-9273 |
| 24 | [ ] | Porfiriato | La crisis de 1907 y las luchas de sucesión en el seno del gobierno favorecieron el inicio de la revolución mexicana, dirigida por Francisco I. Madero. | crisis de 1907, Madero | Porfiriato#709-735 |
| 25 | [ ] | Porfiriato | México: del antiguo régimen a la revolución. | — | Porfiriato#5112-5119 |
| 26 | [ ] | Revolución mexicana | Los antecedentes del conflicto se remontan a la situación de México bajo la dictadura conocida como el porfiriato. | — | Revolución mexicana#29-47 |
| 27 | [ ] | Revolución mexicana | Algunas fuentes lo sitúan el 5 de febrero de 1917, con la proclamación de la Constitución mexicana, el 1 de diciembre de 1924 con la presidencia de Plutarco Elías Calles o el 17 de julio de 1928 con el asesinato del reelecto presidente Álvaro Obregón. | — | Revolución mexicana#679-724 |
| 28 | [ ] | Revolución mexicana | Entonces, Madero, de acuerdo con el Plan de San Luis, fue nombrado presidente provisional y constituyó su Consejo de Estado, en el que incluía entre otros a Venustiano Carranza, su hermano Gustavo y José María Pino Suárez. | Plan de San Luis, Madero | Revolución mexicana#4236-4273 |
| 29 | [ ] | Revolución mexicana | El mayor opositor del desarme y desmovilización de las tropas fue Emiliano Zapata, quien pedía que primero se cumpliera lo prometido por Madero en el Plan de San Luis en lo concerniente a restitución de tierras. | Plan de San Luis, Madero | Revolución mexicana#4559-4595 |
| 30 | [ ] | Revolución mexicana | Madero formó el Partido Constitucional Progresista, basado en el Antirreeleccionista y el Plan de San Luis, el cual presentaba como fórmula a Madero en la presidencia y José María Pino Suárez para la vicepresidencia. | Plan de San Luis, Madero | Revolución mexicana#5018-5052 |
| 31 | [ ] | Revolución mexicana | No se tiene un número exacto de la cantidad de muertos que hubo durante la Revolución mexicana. | — | Revolución mexicana#12019-12036 |
| 32 | [ ] | Revolución mexicana | Las fuentes disponibles no concuerdan en cuanto al fin de la Revolución mexicana. | — | Revolución mexicana#12342-12355 |
| 33 | [ ] | Revolución mexicana | La Revolución mexicana conllevó varios cambios sociales. | — | Revolución mexicana#12503-12510 |
| 34 | [ ] | Revolución mexicana | En la República Mexicana existen varios museos y monumentos dedicados a este conflicto bélico. | — | Revolución mexicana#13008-13022 |
| 35 | [ ] | Revolución mexicana | Museo de la Revolución Mexicana.- Este museo se encuentra en la ciudad de Puebla, y es la antigua casa de Aquiles Serdán. | — | Revolución mexicana#13150-13172 |
| 36 | [ ] | Revolución mexicana | El 16 de junio del año 2006, mediante decreto del Congreso de la Unión, el año 2010 fue declarado como el «año del Bicentenario del inicio del movimiento de Independencia Nacional y del Centenario del inicio de la Revolución Mexicana», y el 29 de octubre de 2007, por acuerdo de la LX Legislatura del Senado de la República, se creó la Comisión especial encargada de los festejos del bicentenario de la Independencia y … | — | Revolución mexicana#13339-13450 |
| 37 | [ ] | Revolución mexicana | Durante el conflicto armado muchos camarógrafos mexicanos siguieron los acontecimientos de la revolución. | — | Revolución mexicana#13720-13733 |
| 38 | [ ] | Revolución mexicana | Wikiquote alberga frases célebres de o sobre Revolución mexicana. | — | Revolución mexicana#14452-14461 |
| 39 | [ ] | Revolución mexicana | «Comisión Especial Encargada de los Festejos del Bicentenario de la Independencia y del Centenario de la Revolución Mexicana del Senado de la República». | — | Revolución mexicana#14481-14504 |
| 40 | [ ] | Revolución mexicana | «Portal de la Revolución mexicana». | — | Revolución mexicana#14581-14586 |

---

## C2 (causalidad)

**Pregunta:** ¿Por qué cayó el Imperio Azteca?
**Puntos clave (guía, no juez):** Alianzas con tlaxcaltecas; enfermedades; superioridad militar española; muerte de Moctezuma
**Anotada:** [ ] sí   (marca esta casilla al terminar la pregunta)

| # | Evidencia | Artículo | Oración | Puntos clave en la oración | Ref |
|---|---|---|---|---|---|
| 1 | [ ] | Civilización maya | En el siglo xvi el Imperio español conquistó la región mesoamericana, y tras una larga serie de campañas militares la última ciudad maya cayó en 1697. | — | Civilización maya#429-455 |
| 2 | [ ] | Civilización maya | El florecimiento cultural del Preclásico Tardío experimentó un colapso en el siglo i d. C., y muchas de las grandes ciudades mayas de esta época fueron abandonados; se desconoce la causa de este colapso. | — | Civilización maya#1948-1982 |
| 3 | [ ] | Civilización maya | Después de la caída de Chichén Itzá, la región maya carecía de un poder dominante hasta el surgimiento de la ciudad de Mayapán en el siglo xii. | — | Civilización maya#3409-3436 |
| 4 | [ ] | Conquista de México | Los españoles basaban su riqueza en las encomiendas, pero debido a que la población nativa había sido diezmada por las campañas de conquista y las enfermedades, los colonos estaban ansiosos de conseguir nuevas oportunidades de medro. | enfermedades | Conquista de México#689-725 |
| 5 | [ ] | Conquista de México | A pesar del anuncio de exterminio los caballos, las armas y las tácticas militares españolas se impusieron a los tlaxcaltecas, quienes atacaban de forma inarticulada, sin cooperar entre sí, tratando siempre de capturar enemigos en lugar de liquidarlos. | superioridad militar española | Conquista de México#7332-7370 |
| 6 | [ ] | Cultura teotihuacana | De Teotihuacán a los aztecas: antología de fuentes e interpretaciones históricas, 123-129. | — | Cultura teotihuacana#13172-13184 |
| 7 | [ ] | Hernán Cortés | Los aztecas creían en un mito de origen tolteca, según el cual el mundo en que vivían debía desaparecer. | — | Hernán Cortés#4517-4536 |
| 8 | [ ] | Hernán Cortés | Por esto, los aztecas consideraban que los españoles eran teules (de teolt, dios) que marcharían sobre ellos inexorablemente. | — | Hernán Cortés#4642-4660 |
| 9 | [ ] | Hernán Cortés | Cortés, al informarse de qué se trataba, animó a líder totonaca Quauhtlaebana a liberarse del yugo azteca. | — | Hernán Cortés#5433-5450 |
| 10 | [ ] | Historia de México | Su muerte significó el fin de la Unidad Mixteca de Oaxaca. | — | Historia de México#5284-5295 |
| 11 | [ ] | Historia de México | Así estaba por iniciar el Imperio Azteca. | — | Historia de México#6060-6067 |
| 12 | [ ] | Historia de México | A su muerte, Nezahualpilli recibió el trono de Texcoco y el Imperio Azteca le envió a Chalchiunenetzin como concubina para casarse. | — | Historia de México#6282-6303 |
| 13 | [ ] | Historia de México | Esto supuso el comienzo del expansionismo azteca pues ordenó ataques contra tarascos, matlatzincas, chontales y cuitlatecos. | — | Historia de México#6528-6544 |
| 14 | [ ] | Historia de México | Su avance destruyó por completo a la Gran Tenochtitlán, se sabe que mientras los españoles saqueaban los templos, los tlaxcaltecas aliados capturaban niños y mujeres para comer sus carnes en sacrificio ritual. | — | Historia de México#8706-8738 |
| 15 | [ ] | Historia de México | Esa opulencia que crecía en la Nueva España fue pronto codiciada por los países europeos enemigos de España, así que aprovechando los rumores de las muchas enfermedades del rey y la desatención que ponía sobre los reinos, iniciaron ataques piratas en las costas del Golfo de México. | enfermedades | Historia de México#12105-12152 |
| 16 | [ ] | Imperio azteca | El Imperio mexica o Triple Alianza (del náhuatl: Exkan Tlahtoloyan o Ēxcān Tlahtōlōyān ‘Los tres lugares donde se dan órdenes’), llamado también Imperio azteca y —con más precisión— Imperio tenochca, fue un imperio organizado en una confederación compleja, multiétnica y flexible de ciudades estado con situaciones políticas diversas, que existió en el área central de Mesoamérica durante el Posclásico Tardío hasta la … | — | Imperio azteca#3-67 |
| 17 | [ ] | Imperio azteca | A partir de entonces, los territorios del Imperio azteca se fueron ampliando hasta llegar a ocupar el centro de México, la zona central de Oaxaca, la costa del golfo de México, Guerrero y el Soconusco. | — | Imperio azteca#219-254 |
| 18 | [ ] | Imperio azteca | El fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españoles —en alianza con los tlaxcaltecas y totonacas, entre otros pueblos indígenas— derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco. | — | Imperio azteca#254-288 |
| 19 | [ ] | Imperio azteca | Fue encabezado por los mexicas —mal conocidos como aztecas—, un pueblo que, de acuerdo con algunos documentos históricos como la Tira de la Peregrinación, era originario de un sitio —tal vez mítico— conocido como Aztlán, al que se suele ubicar fuera de los confines de Mesoamérica. | — | Imperio azteca#1244-1290 |
| 20 | [ ] | Imperio azteca | Originalmente, el imperio azteca era una alianza suelta entre tres ciudades: Tenochtitlan, Texcoco y el socio menor, Tlacopan. | — | Imperio azteca#2235-2253 |
| 21 | [ ] | Imperio azteca | Aquí los mexicas se limitaron a construir un campamento comercial, el cual era el medio de contacto entre el Imperio azteca y los reinos fragmentados de los mayas. | — | Imperio azteca#9978-10006 |
| 22 | [ ] | Imperio azteca | El actual territorio del estado México fue el principal y mayor tributario de maderas, carnes y vegetales del Imperio azteca. | — | Imperio azteca#10197-10217 |
| 23 | [ ] | Imperio azteca | Y de donde se obtuvo parte de lo que fue la cultura azteca. | — | Imperio azteca#10217-10230 |
| 24 | [ ] | Imperio azteca | Aztec Warfare: Imperial Expansion and Political Control (en inglés). | — | Imperio azteca#10716-10725 |
| 25 | [ ] | Imperio azteca | Santamarina Novillo, Carlos, El sistema de dominación azteca: el Imperio Tepaneca. | — | Imperio azteca#10875-10886 |
| 26 | [ ] | Imperio azteca | Wikimedia Commons alberga una categoría multimedia sobre Imperio azteca. | — | Imperio azteca#10948-10957 |
| 27 | [ ] | Moctezuma II | Sin embargo, sus gobiernos no duraron mucho tiempo, pues el imperio caería bajo control español en agosto de 1521, un año después de su muerte. | — | Moctezuma II#692-717 |
| 28 | [ ] | Moctezuma II | La mayoría de las reformas y políticas de Moctezuma no durarían mucho después de su muerte, pues tras pasar un año de su muerte, las fuerzas castellanas y tlaxcaltecas lograron derrotar a las fuerzas del Imperio mexica durante la conquista de México, cayendo bajo control europeo el 13 de agosto de 1521. | muerte de Moctezuma | Moctezuma II#2633-2685 |
| 29 | [ ] | Moctezuma II | Este acueducto fue destruido a menos de un año de la muerte de Moctezuma, durante el sitio de Tenochtitlan en las etapas tardías de la conquista de México en mayo de 1521, cuando las fuerzas castellanas decidieron destruirlo para cortar el suministro de agua de la ciudad. | muerte de Moctezuma | Moctezuma II#4036-4083 |
| 30 | [ ] | Moctezuma II | Parte de Tenochtitlán se inundó. | — | Moctezuma II#12428-12433 |
| 31 | [ ] | Moctezuma II | A pesar de que soldados como Díaz del Castillo dicen que este fue el motivo principal del arresto, algunos historiadores contemporáneos a la Conquista de México, como Francisco López de Gómara, sospecharon que Cortés ya planeaba arrestar a Moctezuma para usurpar el dominio de México antes de conocerlo, y la historia de la muerte de Escalante fue simplemente una excusa para ejecutar este plan. | muerte de Moctezuma | Moctezuma II#14852-14916 |
| 32 | [ ] | Virreinato de Nueva España | La conquista de Yucatán fue la más tardía de las que finalmente integraron el virreinato de la Nueva España, ya que los últimos reductos mayas no fueron dominados íntegramente hasta el año de 1697 —es decir, más de siglo y medio después de la conquista de México—, con la conquista de Tayasal. | — | Virreinato de Nueva España#1074-1126 |
| 33 | [ ] | Virreinato de Nueva España | Varias premoniciones en años anteriores hicieron creer a Moctezuma Xocoyotzin, soberano azteca o tlatoani, que el fin de su imperio estaba cerca. | — | Virreinato de Nueva España#1396-1418 |
| 34 | [ ] | Virreinato de Nueva España | Los españoles decidieron aprovechar la situación para obtener riquezas e influencia dentro de la corte azteca. | — | Virreinato de Nueva España#1460-1476 |
| 35 | [ ] | Virreinato de Nueva España | Las estrategias indígenas con la ayuda de los tlatelolcas lograron echar de la ciudad a los conquistadores, que en el acto perdieron cerca de mil soldados y varios caudales de dinero y oro. | — | Virreinato de Nueva España#1550-1583 |
| 36 | [ ] | Virreinato de Nueva España | Sin embargo, desde el transcurso mismo de la conquista ocurrió un brusco descenso en la población indígena de Nueva España, causado por el contacto con el mundo español, debido a las enfermedades traídas por los conquistadores, como viruela y tuberculosis, a las cuales los lugareños no podían resistir por su falta de defensas. | enfermedades | Virreinato de Nueva España#9016-9069 |
| 37 | [ ] | Virreinato de Nueva España | Los indígenas causaban muchos problemas a sus amos españoles, como rebeldía y poca resistencia a las enfermedades. | enfermedades | Virreinato de Nueva España#10169-10186 |

---

## C3 (causalidad)

**Pregunta:** ¿Qué provocó la Guerra de Reforma?
**Puntos clave (guía, no juez):** Constitución de 1857; liberales vs conservadores; Ley Juárez; Ley Lerdo
**Anotada:** [ ] sí   (marca esta casilla al terminar la pregunta)

| # | Evidencia | Artículo | Oración | Puntos clave en la oración | Ref |
|---|---|---|---|---|---|
| 1 | [ ] | Benito Juárez | Juárez es considerado un símbolo de soberanía nacional, resistencia, libertad y legalidad al liderar a su país durante la Guerra de Reforma y la Segunda Intervención Francesa. | Ley Juárez | Benito Juárez#71-98 |
| 2 | [ ] | Benito Juárez | A pesar de tratarse de un presidente sin antecedentes militares, fue una figura clave tanto en la Guerra de Reforma como en la segunda intervención francesa. | — | Benito Juárez#180-206 |
| 3 | [ ] | Benito Juárez | En diciembre de ese mismo año, durante el golpe de Estado ocasionado por conflictos entre conservadores que apoyaban a la iglesia y liberales que habían apoyado la separación Iglesia-Estado, Juárez fue apresado por las fuerzas del propio Comonfort. | liberales vs conservadores, Ley Juárez | Benito Juárez#2719-2757 |
| 4 | [ ] | Benito Juárez | Sin embargo, el propio Comonfort, quien había organizado su propio golpe de Estado contra su gobierno, acudió un mes después a pedirle a Juárez su ayuda, ya que tanto liberales como conservadores no habían llegado a ningún acuerdo y el gobierno se debilitaba cada vez más. | liberales vs conservadores, Ley Juárez | Benito Juárez#2795-2841 |
| 5 | [ ] | Benito Juárez | Esto ocasionó la guerra de los Tres Años. | — | Benito Juárez#2900-2908 |
| 6 | [ ] | Benito Juárez | La Iglesia católica estaba fuertemente disgustada con la aplicación de las Leyes de Reforma en México. | — | Benito Juárez#3837-3853 |
| 7 | [ ] | Benito Juárez | Exactamente un año antes de que terminara el período constitucional de Juárez, González Ortega entró a la oficina de Lerdo de Tejada preguntando si se le entregaría la presidencia ese día o al siguiente, argumentando que la Constitución de 1857 no era muy clara, respecto a lo cual, Lerdo le pidió unas horas para responder. | Constitución de 1857, Ley Juárez, Ley Lerdo | Benito Juárez#4919-4974 |
| 8 | [ ] | Benito Juárez | (En referencia a los víveres para el ejército republicano). | — | Benito Juárez#9645-9654 |
| 9 | [ ] | Benito Juárez | Ardo en deseos de que esta guerra se acabe, ¿Por qué siempre es el pobre el que sufre más? | — | Benito Juárez#9846-9865 |
| 10 | [ ] | Benito Juárez | La Reforma (Primera edición). | — | Benito Juárez#16041-16045 |
| 11 | [ ] | Conquista de México | Los que estaban a favor de la aventura, no necesitaban artificios para decidirse: Pues, ¿de qué condición somos los españoles para no ir adelante, y estarnos en partes que no tengamos provecho de guerra? | — | Conquista de México#6439-6473 |
| 12 | [ ] | Guerra de Independencia de México | Por otra parte, las guerras en Europa habían provocado escasez y desempleo. | — | Guerra de Independencia de México#8359-8371 |
| 13 | [ ] | Guerra de Independencia de México | Durante este período cobra importancia el posicionamiento ideológico de la causa insurgente. | — | Guerra de Independencia de México#8532-8544 |
| 14 | [ ] | Guerra de Reforma | La Guerra de Reforma, también conocida como la guerra de los tres años, fue una guerra civil que aconteció en México desde el 17 de diciembre de 1857 al 11 de enero de 1861, como consecuencia de la promulgación de la Constitución de 1857 y en especial de las llamadas Leyes de Reforma. | Constitución de 1857 | Guerra de Reforma#4-57 |
| 15 | [ ] | Guerra de Reforma | Sin embargo, mientras esos ordenamientos se convertían en realidad, la guerra civil había agotado y empobrecido al país. | — | Guerra de Reforma#1094-1112 |
| 16 | [ ] | Guerra de Reforma | La Reforma y el Segundo Imperio (1853-1867). | — | Guerra de Reforma#1840-1847 |
| 17 | [ ] | Guerra de Reforma | Leyes de Reforma y Etapas de la Reforma en México. | — | Guerra de Reforma#1857-1867 |
| 18 | [ ] | Historia de México | La Modernidad igualmente llegaría paulatinamente, a través de ideólogos que desde el siglo XVIII proponían ideas transformadoras: el reformismo juarista, intentos de reforma en 1892 y 1903 por parte de los "científicos" del Porfiriato, la revolución de 1910 y la Constitución de 1917. | — | Historia de México#1128-1171 |
| 19 | [ ] | Historia de México | Y en el ala derecha, un joven militar indígena que se había unido a los liberales en la guerra de Reforma, estaba a cargo: Porfirio Díaz. | — | Historia de México#31550-31576 |
| 20 | [ ] | Historia de México | Fue el círculo cercano a Juárez quien le hizo ver la guerra ya no era por defensa de las leyes liberales o la reforma, sino por soberanía nacional. | Ley Juárez | Historia de México#33428-33456 |
| 21 | [ ] | Historia de México | Por eso cuando Juárez retornó triunfal como presidente a la Ciudad de México en julio de 1867, la mejor forma en que pudo legitimar el poder republicano fue restablecer la Constitución de 1857, ejecutar de nuevo las Leyes de Reforma y llamar a elecciones el 22 de septiembre. | Constitución de 1857, Ley Juárez | Historia de México#34498-34546 |
| 22 | [ ] | Historia de México | A finales de 1870 Juárez se preparaba para un nuevo proceso electoral contra Díaz y Lerdo de Tejada, pero la libertad de expresión y su forma autoritaria de gobernar por medio de vetos constantes al congreso jugaban en su contra. | Ley Juárez, Ley Lerdo | Historia de México#35175-35215 |
| 23 | [ ] | Historia de México | Tras la muerte de Juárez, los adheridos al Plan de la Noria sin motivo para combatir, acordaron el cese al fuego tras la amnistía emitida por el interino Sebastián Lerdo de Tejada había expedido una amnistía. | Ley Juárez, Ley Lerdo | Historia de México#35782-35818 |
| 24 | [ ] | Historia de México | Nadie esperaba que Lerdo fuese más radical que Juárez pues elevó las Leyes de Reforma a nivel constitucional, así los estados que habían intentado sortearlas ya no tenían pretexto de no cumplirlas y eso abarcó también a los funcionarios de gobierno. | Ley Juárez, Ley Lerdo | Historia de México#36043-36084 |
| 25 | [ ] | Historia de México | Quizá aquel tiempo marcó el inicio del desgaste del régimen. | — | Historia de México#40298-40308 |
| 26 | [ ] | Historia de México | Una suma de factores serán la causa de la caída del porfiriato: Los grupos anarquistas surgidos en 1900 con Antonio Horcasitas y los hermanos Flores Magón; el surgimiento del Manifiesto del Partido Liberal de 1906; las represiones sangrientas a obreros, indígenas y campesinos; la concentración de la riqueza en el 1 % de la población; la crisis económica de 1908; pero nada será tan relevante ni determinante como la … | — | Historia de México#41339-41411 |
| 27 | [ ] | Historia de México | El problema del hueco legal sobre la expropiación de tierras comunales que habían heredado Juárez y Lerdo desde hacía medio siglo, al fin estalló. | Ley Juárez, Ley Lerdo | Historia de México#43647-43671 |
| 28 | [ ] | Historia de México | Promulgó leyes en favo del divorcio, del trabajo, de previsión social. | — | Historia de México#50519-50530 |
| 29 | [ ] | Historia de México | Si en la guerra de Reforma había surgido para que la Iglesia dejara de meterse en asuntos del Estado, ahora el Estado quería meterse en los asuntos de la Iglesia. | — | Historia de México#51674-51704 |
| 30 | [ ] | Historia de México | Mientras la clase intelectual permanecía absorta en su mundo, la guerra cristera se recrudecía. | — | Historia de México#53202-53216 |
| 31 | [ ] | Historia de México | La historia y su gabinete lo apodarían El corrido de la revolución. | — | Historia de México#55200-55212 |
| 32 | [ ] | Historia de México | Así, en lo alto del Frontón México, el 14 de septiembre de 1939, junto con los grupos progresistas católicos, ex maderistas, ex vasconcelistas y otros personajes traicionados por la revolución, se leen los principios de doctrina que crean al Partido Acción Nacional, PAN. | — | Historia de México#59497-59540 |
| 33 | [ ] | Historia de México | El estado de guerra en México y el mundo, provoca la inflación desacelerada de 1943. | — | Historia de México#63277-63292 |
| 34 | [ ] | Historia de México | La corrupción, presente en el sistema político desde tiempos del alemanismo en los años 1940, tuvo un auge significativo, los excedentes presupuestarios dirigidos a múltiples instituciones públicas, no llegaron a sus proyectos finales, mientras muchos funcionarios se enriquecen proporcionalmente. | — | Historia de México#68531-68570 |
| 35 | [ ] | Moctezuma II | A inicios de su reinado, en 1505, hubo una fuerte hambruna que duró 3 años a causa de una sequía que azotó a gran parte del imperio. | — | Moctezuma II#2753-2780 |
| 36 | [ ] | Moctezuma II | La intención de las guerras floridas ha sido interpretada a lo largo de la mayoría de los años como guerras puramente religiosas, con el único fin de facilitar la captura de prisioneros de guerra para sacrificio humano. | — | Moctezuma II#6758-6795 |
| 37 | [ ] | Porfiriato | Porfirio Díaz fue un militar que destacó por su participación en la guerra de Reforma y en la Intervención francesa, en la que logró recuperar para la causa republicana la Ciudad de México y Puebla. | — | Porfiriato#387-422 |
| 38 | [ ] | Porfiriato | El clero recobró gran parte del poder perdido con las Leyes de Reforma y la guerra de los Tres Años. | — | Porfiriato#4819-4839 |
| 39 | [ ] | Revolución mexicana | Los argumentos del pintor Gerardo Murillo (conocido por su seudónimo «Dr. Atl») y de Obregón convencieron a los dirigentes de la organización de aliarse con la revolución constitucionalista, misma que ya había definido su vocación social durante la guerra. | — | Revolución mexicana#10043-10082 |
| 40 | [ ] | Virreinato de Nueva España | Desde principios del siglo XIX, el virreinato cayó en crisis (agravada por la guerra contra las tropas francesas en la Península) y su consecuencia directa fue la crisis política en México de 1808 que acabó con el gobierno de José de Iturrigaray y, más adelante, dio pie a la Conjura de Valladolid y la conspiración de Querétaro. | — | Virreinato de Nueva España#567-624 |

---

## C4 (causalidad)

**Pregunta:** ¿Por qué terminó el Porfiriato?
**Puntos clave (guía, no juez):** Revolución Mexicana; renuncia de Díaz en 1911; Plan de San Luis; descontento social
**Anotada:** [ ] sí   (marca esta casilla al terminar la pregunta)

| # | Evidencia | Artículo | Oración | Puntos clave en la oración | Ref |
|---|---|---|---|---|---|
| 1 | [ ] | Benito Juárez | Ardo en deseos de que esta guerra se acabe, ¿Por qué siempre es el pobre el que sufre más? | — | Benito Juárez#9846-9865 |
| 2 | [ ] | Conquista de México | Cuando Rodrigo de Figueroa, juez de residencia de La Española, se enteró de los planes de Velázquez, consideró que la pugna no era beneficiosa para la corona y por tal motivo envió al oidor (juez) Lucas Vázquez de Ayllón junto con el alguacil de Santo Domingo Luis de Sotelo y el escribano Pedro de Ledesma para detener la expedición. | Plan de San Luis | Conquista de México#9789-9848 |
| 3 | [ ] | Cultura teotihuacana | Por ejemplo, George Cowgill y Evelyn Rattray han propuesto que la decadencia de Teotihuacán ocurrió entre cincuenta y cien años antes de la fecha sugerida por Millon. | — | Cultura teotihuacana#3781-3808 |
| 4 | [ ] | Emiliano Zapata | Tras esta entrevista decidieron tomar las armas Pablo Torres Burgos, Emiliano Zapata, Rafael Merino y cerca de 60 campesinos, entre los que se encontraban Catarino Perdomo, Próculo Capistrán, Manuel Rojas, Juan Sánchez, Cristóbal Gutiérrez, Julio Díaz, Zacarías y Refugio Torres, Jesús Becerra, Bibiano Cortés, Serafín Plascencia, Maurilio Mejía y Celestino Benítez: el 10 de marzo de 1911, reunidos durante la feria de … | renuncia de Díaz en 1911, Plan de San Luis | Emiliano Zapata#979-1053 |
| 5 | [ ] | Emiliano Zapata | Las reivindicaciones zapatistas (que serían contenidas en el plan de Ayala de noviembre de 1911) suponían una reforma agraria radical —«La tierra es de quien la trabaja», frase de Teodoro Flores, padre de los hermanos Flores Magón, que se convertiría en lema de su lucha—[cita requerida] inaceptable para los sucesores de Porfirio Díaz. | renuncia de Díaz en 1911 | Emiliano Zapata#1135-1188 |
| 6 | [ ] | Emiliano Zapata | En él se exigía la redención de los indígenas y la repartición de los latifundios creados durante el porfiriato. | — | Emiliano Zapata#1725-1744 |
| 7 | [ ] | Historia de México | Los criterios sobre qué hechos considerarlos como coyuntura y el criterio para ver qué tan relevantes fueron pueden diferir enormemente entre historiadores. | — | Historia de México#317-339 |
| 8 | [ ] | Historia de México | Al menos entre las élites porfiristas se identifica plenamente la intención de vivir y pensar de un modo secularista, copiando rasgos de Europa. | — | Historia de México#1171-1194 |
| 9 | [ ] | Historia de México | El ascenso de Porfirio Díaz al poder en 1876 empezó un periodo conocido como el Porfiriato, mismo que duró hasta 1911 con su exilio. | renuncia de Díaz en 1911 | Historia de México#1749-1773 |
| 10 | [ ] | Historia de México | Pero también es una década de momentos obscuros como el saqueo de Puebla orillado por una rencilla entre Palafox y el nuevo virrey conde de Salvatierra, que culminó en la salida de Palafox de la Nueva España en 1648. | — | Historia de México#11690-11729 |
| 11 | [ ] | Historia de México | En 1655 la detención del maestro mayor de la catedral Melchor Pérez de Soto por poseer libros prohibidos en su biblioteca personal, acabó con su muerte en las celdas inquisitoriales el 16 de marzo y la impresionante colección de 1 600 libros perdidos para siempre. | — | Historia de México#11798-11843 |
| 12 | [ ] | Historia de México | Para cuando el gobierno juarista se estableció en San Luis Potosí a mediados de 1863, el ejército francés ya tenía órdenes de acabar con cualquier alzamiento armado que atentara contra el nuevo plan. | Plan de San Luis | Historia de México#32228-32261 |
| 13 | [ ] | Historia de México | Así acabó poco a poco con los lerdistas. | — | Historia de México#37170-37178 |
| 14 | [ ] | Historia de México | Eso sumado a los aires de lucha obrera y social que se daban en todo el mundo, marcaron la última década del Porfiriato. | — | Historia de México#40333-40356 |
| 15 | [ ] | Historia de México | Una suma de factores serán la causa de la caída del porfiriato: Los grupos anarquistas surgidos en 1900 con Antonio Horcasitas y los hermanos Flores Magón; el surgimiento del Manifiesto del Partido Liberal de 1906; las represiones sangrientas a obreros, indígenas y campesinos; la concentración de la riqueza en el 1 % de la población; la crisis económica de 1908; pero nada será tan relevante ni determinante como la … | — | Historia de México#41339-41411 |
| 16 | [ ] | Historia de México | Don Porfirio es militar de carrera y político de trayectoria, lidió con el país casi 30 años. | — | Historia de México#43095-43112 |
| 17 | [ ] | Historia de México | Aquel fue el fin del Porfiriato. | — | Historia de México#43232-43238 |
| 18 | [ ] | Historia de México | Aquella fue la Batalla de Celaya. | — | Historia de México#47534-47540 |
| 19 | [ ] | Historia de México | Aquel acto, en medio de la Gran Guerra, también sacudió a los norteamericanos que intentaban mantener distancia del conflicto europeo; sobre todo después de que la inteligencia norteamericana descubriera que la revolución mexicana había provocado avances tecnológicos de preocupación como el cañón Mondragón. | Revolución Mexicana | Historia de México#47852-47895 |
| 20 | [ ] | Historia de México | Ordenó la construcción de un monumento en memoria de Obregón en el sitio donde lo asesinaron, terminó una presa en Aguascalientes y logró que en su gobierno se concluyera un espacio que estaba en obra negra desde el porfiriato: El Palacio de Bellas Artes. | — | Historia de México#55855-55899 |
| 21 | [ ] | Historia de México | No había mejor opción de continuidad para el progreso nacional y la permanencia silenciosa de Calles tras bambalinas. | — | Historia de México#55992-56010 |
| 22 | [ ] | Historia de México | Aquel fue el fin del maximato. | — | Historia de México#57226-57232 |
| 23 | [ ] | Moctezuma II | Historiadores modernos, como Matthew Restall, por lo tanto, han llegado a la conclusión de que es posible que algunos de los eventos descritos hayan sucedido, pero que no se prueba que Moctezuma haya verdaderamente interpretado estas señales como el anuncio del fin de su imperio. | — | Moctezuma II#12557-12602 |
| 24 | [ ] | Pancho Villa | Doroteo Arango (ahora bajo el nombre de Francisco Villa) acabó con la vida de su rival y los hombres de este, empezando a seguir una causa en defensa de la clase popular que era fuertemente explotada, al punto de comparación con la esclavitud. | — | Pancho Villa#501-544 |
| 25 | [ ] | Pancho Villa | Aunque este se debió haber llamado Agustín Villa Arango, se desconocen las causas de por qué Jesús Villa no dio nombre a su hijo y de por qué este recibió el apellido de su madre. | — | Pancho Villa#644-679 |
| 26 | [ ] | Pancho Villa | La serie de victorias de Villa desde el comienzo de la Revolución mexicana fue fundamental para la caída del dictador Porfirio Díaz, el triunfo de Francisco Madero y la derrota del usurpador Victoriano Huerta. | Revolución Mexicana | Pancho Villa#6577-6611 |
| 27 | [ ] | Porfiriato | El porfiriato o porfirismo fue un período de la historia de México en el que el gobierno estuvo bajo el control (total o mayoritario) del militar, político y dictador Porfirio Díaz, entre el 28 de noviembre de 1876 y el 27 de mayo de 1911. | renuncia de Díaz en 1911 | Porfiriato#2-47 |
| 28 | [ ] | Porfiriato | En el porfiriato la política se aplicó de tal manera que todo quedaba subordinado al presidente. | — | Porfiriato#47-63 |
| 29 | [ ] | Porfiriato | La literatura fue el campo cultural que más avances tuvo en el Porfiriato. | — | Porfiriato#1895-1908 |
| 30 | [ ] | Porfiriato | La primera etapa del porfiriato empieza en 1877 y termina en el inicio de tercer periodo presidencial de Porfirio Díaz (1888) o cuando se eliminó toda restricción legal a la reelección indefinida (1890). | — | Porfiriato#3204-3237 |
| 31 | [ ] | Porfiriato | Además una represión a la prensa libre, que era silenciada ya fuese por medio de sobornos o bien por torturas y desapariciones. | — | Porfiriato#4739-4761 |
| 32 | [ ] | Porfiriato | El Porfiriato vida social México: Hermes (1972). | — | Porfiriato#5050-5057 |
| 33 | [ ] | Porfiriato | El Porfiriato Vida política interior 2.ª Parte México: Hermes (1972). | — | Porfiriato#5064-5074 |
| 34 | [ ] | Revolución mexicana | Los antecedentes del conflicto se remontan a la situación de México bajo la dictadura conocida como el porfiriato. | — | Revolución mexicana#29-47 |

---

## V1 (comparativa)

**Pregunta:** ¿En qué se diferencian los mayas y los olmecas?
**Puntos clave (guía, no juez):** Olmecas: civilización madre, cabezas colosales, zona costera; Mayas: escritura, calendario, ciudades-estado
**Anotada:** [ ] sí   (marca esta casilla al terminar la pregunta)

| # | Evidencia | Artículo | Oración | Puntos clave en la oración | Ref |
|---|---|---|---|---|---|
| 1 | [ ] | Civilización maya | La cultura maya fue una civilización mesoamericana que se desarrolló en lo que actualmente comprenden los territorios de Guatemala y México (en la península de Yucatán, Chiapas y Tabasco) principalmente, así como en Belice, y la parte occidental de Honduras y El Salvador (Correspondiendo a los departamentos respectivos de Honduras los de Copán, Cortés, Santa Bárbara, Ocotepeque y Lempira y El Salvador los de Santa … | — | Civilización maya#3-78 |
| 2 | [ ] | Civilización maya | El territorio de los mayas y los mayas mantuvieron una relación dinámica con las culturas vecinas, incluyendo los olmecas, los mixtecos, los de Teotihuacán, los aztecas, y otros. | Olmecas, Mayas | Civilización maya#1111-1139 |
| 3 | [ ] | Civilización maya | Los estudios modernos consideran estos períodos como divisiones arbitrarias de la cronología maya, en lugar de ser indicativos de la evolución cultural de los mayas o de su decadencia. | Mayas | Civilización maya#1586-1615 |
| 4 | [ ] | Civilización maya | La ocupación maya de Aguada Fénix en México ha sido fechada en el 1,000 a. C. colocándola como la ciudad maya más antigua, y marca el paso de la civilización maya del nomadismo a un estilo de vida sedentario, y el inicio de la construcción de las ciudades-estado mayas; Ceibal en Guatemala data del 950 a. C. y Cuello, Belice, ha sido fechada alrededor de 900 a. C. | Mayas, ciudades-estado | Civilización maya#1652-1720 |
| 5 | [ ] | Civilización maya | El tzolk'in, el calendario ritual de 260 días, sigue en uso en las comunidades mayas modernas en las tierras altas de Guatemala y Chiapas, y millones de hablantes de idiomas mayas habitan el territorio en el que sus antepasados desarrollaron su civilización. | Mayas, calendario | Civilización maya#4306-4348 |
| 6 | [ ] | Civilización maya | La segunda mitad del siglo xix vio el registro y la recuperación de relatos etnohistóricos de los mayas, y se dieron los primeros pasos en el desciframiento de los glifos mayas. | Mayas | Civilización maya#4450-4481 |
| 7 | [ ] | Civilización maya | Con los avances en la comprensión de la escritura maya que se lograron desde la década de 1950 en adelante, los textos revelaron las actividades bélicas de los reyes mayas clásicos, y ya no podía sostenerse la idea de que los mayas fuesen pacíficos. | Mayas, escritura | Civilización maya#4662-4706 |
| 8 | [ ] | Civilización maya | El arte maya, elaborado a partir de materiales perecederos y no perecederos, sirvió para conectar los mayas con sus antepasados. | Mayas | Civilización maya#8903-8923 |
| 9 | [ ] | Civilización maya | Su forma puede variar considerablemente, pero por lo general representan figuras humanas, animales y formas geométricas asociadas con la religión maya. | — | Civilización maya#9510-9531 |
| 10 | [ ] | Civilización maya | Por el período Posclásico, se utilizó también el yucateco en los códices mayas, junto al choltí clásico. | Mayas | Civilización maya#12937-12954 |
| 11 | [ ] | Civilización maya | Las semejanzas entre la escritura ístmica y la escritura maya temprana de la costa del Pacífico, sugieren que ambos sistemas se desarrollaron en tándem. | escritura | Civilización maya#13102-13126 |
| 12 | [ ] | Civilización maya | El sistema de escritura maya, a menudo denominado jeroglíficos mayas por una semejanza superficial con los jeroglíficos egipcios, es un sistema de escritura logosilábico, que combina un silabario de signos fonéticos, que representan sílabas, con logogramas que representan palabras completas. | Mayas, escritura | Civilización maya#13313-13353 |
| 13 | [ ] | Civilización maya | Los mayas también utilizaron pequeñas secciones de un signo principal para representar al signo principal entero, y los escribas mayas eran muy inventivos en el uso y la adaptación de elementos de los glifos. | Mayas | Civilización maya#13972-14006 |
| 14 | [ ] | Civilización maya | El calendario maya estaba intrínsecamente ligado al ritual maya, y era fundamental para las prácticas religiosas mayas. | Mayas, calendario | Civilización maya#14403-14420 |
| 15 | [ ] | Civilización maya | Además, el conjunto del arte maya, la arquitectura y la escritura contribuye a la reconstrucción de las antiguas creencias mayas; estos pueden combinarse con fuentes etnográficas, incluidos los registros de las prácticas religiosas mayas elaboradas por los españoles durante la conquista. | Mayas, escritura | Civilización maya#16039-16080 |
| 16 | [ ] | Civilización maya | Los mayas tenían una tan amplia interpretación de lo que era sagrado, que la identificación de deidades con diferentes funciones específicas sería incorrecta. | Mayas | Civilización maya#16903-16926 |
| 17 | [ ] | Civilización maya | Wikisource contiene obras originales de o sobre los mayas. | Mayas | Civilización maya#17752-17761 |
| 18 | [ ] | Cultura olmeca | Sin embargo, no está claro el proceso que dio origen al estilo artístico identificado con esta sociedad, ni hasta qué punto los rasgos culturales que se revelan en la evidencia arqueológica son creación de los olmecas del área nuclear. | Olmecas | Cultura olmeca#129-168 |
| 19 | [ ] | Cultura olmeca | Se sabe, por ejemplo, que algunos de los atributos propiamente olmecas podrían haber aparecido primero en Chiapas o en los Valles Centrales de Oaxaca. | Olmecas | Cultura olmeca#168-192 |
| 20 | [ ] | Cultura olmeca | Sea cual haya sido el origen de la cultura olmeca, la red de intercambios comerciales entre distintas zonas de Mesoamérica contribuyó a la difusión de muchos elementos culturales que son identificados con la cultura olmeca, incluidos el culto a las montañas y a las cuevas, el culto a la Serpiente Emplumada como deidad asociada a la agricultura, el simbolismo religioso del jade e incluso el propio estilo artístico, … | — | Cultura olmeca#220-305 |
| 21 | [ ] | Cultura olmeca | Los olmecas crearon sistemas políticos centralizados y respaldados por la religión y el poder hereditario que no tenían paralelo en otros pueblos. | Olmecas | Cultura olmeca#309-331 |
| 22 | [ ] | Cultura olmeca | La palabra "olmeca", simplificación de "Olmecas Uixtotin", significa "habitantes de la región del hule" y fue utilizada por los aztecas y mexicas para nombrar a varios pueblos, étnica y lingüísticamente diversos, que ocuparon la región de Veracruz y Tabasco a través de los siglos. | Olmecas | Cultura olmeca#936-980 |
| 23 | [ ] | Cultura olmeca | Fue el centro ceremonial más importante de los olmecas. | Olmecas | Cultura olmeca#1330-1339 |
| 24 | [ ] | Cultura olmeca | Más allá de las fronteras mexicanas, vestigios de una presencia olmeca se encuentran en: Guatemala (Takalik Abaj), Belice, El Salvador, Honduras y Nicaragua. | — | Cultura olmeca#1736-1759 |
| 25 | [ ] | Cultura olmeca | Normalmente, aparecen mezclados entre ellos, cabezas de unos y cuerpos de otros, creando seres mitológicos. | — | Cultura olmeca#1960-1975 |
| 26 | [ ] | Cultura olmeca | Entre otras cosas, se acredita a los olmecas el desarrollo del calendario, la escritura y la epigrafía. | Olmecas, escritura, calendario | Cultura olmeca#2135-2152 |
| 27 | [ ] | Cultura olmeca | "Los Olmecas y su influencia en Mesoamérica: ¿cuestión de opinión o cuestión de evidencia?"/En El Mediterráneo americano: población, cultura e historia/XXVII Mesa Redonda de la Sociedad Mexicana de Antropología/SMA-UNAM-IIA/México. | Olmecas | Cultura olmeca#2535-2564 |
| 28 | [ ] | Cultura olmeca | "Dioses y poder"/ En Olmeca, the Most Ancient Civilization of the Americas, a Road to the Maya, Special Exhibitions Celebrating 400th Anniversary of Mexico-Japan Frienship, Gobierno de Japón, Embajada de México en Japón, INAH. | — | Cultura olmeca#2567-2601 |
| 29 | [ ] | Cultura teotihuacana | Algunos textos descubiertos en el área maya suelen relacionar el glifo puh (tule) con personajes de filiación teotihuacana representados en estelas de ciudades mayas tan importantes como Tikal, Uaxactún y Bonampak. | Mayas | Cultura teotihuacana#1391-1422 |
| 30 | [ ] | Cultura teotihuacana | Asimismo, los autores señalan que existe una estrecha relación entre reglas comunes de representación gráfica del sistema teotihuacano, los del zapoteco, el epi-olmeca y el maya para crear un sistema totalmente autóctono empleado por los habitantes de la ciudad, siendo el mismo complejo y altamente desarrollado. | — | Cultura teotihuacana#3343-3389 |
| 31 | [ ] | Historia de México | Los criterios sobre qué hechos considerarlos como coyuntura y el criterio para ver qué tan relevantes fueron pueden diferir enormemente entre historiadores. | — | Historia de México#317-339 |
| 32 | [ ] | Historia de México | A continuación se detalla una lista de las principales culturas del México prehispánico. | — | Historia de México#3200-3213 |
| 33 | [ ] | Historia de México | Si bien cada cultura tiene características que las diferencian de otras, no eran regiones unificadas. | — | Historia de México#3233-3248 |
| 34 | [ ] | Historia de México | Al mismo tiempo surgen las comunidades alfareras de Tlatilco, en el actual Estado de México (2 500 a. n. e.); los Capacha,en Guerrero y Sinaloa (2000 a. n. e.) y los Mayas, cuya estructura más antigua conocida es la de Aguada Fénix en Tabasco (1 500 a. n. e.). | Mayas | Historia de México#3453-3502 |
| 35 | [ ] | Historia de México | La aparición de los tronos Olmecas que se llevan desde la región de Los Tuxtlas hasta la zona olmeca, también define este periodo. | Olmecas | Historia de México#3578-3601 |
| 36 | [ ] | Imperio azteca | Esta misma práctica también parece haber existido entre los mayas. | Mayas | Imperio azteca#4930-4940 |
| 37 | [ ] | Imperio azteca | Los aztecas intentaron combinar dos sistemas religiosos en conflicto: la tradición de los guerreros y cazadores chichimecas y la herencia de los agricultores sedentarios. | — | Imperio azteca#8261-8285 |
| 38 | [ ] | Porfiriato | Así sucedió con los yaquis de Sonora y con los mayas en Yucatán. | Mayas | Porfiriato#230-243 |
| 39 | [ ] | Virreinato de Nueva España | Tanto en los registros oficiales como en la imaginación del vulgo, estas castas han pasado a la historia con un nombre y características que los diferenciaban de otros pueblos y razas. | — | Virreinato de Nueva España#9832-9863 |
| 40 | [ ] | Virreinato de Nueva España | Coyote: resultado de la unión de indígena y mestizo. | — | Virreinato de Nueva España#9976-9985 |
| 41 | [ ] | Virreinato de Nueva España | La organización política que los españoles permitieron conservar diferenciaba a los caciques gobernantes, quienes gozaban de privilegios, de los indígenas de la más baja clase social. | — | Virreinato de Nueva España#12042-12068 |
| 42 | [ ] | Virreinato de Nueva España | De los indígenas de dicha clase, fray Rodrigo de Loaysa escribió que «[...] son como sardinas en el mar. | — | Virreinato de Nueva España#12068-12087 |

---

## V2 (comparativa)

**Pregunta:** ¿Qué diferencias hay entre Zapata y Villa?
**Puntos clave (guía, no juez):** Zapata: agrarismo, sur, Plan de Ayala; Villa: norte, División del Norte, carácter militar
**Anotada:** [ ] sí   (marca esta casilla al terminar la pregunta)

| # | Evidencia | Artículo | Oración | Puntos clave en la oración | Ref |
|---|---|---|---|---|---|
| 1 | [ ] | Benito Juárez | Maximiliano, luego de reflexionar pide a un general de su confianza de nombre Miguel López ir como mensajero ante el Gral. Mariano Escobedo y plantearle su rendición condicionada. | — | Benito Juárez#9945-9973 |
| 2 | [ ] | Emiliano Zapata | Madero ofrece a Zapata una hacienda en el estado de Morelos "como pago a sus servicios a la Revolución", cosa que enfurece a Zapata que le contesta: | Zapata | Emiliano Zapata#1586-1613 |
| 3 | [ ] | Emiliano Zapata | La población de la capital del país, huía al saber la cercanía del ejército de Zapata. | Zapata | Emiliano Zapata#2777-2793 |
| 4 | [ ] | Emiliano Zapata | En septiembre, Venustiano Carranza envió a Juan Sarabia, a Antonio I. Villarreal y a Luis Cabrera Lobato a conferenciar con Emiliano Zapata, pero nuevamente el caudillo suriano exigió la renuncia de Venustiano Carranza al Poder Ejecutivo, y el reconocimiento del plan de Ayala. | Zapata, Plan de Ayala, Villa | Emiliano Zapata#2817-2860 |
| 5 | [ ] | Emiliano Zapata | El 4 de diciembre de ese año Villa y Zapata tuvieron la célebre entrevista de Xochimilco, lográndose una alianza militar entre ambos ejércitos. | Zapata, Villa | Emiliano Zapata#3132-3155 |
| 6 | [ ] | Emiliano Zapata | Villa aceptó en cambio el plan de Ayala, a excepción de sus acusaciones a Francisco I. Madero, quien había sido su redentor y se obligó a dar armas a Zapata. | Zapata, Plan de Ayala, Villa | Emiliano Zapata#3155-3185 |
| 7 | [ ] | Historia de México | Los criterios sobre qué hechos considerarlos como coyuntura y el criterio para ver qué tan relevantes fueron pueden diferir enormemente entre historiadores. | — | Historia de México#317-339 |
| 8 | [ ] | Historia de México | Tras las discrepancias que Carranza había tenido con Villa, el 8 de julio firmaron el Pacto de Torreón, donde Villa presentaba disculpas a Carranza que seguiría como primer jefe a cambio de convocar una convención de generales que crearan un nuevo programa de gobierno que satisficiera a todos. | Villa | Historia de México#46791-46839 |
| 9 | [ ] | Historia de México | En el colmo del ridículo, Villa solicita que lo fusilen junto a Carranza el 3 de noviembre, y Zapata es el único que insiste en no abandonar su posición. | Zapata, Villa | Historia de México#47140-47169 |
| 10 | [ ] | Historia de México | Ante los actos, Carranza desconoce la convención y sus acuerdos el 10 de noviembre, pues ni Villa ni Zapata están dispuestos a abandonar el poder. | Zapata, Villa | Historia de México#47188-47213 |
| 11 | [ ] | Historia de México | Es entonces que Zapata y Villa deciden entrar a la Ciudad de México. | Zapata, Villa | Historia de México#47235-47248 |
| 12 | [ ] | Historia de México | Después de entrevistarse en Xochimilco y verse las caras por primera vez, Villa y Zapata se volvieron a encontrar en la ciudad el día 6, tomandose la afamada foto dentro del Palacio Nacional en donde Villa se sienta burlonamente en la silla presidencial. | Zapata, Villa | Historia de México#47329-47372 |
| 13 | [ ] | Historia de México | Ambos acordaron atacar a Carranza. | — | Historia de México#47372-47377 |
| 14 | [ ] | Historia de México | Mientras tanto Villa y Zapata continuaron el enfrentamiento frontal con el gobierno a través de la guerra de guerrillas en Chihuahua y Morelos respectivamente. | Zapata, Villa | Historia de México#48858-48882 |
| 15 | [ ] | Historia de México | El Géneral Pancho Villa, había muerto. | Villa | Historia de México#50844-50850 |
| 16 | [ ] | Miguel Hidalgo y Costilla | Luego de la derrota en Puente de Calderón, las diferencias entre Hidalgo y Allende, los principales jefes de la insurrección, parecían ya irreconciliables. | — | Miguel Hidalgo y Costilla#6048-6071 |
| 17 | [ ] | Moctezuma II | De todas maneras, hay que indicar que como la cultura mexica hacía diferencias entre los diferentes tipos de esposas y las concubinas, no todos sus descendientes tendrían la misma categoría social. | — | Moctezuma II#19099-19130 |
| 18 | [ ] | Pancho Villa | José Doroteo Arango Arámbula (La Coyotada, Durango, 5 de junio de 1878-Hidalgo del Parral, Chihuahua, 20 de julio de 1923), conocido por su seudónimo Francisco Villa o por su hipocorístico Pancho Villa, fue un militar y revolucionario mexicano que se destacó como uno de los principales jefes de la Revolución mexicana siendo el Comandante Supremo de la División del Norte del 29 de septiembre de 1913 hasta su amnistía … | Villa, norte, División del Norte | Pancho Villa#3-78 |
| 19 | [ ] | Pancho Villa | Aunque este se debió haber llamado Agustín Villa Arango, se desconocen las causas de por qué Jesús Villa no dio nombre a su hijo y de por qué este recibió el apellido de su madre. | Villa | Pancho Villa#644-679 |
| 20 | [ ] | Pancho Villa | A Pancho Villa lo representaron Miguel Silva, Manuel Bonilla y José Isabel Robles; A Pablo González Garza: Antonio I. Villarreal, Cesáreo L. Castro y Luis Caballero. | Villa | Pancho Villa#1929-1955 |
| 21 | [ ] | Pancho Villa | A pesar de la victoria, Villa estaba molesto con Venustiano Carranza, quien lo despreciaba por su reputación de bandolero, ya que nunca le concedió a la División del Norte el grado de Ejército ni a Villa el grado de general de división. | Villa, norte, División del Norte | Pancho Villa#2092-2134 |
| 22 | [ ] | Pancho Villa | Villa tomó la Ciudad de México, a nombre del gobierno de la Convención, junto con su aliado Emiliano Zapata, en diciembre de 1914. | Zapata, Villa | Pancho Villa#2304-2327 |
| 23 | [ ] | Pancho Villa | Villa y Zapata entraron juntos al Palacio Nacional con el presidente convencionista Eulalio Gutiérrez Ortiz y el momento fue plasmado en la famosa fotografía en la que Villa se sentó en la silla presidencial ante los fotógrafos. | Zapata, Villa | Pancho Villa#2386-2423 |
| 24 | [ ] | Pancho Villa | También tuvo mucho que ver el terreno que no era favorable para la caballería de la División del Norte y el hecho que a Villa se le vendió municiones defectuosas, el historiador Paco Ignacio Taibo II las llamó las "balas de palo". | Villa, norte, División del Norte | Pancho Villa#2570-2612 |
| 25 | [ ] | Pancho Villa | Es sabido que Pancho Villa y Emiliano Zapata son figuras históricas que han sido denostadas, calumniadas por la prensa de la época y hasta han querido borrarlos de la historia de México. | Zapata, Villa | Pancho Villa#5326-5358 |
| 26 | [ ] | Pancho Villa | En 2000, la banda Brujería incluyó en su álbum Brujerizmo la canción «División del Norte», dedicada a dicha división y a Pancho Villa. | Villa, norte, División del Norte | Pancho Villa#6424-6447 |
| 27 | [ ] | Pancho Villa | En la segunda temporada de la serie mexicana La Reina Del Sur se menciona al personaje “Zurdo Villa” como nieto de Pancho Villa, sin embargo esto es solo ficción. | Villa | Pancho Villa#6541-6570 |
| 28 | [ ] | Pancho Villa | YouTube.com (película de la entrada de Zapata y Villa al centro de México, D. F.). | Zapata, Villa | Pancho Villa#6879-6894 |
| 29 | [ ] | Revolución mexicana | Desde el comienzo de su mandato tuvo diferencias con otros líderes revolucionarios, que provocaron el levantamiento de Emiliano Zapata y Pascual Orozco contra el Gobierno maderista. | Zapata | Revolución mexicana#383-409 |
| 30 | [ ] | Revolución mexicana | En el reacomodo de las fuerzas fueron asesinados los principales jefes: Emiliano Zapata en 1919, Venustiano Carranza en 1920, Francisco Villa en 1923, y Álvaro Obregón en 1928. | Zapata, Villa | Revolución mexicana#608-636 |
| 31 | [ ] | Revolución mexicana | En Chihuahua y parte de la Comarca Lagunera operó la División del Norte de Francisco Villa. | Villa, norte, División del Norte | Revolución mexicana#7681-7697 |
| 32 | [ ] | Revolución mexicana | A pesar de la victoria, Villa no pudo ser el primero en llegar a la capital debido a que Carranza bloqueó los envíos de carbón a la División del Norte, el cual era necesario para alimentar los ferrocarriles de Villa. | Villa, norte, División del Norte | Revolución mexicana#8799-8839 |
| 33 | [ ] | Revolución mexicana | Con el traslado de la sede, Villa decidió enviar a sus delegados y Zapata hizo lo mismo. | Zapata, Villa | Revolución mexicana#9339-9356 |
| 34 | [ ] | Revolución mexicana | Los últimos dos grupos contaban para entonces con la ventaja de tener un ejército más numeroso y habían ocupado la capital, aunque conforme avanzó ese año la balanza se fue inclinando hacia el bando carrancista gracias a las victorias de Álvaro Obregón frente al ejército de Francisco Villa y a que, a pesar del pacto realizado en Xochimilco, nunca hubo una verdadera colaboración entre Villa y Zapata debido a que este … | Zapata, Villa | Revolución mexicana#9685-9772 |
| 35 | [ ] | Revolución mexicana | El 6 de abril de ese año las fuerzas de Villa intentaron tomar Celaya, la cual estaba bajo el control de Obregón, quien pudo defender la plaza, causando alrededor de 2000 bajas en el bando contrario. | Villa | Revolución mexicana#9772-9808 |
| 36 | [ ] | Revolución mexicana | Vámonos con Pancho Villa (1935) de Fernando de Fuentes. | Villa | Revolución mexicana#13882-13891 |
| 37 | [ ] | Virreinato de Nueva España | Antonio de Mendoza y Pacheco, fue el primer virrey enviado a la Nueva España en 1535, y quien debería reconciliar las diferencias entre españoles y nativos. | — | Virreinato de Nueva España#7382-7408 |

---

## V3 (comparativa)

**Pregunta:** ¿En qué se parecen el Virreinato y el Imperio Azteca?
**Puntos clave (guía, no juez):** Control centralizado; tributo; dominio territorial; jerarquía religiosa ligada al poder
**Anotada:** [ ] sí   (marca esta casilla al terminar la pregunta)

| # | Evidencia | Artículo | Oración | Puntos clave en la oración | Ref |
|---|---|---|---|---|---|
| 1 | [ ] | Civilización maya | A diferencia de los aztecas e incas, el sistema político maya nunca incorporó toda el área cultural maya en un solo Estado o imperio. | — | Civilización maya#4734-4758 |
| 2 | [ ] | Cultura olmeca | Se sabe, por ejemplo, que algunos de los atributos propiamente olmecas podrían haber aparecido primero en Chiapas o en los Valles Centrales de Oaxaca. | tributo | Cultura olmeca#168-192 |
| 3 | [ ] | Cultura teotihuacana | De Teotihuacán a los aztecas: antología de fuentes e interpretaciones históricas, 123-129. | — | Cultura teotihuacana#13172-13184 |
| 4 | [ ] | Hernán Cortés | Por esto, los aztecas consideraban que los españoles eran teules (de teolt, dios) que marcharían sobre ellos inexorablemente. | — | Hernán Cortés#4642-4660 |
| 5 | [ ] | Hernán Cortés | Por la riqueza y población de la región del Anáhuac, los encomenderos mexicanos se fueron convirtiendo en una pujante aristocracia colonial hereditaria, encabezada por el propio Cortés, quien se quedó con el control —así como el monopolio del tributo y la mano de obra— de los núcleos más poblados y productivos del valle de México, como Texcoco, Huexotla, Chiauhtla, Tezayuca, Coatlichan, Chalco (incluyendo todas sus … | tributo | Hernán Cortés#11967-12037 |
| 6 | [ ] | Historia de México | Así estaba por iniciar el Imperio Azteca. | — | Historia de México#6060-6067 |
| 7 | [ ] | Historia de México | A su muerte, Nezahualpilli recibió el trono de Texcoco y el Imperio Azteca le envió a Chalchiunenetzin como concubina para casarse. | — | Historia de México#6282-6303 |
| 8 | [ ] | Historia de México | Esto supuso el comienzo del expansionismo azteca pues ordenó ataques contra tarascos, matlatzincas, chontales y cuitlatecos. | — | Historia de México#6528-6544 |
| 9 | [ ] | Historia de México | Aquel primer gran acto bélico demostró el poderío de los extranjeros por toda la región, algunos reinos como Cempoallan (asediado por la viruela) detuvieron la entrega de tributos y los enemigos de Tenochtitlán permanecieron al margen de lo que pasaría en la ciudad. | tributo | Historia de México#7897-7940 |
| 10 | [ ] | Imperio azteca | El Imperio mexica o Triple Alianza (del náhuatl: Exkan Tlahtoloyan o Ēxcān Tlahtōlōyān ‘Los tres lugares donde se dan órdenes’), llamado también Imperio azteca y —con más precisión— Imperio tenochca, fue un imperio organizado en una confederación compleja, multiétnica y flexible de ciudades estado con situaciones políticas diversas, que existió en el área central de Mesoamérica durante el Posclásico Tardío hasta la … | — | Imperio azteca#3-67 |
| 11 | [ ] | Imperio azteca | El fin del Imperio azteca ocurrió el 13 de agosto de 1521, cuando los españoles —en alianza con los tlaxcaltecas y totonacas, entre otros pueblos indígenas— derrotaron la resistencia mexica en Tenochtitlan y Tlatelolco. | — | Imperio azteca#254-288 |
| 12 | [ ] | Imperio azteca | La Triple Alianza (mexicas, acolhuas y tepanecas), comúnmente llamada Imperio mexica, fue la formación política mexica derivada del proceso de expansión territorial del dominio económico de la ciudad-estado México-Tenochtitlan, que floreció en el siglo XIV en Mesoamérica. | dominio territorial | Imperio azteca#1207-1244 |
| 13 | [ ] | Imperio azteca | Fue encabezado por los mexicas —mal conocidos como aztecas—, un pueblo que, de acuerdo con algunos documentos históricos como la Tira de la Peregrinación, era originario de un sitio —tal vez mítico— conocido como Aztlán, al que se suele ubicar fuera de los confines de Mesoamérica. | — | Imperio azteca#1244-1290 |
| 14 | [ ] | Imperio azteca | Originalmente, el imperio azteca era una alianza suelta entre tres ciudades: Tenochtitlan, Texcoco y el socio menor, Tlacopan. | — | Imperio azteca#2235-2253 |
| 15 | [ ] | Imperio azteca | Sin embargo, con el tiempo fue Tenochtitlan quien asumió una autoridad suprema en la alianza, y aunque cada ciudad socia compartía los despojos de guerra y los derechos a los tributos regulares de las provincias y fue gobernada por su propio Huetlatoani, fue Tenochtitlan el que se convirtió en la más grande, la más poderosa, y la más influyente de las tres ciudades. | tributo | Imperio azteca#2276-2339 |
| 16 | [ ] | Imperio azteca | Nuevamente, la Matrícula de Tributos indica que el Imperio demandaba chalchihuites en forma de ristras a ciertas provincias, tanto del occidente como del oriente, como Tepecoacuilco (en el actual Estado de Guerrero), de donde se demandaban cinco ristras. | tributo | Imperio azteca#6407-6445 |
| 17 | [ ] | Imperio azteca | No obstante, la Relación de Tepeucila, un documento de 1579, redacta que sí existía una mina de oro en el pueblo, llamada Tecpanapa, que era usada para pagar tributos, tanto al Imperio mexica como al Imperio español, después de la Conquista, aunque no hay evidencia arqueológica ni testimonios abundantes sobre este tema. | tributo | Imperio azteca#6586-6638 |
| 18 | [ ] | Imperio azteca | Los aztecas intentaron combinar dos sistemas religiosos en conflicto: la tradición de los guerreros y cazadores chichimecas y la herencia de los agricultores sedentarios. | — | Imperio azteca#8261-8285 |
| 19 | [ ] | Imperio azteca | Los tributos llegaban a Tenochtitlan de todas las regiones del imperio: alimentos, tejidos, artículos preciosos, y también seres humanos cautivos destinados al sacrificio. | tributo | Imperio azteca#8942-8965 |
| 20 | [ ] | Imperio azteca | También se capturaban quetzales para extraerles sus plumas y elaborar vistosos trajes y penachos de la realeza Azteca. | — | Imperio azteca#9091-9109 |
| 21 | [ ] | Imperio azteca | Aquí los mexicas se limitaron a construir un campamento comercial, el cual era el medio de contacto entre el Imperio azteca y los reinos fragmentados de los mayas. | — | Imperio azteca#9978-10006 |
| 22 | [ ] | Imperio azteca | El actual territorio del estado México fue el principal y mayor tributario de maderas, carnes y vegetales del Imperio azteca. | — | Imperio azteca#10197-10217 |
| 23 | [ ] | Imperio azteca | Y de donde se obtuvo parte de lo que fue la cultura azteca. | — | Imperio azteca#10217-10230 |
| 24 | [ ] | Imperio azteca | Aztec Warfare: Imperial Expansion and Political Control (en inglés). | — | Imperio azteca#10716-10725 |
| 25 | [ ] | Imperio azteca | Santamarina Novillo, Carlos, El sistema de dominación azteca: el Imperio Tepaneca. | — | Imperio azteca#10875-10886 |
| 26 | [ ] | Imperio azteca | Everyday Life in the Aztec World (en inglés). | — | Imperio azteca#10930-10938 |
| 27 | [ ] | Imperio azteca | Wikimedia Commons alberga una categoría multimedia sobre Imperio azteca. | — | Imperio azteca#10948-10957 |
| 28 | [ ] | Virreinato de Nueva España | Varias premoniciones en años anteriores hicieron creer a Moctezuma Xocoyotzin, soberano azteca o tlatoani, que el fin de su imperio estaba cerca. | — | Virreinato de Nueva España#1396-1418 |
| 29 | [ ] | Virreinato de Nueva España | Los españoles decidieron aprovechar la situación para obtener riquezas e influencia dentro de la corte azteca. | — | Virreinato de Nueva España#1460-1476 |
| 30 | [ ] | Virreinato de Nueva España | Cuando los españoles llegaron al Nuevo Mundo, se encontraron con civilizaciones muy bien constituidas: el imperio teocrático de los incas que estaba en su apogeo, la confederación de los mexicas y la cultura maya. | — | Virreinato de Nueva España#11872-11906 |

---

## R1 (relacional)

**Pregunta:** ¿Qué relación tuvo Juárez con la Guerra de Reforma?
**Puntos clave (guía, no juez):** Juárez lideró el bando liberal; promulgó las Leyes de Reforma; fue presidente durante el conflicto
**Anotada:** [ ] sí   (marca esta casilla al terminar la pregunta)

| # | Evidencia | Artículo | Oración | Puntos clave en la oración | Ref |
|---|---|---|---|---|---|
| 1 | [ ] | Benito Juárez | Juárez es considerado un símbolo de soberanía nacional, resistencia, libertad y legalidad al liderar a su país durante la Guerra de Reforma y la Segunda Intervención Francesa. | — | Benito Juárez#71-98 |
| 2 | [ ] | Benito Juárez | Juárez marcó un parteaguas en la historia nacional y fue protagonista de primer nivel de esta época. | — | Benito Juárez#163-180 |
| 3 | [ ] | Benito Juárez | La razón fue la duda de los golpistas ante su posición, ya que Juárez nunca se declaró abiertamente en contra ni a favor del conflicto, irónicamente causado por la ley cuyas bases él mismo había ayudado a sentar. | — | Benito Juárez#2757-2795 |
| 4 | [ ] | Benito Juárez | Ante esto, Juárez solicitó al congreso facultades extraordinarias. | — | Benito Juárez#3585-3593 |
| 5 | [ ] | Benito Juárez | La encomienda de Juárez era asegurarse que los Estados Unidos estuvieran del lado de la República y en contra del imperialismo francés. | — | Benito Juárez#4486-4508 |
| 6 | [ ] | Benito Juárez | De esto había tenido noticia Juárez. | — | Benito Juárez#5129-5135 |
| 7 | [ ] | Benito Juárez | Juárez dijo: "No puedo creer que los hacendados de la región piensen más en su beneficio personal que en los inmensos sacrificios que la patria hace por darles orden y paz; mándame una lista de todos los | — | Benito Juárez#9654-9691 |
| 8 | [ ] | Benito Juárez | Juárez sale rumbo a Palacio Nacional por "El paseo de la Emperatriz", que desde ese momento cambia de nombre a paseo de la Reforma. | — | Benito Juárez#11185-11209 |
| 9 | [ ] | Benito Juárez | Luego de pasar por el paseo de la Reforma, Juárez y su comitiva se dirigen hacia el Palacio de Minería por la que hoy es la avenida Juárez. | — | Benito Juárez#11221-11249 |
| 10 | [ ] | Benito Juárez | Juárez decía a menudo que eran los tiempos de la paz y la concordia. | — | Benito Juárez#12074-12088 |
| 11 | [ ] | Benito Juárez | Existieron otros altercados militares durante 1871 que fueron controlados pero que reflejaban la inestabilidad política de Juárez y el apoyo armado a Porfirio Díaz. | — | Benito Juárez#13756-13780 |
| 12 | [ ] | Benito Juárez | Juárez tuvo la insistencia de los ministros de relaciones exteriores José María Lafragua y el ministro de la Guerra el general Alatorre, en esa tarde ambos pidieron ver al presidente para recibir instrucciones. | — | Benito Juárez#14240-14273 |
| 13 | [ ] | Benito Juárez | La historia de Juárez también llegó al Cine estadounidense. | — | Benito Juárez#14905-14914 |
| 14 | [ ] | Benito Juárez | Juárez fue ferviente en la práctica masónica. | — | Benito Juárez#15476-15483 |
| 15 | [ ] | Benito Juárez | Juárez y sus contemporáneos (1.ª edición). | — | Benito Juárez#15833-15839 |
| 16 | [ ] | Benito Juárez | Bibliografía sobre Benito Juárez. | — | Benito Juárez#16119-16123 |
| 17 | [ ] | Guerra de Reforma | La Guerra de Reforma, también conocida como la guerra de los tres años, fue una guerra civil que aconteció en México desde el 17 de diciembre de 1857 al 11 de enero de 1861, como consecuencia de la promulgación de la Constitución de 1857 y en especial de las llamadas Leyes de Reforma. | promulgó las Leyes de Reforma | Guerra de Reforma#4-57 |
| 18 | [ ] | Guerra de Reforma | Comonfort trató de buscar una reconciliación con el partido liberal; encarceló a Juárez y llevó a cabo enfrentamientos armados contra los conservadores, en los cuales saldría mal librado. | — | Guerra de Reforma#644-672 |
| 19 | [ ] | Guerra de Reforma | Juárez estableció su gobierno, en un primer momento, en Guanajuato, mientras Zuloaga gobernaba en la capital con las llamadas Cinco Leyes, que de hecho derogaban algunas de las reformas liberales como la Ley Lerdo, la Ley Iglesias y la Ley Juárez, entre otras. | promulgó las Leyes de Reforma | Guerra de Reforma#768-811 |
| 20 | [ ] | Guerra de Reforma | Las leyes decretadas por Juárez en México en 1859 y 1860, mientras se encontraba situado en el puerto de Veracruz, conocidas como Leyes de Reforma, son consideradas por algunos autores como el punto de quiebre de esta guerra. | promulgó las Leyes de Reforma | Guerra de Reforma#935-973 |
| 21 | [ ] | Guerra de Reforma | Leyes de Reforma y Etapas de la Reforma en México. | promulgó las Leyes de Reforma | Guerra de Reforma#1857-1867 |
| 22 | [ ] | Hernán Cortés | Fue de inestimable ayuda su relación con una mujer nativa, doña Marina (la Malinche), que le sirvió de intérprete y con quien tuvo un hijo llamado Martín. | — | Hernán Cortés#216-243 |
| 23 | [ ] | Historia de México | Así mientras Zuloaga derogaba las leyes de reforma, Juárez intentaría hacerlas cumplir en la capital de Guanajuato. | promulgó las Leyes de Reforma | Historia de México#29716-29733 |
| 24 | [ ] | Historia de México | Rompiendo las líneas defensivas en Veracruz y luego Córdoba, Zaragoza se apresuba a preparar un ejército en Puebla. | — | Historia de México#31368-31386 |
| 25 | [ ] | Historia de México | La caída era inevitable, Juárez ordenó llevarse todos los archivos del gobierno para establecerse, como ya había pasado en la guerra de Reforma, en otro lugar provisional. | — | Historia de México#32081-32108 |
| 26 | [ ] | Historia de México | Si bien la idea era introducir gobernantes de pensamiento liberal en estas ciudades, los verdaderos liberales le eran fiel a Juárez. | — | Historia de México#33243-33264 |
| 27 | [ ] | Historia de México | Sin quererlo, Maximiliano estaba dándole recursos a Juárez para lograr con apoyo de los nuevos estados liberales, una guerra de guerrillas. | — | Historia de México#33293-33314 |
| 28 | [ ] | Historia de México | Fue el círculo cercano a Juárez quien le hizo ver la guerra ya no era por defensa de las leyes liberales o la reforma, sino por soberanía nacional. | promulgó las Leyes de Reforma | Historia de México#33428-33456 |
| 29 | [ ] | Historia de México | Por eso cuando Juárez retornó triunfal como presidente a la Ciudad de México en julio de 1867, la mejor forma en que pudo legitimar el poder republicano fue restablecer la Constitución de 1857, ejecutar de nuevo las Leyes de Reforma y llamar a elecciones el 22 de septiembre. | promulgó las Leyes de Reforma | Historia de México#34498-34546 |
| 30 | [ ] | Historia de México | Desde el 31 de diciembre de 1867, Julio Chávez López había proclamado en Chalco (Estado de México) el Manifiesto a todos los oprimidos y los pobres de México y del universo, que por primera vez intruduce en la lucha las ideas socialistas para reformar la propiedad agraria y devolverla a los pueblos a quienes Juárez se las había arrebatado en su plan de desamortización. | — | Historia de México#34971-35035 |
| 31 | [ ] | Historia de México | El movimiento armado inició en Texcoco con el apoyo del general Miguel Negrete, que tomó los fuertes de Loreto y Guadalupe; pero fue vencido, aprehendido, procesado y sentenciado a muerte; sin embargo, el general Porfirio Díaz le concedió su indulto por su pasado en la participación en el sitio de Puebla. | — | Historia de México#35035-35086 |
| 32 | [ ] | Historia de México | Tras la muerte de Juárez, los adheridos al Plan de la Noria sin motivo para combatir, acordaron el cese al fuego tras la amnistía emitida por el interino Sebastián Lerdo de Tejada había expedido una amnistía. | — | Historia de México#35782-35818 |
| 33 | [ ] | Historia de México | Nadie esperaba que Lerdo fuese más radical que Juárez pues elevó las Leyes de Reforma a nivel constitucional, así los estados que habían intentado sortearlas ya no tenían pretexto de no cumplirlas y eso abarcó también a los funcionarios de gobierno. | promulgó las Leyes de Reforma | Historia de México#36043-36084 |
| 34 | [ ] | Miguel Hidalgo y Costilla | La guerra en la región de Guadalajara. | — | Miguel Hidalgo y Costilla#9319-9326 |
| 35 | [ ] | Porfiriato | El clero recobró gran parte del poder perdido con las Leyes de Reforma y la guerra de los Tres Años. | promulgó las Leyes de Reforma | Porfiriato#4819-4839 |
| 36 | [ ] | Virreinato de Nueva España | La importancia de la imagen radica en que durante siglos ha tenido un papel preponderante en la historia de México, como símbolo patrio no oficial, ya que su fiesta (12 de diciembre) no fue abolida del calendario con las Leyes de Reforma, inspiró a grupos insurgentes como estandarte de su lucha y es considerada por la mayor parte del pueblo mexicano y la Iglesia católica como la patrona de México y de toda América. | promulgó las Leyes de Reforma | Virreinato de Nueva España#16726-16800 |

---

## R2 (relacional)

**Pregunta:** ¿Cómo se relacionan Hernán Cortés y Moctezuma II?
**Puntos clave (guía, no juez):** Encuentro en Tenochtitlan en 1519; Moctezuma tomado como rehén; su muerte; destrucción del imperio
**Anotada:** [ ] sí   (marca esta casilla al terminar la pregunta)

| # | Evidencia | Artículo | Oración | Puntos clave en la oración | Ref |
|---|---|---|---|---|---|
| 1 | [ ] | Conquista de México | Cortés se dirigió a la isla de Cozumel siguiendo el trayecto de sus antecesores. | — | Conquista de México#3759-3773 |
| 2 | [ ] | Conquista de México | La convivencia entre Cortés y Moctezuma había creado un vínculo de amistad y el tlatoani, antes de morir, pidió a Cortés que favoreciese a su hijo, de nombre Chimalpopoca. | — | Conquista de México#11788-11817 |
| 3 | [ ] | Conquista de México | Este hecho fue descrito por el propio Hernán Cortés en su tercera carta de relación a Carlos I de España: | — | Conquista de México#16118-16138 |
| 4 | [ ] | Conquista de México | Ante el vacío de poder en la ciudad texcocana Tecocoltzin asumió el cargo, a su muerte prematura le sucedió Ahuaxpictzatzin quien reinó unos días hasta que se nombró a Ixtlilxóchitl y fue bautizado con el nombre de Hernando Ixtlilxóchitl, “el único jefe de los conquistadores que se igualaba con Hernán Cortés” de manera que la caída de Tenochtitlan fue “hazaña de Cortés e Ixtlilxóchitl”. | su muerte | Conquista de México#16654-16718 |
| 5 | [ ] | Conquista de México | Cortés explicó lo acontecido con el poderío mexica, y el halach uinik no tenía aún las noticias de Tenochtitlan pero le contó acerca de noticias de guerras acontecidas con los mayas chontales de Centla con los dzules (hombres blancos). | — | Conquista de México#20427-20466 |
| 6 | [ ] | Conquista de México | CORTÉS, Hernán (2) (1520) Ordenanzas militare y civiles mandadas pregonar por don Hernando Cortés [2] | — | Conquista de México#24205-24220 |
| 7 | [ ] | Conquista de México | PALOMARES, Manolo (2022) "Hernán Cortés. | — | Conquista de México#24685-24690 |
| 8 | [ ] | Hernán Cortés | Hernán Cortés se casó dos veces y tuvo once hijos documentados en seis relaciones diferentes. | — | Hernán Cortés#934-949 |
| 9 | [ ] | Hernán Cortés | Según la obra del fraile Bernardino de Sahagún y sus colaboradores nahuas, según un discurso de Moctezuma recogido en la segunda carta de Cortés a Carlos I y según otras fuentes redactadas en español, el emperador azteca interpretó que Cortés era Quetzalcóatl. | — | Hernán Cortés#4600-4642 |
| 10 | [ ] | Hernán Cortés | Cortés encargó que dos de los calpixques fuesen a su presencia, se mostró ajeno a lo ocurrido y les dio un mensaje para Moctezuma, indicando que quería ser su amigo e ir a visitarlo. | — | Hernán Cortés#5462-5496 |
| 11 | [ ] | Hernán Cortés | A la entrada de la ciudad, realizada el 8 de noviembre de 1519, se produjo el encuentro de Moctezuma y Cortés, haciendo de intérpretes Doña Marina y Gerónimo de Aguilar. | Encuentro en Tenochtitlan en 1519 | Hernán Cortés#6627-6657 |
| 12 | [ ] | Hernán Cortés | Moctezuma II creyó que los españoles eran enviados del dios que vendría del Este —este es Quetzalcóatl o Serpiente Emplumada— y fue un espléndido anfitrión de estos, obsequiándole entre otras cosas, el Tocado del Dios Quetzalcóatl, conocido como Penacho de Moctezuma y el cual, fue enviado junto con otros presentes a la Corte Imperial. | — | Hernán Cortés#6657-6711 |
| 13 | [ ] | Hernán Cortés | Una vez que Moctezuma cayó en la celada de los españoles, Cortés lo tuvo como rehén so pena de muerte inmediata. | Moctezuma tomado como rehén, su muerte | Hernán Cortés#7090-7111 |
| 14 | [ ] | Hernán Cortés | Existen dos versiones de la muerte de Moctezuma: una es que cuando hablaba a su pueblo, recibió una pedrada de los propios mexicas que lo hirió de muerte; la otra dice que Hernán Cortés ordenó matarlo cuando vio que no podía calmar al pueblo, si bien esta última versión fue aportada por los mexicas y se considera menos probable. | su muerte | Hernán Cortés#7613-7672 |
| 15 | [ ] | Hernán Cortés | En 1629 a la muerte de Pedro Cortés, cuarto marqués del Valle y último descendiente de Hernán Cortés en línea masculina, las autoridades civiles y eclesiásticas de la provincia española decidieron sepultarlos en la misma iglesia, así que los restos de Cortés fueron inhumados cerca del altar mayor (en un nicho detrás del sagrario) en la iglesia del convento de San Francisco (México), ubicado frente a la plaza de … | su muerte | Hernán Cortés#12460-12546 |
| 16 | [ ] | Hernán Cortés | Obras de Hernán Cortés en Internet Archive. | — | Hernán Cortés#14294-14301 |
| 17 | [ ] | Hernán Cortés | Portal dedicado a Hernán Cortés en la Biblioteca Virtual Miguel de Cervantes. | — | Hernán Cortés#14312-14324 |
| 18 | [ ] | Moctezuma II | Moctezuma Xocoyotzin (en náhuatl clásico: Motēcuzōmah Xōcoyōtzin; AFI [moteːkʷˈsoːmaḁ ʃoːkoˈjoːt͡sin̥] (): ‘Moctezuma el Joven’ (México-Tenochtitlan, c. 1466-México-Tenochtitlan, 29 de junio de 1520), también llamado Moctezuma II, fue el noveno Huey Tlatoani de México-Tenochtitlán y, por ende, emperador de facto del Imperio mexica entre 1502 o 1503 hasta su magnicidio el 29 de junio de 1520. | — | Moctezuma II#3-58 |
| 19 | [ ] | Moctezuma II | Inicialmente, el contacto entre los europeos y los mexicas fue pacífico, pero hostilidades empezaron prontamente después de que Moctezuma se volvió prisionero de los castellanos en su propio palacio en noviembre de 1519. | — | Moctezuma II#149-182 |
| 20 | [ ] | Moctezuma II | A lo largo de los siglos se ha pensado comúnmente que la conquista fue causada porque Moctezuma, de alguna forma, relacionó a los españoles con la deidad Quetzalcóatl a causa de una antigua profecía. | — | Moctezuma II#182-216 |
| 21 | [ ] | Moctezuma II | La ortografía Moctezuma es la más frecuente y moderna; no obstante, Hernán Cortés transcribió su nombre como Mutecçuma o Muteçuma y la mayoría de las fuentes de los siglos xvi y xvii refieren que su nombre fue Moteucçoma, incluido fray Bernardino de Sahagún que usó una forma más próxima al náhuatl: Motecuçoma y Motecuzomatzin. | — | Moctezuma II#932-986 |
| 22 | [ ] | Moctezuma II | A causa de estos eventos, Cacamatzin, quien inicialmente había dado la bienvenida a los españoles, intentó formar una armada para matarlos y liberar a Moctezuma a inicios de 1520, intentando reunir soldados y formar una alianza con los señores de Coyoacán, Tlacopan, Iztapalapa y el pueblo matlatzinca. | — | Moctezuma II#11960-12007 |
| 23 | [ ] | Moctezuma II | Ante esta amenaza, Cortés le exigió a Moctezuma hacer algo al respecto. | — | Moctezuma II#12064-12076 |
| 24 | [ ] | Moctezuma II | El momento más importante en el reinado de Moctezuma II fue la primera vez que estableció contacto con la gente de España, que fue la primera nación europea que contactó el Imperio mexica. | — | Moctezuma II#12697-12730 |
| 25 | [ ] | Moctezuma II | Según se describió en la segunda carta de relación de Hernán Cortés al emperador Carlos V: | — | Moctezuma II#14338-14354 |
| 26 | [ ] | Moctezuma II | Cortés reportó que Moctezuma le había entonces ofrecido inmediatamente todas sus tierras al rey de España, aunque algunos historiadores modernos ven esto como simplemente Cortés diciéndole al rey de España lo que «necesitaba escuchar», pues han cuestionado que un rey como Moctezuma hubiera hecho algo semejante. | — | Moctezuma II#14383-14429 |
| 27 | [ ] | Moctezuma II | A pesar de que soldados como Díaz del Castillo dicen que este fue el motivo principal del arresto, algunos historiadores contemporáneos a la Conquista de México, como Francisco López de Gómara, sospecharon que Cortés ya planeaba arrestar a Moctezuma para usurpar el dominio de México antes de conocerlo, y la historia de la muerte de Escalante fue simplemente una excusa para ejecutar este plan. | su muerte | Moctezuma II#14852-14916 |
| 28 | [ ] | Moctezuma II | Una creencia popular formado a partir de varias fuentes indígenas y franciscanas escritas tiempo después de la conquista afirma que Moctezuma suponía que Cortés era el dios Quetzalcóatl o que de alguna forma él relacionó a los españoles con esta deidad. | — | Moctezuma II#15441-15482 |
| 29 | [ ] | Moctezuma II | También es de notar que Sahagún era un fraile franciscano, lo cual probablemente habría hecho que su narración (al igual que las de otros frailes franciscanos) fuera afectada por un cierto apoyo a Cortés que existía entre frailes de esta orden, un apoyo que se ve reflejado en una carta del fraile Motolinía al rey Carlos enviada el 2 de enero de 1555, en la cual pregunta «¿quién así amó i [sic] defendió los Indios en … | — | Moctezuma II#17567-17648 |
| 30 | [ ] | Moctezuma II | Existen varias versiones acerca de la muerte de Moctezuma, dependiendo de la fuente consultada. | su muerte | Moctezuma II#18256-18270 |
| 31 | [ ] | Moctezuma II | Moctezuma II tuvo numerosas esposas y concubinas de quienes tuvo muchos hijos. | — | Moctezuma II#19055-19067 |
| 32 | [ ] | Moctezuma II | A la muerte de este, fue bautizada y llamada Isabel Moctezuma por Hernán Cortés y los españoles. | su muerte | Moctezuma II#19198-19215 |
| 33 | [ ] | Moctezuma II | El II conde de Moctezuma fue el hijo de Pedro Tesifón, llamado Diego Luis de Moctezuma y Porres. | — | Moctezuma II#19436-19454 |
| 34 | [ ] | Moctezuma II | Mariana Leonor Moctezuma fue también una de las hijas de Moctezuma II. | — | Moctezuma II#19668-19680 |
| 35 | [ ] | Moctezuma II | Se cree que era hija de Moctezuma con una princesa mixteca, Tzihuacxoachitzin II de Acatlán, de un pueblo y provincia que estaba en alianza con Tenochtitlán en el momento de la invasión española. | — | Moctezuma II#19680-19713 |
| 36 | [ ] | Moctezuma II | Finalmente, otra hija de Moctezuma II que sobrevivió fue Xipaguatzin, que una vez cristianizada fue llamada María de Moctezuma y que se casó o convivió con Juan de Grau Ribó, noble barón de Toloríu (Cataluña) y que participó junto a Cortés en la conquista de Tenochtitlán. | — | Moctezuma II#20005-20051 |
| 37 | [ ] | Moctezuma II | Cuando Hernán Cortés y su ejército llegaron a la gran Tenochtitlán, los conquistadores se alojaron en el palacio de Axayácatl, padre de Moctezuma. | — | Moctezuma II#20302-20325 |
| 38 | [ ] | Virreinato de Nueva España | Cartas de relación, de Hernán Cortés (1485-1547). | — | Virreinato de Nueva España#21581-21588 |
| 39 | [ ] | Virreinato de Nueva España | Relación de algunas cosas de las que acaescieron a Hernando Cortés [...], de Andrés de Tapia (¿1497?-1561). | — | Virreinato de Nueva España#21603-21620 |

---

## R3 (relacional)

**Pregunta:** ¿Qué papel jugó el Virreinato en la Independencia?
**Puntos clave (guía, no juez):** Agravios acumulados; criollos excluidos del poder; influencia ilustrada; debilitamiento de España
**Anotada:** [ ] sí   (marca esta casilla al terminar la pregunta)

| # | Evidencia | Artículo | Oración | Puntos clave en la oración | Ref |
|---|---|---|---|---|---|
| 1 | [ ] | Civilización maya | Dentro de una entidad política, los centros de población medianos habrían jugado un papel clave en la gestión de los recursos y el manejo de conflictos internos. | — | Civilización maya#4974-5001 |
| 2 | [ ] | Civilización maya | En el Clásico Tardío, algunas entidades políticas alcanzaron un largo período de dominación sobre otras grandes entidades políticas, como el dominio de El Caracol sobre Naranjo durante medio siglo. | — | Civilización maya#5026-5055 |
| 3 | [ ] | Civilización maya | El poder político maya se vio reforzado por el poder militar, y la captura y humillación de guerreros enemigos jugó un papel importante en la cultura de la élite. | — | Civilización maya#5136-5165 |
| 4 | [ ] | Conquista de México | No sería hasta tres siglos más tarde que luego de la independencia de México se entenderá a «México» como la totalidad del territorio heredado del anterior Virreinato de la Nueva España. | — | Conquista de México#112-143 |
| 5 | [ ] | Conquista de México | Ahí empezó la política de pactos de Cortés que habría de permitirle capitanear una rebelión de pueblos sometidos que sería determinante en la conquista de los territorios del Imperio mexica. | — | Conquista de México#5857-5887 |
| 6 | [ ] | Emiliano Zapata | Esto dio lugar a que Francisco León de la Barra, presidente interino, lo considerara rebelde, por lo que mandó fuerzas a someterlo: mil hombres bajo el mando de los generales Victoriano Huerta y Aureliano Blanquet. | — | Emiliano Zapata#1368-1403 |
| 7 | [ ] | Guerra de Independencia de México | Los pueblos indígenas debían pagar un tributo al gobierno y estaban sujetos a un régimen de autoridad que, por ambiguo, provocaba numerosas confrontaciones entre españoles, criollos y mestizos. | — | Guerra de Independencia de México#852-880 |
| 8 | [ ] | Guerra de Independencia de México | Al establecerse además el libre comercio entre el virreinato, creció el poder económico y político de los criollos y los mestizos que comenzaron a ocupar también más espacios en la administración virreinal. | criollos excluidos del poder | Guerra de Independencia de México#1474-1506 |
| 9 | [ ] | Guerra de Independencia de México | Estas facciones estaban formadas sobre todo por los miembros de las clases altas y medias, es decir, por españoles peninsulares, criollos y algunos mestizos —muy pocos— que habían llegado a ocupar algún cargo en la estructura de poder colonial. | criollos excluidos del poder | Guerra de Independencia de México#2929-2968 |
| 10 | [ ] | Guerra de Independencia de México | Entre sus revolucionarias propuestas estaban: la organización de la enseñanza gratuita, sin ninguna distinción de clases sociales y sin la exclusión de los indios; crear sociedades agrícolas de producción; otorgar libertad de comercio; creación de ayuntamientos por elección popular; y división del gobierno en tres poderes: Legislativo, Ejecutivo y Judicial. | — | Guerra de Independencia de México#5794-5844 |
| 11 | [ ] | Guerra de Independencia de México | Durante esta época, el movimiento independentista no solo realizó acciones bélicas, sino que se dotó a sí mismo de una estructura y un cuerpo jurídico. | — | Guerra de Independencia de México#8507-8532 |
| 12 | [ ] | Guerra de Independencia de México | Este fue un punto de discordia con López Rayón quien manifestó no estar de acuerdo con el primer punto mencionado en los Sentimientos de la Nación, pues defendía que la tesis que había abrazado el movimiento autonomista de 1808, debería seguir subsistiendo, es decir, América era dependiente del rey de España, pero no de la nación española, por tanto, la independencia buscada no era con respecto a la Corona, sino del … | — | Guerra de Independencia de México#14157-14236 |
| 13 | [ ] | Guerra de Independencia de México | Cronología de la Independencia (1808-1821) (1a. edición). | — | Guerra de Independencia de México#32436-32443 |
| 14 | [ ] | Guerra de Independencia de México | «El inicio de la independencia en México: el cura Hidalgo». | — | Guerra de Independencia de México#32621-32631 |
| 15 | [ ] | Guerra de Independencia de México | Atlas de historia de la revolución de independencia. | — | Guerra de Independencia de México#33480-33488 |
| 16 | [ ] | Historia de México | Aquellas misteriosas muertes pusieron fin a las ideas de sublevaciones en el Virreinato de Nueva España, pero la reciente Independencia de Estados Unidos en 1783 (donde participó Bernardo favoreciendo a los norteamericanos) y el estallido de la Revolución Francesa en 1789, provocarían una inestabilidad en España que marcó el inicio del fin del Virreinato. | — | Historia de México#14205-14259 |
| 17 | [ ] | Historia de México | Inspirados en las revoluciones europeas y la independencia norteamericana, las ideas de independizarse, crecían lentamente. | — | Historia de México#15309-15324 |
| 18 | [ ] | Historia de México | Lo que falta es la independencia. | — | Historia de México#17036-17042 |
| 19 | [ ] | Historia de México | Así, tras 10 días de intenso debate y acuerdos entre ambos, el 24 de febero de 1821 proclaman el Plan de Iguala que proclamaba la Independencia de la América Septentrional bajo tres garantías: independencia, unión y religión. | — | Historia de México#17714-17751 |
| 20 | [ ] | Historia de México | Pero la estrategia jugó en su contra. | — | Historia de México#33236-33243 |
| 21 | [ ] | Historia de México | Pero la pésima geografía jugó en su contra. | — | Historia de México#34146-34154 |
| 22 | [ ] | Miguel Hidalgo y Costilla | Historia de Méjico: desde los primeros movimientos que prepararon su independencia en el año de 1808 hasta la época presente.. | — | Miguel Hidalgo y Costilla#9095-9115 |
| 23 | [ ] | Miguel Hidalgo y Costilla | Historia de Méjico: desde los primeros movimientos que prepararon su independencia en el año de 1808 hasta la época presente (Edición Facsimilar). | — | Miguel Hidalgo y Costilla#9124-9146 |
| 24 | [ ] | Miguel Hidalgo y Costilla | Cronología de la Independencia (1808-1821) (Primera edición). | — | Miguel Hidalgo y Costilla#9173-9180 |
| 25 | [ ] | Miguel Hidalgo y Costilla | De la insurrección a la independencia. | — | Miguel Hidalgo y Costilla#9313-9319 |
| 26 | [ ] | Virreinato de Nueva España | Esta última fue el antecedente directo de la independencia de México, la que, al consumarse en 1821, desintegró el virreinato y dio paso al Primer Imperio mexicano, en el que finalmente se coronaría Agustín de Iturbide. | — | Virreinato de Nueva España#624-660 |
| 27 | [ ] | Virreinato de Nueva España | El virrey, cuyo término significa etimológicamente en lugar del rey, concentraba todo el poder público, como ya se ha dicho. | — | Virreinato de Nueva España#6268-6288 |
| 28 | [ ] | Virreinato de Nueva España | En la Nueva España jugaba un papel de soberano, pero en realidad únicamente obedecía las órdenes del rey de España. | — | Virreinato de Nueva España#6304-6324 |
| 29 | [ ] | Virreinato de Nueva España | Mediante la Primera breve Inter caetera, suscrita por el papa Alejandro VI, se otorga a los Reyes Católicos, en pago a sus servicios y a su fidelidad a la Iglesia católica, la autorización y facultades necesarias para evangelizar a los habitantes de las tierras descubiertas por Cristóbal Colón, apenas un año antes, sirviendo esta bula como apoyo jurídico que permitió a los peninsulares la evangelización y dominio … | — | Virreinato de Nueva España#14687-14759 |
| 30 | [ ] | Virreinato de Nueva España | Algunos franciscanos de relieve en Nueva España fueron: | — | Virreinato de Nueva España#15093-15101 |
| 31 | [ ] | Virreinato de Nueva España | Según el Nican mopohua, jugó un papel importante en la aparición de la Virgen de Guadalupe, en 1531, supuesto que no consta en ninguna otra fuente histórica, ni en sus propias memorias. | — | Virreinato de Nueva España#15130-15162 |
| 32 | [ ] | Virreinato de Nueva España | En el ámbito de la lingüística aplicada, la tipografía jugó un papel crucial al idear soluciones para representar fonemas ausentes en el alfabeto latino. | — | Virreinato de Nueva España#19405-19429 |
| 33 | [ ] | Virreinato de Nueva España | Un ejemplo notable es el de fray Francisco de la Parra, quien hacia 1550 desarrolló una ortografía especializada para las lenguas mayenses. | — | Virreinato de Nueva España#19429-19451 |

---

## M1 (multihop)

**Pregunta:** ¿Qué civilizaciones existían antes de los españoles y cuál dominaba en 1519?
**Puntos clave (guía, no juez):** Olmecas; mayas; teotihuacanos; aztecas; el Imperio Azteca dominaba en 1519
**Anotada:** [ ] sí   (marca esta casilla al terminar la pregunta)

| # | Evidencia | Artículo | Oración | Puntos clave en la oración | Ref |
|---|---|---|---|---|---|
| 1 | [ ] | Civilización maya | El territorio de los mayas y los mayas mantuvieron una relación dinámica con las culturas vecinas, incluyendo los olmecas, los mixtecos, los de Teotihuacán, los aztecas, y otros. | Olmecas, mayas, aztecas | Civilización maya#1111-1139 |
| 2 | [ ] | Civilización maya | En vísperas de la conquista española, varios poderosos estados mayas dominaron las tierras altas de Guatemala. | mayas | Civilización maya#3766-3782 |
| 3 | [ ] | Civilización maya | Periodo de contacto y conquista española (1511-1697 d. C.) | — | Civilización maya#3824-3833 |
| 4 | [ ] | Civilización maya | Desde 1517 hasta 1519, tres expediciones españolas independientes exploraron las costas de Yucatán, y Tabasco, en este último en 1519 entablaron una serie de combates con los habitantes mayas, Destacando la Batalla de Centla contra los mayas chontales de Potonchán, que fue la primera gran batalla de los españoles en lo que más tarde sería la Nueva España. | mayas | Civilización maya#3871-3929 |
| 5 | [ ] | Civilización maya | Los textiles mayas están mal representados en el registro arqueológico, a pesar de que —en comparación con otras culturas precolombinas, como los aztecas y la región andina— es probable que eran artículos de alto valor. | mayas, aztecas | Civilización maya#9569-9604 |
| 6 | [ ] | Civilización maya | Por lo tanto, la interpretación sacerdotal de los registros astronómicos y los libros era crucial, ya que el sacerdote entendería qué deidad necesitaba la propiciación ritual requerida, cuándo realizar las ceremonias correctas, y cuál sería una ofrenda apropiada. | — | Civilización maya#16962-17000 |
| 7 | [ ] | Conquista de México | A partir de estos acontecimientos, que modificaron drásticamente la geopolítica mundial en los albores del siglo XVI, discurrirían aproximadamente tres siglos de dominación territorial española y resistencia indígena. | — | Conquista de México#248-276 |
| 8 | [ ] | Conquista de México | Los que estaban a favor de la aventura, no necesitaban artificios para decidirse: Pues, ¿de qué condición somos los españoles para no ir adelante, y estarnos en partes que no tengamos provecho de guerra? | — | Conquista de México#6439-6473 |
| 9 | [ ] | Conquista de México | Xicohténcatl Huehue, Maxixcatzin, Citlalpopocatzin, Hueyolotzin y algunos otros señores importantes recibieron a los españoles el 18 de septiembre de 1519. | — | Conquista de México#7496-7516 |
| 10 | [ ] | Conquista de México | Pero Alvarado descubrió serios indicios[¿cuál?] de que una conspiración estaba en marcha contra los españoles aprovechando la ausencia de Cortés y que en la ceremonia de honor los españoles serían sacrificados. | — | Conquista de México#11304-11335 |
| 11 | [ ] | Conquista de México | Con esto el camino más directo de Tlaxcala a la base española en Texcoco quedó definitivamente abierto, y los españoles dominaron tanto el este como el sur de la región de lagos. | — | Conquista de México#14547-14579 |
| 12 | [ ] | Conquista de México | -Las obras históricas de Fernando de Alva Ixtlilxóchilt, el Compendio histórico del Reino de Texcoco y la Historia de la nación chichimeca que narran la irrupción española desde la perspectiva de la “familia real texcocana”. | — | Conquista de México#16419-16454 |
| 13 | [ ] | Conquista de México | AGUILAR, Francisco de (1565) "Relación breve de la conquista de la Nueva España" [7] | — | Conquista de México#25013-25027 |
| 14 | [ ] | Cultura olmeca | La palabra "olmeca", simplificación de "Olmecas Uixtotin", significa "habitantes de la región del hule" y fue utilizada por los aztecas y mexicas para nombrar a varios pueblos, étnica y lingüísticamente diversos, que ocuparon la región de Veracruz y Tabasco a través de los siglos. | Olmecas, aztecas | Cultura olmeca#936-980 |
| 15 | [ ] | Cultura teotihuacana | No es asombroso que todas las civilizaciones de la meseta mexicana dijeran descender de la civilización de Teotihuacán. | — | Cultura teotihuacana#10721-10739 |
| 16 | [ ] | Guerra de Independencia de México | A lo largo de los tres siglos de dominio español hubo varios estallidos sociales en la Nueva España, entre ellos la rebelión de los pericúes de 1734 a 1737 en Vieja California, la rebelión de 1761 de los mayas, encabezada por Jacinto Canek y las rebeliones de los seris y los pimas en Sonora a lo largo de todo el siglo XVIII. | mayas | Guerra de Independencia de México#902-964 |
| 17 | [ ] | Guerra de Independencia de México | Los dominios españoles en América ante la ocupación de la metrópoli | — | Guerra de Independencia de México#2775-2786 |
| 18 | [ ] | Hernán Cortés | Los caciques ofrecieron ocho doncellas para que tuvieran descendencia con los españoles. | — | Hernán Cortés#5573-5585 |
| 19 | [ ] | Historia de México | El periodo prehispánico se refiere a todo lo acontecido antes de la llegada de los españoles en 1519. | — | Historia de México#59-77 |
| 20 | [ ] | Historia de México | El periodo virreinal abarca desde la llegada de los españoles a territorio mexicano en 1519, hasta la consumación de la guerra de Independencia en 1821. | — | Historia de México#116-141 |
| 21 | [ ] | Historia de México | A partir de la institución del Virreinato, entre 1521 y 1535 en distintas zonas de México, empezaría una Edad Media, mezcla de feudalismo con despotismo tributario. | — | Historia de México#1026-1052 |
| 22 | [ ] | Historia de México | Todo lo anterior terminó con el inicio de la conquista a manos de los españoles en el siglo XVI. | — | Historia de México#1566-1585 |
| 23 | [ ] | Historia de México | Cronología de los grandes grupos culturales prehispánicos (las fechas son aproximadas y distintos autores discrepan en torno a ellas) hasta la conquista española. | — | Historia de México#3138-3161 |
| 24 | [ ] | Historia de México | A finales del siglo XV y principios del XVI, el Reino de España, al igual que otras potencias europeas como Portugal, buscaba intensamente nuevas rutas comerciales hacia Asia. | — | Historia de México#7409-7437 |
| 25 | [ ] | Historia de México | Fue el fin del discurso antiestadounidense que desde 1847 dominaba al país. | — | Historia de México#64786-64798 |
| 26 | [ ] | Imperio azteca | Cuando los conquistadores españoles llegaron en 1519, célula fundamental de la estructura política en Mesoamérica era el altépetl, una unidad base autónoma, que se asociaba o subordinaba a otras. | — | Imperio azteca#127-156 |
| 27 | [ ] | Imperio azteca | Los mexicas fueron una tribu de nómadas que formaron uno de los imperios más grandes e importantes de la América precolombina en solo 200 años. | — | Imperio azteca#1053-1078 |
| 28 | [ ] | Imperio azteca | Con Moctezuma II (1502-1520), los mexicas se habían transformado en uno de los principales imperios que dominaba un vasto territorio y millones de súbditos. | — | Imperio azteca#1183-1207 |
| 29 | [ ] | Imperio azteca | Cervera Obregón, Marco A., Breve historia de los aztecas, Nowtilus, Madrid, 2008 | aztecas | Imperio azteca#10621-10633 |
| 30 | [ ] | Moctezuma II | Aproximadamente en el año 1507, la nación de Huejotzingo invadiría a Tlaxcala, comenzando una guerra que en su primera etapa duraría alrededor de 5 años. y que en total duraría hasta la llegada de los españoles en 1519. | — | Moctezuma II#8466-8504 |
| 31 | [ ] | Moctezuma II | La crisis volvería a tener efecto tras la llegada de los españoles a México en el año 1519, tras del arresto de Moctezuma II en su propio palacio y la ejecución de un recolector de tributos y militar mexica, Quetzalpopoca, eventos sucedidos entre noviembre y diciembre de 1519. | — | Moctezuma II#11912-11960 |
| 32 | [ ] | Moctezuma II | La primera vez que Moctezuma oyó de la llegada de extranjeros nunca antes vistos, de piel blanca y grandes barbas desde las playas del este, sucedió en el año 13 Tochtli del calendario mexica, equivalente al año 1518 del gregoriano, durante la expedición del explorador español Juan de Grijalva, quien visitó el pueblo maya de Potonchán en ese año. | — | Moctezuma II#12767-12826 |
| 33 | [ ] | Moctezuma II | Según describió Hernán Cortés en la carta, fechada al 30 de octubre de 1520, haciéndola una de nuestras fuentes más tempranas sobre la conquista, Moctezuma sospechaba que los españoles eran descendientes de los ancestros de los mexicas, los cuales emigraron a la tierra del valle de México mucho antes de la llegada de los españoles, pero que ellos eran humanos igual que él, y que los mexican los habían estado … | — | Moctezuma II#16881-16966 |
| 34 | [ ] | Moctezuma II | Estos textos los habrá usado Cortés como una forma de justificar su conquista y su rebelión en contra del gobernador de Cuba ante el rey Carlos, esencialmente asegurando que los mexicas tomaban al rey Carlos como su Mesías, usando la creencia que existía desde la Edad Media en la cual se pensaba del emperador romano-germánico (título que poseía el rey Carlos desde 1519) como un representante de Jesús y defensor del … | — | Moctezuma II#17039-17168 |
| 35 | [ ] | Virreinato de Nueva España | Esta capitanía general fue creada a partir de las conquistas capitaneadas por Francisco de Montejo el Adelantado, que junto con su hijo y sobrino, homónimos, dominaron a los grupos mayas que habitaban la península de Yucatán a su llegada en los albores del siglo XVI. | mayas | Virreinato de Nueva España#986-1031 |
| 36 | [ ] | Virreinato de Nueva España | La conquista de Yucatán fue la más tardía de las que finalmente integraron el virreinato de la Nueva España, ya que los últimos reductos mayas no fueron dominados íntegramente hasta el año de 1697 —es decir, más de siglo y medio después de la conquista de México—, con la conquista de Tayasal. | mayas | Virreinato de Nueva España#1074-1126 |
| 37 | [ ] | Virreinato de Nueva España | En ese mismo período, la labor de los franciscanos hizo posible la fundación de Paso del Norte, en 1682. | — | Virreinato de Nueva España#2285-2304 |
| 38 | [ ] | Virreinato de Nueva España | Cuando los españoles llegaron al Nuevo Mundo, se encontraron con civilizaciones muy bien constituidas: el imperio teocrático de los incas que estaba en su apogeo, la confederación de los mexicas y la cultura maya. | — | Virreinato de Nueva España#11872-11906 |
| 39 | [ ] | Virreinato de Nueva España | Bartolomé de las Casas presidió esta organización religiosa durante su estancia en Nueva España, y en 1542 escribió al rey informándole acerca de la situación social en Nueva España, que más tarde recopiló en su obra Brevísima relación de la destrucción de las Indias. | — | Virreinato de Nueva España#15234-15278 |
| 40 | [ ] | Virreinato de Nueva España | Ya en el siglo XVII existían frailes indígenas y mestizos que dominaban la tipografía en lenguas nativas, colaborando activamente en la producción impresa. | — | Virreinato de Nueva España#19339-19362 |
| 41 | [ ] | Virreinato de Nueva España | Relación breve de la conquista de la Nueva España, de Francisco de Aguilar (1479-1571). | — | Virreinato de Nueva España#21526-21540 |

---

## M2 (multihop)

**Pregunta:** ¿Cómo influyeron las reformas de Juárez en la Revolución décadas después?
**Puntos clave (guía, no juez):** Constitución de 1857; separación Iglesia-Estado; antecedente liberal que Díaz traicionó
**Anotada:** [ ] sí   (marca esta casilla al terminar la pregunta)

| # | Evidencia | Artículo | Oración | Puntos clave en la oración | Ref |
|---|---|---|---|---|---|
| 1 | [ ] | Benito Juárez | Juárez es considerado un símbolo de soberanía nacional, resistencia, libertad y legalidad al liderar a su país durante la Guerra de Reforma y la Segunda Intervención Francesa. | — | Benito Juárez#71-98 |
| 2 | [ ] | Benito Juárez | Además de ser promotor de las Leyes de Reforma y la Constitución de 1857 que consolidaron a México como un estado laico. | Constitución de 1857 | Benito Juárez#98-120 |
| 3 | [ ] | Benito Juárez | Benito Juárez vivió una época crucial en la formación del Estado mexicano, considerada por muchos historiadores como la consolidación de la nación como república. | — | Benito Juárez#139-163 |
| 4 | [ ] | Benito Juárez | En el exilio, Juárez buscó apoyar a la revolución que se estaba gestando en Ayutla. | — | Benito Juárez#2448-2463 |
| 5 | [ ] | Benito Juárez | En diciembre de ese mismo año, durante el golpe de Estado ocasionado por conflictos entre conservadores que apoyaban a la iglesia y liberales que habían apoyado la separación Iglesia-Estado, Juárez fue apresado por las fuerzas del propio Comonfort. | separación Iglesia-Estado | Benito Juárez#2719-2757 |
| 6 | [ ] | Benito Juárez | Juárez llegó a San Luis Potosí, donde intentó rehacer su gobierno. | — | Benito Juárez#4285-4296 |
| 7 | [ ] | Benito Juárez | Fue ahí donde Juárez dio el Grito de Independencia en 1864. | — | Benito Juárez#4727-4738 |
| 8 | [ ] | Benito Juárez | Exactamente un año antes de que terminara el período constitucional de Juárez, González Ortega entró a la oficina de Lerdo de Tejada preguntando si se le entregaría la presidencia ese día o al siguiente, argumentando que la Constitución de 1857 no era muy clara, respecto a lo cual, Lerdo le pidió unas horas para responder. | Constitución de 1857 | Benito Juárez#4919-4974 |
| 9 | [ ] | Benito Juárez | La división entre los republicanos en México se hizo más dramática, ya que el período constitucional de Juárez se acercaba a su fin. | — | Benito Juárez#6697-6720 |
| 10 | [ ] | Benito Juárez | Juárez sale rumbo a Palacio Nacional por "El paseo de la Emperatriz", que desde ese momento cambia de nombre a paseo de la Reforma. | — | Benito Juárez#11185-11209 |
| 11 | [ ] | Benito Juárez | Luego de pasar por el paseo de la Reforma, Juárez y su comitiva se dirigen hacia el Palacio de Minería por la que hoy es la avenida Juárez. | — | Benito Juárez#11221-11249 |
| 12 | [ ] | Benito Juárez | Juárez decía a menudo que eran los tiempos de la paz y la concordia. | — | Benito Juárez#12074-12088 |
| 13 | [ ] | Guerra de Independencia de México | Este grupo estaba concentrado en los consulados de México y Guadalajara, que constituyeron la pieza fundamental en la circulación de capitales en el territorio novohispano. | — | Guerra de Independencia de México#1316-1341 |
| 14 | [ ] | Guerra de Independencia de México | En las últimas décadas del siglo XVIII, Nueva España estaba en bancarrota a causa de la expoliación de sus finanzas por parte de la metrópoli. | — | Guerra de Independencia de México#1506-1531 |
| 15 | [ ] | Guerra de Reforma | La Guerra de Reforma, también conocida como la guerra de los tres años, fue una guerra civil que aconteció en México desde el 17 de diciembre de 1857 al 11 de enero de 1861, como consecuencia de la promulgación de la Constitución de 1857 y en especial de las llamadas Leyes de Reforma. | Constitución de 1857 | Guerra de Reforma#4-57 |
| 16 | [ ] | Guerra de Reforma | Juárez estableció su gobierno, en un primer momento, en Guanajuato, mientras Zuloaga gobernaba en la capital con las llamadas Cinco Leyes, que de hecho derogaban algunas de las reformas liberales como la Ley Lerdo, la Ley Iglesias y la Ley Juárez, entre otras. | — | Guerra de Reforma#768-811 |
| 17 | [ ] | Guerra de Reforma | Las leyes decretadas por Juárez en México en 1859 y 1860, mientras se encontraba situado en el puerto de Veracruz, conocidas como Leyes de Reforma, son consideradas por algunos autores como el punto de quiebre de esta guerra. | — | Guerra de Reforma#935-973 |
| 18 | [ ] | Guerra de Reforma | Leyes de Reforma y Etapas de la Reforma en México. | — | Guerra de Reforma#1857-1867 |
| 19 | [ ] | Historia de México | Así mientras Zuloaga derogaba las leyes de reforma, Juárez intentaría hacerlas cumplir en la capital de Guanajuato. | — | Historia de México#29716-29733 |
| 20 | [ ] | Historia de México | El 31 de julio llegó el decreto de secularización, donde cementerios y panteones pasaron a manos de estado y el 4 de diciembre llegó la ley de libertad de cultos; que si bien protegía el derecho a ejercer la religión, para la iglesia católica cimentada en México por obra de la conquista espiritual, significó un absoluto atentado. | separación Iglesia-Estado | Historia de México#30512-30569 |
| 21 | [ ] | Historia de México | Tras proclamar elecciones, el apoyo a los liberales se hizo rotundamente evidente y Juárez se convirtió en el presidente del país. | — | Historia de México#30647-30668 |
| 22 | [ ] | Historia de México | Maximiliano solicitó revisar las reformas políticas dejadas por el gobierno anterior; no las de Santa Anna, sino las de Juárez. | — | Historia de México#33010-33030 |
| 23 | [ ] | Historia de México | Si bien la idea era introducir gobernantes de pensamiento liberal en estas ciudades, los verdaderos liberales le eran fiel a Juárez. | — | Historia de México#33243-33264 |
| 24 | [ ] | Historia de México | Fue el círculo cercano a Juárez quien le hizo ver la guerra ya no era por defensa de las leyes liberales o la reforma, sino por soberanía nacional. | — | Historia de México#33428-33456 |
| 25 | [ ] | Historia de México | Fue paradójico que quien mayor impulso dio al poder liberal, fuese la corona de Maximiliano, y eso lo sabía Juárez. | — | Historia de México#34478-34498 |
| 26 | [ ] | Historia de México | Por eso cuando Juárez retornó triunfal como presidente a la Ciudad de México en julio de 1867, la mejor forma en que pudo legitimar el poder republicano fue restablecer la Constitución de 1857, ejecutar de nuevo las Leyes de Reforma y llamar a elecciones el 22 de septiembre. | Constitución de 1857 | Historia de México#34498-34546 |
| 27 | [ ] | Historia de México | Temiendo que el Congreso tuviese más poder como había ocurrido toda la primera mitad del siglo XIX, Juárez dividió al poder legislativo en cámara alta y baja, Senadores y Diputados. | — | Historia de México#34565-34595 |
| 28 | [ ] | Historia de México | Benito Juárez, que de los muchos aciertos que tuvo, quizá el mayor fue escuchar a sus consejeros y gobernar en conjunto con una generación que cambió al país. | — | Historia de México#37012-37040 |
| 29 | [ ] | Historia de México | Una vez electos, de diciembre de 1916 a enero de 1917 se reunieron en la ciudad de Querétaro para redactarla; en los debates se conformaron dos sectores, los radicales y los moderados, los primeros querían elevar a la constitución los derechos sociales, laborales y agrarios, los segundos mantener el espíritu liberal de la carta magna de 1857; el resultado fue la creación de la primera constitución en el mundo que … | Constitución de 1857 | Historia de México#48089-48215 |
| 30 | [ ] | Historia de México | Esta característica resultó contraproducente, pues significó el inicio de varios elementos distintivos de la política mexicana en las siguientes décadas. | — | Historia de México#65254-65274 |
| 31 | [ ] | Historia de México | Igualmente, el Partido de la Revolución Democrática, se convirtió en uno de los opositores de la reforma votando en contra de ella en ambas cámaras e interponiendo acciones legales en contra de la reforma publicada. | — | Historia de México#73872-73907 |
| 32 | [ ] | Imperio azteca | Parece ser que en algunas regiones el cacao se continuó usando hasta el siglo XIX, ya después de la Independencia de México. | — | Imperio azteca#4716-4738 |
| 33 | [ ] | Imperio azteca | La región volcánica de Zináparo (en el actual Estado de Michoacán) nos muestra cómo se obtenía la obsidiana en la época prehispánica. | — | Imperio azteca#5991-6013 |
| 34 | [ ] | Imperio azteca | Influyeron en la lengua y la cerámica ceremonial. | — | Imperio azteca#9834-9842 |
| 35 | [ ] | Moctezuma II | Sin embargo, esta situación cambiaría drásticamente después de que una serie de guerras entre México y Huejotzingo influyeron en las fuerzas militares de esta región volviéndose más débiles, lo cual provocó que Tlaxcala se volviera la región más poderosa del valle después de una desastrosa invasión huejotzinga apoyada por México. | — | Moctezuma II#4594-4644 |
| 36 | [ ] | Moctezuma II | Los datos ofrecidos en el Códice Florentino sobre esta leyenda fueron escritos décadas después de la conquista, aproximadamente en 1555. | — | Moctezuma II#12537-12557 |
| 37 | [ ] | Pancho Villa | Rentería y Seañez finalmente recibieron pequeñas pensiones del gobierno décadas después de la muerte de Villa. | — | Pancho Villa#4925-4941 |
| 38 | [ ] | Porfiriato | Con la entrada de José Ives Limantour en Hacienda en 1893 surgió un auge de las compañías enajenadoras de terrenos comunes baldíos, se modificó la Constitución de 1857 para permitir las reelecciones y se aprobó la ley que otorgaba la gran explotación minera a los capitales de los Estados Unidos y el Reino Unido. | Constitución de 1857 | Porfiriato#588-642 |
| 39 | [ ] | Revolución mexicana | Durante estos 35 años, México experimentó un notable crecimiento económico y tuvo estabilidad política, pero estos logros se realizaron con altos costos sociales, que pagaron los estratos menos favorecidos de la sociedad y la oposición política al régimen de Díaz. | — | Revolución mexicana#63-103 |
| 40 | [ ] | Revolución mexicana | La Revolución mexicana conllevó varios cambios sociales. | — | Revolución mexicana#12503-12510 |
| 41 | [ ] | Revolución mexicana | Durante el conflicto armado muchos camarógrafos mexicanos siguieron los acontecimientos de la revolución. | — | Revolución mexicana#13720-13733 |
| 42 | [ ] | Revolución mexicana | A partir de la década de 1930 comienza en México la llamada "Época de oro del cine mexicano", período durante el cual la Revolución mexicana fue un tema recurrente. | — | Revolución mexicana#13817-13846 |
| 43 | [ ] | Revolución mexicana | Wikiquote alberga frases célebres de o sobre Revolución mexicana. | — | Revolución mexicana#14452-14461 |

---

## T1 (trampa) — PREGUNTA TRAMPA

**Pregunta:** ¿Quién es el presidente actual de México?
**Puntos clave (guía, no juez):** 
**Anotada:** [ ] sí   (marca esta casilla al terminar la pregunta)

| # | Evidencia | Artículo | Oración | Puntos clave en la oración | Ref |
|---|---|---|---|---|---|
| 1 | [ ] | Benito Juárez | Benito Pablo Juárez García (San Pablo Guelatao, Intendencia de Oaxaca; 21 de marzo de 1806 - Ciudad de México, 18 de julio de 1872), conocido como El Benemérito de las Américas, fue un abogado, jurista y político mexicano de origen indígena de la etnia zapoteca que se desempeñó como presidente de México desde el 21 de enero de 1858 hasta su fallecimiento el 18 de julio de 1872. | — | Benito Juárez#3-71 |
| 2 | [ ] | Benito Juárez | Su biografía durante los años que ocupó la presidencia es una parte sobresaliente de la historia de México. | — | Benito Juárez#206-224 |
| 3 | [ ] | Benito Juárez | Siward, el apoyo para ocupar por duodécima vez la presidencia de México. | — | Benito Juárez#8406-8418 |
| 4 | [ ] | Benito Juárez | Juárez instruyó a Sebastián Lerdo de Tejada que se encargara de convocar las elecciones. | — | Benito Juárez#11511-11525 |
| 5 | [ ] | Benito Juárez | de Arqueología, Historia y Etnografía de México y de allí en 1939 al Instituto Nacional de Antropología e Historia que lo dispuso exhibir en el Museo Nacional de Historia que es su ubicación actual. | — | Benito Juárez#15184-15218 |
| 6 | [ ] | Benito Juárez | A la ceremonia de iniciación de Juárez concurrieron distinguidos masones, como Manuel Crescencio Rejón, autor de la Constitución de Yucatán de 1840; Valentín Gómez Farías, presidente de México; Pedro Zubieta, comandante General en el Distrito Federal y el Estado de México; el diputado Fernando Ortega; el diputado Tiburcio Cañas; el diputado Francisco Banuet; el diputado Agustín Buenrostro; el diputado Joaquín … | — | Benito Juárez#15504-15572 |
| 7 | [ ] | Conquista de México | Poco después Cortés sospechó de una posible sublevación simultánea por parte de los mexicas tanto en el viaje como en la ciudad. | — | Conquista de México#20276-20298 |
| 8 | [ ] | Conquista de México | El 17 de abril de 1535 se creó el Virreinato de Nueva España y Antonio de Mendoza fue nombrado virrey, gobernador, capitán general y presidente de la Real Audiencia de México. | — | Conquista de México#22479-22510 |
| 9 | [ ] | Conquista de México | Faltaban algunos territorios por agregarse al creciente dominio español en América del Norte y lo que se conoce hoy como México: | — | Conquista de México#22652-22673 |
| 10 | [ ] | Conquista de México | Más avanzado el período virreinal de la Nueva España, el Nuevo Reino de León se dividió en tres regiones: la colonia de Nuevo Santander, que corresponde en gran medida al actual estado de Tamaulipas; el propio Nuevo Reino de León, que corresponde prácticamente al actual estado de Nuevo León y Nueva Extremadura, que es el actual estado de Coahuila. | — | Conquista de México#23805-23864 |
| 11 | [ ] | Conquista de México | México: Porrúa. p. 236. | — | Conquista de México#23936-23940 |
| 12 | [ ] | Cultura olmeca | La cultura olmeca fue una civilización que se desarrolló durante el periodo preclásico de Mesoamérica, en parte de los territorios actuales de México. | — | Cultura olmeca#3-26 |
| 13 | [ ] | Cultura teotihuacana | La vegetación del valle de Teotihuacán ha cambiado poco respecto a la época prehispánica, aunque es evidente que el paisaje actual es resultado de una combinación de factores naturales y antropogénicos. | — | Cultura teotihuacana#2358-2389 |
| 14 | [ ] | Hernán Cortés | En 1981, el entonces presidente de México José López Portillo trató de promover el reconocimiento público de Hernán Cortés. | — | Hernán Cortés#13950-13969 |
| 15 | [ ] | Historia de México | La historia de México es la narración cronológica y demostrable de los acontecimientos del pasado relacionados con el actual territorio de México, país ubicado en América del Norte. | — | Historia de México#4-32 |
| 16 | [ ] | Historia de México | El México moderno abarca la consolidación del presidencialismo (y los sexenios), la estabilidad de los partidos políticos y culmina con el inicio de cambio de régimen en 1994. | — | Historia de México#1849-1877 |
| 17 | [ ] | Historia de México | Se le denomina México contemporáneo desde 1994 hasta la actualidad, protagonista de los últimos procesos recientes o actuales. | — | Historia de México#1877-1895 |
| 18 | [ ] | Historia de México | El territorio actual de México fue descubierto y habitado por grupos de cazadores y recolectores nómadas hace más de 30 000 años. | — | Historia de México#1998-2020 |
| 19 | [ ] | Historia de México | La época virreinal fue la base del mosaico cultural y racial del actual México. | — | Historia de México#9947-9961 |
| 20 | [ ] | Historia de México | Vasconcelos, amenazado de muerte, proclamó el Plan de Guaymas donde llamaba al país a levantarse en armas, pero la amplia sociedad mexicana que veía la consolidación del poder y ya estaba harta de 20 años de guerra, simplemente hizo caso omiso. | — | Historia de México#54377-54418 |
| 21 | [ ] | Historia de México | Pero la vida en México tenía que seguir con o sin presidente. | — | Historia de México#54680-54692 |
| 22 | [ ] | Historia de México | Fue el primer y único presidente en la historia de México en renunciar al cargo por voluntad propia. | — | Historia de México#55166-55184 |
| 23 | [ ] | Historia de México | Mientras tanto en México, daba inicio la carrera por la sucesión presidencial. | — | Historia de México#63983-63995 |
| 24 | [ ] | Historia de México | El 2 de julio de 2000 se llevaron a cabo las elecciones presidenciales; México vivió por primera vez, tras 71 años de gobiernos priistas, la alternancia política cuando Vicente Fox candidato de la Alianza por el cambio (de los partidos Acción Nacional y Verde Ecologista de México), con el 43.5 % de los votos, derrotó al PRI (y su candidato Francisco Labastida) y a la Alianza por México (y su candidato Cuauhtémoc … | — | Historia de México#70890-70963 |
| 25 | [ ] | Historia de México | Andrés Manuel López Obrador desempeñó el cargo de Presidente de México desde el 1 de diciembre de 2018 hasta el 30 de septiembre de 2024. | — | Historia de México#75242-75267 |
| 26 | [ ] | Historia de México | Fue juramentada como presidenta de México el 1 de octubre de 2024. | — | Historia de México#75892-75904 |
| 27 | [ ] | Historia de México | Contenido relacionado con México. | — | Historia de México#75912-75916 |
| 28 | [ ] | Imperio azteca | El Cihuacóatl del Imperio Mexica era una especie de "coemperador". | — | Imperio azteca#1509-1519 |
| 29 | [ ] | Imperio azteca | El actual territorio del estado México fue el principal y mayor tributario de maderas, carnes y vegetales del Imperio azteca. | — | Imperio azteca#10197-10217 |
| 30 | [ ] | Miguel Hidalgo y Costilla | En México se le considera el padre de la Patria. | — | Miguel Hidalgo y Costilla#55-65 |
| 31 | [ ] | Miguel Hidalgo y Costilla | Breve historia de México. | — | Miguel Hidalgo y Costilla#9389-9393 |
| 32 | [ ] | Moctezuma II | El actual embajador de México en Estados Unidos, Esteban Moctezuma Barragán, es descendiente de Moctezuma. | — | Moctezuma II#20187-20202 |
| 33 | [ ] | Porfiriato | México: del antiguo régimen a la revolución. | — | Porfiriato#5112-5119 |
| 34 | [ ] | Revolución mexicana | En el estado de Coahuila surgió además el libro La sucesión presidencial en 1910, donde su autor, un hacendado de nombre Francisco I. Madero, hace un análisis de la situación política mexicana y además hace una crítica el gobierno de Díaz, aunque de manera moderada y positiva. | — | Revolución mexicana#2145-2192 |
| 35 | [ ] | Revolución mexicana | A raíz de la entrevista de Creelman al presidente Díaz, y de la aparición del libro de Madero, surgieron varios partidos políticos, algunos a favor del actual gobierno y otros completamente en contra. | — | Revolución mexicana#2192-2225 |
| 36 | [ ] | Revolución mexicana | Se nombraba además a Carranza jefe del «Ejército Constitucionalista» y se le daba la facultad de ocupar interinamente la presidencia de México para convocar a elecciones. | — | Revolución mexicana#7246-7272 |
| 37 | [ ] | Virreinato de Nueva España | Incluyó lo que actualmente es México, más los actuales estados estadounidenses de California, Nevada, Colorado, Utah, Nuevo México, Arizona, Texas, Oregón, Washington, Florida y partes de Idaho, Montana, Wyoming, Kansas, Oklahoma y Luisiana, por parte de los actuales Estados Unidos; así como la parte suroeste de la Columbia Británica del actual Canadá; más la capitanía general de Guatemala (que incluía los actuales … | — | Virreinato de Nueva España#156-290 |

---

## T2 (trampa) — PREGUNTA TRAMPA

**Pregunta:** ¿Cuál es el PIB actual de México?
**Puntos clave (guía, no juez):** 
**Anotada:** [ ] sí   (marca esta casilla al terminar la pregunta)

| # | Evidencia | Artículo | Oración | Puntos clave en la oración | Ref |
|---|---|---|---|---|---|
| 1 | [ ] | Benito Juárez | de Arqueología, Historia y Etnografía de México y de allí en 1939 al Instituto Nacional de Antropología e Historia que lo dispuso exhibir en el Museo Nacional de Historia que es su ubicación actual. | — | Benito Juárez#15184-15218 |
| 2 | [ ] | Benito Juárez | México: Fondo de Cultura Económica. | — | Benito Juárez#15627-15632 |
| 3 | [ ] | Conquista de México | En 1598, Juan de Oñate cruzó el paso del norte, donde hoy se encuentran las ciudades de El Paso y Ciudad Juárez, para dirigirse a los territorios de los actuales estados de Nuevo México y Texas comenzando de esta manera la colonización y sometimiento de algunos pueblos originarios como los zuñi, hopi, wichita y los acoma. | — | Conquista de México#23355-23411 |
| 4 | [ ] | Conquista de México | Más avanzado el período virreinal de la Nueva España, el Nuevo Reino de León se dividió en tres regiones: la colonia de Nuevo Santander, que corresponde en gran medida al actual estado de Tamaulipas; el propio Nuevo Reino de León, que corresponde prácticamente al actual estado de Nuevo León y Nueva Extremadura, que es el actual estado de Coahuila. | — | Conquista de México#23805-23864 |
| 5 | [ ] | Conquista de México | México: Porrúa. p. 236. | — | Conquista de México#23936-23940 |
| 6 | [ ] | Cultura olmeca | La cultura olmeca fue una civilización que se desarrolló durante el periodo preclásico de Mesoamérica, en parte de los territorios actuales de México. | — | Cultura olmeca#3-26 |
| 7 | [ ] | Cultura teotihuacana | La mayor parte de la población de la ciudad se dispersó por diversas localidades en la cuenca de México. | — | Cultura teotihuacana#493-512 |
| 8 | [ ] | Cultura teotihuacana | Se han realizado investigaciones con el propósito de observar cuál ha sido el impacto de la actividad humana sobre los suelos de Teotihuacán. | — | Cultura teotihuacana#2241-2264 |
| 9 | [ ] | Cultura teotihuacana | La vegetación del valle de Teotihuacán ha cambiado poco respecto a la época prehispánica, aunque es evidente que el paisaje actual es resultado de una combinación de factores naturales y antropogénicos. | — | Cultura teotihuacana#2358-2389 |
| 10 | [ ] | Cultura teotihuacana | Las condiciones del valle favorecieron la concentración demográfica por ser benéficas para el estilo de vida mesoamericano basado en la agricultura. | — | Cultura teotihuacana#2521-2542 |
| 11 | [ ] | Cultura teotihuacana | La larga presencia de los otomíes en el valle de México ha llevado a plantear que ellos fueron los fundadores de la ciudad. | — | Cultura teotihuacana#2776-2799 |
| 12 | [ ] | Guerra de Independencia de México | La pérdida de esta posesión tuvo una importancia decisiva para la economía del Imperio español, ya que los ingresos mexicanos representaban el ochenta por ciento del total de los caudales americanos al final del periodo colonial. | — | Guerra de Independencia de México#54-90 |
| 13 | [ ] | Guerra de Independencia de México | México: Fondo de Cultura Económica, El Colegio de México, Fideicomiso Historia de las Américas. pp. 11-50. | — | Guerra de Independencia de México#32413-32429 |
| 14 | [ ] | Guerra de Independencia de México | México: Fondo de Cultura Económica. | — | Guerra de Independencia de México#32515-32520 |
| 15 | [ ] | Guerra de Independencia de México | México: Fondo de Cultura Económica. | — | Guerra de Independencia de México#32574-32579 |
| 16 | [ ] | Guerra de Independencia de México | México: Fondo de Cultura Económica, El Colegio de México, Fideicomiso Historia de las Américas. pp. 84-104. | — | Guerra de Independencia de México#32599-32615 |
| 17 | [ ] | Guerra de Independencia de México | México: Fondo de Cultura Económica. | — | Guerra de Independencia de México#33411-33416 |
| 18 | [ ] | Guerra de Independencia de México | México: Fondo de Cultura Económica. | — | Guerra de Independencia de México#33437-33442 |
| 19 | [ ] | Historia de México | La historia de México es la narración cronológica y demostrable de los acontecimientos del pasado relacionados con el actual territorio de México, país ubicado en América del Norte. | — | Historia de México#4-32 |
| 20 | [ ] | Historia de México | Se le denomina México contemporáneo desde 1994 hasta la actualidad, protagonista de los últimos procesos recientes o actuales. | — | Historia de México#1877-1895 |
| 21 | [ ] | Historia de México | El territorio actual de México fue descubierto y habitado por grupos de cazadores y recolectores nómadas hace más de 30 000 años. | — | Historia de México#1998-2020 |
| 22 | [ ] | Historia de México | La época virreinal fue la base del mosaico cultural y racial del actual México. | — | Historia de México#9947-9961 |
| 23 | [ ] | Historia de México | El país llegó a tasas de crecimiento que no había tenido, ni siquiera durante el Milagro mexicano, en 1979 fue de 9.7 % y el promedio general del sexenio repitió las de aquel lapso con 6.57 %. | — | Historia de México#68442-68479 |
| 24 | [ ] | Historia de México | La economía dio un salto cuantitativo respecto a la crisis de 1994, alcanzando tasas de crecimiento similares a las del Milagro mexicano a partir de 1997. | — | Historia de México#70639-70665 |
| 25 | [ ] | Historia de México | Andrés Manuel López Obrador desempeñó el cargo de Presidente de México desde el 1 de diciembre de 2018 hasta el 30 de septiembre de 2024. | — | Historia de México#75242-75267 |
| 26 | [ ] | Historia de México | Contenido relacionado con México. | — | Historia de México#75912-75916 |
| 27 | [ ] | Imperio azteca | Los aztecas se establecieron en el centro del valle de México, expandiendo su control hacia ciudades-estado ubicadas en los actuales estados de México, Morelos, Veracruz, y otros; la costa de Chiapas e Hidalgo. | — | Imperio azteca#1019-1052 |
| 28 | [ ] | Imperio azteca | Otras provincias eran Tochtepec (en el actual Estado de Oaxaca), que pagaba 7 ristras y 3 cuentas grandes; Xoconochco (en el Estado de Chiapas, donde ahora está la frontera entre Guatemala y México), que pagaba 2 ristras (3 según un documento de 1554); Cuetlaxtlan (en el Estado de Veracruz), que pagaba una; y Tuchpa (en el norte de Veracruz), que pagaba 2, además de una ristra de cuentas y dos mosaicos de turquesa. | — | Imperio azteca#6475-6548 |
| 29 | [ ] | Imperio azteca | El actual territorio del estado México fue el principal y mayor tributario de maderas, carnes y vegetales del Imperio azteca. | — | Imperio azteca#10197-10217 |
| 30 | [ ] | Moctezuma II | El actual embajador de México en Estados Unidos, Esteban Moctezuma Barragán, es descendiente de Moctezuma. | — | Moctezuma II#20187-20202 |
| 31 | [ ] | Porfiriato | En este banco participaba capital mexicano y español, y tenía las siguientes funciones: recaudaba impuestos, otorgaba préstamos y anticipos al gobierno y se encargaba de la Tesorería General. | — | Porfiriato#1155-1183 |
| 32 | [ ] | Porfiriato | Zavala, Silvio: Apuntes de historia nacional 1808-1974 México:Fondo de Cultura Económica (1995) ISBN 968-16-3442-X. | — | Porfiriato#5241-5255 |
| 33 | [ ] | Revolución mexicana | Durante estos 35 años, México experimentó un notable crecimiento económico y tuvo estabilidad política, pero estos logros se realizaron con altos costos sociales, que pagaron los estratos menos favorecidos de la sociedad y la oposición política al régimen de Díaz. | — | Revolución mexicana#63-103 |
| 34 | [ ] | Revolución mexicana | La mayoría de las fuentes apuntan que entre un millón, y tres millones de personas murieron durante esta etapa de la historia de México. | — | Revolución mexicana#12036-12060 |
| 35 | [ ] | Virreinato de Nueva España | Incluyó lo que actualmente es México, más los actuales estados estadounidenses de California, Nevada, Colorado, Utah, Nuevo México, Arizona, Texas, Oregón, Washington, Florida y partes de Idaho, Montana, Wyoming, Kansas, Oklahoma y Luisiana, por parte de los actuales Estados Unidos; así como la parte suroeste de la Columbia Británica del actual Canadá; más la capitanía general de Guatemala (que incluía los actuales … | — | Virreinato de Nueva España#156-290 |

---

## T3 (trampa) — PREGUNTA TRAMPA

**Pregunta:** ¿Qué equipos jugaron la final del fútbol mexicano en 2024?
**Puntos clave (guía, no juez):** 
**Anotada:** [ ] sí   (marca esta casilla al terminar la pregunta)

| # | Evidencia | Artículo | Oración | Puntos clave en la oración | Ref |
|---|---|---|---|---|---|
| 1 | [ ] | Conquista de México | Era la víspera del ataque final. | — | Conquista de México#15149-15155 |
| 2 | [ ] | Conquista de México | México: Porrúa. p. 236. | — | Conquista de México#23936-23940 |
| 3 | [ ] | Cultura olmeca | Aunque se han encontrado vestigios de su presencia en amplias zonas de Mesoamérica, se considera que el área cultural olmeca —zona metropolitana— abarca la parte sureste del estado mexicano de Veracruz y el oeste de Tabasco. | — | Cultura olmeca#26-62 |
| 4 | [ ] | Cultura olmeca | En ocasiones para sus representaciones religiosas tienden a la abstracción, con lo cual no se sabe exactamente qué pudo significar la muerte. | — | Cultura olmeca#1975-1997 |
| 5 | [ ] | Cultura teotihuacana | En la actualidad parece haber consenso en torno a la cronología propuesta por René Millon y su equipo de colaboradores. | — | Cultura teotihuacana#3742-3762 |
| 6 | [ ] | Cultura teotihuacana | Sugiyama y su equipo han demostrado que la cueva fue cavada completamente por humanos. | — | Cultura teotihuacana#8962-8976 |
| 7 | [ ] | Cultura teotihuacana | El remoto pasado de México (trad. | — | Cultura teotihuacana#13343-13349 |
| 8 | [ ] | Guerra de Independencia de México | El movimiento de la independencia de México tiene como marco la Ilustración y las revoluciones liberales de la última parte del siglo XVIII. | — | Guerra de Independencia de México#124-147 |
| 9 | [ ] | Guerra de Independencia de México | La economía novohispana entró en crisis a final del siglo XVIII, período que coincide con las reformas borbónicas adoptadas por la Corona. | — | Guerra de Independencia de México#1356-1378 |
| 10 | [ ] | Guerra de Independencia de México | Esta era la situación en Nueva España al final del primer tercio de 1817. | — | Guerra de Independencia de México#19710-19724 |
| 11 | [ ] | Guerra de Independencia de México | Ese mismo año, la República mexicana se integró por diecinueve estados (Yucatán argumentaría más tarde su incorporación como república federada), cinco territorios y un distrito federal. | — | Guerra de Independencia de México#32158-32184 |
| 12 | [ ] | Guerra de Independencia de México | Historia de México, desde los primeros movimientos que depararon su independencia en 1808 hasta la época presente. | — | Guerra de Independencia de México#32241-32258 |
| 13 | [ ] | Guerra de Independencia de México | Historia de México: legado y pasado reciente. | — | Guerra de Independencia de México#32499-32506 |
| 14 | [ ] | Guerra de Independencia de México | Historia mínima de México. | — | Guerra de Independencia de México#32536-32540 |
| 15 | [ ] | Guerra de Independencia de México | Revista de Estudios Históricos (México) (julio-diciembre): 212-216. | — | Guerra de Independencia de México#32688-32695 |
| 16 | [ ] | Guerra de Independencia de México | Consultado el 26 de junio de 2024. | — | Guerra de Independencia de México#32775-32782 |
| 17 | [ ] | Guerra de Reforma | Nueva Historia general de México, pp. 444-464. | — | Guerra de Reforma#1885-1892 |
| 18 | [ ] | Historia de México | En 1910 inició la Revolución Mexicana, un periodo de grandes conflictos entre múltiples facciones y con distintos principios durante el transcurso de la misma: su fecha de terminación es actualmente objeto de debate entre distintos historiadores, pues la sitúan en 1917, 1920 o 1924. | — | Historia de México#1773-1817 |
| 19 | [ ] | Historia de México | Se le denomina México contemporáneo desde 1994 hasta la actualidad, protagonista de los últimos procesos recientes o actuales. | — | Historia de México#1877-1895 |
| 20 | [ ] | Historia de México | Fue evidente que México superaba en número y ganaría a Estados Unidos, pero la tarde del día 23 cuando ya estaba por acabar con el ejército estadounidense, Santa Anna ordenó la retirada rumbo a Agua Nevada y su regreso a San Luis Potosí. | — | Historia de México#25890-25933 |
| 21 | [ ] | Historia de México | Todo jugaba en contra de México: inferioridad de capacidades militares, disputas por el poder en la capital, nueve cambios en la presidencia entre siete personajes (Paredes Arrillaga, Bravo, Salas, Gómez Farías, Santa Anna, Anaya y De la Peña); la indiferencia de los estados para proveer defensa nacional; las divisiones entre los combatientes e incluso en medio de la guerra, los federalistas reinstalaron la … | — | Historia de México#26038-26104 |
| 22 | [ ] | Historia de México | Los estadounidenses permanecieron en la Ciudad de México cerca de 5 meses, tiempo en el cual la crónicas de su trato con los mexicanos eran funestas. | — | Historia de México#26623-26649 |
| 23 | [ ] | Historia de México | Pero la estrategia jugó en su contra. | — | Historia de México#33236-33243 |
| 24 | [ ] | Historia de México | Pero la pésima geografía jugó en su contra. | — | Historia de México#34146-34154 |
| 25 | [ ] | Historia de México | Aquel sería para muchos el punto cumbre de la revolución mexicana. | — | Historia de México#48413-48424 |
| 26 | [ ] | Historia de México | En 1970, México volvió a estar en la mira del mundo con la celebración del Campeonato Mundial de Fútbol. | — | Historia de México#67347-67366 |
| 27 | [ ] | Historia de México | El México contemporáneo de 1970 al 2000 se caracterizó por un proceso —económicamente hablando— contrario a la anterior sección: tras el fin del Milagro mexicano, la economía tuvo un proceso de desfortalecimiento y que, debido a las dudosa administración de José López Portillo, se desencadenó en 1982 con el estallido de una crisis económica, en la que el enfoque del «Estado benefactor» y el modelo de sustitución de … | — | Historia de México#67369-67456 |
| 28 | [ ] | Historia de México | Andrés Manuel López Obrador desempeñó el cargo de Presidente de México desde el 1 de diciembre de 2018 hasta el 30 de septiembre de 2024. | — | Historia de México#75242-75267 |
| 29 | [ ] | Historia de México | Claudia Sheinbaum, sucesora política del presidente López Obrador, ganó las elecciones presidenciales de 2024 y al asumir el cargo, se convirtió en la primera mujer en dirigir el país en la historia de México. | — | Historia de México#75858-75892 |
| 30 | [ ] | Historia de México | Fue juramentada como presidenta de México el 1 de octubre de 2024. | — | Historia de México#75892-75904 |
| 31 | [ ] | Historia de México | Contenido relacionado con México. | — | Historia de México#75912-75916 |
| 32 | [ ] | Imperio azteca | Consultado el 3 de enero de 2024. | — | Imperio azteca#10832-10839 |
| 33 | [ ] | Pancho Villa | En 1971 existió un grupo de rock mexicano llamado La División del Norte. | — | Pancho Villa#6411-6424 |
| 34 | [ ] | Pancho Villa | El Gobierno de México, en su honor, declaró el año 2023 como el Año de Francisco Villa por su legado e importancia en el desarrollo de la Revolución mexicana. | — | Pancho Villa#6774-6803 |
| 35 | [ ] | Revolución mexicana | Durante estos 35 años, México experimentó un notable crecimiento económico y tuvo estabilidad política, pero estos logros se realizaron con altos costos sociales, que pagaron los estratos menos favorecidos de la sociedad y la oposición política al régimen de Díaz. | — | Revolución mexicana#63-103 |
| 36 | [ ] | Revolución mexicana | Al final fue asesinado al salir del sótano de la vivienda en donde se ocultaba. | — | Revolución mexicana#2918-2933 |
| 37 | [ ] | Revolución mexicana | Algunas fuentes lo sitúan en el año de 1917, con la proclamación de la Constitución mexicana, o 1924 con la de Plutarco Elías Calles. | — | Revolución mexicana#12355-12379 |
| 38 | [ ] | Virreinato de Nueva España | Breve Historia de México. | — | Virreinato de Nueva España#23403-23407 |
