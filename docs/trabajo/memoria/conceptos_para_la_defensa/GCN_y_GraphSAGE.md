# GCN y GraphSAGE: Las Redes Neuronales de Grafos que están revolucionando el análisis de redes

A diferencia de los modelos clásicos que han usado en el proyecto (como kNN o Árboles de Decisión) que esperan datos en forma de tabla clásica, las Redes Neuronales de Grafos están diseñadas de forma nativa para "entender" redes donde los elementos están conectados entre sí.

Aquí tienes la explicación directa de cada uno de estos dos modelos avanzados:

### 1. GCN (Graph Convolutional Network)

Es el estándar de oro inicial para trabajar con grafos. Su nombre viene de la "convolución", un concepto que se usa mucho en inteligencia artificial para analizar imágenes mirando los píxeles vecinos.

- **¿Cómo funciona?** GCN actualiza la representación matemática de un nodo (un artículo científico) combinando sus propias características con las de todos sus vecinos directos en el grafo.
- **Su limitación:** Es un modelo "transductivo". Esto significa que necesita ver el grafo completo durante el entrenamiento. Si mañana publicas un artículo nuevo y lo añades a la red Cora, tendrías que volver a entrenar el modelo GCN casi desde cero para que entienda dónde encaja el nuevo artículo.

### 2. GraphSAGE (Graph Sample and AggreGate)

GraphSAGE nació para solucionar los problemas de escalabilidad de GCN. "SAGE" viene de _Sample_ (Muestrear) y _Aggregate_ (Agregar).

- **¿Cómo funciona?** En lugar de mirar a _todos_ los vecinos de un nodo a la vez (lo cual colapsaría la memoria de un ordenador si el grafo es gigante, como las conexiones de Facebook), GraphSAGE toma una **muestra aleatoria** de vecinos de cada nodo y combina su información.
- **Su superpoder:** Es un modelo "inductivo". En lugar de aprender un vector fijo para cada nodo existente, aprende una _función_ (una receta). Esto significa que si introduces un artículo completamente nuevo en la red, GraphSAGE puede aplicar su receta y clasificarlo inmediatamente sin necesidad de reentrenarse.

---

### ¿Por qué son el futuro natural de este proyecto?

En el documento, los autores logran su mejor resultado (un F1-macro de 0.8680) usando **Node2Vec** combinado con kNN.

El problema de Node2Vec es que, aunque es muy bueno aprendiendo la topología (quién se conecta con quién mediante "random walks"), es completamente **ciego a los textos** durante esa fase. Aprende la estructura por un lado y luego le pega los atributos textuales.

**GCN y GraphSAGE hacen magia porque combinan ambas cosas simultáneamente.** Mientras la red neuronal procesa quién cita a quién, _también_ está leyendo las palabras clave de los artículos en ese mismo instante. Esta capacidad de fusionar topología (estructura) y características de los nodos (texto) en un solo paso es lo que hace que arrasen en datasets como Cora.
