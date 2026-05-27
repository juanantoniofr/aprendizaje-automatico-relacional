# Tarea 1.4: Extracción de características relacionales.

El objetivo principal de esta etapa es realizar la **construcción manual de _features_ (características) relacionales** para caracterizar los nodos de la red de citas. En lugar de usar únicamente las palabras del texto de las publicaciones, vamos a utilizar la estructura del grafo para obtener nueva información predictiva.

Específicamente, se exige extraer métricas basadas en tres conceptos clave de la teoría de grafos:

- 1. **Centralidad:** Mide la importancia de un nodo en la red. Dependiendo de la función que usemos en `NetworkX`, podemos medir la centralidad de grado (_degree_), la de cercanía (_closeness_) o la de intermediación (_betweenness_).
- 2. **Coeficiente de clustering:** Mide la tendencia de los nodos a agruparse en triángulos o vecindarios densos.
- 3. **Detección de comunidades:** Sirve para agrupar las publicaciones en clústeres fuertemente conectados (se pueden usar métodos como _Louvain_, _Girvan-Newman_ o _Walktrap_).

Una vez extraídas, estas métricas se combinarán opcionalmente con las propiedades nativas de los nodos (el vector de 1433 palabras) para entrenar los modelos de _Machine Learning_.

## ¿Qué información necesitamos de las tareas anteriores?

Necesitamos lo siguiente sobre el resultado de la Tarea 1.3:

- 1. **El objeto del grafo:** Ya tenemos construido el objeto de la red en memoria (normalmente llamado `G`) usando `NetworkX` a partir de los 2708 nodos y 5429 enlaces del dataset Cora.
- 2. **El tipo de grafo:** Hemos construido un grafo no dirigido (`nx.Graph()`).

## Preguntas a responder:

- ¿por qué hemos elegido un grafo no dirigido para representar la red de citas?

Tener un grafo no dirigido simplifica el cálculo y es el tipo de grafo ideal (y en algunos casos, un requisito estricto) para que funcionen los algoritmos de detección de comunidades y el coeficiente de clustering de NetworkX.
