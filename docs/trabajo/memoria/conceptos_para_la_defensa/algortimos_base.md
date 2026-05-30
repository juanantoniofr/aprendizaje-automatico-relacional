# Algoritmos base: cómo toman sus decisiones internamente

## 1. Árboles de Decisión (CART - Classification and Regression Trees)

Este algoritmo (que resultó ser nuestro mejor modelo en la Tarea 2.1) toma sus decisiones realizando un particionado recursivo de los datos **creando una jerarquía de reglas de tipo condicional** (reglas _Si... entonces..._).

- **Funcionamiento interno:** La estructura es un árbol binario donde cada **nodo interno** evalúa un atributo concreto (ya sea una palabra del texto o la centralidad) comprobando si supera o no un valor umbral.
- **La decisión:** Al clasificar un nuevo artículo científico, el modelo lo hace descender desde la raíz del árbol evaluando las condiciones en cada bifurcación (rama izquierda si no supera el umbral, derecha si lo supera) hasta llegar a un **nodo hoja**. Este nodo hoja está etiquetado con la clase mayoritaria de los ejemplos de entrenamiento que acabaron en esa misma rama, dictando así la predicción final.
- _Nota para la defensa:_ Para decidir dónde hacer los cortes durante el entrenamiento, el algoritmo busca el atributo y el umbral que minimicen la impureza de los datos resultantes, utilizando típicamente el **índice de Gini**.

## 2. k-Vecinos más Cercanos (kNN)

Es un modelo no paramétrico que, internamente, no construye una ecuación ni un árbol, sino que **memoriza directamente todos los ejemplos del conjunto de entrenamiento**. Su decisión se basa puramente en la similitud o distancia.

- **Funcionamiento interno:** Cuando recibe un nuevo artículo para clasificar, el modelo calcula numéricamente la distancia (por ejemplo, la **distancia euclídea** o de Manhattan) entre los atributos de este nuevo artículo y los atributos de todos los artículos que ya memorizó.
- **La decisión:** Ordena estas distancias de menor a mayor y selecciona los $k$ ejemplos de entrenamiento más cercanos. Finalmente, asocia al nuevo artículo **la clase mayoritaria (la que más se repita) entre esos $k$ vecinos**.
- _Nota para la defensa:_ Es vital explicar que, dado que el modelo calcula distancias matemáticas globales, requiere imperativamente la **normalización o tipificación previa de los atributos** (como aplicasteis con `StandardScaler`). Si no se hace, las variables con rangos numéricos más amplios dominarán el cálculo de la similitud y anularán a los demás atributos.

## 3. Naive Bayes (Bayes Ingenuo)

Este es un modelo probabilístico que fundamenta sus decisiones en la **regla de Bayes**. Toma su decisión calculando y comparando las probabilidades de que el artículo pertenezca a cada una de las 7 temáticas posibles.

- **Funcionamiento interno:** Para clasificar un ejemplo, el modelo asume una premisa muy fuerte (y simplista, por eso es "ingenuo"): **asume que los atributos son condicionalmente independientes entre sí** dentro de cada clase. En vuestro caso, asume que la aparición de la palabra "Neural" es matemáticamente independiente de la aparición de la palabra "Networks", lo cual en el lenguaje real rara vez es cierto.
- **La decisión:** El algoritmo multiplica la **probabilidad a priori** de cada clase (la proporción de veces que aparece el tema en el conjunto de entrenamiento) por la probabilidad individual de que cada atributo (cada palabra y métrica de grafo) tenga ese valor concreto dentro de dicha clase. La clase que obtenga el valor final más alto dictará la predicción, usando la regla de **máximo a posteriori (MAP)**.
- _Nota para la defensa:_ Para evitar que la ausencia de una sola palabra en el entrenamiento provoque multiplicaciones por cero (anulando toda la probabilidad), el modelo utiliza técnicas como el **suavizado de Laplace**.

## 4. Redes Neuronales (MLP - Perceptrón Multicapa)

Es un modelo conexionista fuertemente inspirado en el cerebro humano, que toma decisiones encadenando transformaciones matemáticas a lo largo de varias capas.

- **Funcionamiento interno:** La red está compuesta por una capa de entrada (nuestras 1437 características), **capas ocultas** y una capa de salida. Dentro de cada capa oculta hay "neuronas artificiales". Cada neurona multiplica los datos que recibe de la capa anterior por un vector de **pesos** (que representan la importancia de cada conexión), suma un sesgo o _bias_ (que define la facilidad de activación de la neurona), y pasa el resultado por una **función de activación no lineal** (como la función _Rectificador/ReLU_ o _Sigmoide_). Esta no linealidad es lo que les da tanta capacidad expresiva frente a clasificadores más simples.
- **La decisión:** Tras propagar la información capa por capa (_feedforward_), los datos llegan a la capa de salida. Al ser una tarea de clasificación multiclase (7 temas en Cora), la capa de salida suele tener 7 neuronas y emplear la función de activación **softmax**. Esta función convierte los valores brutos de las 7 neuronas en un vector de probabilidades que suman 1, dictando como decisión final **la clase asociada a la neurona con la probabilidad más alta**.
