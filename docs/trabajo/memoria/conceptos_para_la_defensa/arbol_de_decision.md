# Árbol de Decisión

## ¿Por qué en la linea base el algoritmo Árbol de decisión es el que tiene mejor rendimiento?

En la línea base, el modelo utiliza un espacio de entrada compuesto por **1437 variables predictivas** (1433 variables textuales binarias que indican la presencia de palabras clave y 4 características relacionales). Este espacio presenta una **altísima dispersión (_sparsity_ del 98.73%)**, lo que significa que la inmensa mayoría de los atributos textuales para un documento dado son ceros.

El **Árbol de Decisión** logra el mejor rendimiento global en este escenario (alcanzando un F1-macro de 0.7588 en el conjunto de prueba) por las siguientes razones fundamentales:

- **Reglas de corte ortogonal:** Los árboles de clasificación operan construyendo su modelo a través de reglas jerárquicas de particionado basadas en umbrales de variables individuales (por ejemplo, cortes lógicos del tipo _¿Está presente la palabra clave X? Sí/No_).
- **Robustez ante datos binarios dispersos:** Este mecanismo de particionado directo se adapta a la perfección a espacios de alta dimensionalidad que son extremadamente dispersos y binarios.
- **Independencia de distancias geométricas:** La ventaja más crítica del Árbol de Decisión es que **no depende del cálculo de distancias euclídeas entre ejemplos**. En un espacio disperso de 1437 dimensiones, los algoritmos basados en distancias (como k-Vecinos más Cercanos o kNN) son víctimas de la **"maldición de la dimensionalidad"**. En este fenómeno matemático, los puntos del espacio se vuelven casi equidistantes entre sí y la distancia pierde toda su capacidad discriminativa.

Al no requerir métricas de proximidad espacial y trazar las fronteras de decisión basándose directamente en la presencia o ausencia de palabras concretas, el Árbol de Decisión maximiza la extracción de información en la matriz dispersa inicial, posicionándose como el clasificador más fuerte de la línea base.

## ¿por qué el mecanismo de particionado directo del algoritmo de árbol de decisión se adapta a la perfección a espacios de alta dimensionalidad que son extremadamente dispersos y binarios?

El mecanismo de particionado directo de los Árboles de Decisión (CART) se adapta de forma excepcional a este entorno debido a cómo procesa matemáticamente la información en cada paso de su construcción, ignorando el "ruido" masivo de las dimensiones vacías.

Las razones matemáticas y operativas son las siguientes:

**1. Evaluación aislada de características (Fronteras ortogonales)**
El algoritmo CART construye el modelo mediante un particionado recursivo, dividiendo el conjunto de entrenamiento nodo a nodo. En cada nodo interno, el algoritmo **evalúa un solo atributo de manera aislada** (por ejemplo, una palabra específica) y establece un umbral de corte, eligiendo una rama u otra en función de si el ejemplo supera o no dicho umbral. Al evaluar las variables de una en una, el árbol es ciego a la inmensa cantidad de dimensiones irrelevantes; sencillamente ignorará aquellas palabras que no aporten información discriminativa, evitando que el exceso de dimensiones degrade el modelo.

**2. Cortes perfectos sobre datos binarios**
En el dataset Cora, 1433 de las 1437 variables son binarias, representando la presencia (1) o ausencia (0) de palabras clave. Para los atributos discretos, el árbol de decisión evalúa los umbrales en los puntos medios de los valores existentes (en este caso, 0.5). Esto transforma el mecanismo matemático en una regla lógica binaria pura: _¿contiene el documento la palabra X? (Sí/No)_. Este enfoque directo es tremendamente eficiente en conjuntos de atributos dicotómicos.

**3. Maximización de pureza en un entorno disperso (_Sparsity_)**
El objetivo del particionado es encontrar la condición que devuelva los subconjuntos de datos más "puros" posibles, minimizando funciones de impureza como el índice de Gini. Dada la altísima dispersión del texto (98.73% de ceros), la gran mayoría de los documentos no tienen una palabra específica. Sin embargo, cuando una palabra clave está presente, suele ser altamente indicativa de una temática. El árbol detecta inmediatamente qué palabra específica minimiza la impureza global y realiza el corte, aislando de forma instantánea a los documentos que la poseen en una hoja muy pura de su estructura jerárquica.

**4. Inmunidad a distancias diluidas**
Esta es la gran diferencia frente a algoritmos como k-Vecinos más Cercanos (kNN). El modelo kNN arrastra la "maldición de la dimensionalidad" porque al buscar similitudes tiene que calcular distancias (como la euclídea) utilizando las 1437 dimensiones simultáneamente. En un espacio con un 98% de ceros, la apabullante coincidencia en la "ausencia de palabras" entre dos documentos ahoga por completo la similitud real aportada por las pocas palabras que sí comparten. El Árbol de Decisión, al no basarse en ninguna métrica de proximidad espacial o geométrica, es totalmente inmune a esta dilución de las distancias.
