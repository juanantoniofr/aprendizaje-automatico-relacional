# Node2Vec: La evolución de Word2Vec para grafos

Si Word2Vec se usa para palabras, **Node2Vec** es su evolución directa aplicada a **grafos** (redes de nodos y conexiones, como redes sociales, moléculas o sistemas de transporte).

Como los grafos no tienen "frases" escritas que el modelo pueda leer, Node2Vec crea sus propias frases simulando "caminantes" que recorren los nodos al azar (Random Walks). Luego, le pasa estas secuencias al algoritmo de Word2Vec.

La configuración que mencionas define exactamente cómo se construirán esas rutas y cómo las procesará la red neuronal. Aquí tienes el desglose de lo que hace cada parámetro:

### 1. `dimensions = 64` (El tamaño de la representación)

Determina que cada nodo del grafo se convertirá en un vector de **64 números**.

- **Qué hace:** En lugar de usar 300 dimensiones (lo común en textos masivos), 64 es un tamaño intermedio. Es suficiente para capturar patrones estructurales complejos en un grafo mediano o grande, pero lo bastante ligero para que el modelo se entrene rápido y no consuma tanta memoria.

### 2. `walk_length = 30` (La longitud de la "frase")

Define cuántos saltos dará el caminante virtual en una sola expedición.

- **Qué hace:** Si empieza en el Nodo A, saltará de vecino en vecino hasta visitar 30 nodos seguidos. Esta secuencia de 30 nodos se tratará exactamente igual que una frase de 30 palabras en Word2Vec.

### 3. `num_walks = 200` (La intensidad de la exploración)

Indica cuántas caminatas independientes se iniciarán desde **cada uno** de los nodos del grafo.

- **Qué hace:** Si tu grafo tiene 1,000 nodos, Node2Vec lanzará 200 caminatas desde el Nodo 1, luego 200 desde el Nodo 2, y así sucesivamente. Al final, generará un total de 200,000 "frases" de 30 nodos de largo. Esto asegura que el algoritmo explore exhaustivamente todas las rutas posibles del vecindario de cada nodo.

### 4. `window = 10` (El radio de aprendizaje o contexto)

Es el parámetro clásico de Word2Vec aplicado a la caminata.

- **Qué hace:** Al analizar uno de los nodos dentro de una caminata generada, el modelo intentará predecir cuáles son los **10 nodos anteriores y los 10 nodos siguientes** en esa ruta específica. Un tamaño de ventana de 10 es bastante amplio; significa que el modelo considerará que dos nodos son "similares" no solo si están conectados directamente, sino también si pertenecen a la misma comunidad o vecindario extendido dentro del grafo.

---

### Resumen del comportamiento

Con esta configuración, le estás pidiendo a Node2Vec una **exploración muy profunda y extensa**. Al tener 200 caminatas por nodo y una ventana amplia de 10, el modelo priorizará entender la **estructura global y las comunidades** del grafo (nodos de la misma "tribu" tendrán vectores similares), en lugar de fijarse solo en las conexiones hiper-locales y directas.
