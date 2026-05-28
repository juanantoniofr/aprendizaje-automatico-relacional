Basándonos en la plantilla oficial proporcionada por el profesor, podemos inicializar el documento Markdown copiando exactamente esta estructura:

## Resumen y Palabras clave:

Un par de párrafos con el objetivo principal y las conclusiones.

## I. Introducción:

Contexto general, el objetivo marcado y cómo habéis enfocado la solución.

## II. Preliminares:

_Breve introducción a las técnicas empleadas (como Scikit-Learn o NetworkX) y trabajos relacionados (aquí podéis mencionar el paper \_Collective Classification in Network Data_ que usa el dataset Cora)\_

### Métodos empleados:

Para la representación y procesamiento de los datos relacionales se ha empleado la librería de Python _NetworkX_. Esta herramienta permite modelar la red de documentos científicos como un grafo matemático, facilitando la extracción de métricas topológicas complejas. Específicamente, nos apoyamos en la teoría de grafos para calcular medidas topológicas de centralidad, densidad local (coeficiente de _clustering_) y algoritmos de detección de comunidades para identificar subestructuras cohesivas dentro de la red de citas.

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

## IV. Resultados:

Detalle de la configuración de los experimentos, los datos obtenidos y, muy importante, el análisis crítico y comparativa entre modelos.

## V. Conclusiones:

Resumen de lo conseguido e ideas de trabajo futuro.

## Referencias:

Listado bibliográfico.

---

**Consejos para ir completándolo sobre la marcha:**

1.  **Cero código:** Recordad la regla estricta de que **en ningún caso debe incluirse código en la memoria**. En lugar de pegar vuestros scripts de Python, usad el Markdown para ir redactando el pseudocódigo de vuestros algoritmos o los esquemas de la red.
2.  **Justificación continua:** Al cerrar tareas como la 1.4 (Extracción de características), id directamente a la sección "III. Metodología" de vuestro Markdown y explicad **las dificultades encontradas y las decisiones de diseño adoptadas** (por ejemplo, por qué usasteis _Betweenness_ o _Louvain_).
3.  **Integración visual:** A medida que avancéis, podéis ir insertando en este documento las gráficas que ya habéis generado en vuestra exploración de datos (como la distribución de grados o el subgrafo) para tenerlas referenciadas de cara al apartado de "Metodología" o "Resultados".

Hacer esto os garantizará cumplir con los criterios de evaluación del profesor sin tener que redactar seis páginas desde cero en la última semana.

### Para la sección "REFERENCIAS"

**(Asegúrate de tener estas referencias en el listado bibliográfico al final del documento, ya que están citadas en el texto anterior):**

- _[Ref 1]_ Sen, P., Namata, G., Bilgic, M., Getoor, L., Gallagher, B., & Eliassi-Rad, T. (2008). Collective Classification in Network Data. _AI Magazine_, 29(3), 93-106.
- _[Ref 2]_ Fortunato, S. (2010). "Community detection in graphs". _Physics Reports_, 486(3-5): 75-174. _(Para justificar la detección de comunidades)_.
- _[Ref 3]_ Koschützki, D., et al. (2005). "Centrality Indices". In Network Analysis: Methodological Foundations, pp. 16-61, LNCS 3418, Springer-Verlag. _(Para justificar la centralidad)_.

---

**💡 Consejo para tu compañero y tú:** Al pegar este texto en vuestro archivo `borrador_memoria.md`, recordad actualizar los números entre corchetes `[ ]` para que coincidan secuencialmente con el orden en el que iréis listando la bibliografía al final de vuestro artículo IEEE.
