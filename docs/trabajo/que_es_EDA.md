El Análisis Exploratorio de Datos (EDA, por sus siglas en inglés) es la fase inicial de cualquier proyecto de ciencia de datos, y consiste en investigar, describir y resumir las características principales de tu conjunto de datos antes de aplicar algoritmos complejos. Su objetivo es entender qué forma tienen los datos, detectar anomalías, identificar patrones y evaluar si hay problemas (como datos faltantes o clases desbalanceadas).

Dado que el trabajo se centra en el **aprendizaje automático relacional** enfocado en extraer conocimiento de datos estructurados como grafos, y el dataset **Cora** es una red de citas de publicaciones científicas, el EDA será diferente al de un dataset tabular tradicional.

En un dataset relacional como Cora, el EDA debe enfocarse tanto en la estructura de la red (el grafo) como en el contenido de los nodos.

Debería consistir en los siguientes pasos:

**1. Análisis a nivel de Estructura (El Grafo)**
Como los datos son relacionales, necesitas entender la topología de la red:

- **Tamaño de la red:** ¿Cuántos nodos (publicaciones) y aristas (citas) hay en total?
- **Distribución de grados (Degree distribution):** ¿Cuántas citas recibe o hace en promedio cada artículo? Es útil graficar esto para ver si hay "nodos hub" (artículos muy citados).
- **Densidad del grafo:** ¿Qué tan conectada está la red en general?
- **Componentes conexas:** ¿Está todo el grafo conectado en una sola gran red, o hay islas (subgrafos) de artículos que solo se citan entre ellos y están aislados del resto?

**2. Análisis a nivel de Nodos (Características/Features)**
En Cora, cada nodo tiene características (normalmente un vector binario de _bag-of-words_ o bolsa de palabras que indica si ciertas palabras aparecen en el artículo).

- **Dimensionalidad:** ¿Cuántas características (palabras del vocabulario) tiene cada nodo?
- **Dispersión (Sparsity):** Dado que es un texto convertido a binario, la mayoría de los valores serán cero. ¿Qué tan dispersa es esta matriz de características?
- **Valores faltantes o nulos:** Verificar si hay nodos que no tengan características o atributos incompletos (aunque Cora suele venir limpio, es un paso obligatorio del EDA).

**3. Análisis de la Variable Objetivo (Las Etiquetas)**
El objetivo clásico en Cora es clasificar el tema o campo del artículo (por ejemplo, Redes Neuronales, Algoritmos Genéticos, etc.).

- **Distribución de clases:** ¿Cuántas clases diferentes hay? ¿Están balanceadas? Es decir, ¿hay aproximadamente el mismo número de artículos para cada tema, o hay temas predominantes? Esto es vital para saber si necesitarás técnicas para tratar el desbalanceo durante el entrenamiento.

**4. Análisis Relacional (Homofilia)**
Este es el paso más crucial en el aprendizaje automático relacional.

- **Medir la homofilia:** Consiste en comprobar si los nodos conectados tienden a tener la misma etiqueta. En el caso de Cora: ¿Es cierto que los artículos de "Aprendizaje Reforzado" tienden a citar mayoritariamente a otros artículos de "Aprendizaje Reforzado"? Si la homofilia es alta, la estructura del grafo será muy predictiva para tu modelo.

**Herramientas recomendadas para hacer esto en Python:**
Puedes usar bibliotecas clásicas como `pandas`, `matplotlib` y `seaborn` para las distribuciones de clases y características, combinadas con `NetworkX` para el análisis de la topología del grafo y sus medidas de centralidad.
