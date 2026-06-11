# Calibración de Modelo: Asegurando que las probabilidades reflejen la realidad

En el contexto de la inteligencia artificial y el aprendizaje automático, la frase **"Estudiar calibración de probabilidades para despliegue"** hace referencia a un paso crucial de control de calidad antes de lanzar un modelo para que sea utilizado en el mundo real (producción o "despliegue").

Aquí te explico detalladamente qué significa desglosando el concepto:

### 1. ¿Qué son las "probabilidades" en un modelo?

Cuando un clasificador (como el Árbol de Decisión o el kNN que usan en este trabajo ) analiza un documento científico del dataset Cora, no solo te dice _"este documento pertenece a la categoría Neural Networks"_. Normalmente, el modelo también devuelve un número entre 0 y 1 que interpretamos como su **nivel de confianza** (por ejemplo, `0.90` o un 90% de seguridad).

### 2. ¿Qué significa "calibración"?

Un modelo está **bien calibrado** si ese porcentaje de confianza refleja la realidad. Es decir, si el modelo selecciona 100 artículos científicos y en todos ellos afirma estar un "90% seguro" de su predicción, esperaríamos que **exactamente 90 de esos 100 artículos** estén correctamente clasificados.

El problema es que muchos algoritmos clásicos de IA son "mentirosos" o imprecisos con sus niveles de confianza:

- Naive Bayes: Tiende a ser extremadamente drástico debido a sus suposiciones matemáticas. Suele dar probabilidades muy cercanas a 0% o 100%, mostrando una **sobreconfianza** irracional aunque se equivoque.

- Redes Neuronales (MLP): A menudo sufren también de sobreconfianza; aprenden tan bien a ajustar los datos de entrenamiento que sus probabilidades de salida suelen ser más altas de lo que justifica su precisión real en test.

### 3. ¿Por qué es vital para el "despliegue"?

El **despliegue** es el acto de integrar este modelo en un software real donde usuarios o empresas van a depender de él. Si vas a automatizar un proceso en producción, necesitas confiar en la incertidumbre del modelo.

- _Ejemplo práctico:_ Si el modelo clasifica un documento con un 95% de confianza, el sistema automático puede archivarlo directamente. Pero si lo clasifica con un 55% de confianza (mucha incertidumbre), un sistema bien calibrado sabrá que es mejor enviar ese documento a una bandeja de revisión manual para que un humano lo verifique. Si el modelo no está calibrado, podría dar un 95% de confianza falso a un documento erróneo, provocando fallos automatizados en producción.

Para solucionar esto, los autores proponen como trabajo futuro aplicar técnicas matemáticas de post-procesamiento (como el **Escalado de Platt** o la **Regresión Isotónica**) que toman esas probabilidades "deformadas" del modelo y las enderezan para que coincidan con la probabilidad real de acierto.

---

Para que puedas comprender visualmente cómo funciona este fenómeno y cómo se mide mediante un **Diagrama de Fiabilidad (Reliability Diagram)**, he preparado el siguiente simulador interactivo donde podrás experimentar con la calibración de diferentes modelos:
