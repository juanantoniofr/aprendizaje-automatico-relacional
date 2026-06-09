# Tarea 1.4: Extracción de características relacionales.

El objetivo principal de esta etapa es realizar la **construcción manual de _features_ (características) relacionales** para caracterizar los nodos de la red de citas. En lugar de usar únicamente las palabras del texto de las publicaciones, vamos a utilizar la estructura del grafo para obtener nueva información predictiva.

Específicamente, se exige extraer métricas basadas en tres conceptos clave de la teoría de grafos:

- 1. **Centralidad:** Mide la importancia de un nodo en la red. Dependiendo de la función que usemos en `NetworkX`, podemos medir la centralidad de grado (_degree_), la de cercanía (_closeness_) o la de intermediación (_betweenness_).
  - _degree_: Número de conexiones directas que tiene un nodo (número de citas recibidas).
  - _closeness_: Mide la distancia promedio de un nodo a todos los demás nodos, indicando qué tan cerca está de otros artículos en la red.
  - _betweenness_: Mide la cantidad de veces que un nodo actúa como puente a lo largo de los caminos más cortos entre otros nodos, indicando su papel como intermediario en la difusión de información.
- 2. **Coeficiente de clustering:** Mide la tendencia de los nodos a agruparse en triángulos o vecindarios densos.
- 3. **Detección de comunidades:** Sirve para agrupar las publicaciones en clústeres fuertemente conectados (se pueden usar métodos como _Louvain_, _Girvan-Newman_ o _Walktrap_).

Una vez extraídas, estas métricas se combinarán opcionalmente con las propiedades nativas de los nodos (el vector de 1433 palabras) para entrenar los modelos de _Machine Learning_.

## ¿Qué información necesitamos de las tareas anteriores?

Necesitamos lo siguiente sobre el resultado de la Tarea 1.3:

- 1. **El objeto del grafo:** Ya tenemos construido el objeto de la red en memoria (normalmente llamado `G`) usando `NetworkX` a partir de los 2708 nodos y 5429 enlaces del dataset Cora.
- 2. **El tipo de grafo:** Hemos construido un grafo no dirigido (`nx.Graph()`).

## Preguntas a responder:

### Grafo dirigido vs. no dirigido

- ¿por qué hemos elegido un **grafo no dirigido** para representar la red de citas?

Un **grafo no dirigido** (undirected graph) es una estructura de red donde las conexiones (aristas o _edges_) entre los elementos (nodos) **no tienen una dirección específica**.

Imagínalo como una calle de doble sentido: si el nodo A está conectado con el nodo B, entonces el nodo B también está conectado con el nodo A de forma inherente. La relación es bidireccional y simétrica.

### ¿Cuándo y por qué se usa?

- **Cuándo se usa:** Se utiliza para modelar relaciones que son naturalmente **simétricas o recíprocas**.
- _Ejemplos del mundo real:_ Una red de amistades en Facebook (si yo soy tu amigo, tú eres el mío), interacciones entre proteínas en biología, o coautoría en artículos científicos (si escribimos un artículo juntos, ambos somos coautores).

- **Por qué se usa:** 1. **Simplicidad computacional:** Requieren menos memoria y los algoritmos que corren sobre ellos suelen ser más sencillos y rápidos.

2.  **Flujo de información:** En el aprendizaje automático de grafos (como las Graph Neural Networks - GNNs), a menudo queremos que la información o las características (features) fluyan en ambas direcciones entre nodos conectados para que el modelo aprenda el contexto local, independientemente de quién inició la conexión.

### ¿Cuáles son las alternativas?

1. **Grafo Dirigido (_Directed Graph_ o _DiGraph_):** Las aristas tienen dirección (como calles de un solo sentido). Que A apunte a B no significa que B apunte a A.

- _Ejemplo:_ Seguidores en Twitter (yo puedo seguirte, pero tú no a mí).

2. **Grafo Ponderado (_Weighted Graph_):** Puede ser dirigido o no dirigido, pero cada arista tiene un "peso" o valor que representa la fuerza, distancia o costo de la conexión.
3. **Multigrafo (_Multigraph_):** Permite múltiples aristas entre el mismo par de nodos (útil si dos personas han colaborado en varios artículos diferentes).

---

### Tu caso: El dataset Cora y NetworkX

El dataset **Cora** es una red de citas de artículos científicos de Machine Learning.

- Los **nodos** son los artículos.
- Las **aristas** son las citas entre ellos.

**El "truco" con Cora:**
Por naturaleza, una red de citas es **DIRIGIDA**. Un artículo reciente (A) cita a un artículo antiguo (B), por lo que la flecha va de A hacia B ($A \rightarrow B$). El artículo B nunca citará al A porque fue publicado antes.

Sin embargo, en el aprendizaje automático (por ejemplo, si estás haciendo clasificación de nodos para predecir el tema de un artículo), **es una práctica estándar convertir el dataset Cora en un grafo NO DIRIGIDO.** ¿Por qué? Porque si A cita a B, es muy probable que hablen del mismo tema. Al volverlo no dirigido, permites que tu modelo propague información temática tanto de A hacia B como de B hacia A durante el entrenamiento.

**Cómo se maneja esto en NetworkX:**

NetworkX tiene clases específicas para cada tipo. Aquí te muestro cómo interactúan en tu contexto:

```python
import networkx as nx

# 1. Crear un grafo dirigido (la naturaleza original de Cora)
G_dirigido = nx.DiGraph()
G_dirigido.add_edge("Artículo A", "Artículo B") # A cita a B

print("¿Es dirigido?", G_dirigido.is_directed()) # True
print("B apunta a A?", G_dirigido.has_edge("Artículo B", "Artículo A")) # False

# 2. Convertir a grafo NO dirigido para Machine Learning
G_no_dirigido = G_dirigido.to_undirected()

print("\n¿Es dirigido?", G_no_dirigido.is_directed()) # False
print("B apunta a A?", G_no_dirigido.has_edge("Artículo B", "Artículo A")) # True

# 3. Crear un grafo no dirigido desde cero
G_base = nx.Graph()
G_base.add_edge("Art 1", "Art 2")

```

**En resumen para tu proyecto:** Si estás analizando la historia o la influencia (quién citó a quién), mantén Cora como `nx.DiGraph()` (dirigido). Si estás construyendo un modelo para clasificar los artículos basándote en sus vecinos, conviértelo a `nx.Graph()` (no dirigido) usando `.to_undirected()` para que las relaciones fluyan simétricamente.
