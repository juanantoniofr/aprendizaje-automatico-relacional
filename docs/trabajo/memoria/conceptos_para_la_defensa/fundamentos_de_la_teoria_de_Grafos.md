# Fundamentos de la Teoría de Grafos para el Aprendizaje Automático Relacional

En el aprendizaje automático relacional, la estructura matemática del grafo se utiliza para representar conjuntos de datos donde los ejemplos (los nodos) mantienen relaciones explícitas entre sí. A diferencia del aprendizaje automático clásico, que asume que cada ejemplo es independiente, aquí la propia red aporta información adicional que puede mejorar la predicción.

Para la defensa, tenemos que saber explicar las tres métricas topológicas principales que el documento rector exige extraer para utilizarlas como propiedades predictivas en tus modelos:

**1. Medidas de Centralidad**
Evalúan la "importancia" o la influencia relativa de un nodo dentro de la red. Debes tener claras principalmente dos:

- **Centralidad de Grado (_Degree_):** Es la medida más directa e indica simplemente el número de conexiones (citas) que tiene un nodo.
- **Centralidad de Intermediación (_Betweenness_):** Identifica nodos estructurales clave. _Nota estratégica (basada en tus decisiones de diseño previas):_ Debes explicarle al profesor que elegisteis esta métrica porque mide cuántas veces un artículo actúa como el "camino más corto" (o puente) entre otros dos nodos, lo que es ideal para detectar publicaciones interdisciplinares que conectan diferentes áreas temáticas del conocimiento.

**2. Coeficiente de Clustering**
Mide la densidad local de la red; es decir, la tendencia de los nodos a agruparse formando vecindarios muy interconectados. De forma matemática y gráfica, evalúa cuántos de los vecinos de un nodo están también conectados entre sí, formando lo que en teoría de grafos se denominan subestructuras cerradas o **triángulos**. Si te preguntan, puedes justificar que un alto coeficiente de _clustering_ revela que un artículo pertenece a un núcleo de investigación muy específico y fuertemente cohesionado.

**3. Detección de Comunidades**
Consiste en particionar el grafo para agrupar los nodos en subconjuntos latentes (clústeres) que están más densamente conectados entre sí que con el resto de la red. El documento de la práctica muestra comparativas de algoritmos clásicos para esta tarea, concretamente **Louvain, Girvan-Newman y Walktrap**.

- _Justificación para la defensa:_ Como consolidasteis en la Tarea 1.4, decidisteis usar el algoritmo de **Louvain**. Puedes argumentar que tomasteis esta decisión porque es un método altamente eficiente y, como se muestra en los esquemas teóricos proporcionados por el profesor, suele alcanzar valores superiores en la métrica de **modularidad** (una medida que evalúa la calidad de la división en comunidades) en comparación con otros enfoques.
