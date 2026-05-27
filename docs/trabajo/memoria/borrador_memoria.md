Basándonos en la plantilla oficial proporcionada por el profesor, podemos inicializar el documento Markdown copiando exactamente esta estructura:

## Resumen y Palabras clave:

Un par de párrafos con el objetivo principal y las conclusiones.

## I. Introducción:

Contexto general, el objetivo marcado y cómo habéis enfocado la solución.

## II. Preliminares:

_Breve introducción a las técnicas empleadas (como Scikit-Learn o NetworkX) y trabajos relacionados (aquí podéis mencionar el paper \_Collective Classification in Network Data_ que usa el dataset Cora)\_

### Métodos empleados:

Para la representación y procesamiento de los datos relacionales se ha empleado la librería de Python _NetworkX_. Esta herramienta permite modelar la red de documentos científicos como un grafo matemático, facilitando la extracción de métricas topológicas complejas. Específicamente, nos apoyamos en la teoría de grafos para calcular medidas topológicas de centralidad, densidad local (coeficiente de _clustering_) y algoritmos de detección de comunidades para identificar subestructuras cohesivas dentro de la red de citas.

Para la etapa de modelado y clasificación, se ha empleado la librería _Scikit-Learn_. El enfoque adoptado incluye el entrenamiento y la evaluación comparativa de cuatro algoritmos de aprendizaje automático supervisado con distintas naturalezas teóricas: algoritmos basados en instancias (_k-Vecinos más Cercanos_, kNN), modelos de particionado recursivo (Árboles de Decisión), aproximaciones probabilísticas (_Naive Bayes_ Gaussiano) y modelos conexionistas (Redes Neuronales de tipo Perceptrón Multicapa o MLP).

### Trabajo Relacionado:

El análisis y clasificación de nodos en redes interconectadas es un problema ampliamente abordado en la literatura. Como referencia fundamental para nuestro enfoque, destaca el trabajo de Sen _et al._ (2008)[1] sobre clasificación colectiva en datos de redes, en el cual los autores emplean precisamente el conjunto de datos Cora para predecir la temática de los artículos científicos basándose en la correlación de sus enlaces y propiedades. Su investigación demuestra que aprovechar la estructura subyacente de la red (por ejemplo, mediante algoritmos iterativos o inferencia aproximada) mejora significativamente el rendimiento frente a clasificadores tradicionales que tratan cada documento de forma independiente.

## III. Metodología:

_Es la sección más importante durante el desarrollo; aquí debéis describir el dataset, las métricas relacionales y los algoritmos empleados._

### A. Construcción del Grafo y Decisiones de Diseño Topológico

El conjunto de datos Cora original consta de 2708 publicaciones científicas y 5429 enlaces de citación. Para el cálculo de las métricas relacionales, se tomó la **decisión de diseño** de modelar la red de citas como un grafo no dirigido. Esta decisión se fundamenta en dos motivos principales: en primer lugar, permite la fusión de las citas recíprocas (es decir, publicaciones que se citan mutuamente), lo que redujo de forma natural y correcta la red a 5278 aristas únicas; en segundo lugar, la representación como grafo no dirigido es un requisito estructural para garantizar la correcta convergencia y eficiencia de diversos algoritmos de la teoría de grafos, en particular los métodos de detección de comunidades y el cálculo del coeficiente de _clustering_ local. Por otro lado, se garantizó explícitamente la inclusión de nodos aislados que carecían de enlaces pero que poseían propiedades atributivas válidas para la clasificación final.

### B. Extracción de Características Relacionales

Para enriquecer la representación de cada publicación científica más allá de su vector nativo de palabras, se construyó manualmente un conjunto de características (_features_) relacionales evaluando el papel topológico de cada nodo en el grafo. Concretamente, se extrajeron las siguientes métricas:

- **Medidas de Centralidad:** Se evaluó la importancia relativa de cada publicación dentro de la red. Además de la centralidad de grado (_Degree Centrality_), que mide proporcionalmente la cantidad directa de citas de un documento, se decidió implementar la **centralidad de intermediación (_Betweenness Centrality_)** [2]. La elección de esta métrica frente a otras alternativas (como la centralidad de cercanía) radica en su alta capacidad predictiva para identificar nodos que actúan como "puentes" de información entre diferentes áreas temáticas del conocimiento, capturando una dependencia relacional compleja dentro de la red de citas.
- **Coeficiente de Clustering:** Para medir la tendencia de las publicaciones a agruparse en vecindarios densos, se calculó la densidad de triángulos locales (_clustering_) de cada nodo. Esta métrica ayuda a identificar si un artículo pertenece a un núcleo de investigación fuertemente interconectado.
- **Detección de Comunidades:** Se agrupó la red global en clústeres temáticos latentes mediante el **algoritmo de Louvain** [3]. Como decisión de diseño ante las diferentes alternativas (tales como _Girvan-Newman_ o _Walktrap_), se seleccionó Louvain debido a que maximiza de forma eficiente la modularidad del particionado en grafos no dirigidos (alcanzando valores teóricos de similitud superiores a otros métodos). A cada publicación se le asignó un identificador numérico entero correspondiente a la comunidad subyacente descubierta basándose exclusivamente en la topología de los enlaces.

Todas estas propiedades estructurales fueron consolidadas en una única estructura de datos tabular, indexada por el identificador de cada artículo, lista para ser combinada estadísticamente con las propiedades nativas de los documentos.

### C. Configuración Experimental y Modelado

Para la tarea de clasificación de los nodos, se construyó un conjunto de datos consolidado uniendo las 1433 características nativas de los artículos (el vector de palabras) con las características relacionales topológicas extraídas en la fase anterior (centralidad, _clustering_ y comunidad).

Para garantizar una evaluación justa de la capacidad de generalización de los algoritmos, el conjunto de datos se dividió en subconjuntos de entrenamiento (80%) y prueba (20%) mediante el método de validación por retención (_holdout_). Como **decisión de diseño fundamental**, se aplicó una partición estratificada en esta división. Dado que el análisis exploratorio previo reveló un notable desbalanceo de clases (siendo el tema "Neural_Networks" mayoritario y "Rule_Learning" marcadamente minoritario), la estratificación resulta imperativa para preservar la proporción real de las clases en ambos subconjuntos y evitar sesgos en el entrenamiento.

El ajuste de los hiperparámetros de los cuatro modelos base se llevó a cabo mediante una búsqueda en rejilla (_Grid Search_) utilizando validación cruzada estratificada de 5 pliegues (_5-fold cross validation_). Para la selección de la mejor configuración se optó por la métrica _F1-macro_ en lugar de la exactitud global (_Accuracy_). Esta **decisión de diseño** se fundamenta en que el _F1-macro_ calcula el promedio no ponderado de la medida F1 de cada clase, obligando al modelo a penalizar los errores cometidos en las clases minoritarias. De este modo, se asegura que el clasificador se esfuerce en identificar correctamente temáticas con escasos ejemplos, en lugar de sobreajustarse a predecir siempre la clase mayoritaria.

## IV. Resultados:

_Detalle de la configuración de los experimentos, los datos obtenidos y, muy importante, el análisis crítico y comparativa entre modelos._

Los experimentos iniciales tuvieron como propósito establecer una línea base de rendimiento mediante la evaluación de los cuatro modelos construidos (kNN, Naive Bayes, Árbol de Decisión y MLP) utilizando el conjunto de datos integrado (características nativas más relacionales). Tras la optimización de los hiperparámetros mediante validación cruzada en el conjunto de entrenamiento, los modelos definitivos fueron evaluados sobre el 20% de los datos reservados para prueba.

En la Tabla I se resume el rendimiento comparativo de los modelos sobre el subconjunto de validación, destacando su exactitud global y su rendimiento _F1-macro_.

**TABLA I. RENDIMIENTO DE LOS MODELOS BASE EN EL CONJUNTO DE PRUEBA**

| Modelo                     | Exactitud (Accuracy) | F1-macro  | Precision (macro) | Recall (macro) |
| :------------------------- | :------------------: | :-------: | :---------------: | :------------: |
| **Árbol de Decisión**      |      **0.771**       | **0.758** |     **0.762**     |   **0.760**    |
| Perceptrón Multicapa (MLP) |        0.730         |   0.717   |       0.721       |     0.717      |
| Naive Bayes Gaussiano      |        0.452         |   0.428   |       0.437       |     0.422      |
| k-Vecinos más Cercanos     |        0.422         |   0.416   |       0.469       |     0.406      |

_Análisis Crítico:_

Como se observa en los resultados empíricos, el Árbol de Decisión obtuvo con diferencia el mejor rendimiento de generalización, alcanzando un _F1-macro_ de 0.758, seguido por la red neuronal MLP. Por el contrario, los modelos kNN y Naive Bayes mostraron un desempeño significativamente deficiente (ambos por debajo del 0.43 en F1-macro). El éxito del Árbol de Decisión (configurado con una profundidad máxima de 20 y criterio de Gini) sugiere que la combinación de las variables relacionales y textuales requiere reglas de corte jerárquicas y no lineales para discriminar eficazmente la temática de los artículos científicos.

El análisis de la matriz de confusión del Árbol de Decisión demostró que el uso de la métrica _F1-macro_ durante el ajuste de hiperparámetros cumplió su objetivo con éxito: el clasificador mantuvo tasas de verdaderos positivos consistentes a lo largo de todas las temáticas, logrando predecir de forma competente incluso las clases menos representadas, como "Rule_Learning", evitando así el colapso de la red hacia la clase dominante.

## V. Conclusiones:

Resumen de lo conseguido e ideas de trabajo futuro.

## Referencias:

_Listado bibliográfico._

- _[Ref 1]_ Sen, P., Namata, G., Bilgic, M., Getoor, L., Gallagher, B., & Eliassi-Rad, T. (2008). Collective Classification in Network Data. _AI Magazine_, 29(3), 93-106.
- _[Ref 2]_ Fortunato, S. (2010). "Community detection in graphs". _Physics Reports_, 486(3-5): 75-174. _(Para justificar la detección de comunidades)_.
- _[Ref 3]_ Koschützki, D., et al. (2005). "Centrality Indices". In Network Analysis: Methodological Foundations, pp. 16-61, LNCS 3418, Springer-Verlag. _(Para justificar la centralidad)_.

---

**Consejos para ir completándolo sobre la marcha:**

1.  **Cero código:** Recordad la regla estricta de que **en ningún caso debe incluirse código en la memoria**. En lugar de pegar vuestros scripts de Python, usad el Markdown para ir redactando el pseudocódigo de vuestros algoritmos o los esquemas de la red.
2.  **Justificación continua:** Al cerrar tareas como la 1.4 (Extracción de características), id directamente a la sección "III. Metodología" de vuestro Markdown y explicad **las dificultades encontradas y las decisiones de diseño adoptadas** (por ejemplo, por qué usasteis _Betweenness_ o _Louvain_).
3.  **Integración visual:** A medida que avancéis, podéis ir insertando en este documento las gráficas que ya habéis generado en vuestra exploración de datos (como la distribución de grados o el subgrafo) para tenerlas referenciadas de cara al apartado de "Metodología" o "Resultados".

Hacer esto os garantizará cumplir con los criterios de evaluación del profesor sin tener que redactar seis páginas desde cero en la última semana.

**💡 Consejo para tu compañero y tú:** Al pegar este texto en vuestro archivo `borrador_memoria.md`, recordad actualizar los números entre corchetes `[ ]` para que coincidan secuencialmente con el orden en el que iréis listando la bibliografía al final de vuestro artículo IEEE.

**💡 Consejo:**
Recuerda que en el formato de artículo de la IEEE, las tablas tienen una numeración romana (Tabla I, Tabla II, etc.). He llamado a esta "Tabla II" asumiendo que quizá tengas otra tabla antes en tu sección de Exploración de Datos (EDA). Si es vuestra primera y única tabla, cámbiale el nombre a "Tabla I".
