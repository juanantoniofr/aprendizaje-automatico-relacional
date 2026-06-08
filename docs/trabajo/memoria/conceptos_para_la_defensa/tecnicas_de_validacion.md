# Técnicas de validación

Las técnicas de validación tienen como objetivo principal evaluar la **capacidad de generalización** de un modelo, es decir, su aptitud para predecir correctamente la salida (la temática del artículo en nuestro caso) para ejemplos nuevos que no ha conocido previamente durante su entrenamiento.

Para la defensa, debemos dominar principalmente estas dos metodologías que hemos aplicado:

## 1. Validación por retención (_Holdout validation_)

Consiste en dividir el conjunto de ejemplos de los que se dispone en dos subconjuntos: uno de **entrenamiento** (a partir del cual se construye el modelo) y uno de **prueba** (cuyos ejemplos quedan "retenidos" y se usan para medir el rendimiento del modelo, ya que conocemos su respuesta correcta). Esta técnica nos proporciona una estimación _a posteriori_ de la capacidad de generalización del modelo, una vez construido.

_Punto clave para la defensa:_ Debemos explicarle al profesor que no hicimos esta división a ciegas, sino empleando un **muestreo estratificado**. Esto es vital para asegurar que la proporción de ejemplos que pertenecen a las distintas clases en el conjunto inicial se mantenga idéntica tanto en el subconjunto de entrenamiento como en el de prueba. Así justificamos cómo abordamos el fuerte desbalanceo del dataset Cora al separar nuestros datos (un 80% para entrenar y un 20% para testar).

## 2. Validación cruzada con _k_ pliegues (_k-fold cross validation_)

Esta técnica se utiliza a menudo cuando el conjunto de ejemplos es pequeño o, como en nuestra práctica, durante la fase de selección de modelos y ajuste. Consiste en **subdividir el conjunto de ejemplos de manera aleatoria en _k_ subconjuntos, denominados pliegues**, utilizando también un muestreo estratificado.

El proceso es iterativo: se realizan _k_ procesos de validación, donde en cada paso **se separa un pliegue distinto para usarlo como conjunto de prueba, y se entrena el modelo con los ejemplos de los pliegues restantes**. Al finalizar, el método devuelve la media de las _k_ estimaciones obtenidas, proporcionando una estimación _a priori_ de la capacidad de generalización del modelo.

## Relación con la Búsqueda en Rejilla (_Grid Search_)

En la Tarea 2.1 combinamos la validación cruzada con una **búsqueda en rejilla** para seleccionar los mejores hiperparámetros. En este proceso, primero se fijan los valores a considerar para cada hiperparámetro y, a continuación, para cada combinación posible, se estiman las características del modelo (entrenándolo y evaluándolo). Al aplicar validación cruzada de 5 pliegues para cada combinación de la rejilla, garantizamos que la selección del mejor modelo (como nuestro Árbol de Decisión) fuera robusta y no estuviera sobreajustada a una única partición afortunada de los datos.
