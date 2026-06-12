# Word2Vec: Transformando palabras en vectores

**Word2Vec** es un algoritmo fundamental en el campo del Procesamiento del Lenguaje Natural (NLP). Desarrollado por un equipo de investigadores de Google (liderado por Tomas Mikolov) en 2013, su objetivo es **transformar palabras en números**, específicamente en vectores densos (listas de números).

A este proceso se le conoce como **Word Embedding** (incrustación de palabras).

El principio básico de Word2Vec se resume en una famosa frase del lingüista John Rupert Firth: _"Conocerás una palabra por la compañía que frecuenta"_. El algoritmo asume que las palabras que aparecen en contextos similares suelen tener significados similares.

### ¿Cómo funciona internamente?

Word2Vec utiliza una red neuronal superficial (de una sola capa oculta) para aprender estas representaciones matemáticas. No necesita que humanos etiqueten datos; aprende leyendo cantidades masivas de texto y prestando atención a qué palabras aparecen cerca de otras.

Existen dos arquitecturas o formas en las que Word2Vec se entrena:

1. **CBOW (Continuous Bag-of-Words):**
   El modelo intenta predecir una palabra objetivo basándose en su contexto (las palabras que la rodean).

- _Ejemplo:_ Si la frase es _"El perro ladra al cartero"_, el modelo toma ["El", "perro", "al", "cartero"] para intentar adivinar que la palabra que falta en el medio es **"ladra"**.

2. **Skip-gram:**
   Es exactamente lo inverso a CBOW. Toma una palabra objetivo e intenta predecir las palabras del contexto que la rodean.

- _Ejemplo:_ Dada la palabra **"ladra"**, el modelo intenta predecir que las palabras cercanas probablemente sean ["El", "perro", "al", "cartero"].
- _Nota:_ Skip-gram suele funcionar mejor con conjuntos de datos grandes y representa mejor palabras poco frecuentes.

### La magia de Word2Vec: Geometría Semántica

Una vez entrenado, cada palabra del vocabulario se convierte en un vector de, por ejemplo, 300 dimensiones. Lo fascinante es que el espacio vectorial captura la **semántica y sintaxis** del lenguaje de forma geométrica.

- **Similitud:** Palabras similares (como "perro" y "gato") estarán muy cerca la una de la otra en este espacio matemático.
- **Álgebra de palabras:** Puedes realizar sumas y restas con los vectores de las palabras para obtener conceptos lógicos. La ecuación más famosa que demostró esto es:

$$V_{\text{rey}} - V_{\text{hombre}} + V_{\text{mujer}} \approx V_{\text{reina}}$$
