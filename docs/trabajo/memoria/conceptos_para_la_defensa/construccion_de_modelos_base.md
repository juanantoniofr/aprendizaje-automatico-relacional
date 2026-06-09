# Construcción de modelos base

## Naive Bayes vs. Naive Bayes Gaussiano: ¿son lo mismo?

La respuesta corta es **no, no son exactamente lo mismo**.

Para entender la diferencia, piénsalo de esta manera: **Naive Bayes** es el concepto general (la "familia" del algoritmo), mientras que **Naive Bayes Gaussiano** es una versión específica dentro de esa familia adaptada para un tipo particular de datos.

Aquí tienes el desglose exacto de las diferencias:

### 1. Naive Bayes (El concepto general)

Es una técnica de clasificación probabilística basada en el **Teorema de Bayes**. Su característica principal es que hace una suposición "ingenua" (_naive_ en inglés): asume que todas las variables (características o _features_) que usas para predecir son **completamente independientes entre sí**, aunque en el mundo real rara vez lo sean.

En su forma más general, el modelo calcula la probabilidad de una clase $y$ dado un conjunto de características $x_1, x_2, \dots, x_n$ usando la siguiente lógica:

$$P(y|x_1, \dots, x_n) \propto P(y) \prod_{i=1}^{n} P(x_i|y)$$

El problema del modelo general es: ¿Cómo calculamos $P(x_i|y)$ (la probabilidad de observar una característica dada una clase)? La respuesta depende de cómo sean tus datos.

### 2. Naive Bayes Gaussiano (La variante específica)

Aquí es donde entra el Gaussiano. Esta es la versión de Naive Bayes que debes usar cuando tus datos de entrada son **numéricos continuos** (por ejemplo: altura, peso, temperatura, salario en dólares) en lugar de categorías discretas.

Como tienes números continuos, el algoritmo asume que los datos asociados a cada clase se distribuyen según una **Distribución Normal** (también conocida como Campana de Gauss). Para calcular las probabilidades, el algoritmo encuentra la media ($\mu$) y la varianza ($\sigma^2$) de tus características en el conjunto de entrenamiento, y aplica la siguiente fórmula matemática de densidad gaussiana:

$$P(x_i | y) = \frac{1}{\sqrt{2\pi\sigma_y^2}} \exp\left(-\frac{(x_i - \mu_y)^2}{2\sigma_y^2}\right)$$

### Las otras variantes para contrastar

Para que quede aún más claro que el Gaussiano es solo un "sabor" del algoritmo, existen otras versiones de Naive Bayes diseñadas para otros tipos de datos:

- **Multinomial Naive Bayes:** Se usa cuando tus datos son **conteos o frecuencias discretas**. Es el rey indiscutible para la clasificación de texto (por ejemplo, detectar si un correo es Spam contando cuántas veces aparece la palabra "gratis" o "premio").
- **Bernoulli Naive Bayes:** Se usa cuando tus variables son estrictamente **binarias o booleanas** (1 y 0, Verdadero y Falso). Por ejemplo, si una palabra aparece o no aparece en un texto, sin importar cuántas veces lo haga.

**En resumen:** Cuando alguien dice que está usando "Naive Bayes", generalmente se refiere a la lógica probabilística subyacente. Para poder programarlo y aplicarlo a un problema real, siempre tienes que elegir una variante (Gaussiano, Multinomial o Bernoulli) dependiendo de si tus columnas de datos tienen números con decimales, conteos o valores de sí/no.
