# Métricas de rendimiento

El profesor querrá saber exactamente por qué decidimos evaluar nuestros modelos de una forma y no de otra.

Para explicar cómo se mide la eficacia de nuestros clasificadores, debemos tener claros estos conceptos clave que conectan la teoría con la decisión práctica que tomamos en la Tarea 2.1:

## 1. La Matriz de Confusión

Es la herramienta base para evaluar cualquier modelo de clasificación. Se trata de una matriz o tabla de contingencias donde se cruzan las clases reales de los ejemplos con las clases que el modelo ha predicho.

- En la diagonal de esta matriz se encuentran los aciertos (los **Verdaderos Positivos** y **Verdaderos Negativos**), mientras que fuera de la diagonal se contabilizan los errores de clasificación (los **Falsos Positivos** y **Falsos Negativos**).

## 2. Exactitud (Accuracy o Tasa de Acierto)

Es la métrica más intuitiva: calcula la proporción total de ejemplos que el modelo ha clasificado correctamente sobre el total de ejemplos.

- _El problema para tu defensa:_ Debes explicarle al profesor que la exactitud global **no es una métrica fiable para datasets desbalanceados** como Cora. Si recordáis de nuestro análisis exploratorio, la clase "Neural_Networks" tiene 818 artículos y "Rule_Learning" solo 180. Un modelo mediocre que se limitara a predecir siempre "Neural_Networks" tendría una exactitud artificialmente alta, pero sería inútil en la práctica.

## 3. Precisión y Recuerdo (Recall)

Para tener una visión más detallada de los aciertos, se calculan estas dos métricas para cada clase individualmente:

- **Precisión:** Es la proporción de predicciones correctas sobre el total de predicciones que hizo el modelo para esa clase. Es decir, ¿de todos los artículos que el modelo etiquetó como "Theory", cuántos lo eran realmente?
- **Recuerdo (Sensibilidad):** Es la proporción de ejemplos reales de una clase que el modelo logró detectar correctamente. Es decir, ¿de todos los artículos que realmente eran de "Theory" en el dataset, cuántos logró encontrar el modelo?

## 4. La métrica F1-macro (La decisión de diseño clave)

Esta es la métrica que utilizamos para la validación cruzada y para elegir al mejor modelo en la Tarea 2.1. Para la defensa, debes saber explicarla en dos pasos:

- Primero, el **F1 de una clase** combina la Precisión y el Recuerdo de dicha clase calculando su media armónica.
- Segundo, el **F1-macro** calcula el **promedio simple** de los valores F1 de todas las clases.
- _Justificación brillante para el profesor:_ Explica que la palabra "macro" significa que **todas las clases pesan exactamente lo mismo en el cálculo de la nota final, aunque tengan muy pocos ejemplos**. Esto es crucial porque penaliza fuertemente a los modelos que ignoran las clases minoritarias, obligando al clasificador a esforzarse por aprender las características de todos los temas por igual en lugar de ir a lo fácil (la clase dominante).

Para calcular la métrica **F1-Macro** (o Macro F1-score) en un problema de clasificación multiclase, debes calcular el F1-score de cada clase de forma independiente y, luego, sacar el promedio aritmético (la media no ponderada) de todos ellos.

La característica principal del F1-Macro es que **trata a todas las clases por igual**, independientemente de cuántos ejemplos haya de cada una (su soporte). Esto lo hace muy útil cuando te importa el rendimiento de las clases minoritarias tanto como el de las mayoritarias.

Aquí tienes el proceso paso a paso:

### 1. Calcular Precisión y Exhaustividad (Recall) por clase

Para cada clase $i$ en tu conjunto de datos, primero necesitas encontrar sus Verdaderos Positivos ($TP$), Falsos Positivos ($FP$) y Falsos Negativos ($FN$).

- **Precisión ($P_i$):** De todas las predicciones positivas que hizo el modelo para la clase $i$, ¿cuántas eran correctas?

$$P_i = \frac{TP_i}{TP_i + FP_i}$$

- **Exhaustividad ($R_i$):** De todos los casos reales que pertenecen a la clase $i$, ¿cuántos logró encontrar el modelo?

$$R_i = \frac{TP_i}{TP_i + FN_i}$$

### 2. Calcular el F1-score individual para cada clase

El F1-score es la media armónica entre la Precisión y la Exhaustividad. Se calcula para cada clase de forma aislada:

$$F1_i = 2 \times \frac{P_i \times R_i}{P_i + R_i}$$

### 3. Calcular el promedio (F1-Macro)

Finalmente, sumas los F1-scores de todas tus $N$ clases y divides entre el número total de clases:

$$\text{F1-Macro} = \frac{1}{N} \sum_{i=1}^{N} F1_i$$
