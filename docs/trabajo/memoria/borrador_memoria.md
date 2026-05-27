### Título: [Elegir un título, por ejemplo: Clasificación Relacional de Documentos Científicos: Un Enfoque Topológico sobre el Dataset Cora]

**Resumen—** Este documento presenta los avances preliminares en la construcción y evaluación de modelos de aprendizaje automático relacional aplicados al conjunto de datos Cora. El objetivo principal es predecir la temática de artículos científicos combinando sus atributos textuales con características topológicas extraídas de su red de citas. Hasta la fase actual de desarrollo, se ha completado el análisis exploratorio, la extracción de métricas estructurales (centralidad, _clustering_ y comunidades) y el establecimiento de una línea base de rendimiento mediante cuatro algoritmos clásicos de clasificación. Los resultados preliminares muestran que los Árboles de Decisión logran generalizar de manera competitiva frente a modelos conexionistas y probabilísticos.

**Palabras clave—** Aprendizaje Automático Relacional, Teoría de Grafos, Clasificación de Nodos, Dataset Cora.

### I. INTRODUCCIÓN

El análisis de datos estructurados en forma de red se ha convertido en un área de vital importancia debido a la ubicuidad de los grafos en dominios como las redes sociales, biológicas y de comunicaciones. A diferencia del aprendizaje automático tradicional, que asume la independencia entre los ejemplos, el aprendizaje relacional aprovecha las correlaciones inherentes en los enlaces entre nodos para mejorar la capacidad predictiva de los modelos.

En este trabajo en curso, se aborda el problema de la clasificación de nodos en redes de citación científica utilizando el conjunto de datos Cora. El enfoque adoptado consiste en la extracción manual de características topológicas para enriquecer las propiedades nativas de los documentos. El resto de este documento detalla los preliminares teóricos (Sección II), la metodología y decisiones de diseño adoptadas hasta la fecha (Sección III), los resultados empíricos preliminares (Sección IV) y, finalmente, las conclusiones e hitos de trabajo futuro (Sección V).

### II. PRELIMINARES

**A. Métodos empleados**
Para la representación y procesamiento de los datos relacionales se ha empleado la librería de Python _NetworkX_. Específicamente, nos apoyamos en la teoría de grafos para calcular medidas topológicas de centralidad, densidad local (coeficiente de _clustering_) y algoritmos de detección de comunidades para identificar subestructuras cohesivas. Para la etapa de modelado y clasificación, se ha empleado _Scikit-Learn_, evaluando algoritmos basados en instancias (_k-Vecinos más Cercanos_), particionado recursivo (_Árboles de Decisión_), aproximaciones probabilísticas (_Naive Bayes_ Gaussiano) y modelos conexionistas (_Perceptrón Multicapa_).

**B. Trabajo Relacionado**
Como referencia fundamental para nuestro enfoque, destaca el trabajo de Sen _et al._ sobre clasificación colectiva en datos de redes, en el cual los autores emplean el conjunto de datos Cora para predecir la temática de los artículos basándose en la correlación de sus enlaces y propiedades. Su investigación demuestra que aprovechar la estructura subyacente de la red mejora significativamente el rendimiento frente a clasificadores tradicionales que tratan cada documento de forma independiente.

### III. METODOLOGÍA

**A. Análisis Exploratorio de los Datos (EDA)**
El conjunto de datos Cora original consta de 2708 publicaciones científicas divididas en 7 clases temáticas, y 5429 enlaces de citación. La matriz de propiedades nativas está compuesta por un vocabulario binario de 1433 palabras. El análisis exploratorio reveló una extrema dispersión en los datos textuales (un 98.73% de ceros, con un promedio de solo 18.17 palabras presentes por artículo) y un marcado desbalanceo de clases, siendo "Neural_Networks" la clase dominante (818 artículos) frente a clases minoritarias como "Rule_Learning" (180 artículos).

**B. Construcción del Grafo y Extracción de Características**
Como **decisión de diseño**, la red de citas se modeló como un grafo no dirigido. Esto permitió la fusión natural de citas recíprocas en 5278 aristas únicas y garantizó la convergencia estructural para los algoritmos topológicos aplicados posteriormente. Se extrajeron las siguientes métricas relacionales para cada nodo:

- **Centralidad de Intermediación (_Betweenness Centrality_):** Elegida estratégicamente por su alta capacidad predictiva para identificar artículos que actúan como "puentes" de información entre áreas temáticas.
- **Coeficiente de Clustering:** Calculado para medir la tendencia de las publicaciones a agruparse en vecindarios densos interconectados.
- **Detección de Comunidades (Louvain):** Se seleccionó Louvain frente a otras alternativas para maximizar de forma eficiente la modularidad del particionado en el grafo no dirigido.

**C. Configuración Experimental (Modelado Base)**
Para establecer la línea base de clasificación, se construyó un conjunto de datos consolidado uniendo las características textuales y relacionales. Se dividieron los datos en conjuntos de entrenamiento (80%) y prueba (20%). Como **decisión de diseño fundamental**, se aplicó un muestreo estratificado para combatir el desbalanceo de clases evidenciado en el EDA. Asimismo, la optimización de los hiperparámetros mediante búsqueda en rejilla se guio exclusivamente por la métrica _F1-macro_ usando validación cruzada de 5 pliegues, obligando a los modelos a penalizar los errores en las temáticas minoritarias y evitando el sobreajuste a la clase mayoritaria.

### IV. RESULTADOS PRELIMINARES

Los experimentos iniciales han tenido como propósito establecer un _baseline_ evaluando los cuatro modelos clásicos con la totalidad de las variables disponibles.

**TABLA I. RENDIMIENTO DE LOS MODELOS BASE EN EL CONJUNTO DE PRUEBA**

| Modelo                     | Exactitud (Accuracy) | F1-macro  | Precision (macro) | Recall (macro) |
| :------------------------- | :------------------: | :-------: | :---------------: | :------------: |
| **Árbol de Decisión**      |      **0.771**       | **0.758** |     **0.762**     |   **0.760**    |
| Perceptrón Multicapa (MLP) |        0.730         |   0.717   |       0.721       |     0.717      |
| Naive Bayes Gaussiano      |        0.452         |   0.428   |       0.437       |     0.422      |
| k-Vecinos más Cercanos     |        0.422         |   0.416   |       0.469       |     0.406      |

_Análisis Crítico Inicial:_
El Árbol de Decisión obtiene, con diferencia, la mejor capacidad de generalización inicial (_F1-macro_ de 0.758). Esto sugiere que la altísima dispersión del texto combinada con los valores topológicos requiere de reglas de corte jerárquicas estrictas para discriminar la temática de los artículos, algo en lo que fallan modelos probabilísticos ingenuos (Naive Bayes) o basados puramente en distancia métrica (kNN). La matriz de confusión demuestra que, gracias al ajuste por _F1-macro_, el Árbol logra identificar competentemente las clases minoritarias.

### V. CONCLUSIONES Y TRABAJO FUTURO

El trabajo desarrollado hasta el momento permite concluir que la integración de propiedades estructurales (centralidad y comunidades) en un clasificador de particionado jerárquico establece una línea base robusta para la predicción temática en el dataset Cora, sorteando con éxito el desbalanceo de clases y la extrema dispersión de las variables nativas.

**Trabajo Futuro:**
Para completar el modelado definitivo, los próximos pasos de la investigación se centrarán en dos hitos:

1.  **Análisis de Correlaciones:** Se aplicarán tests estadísticos para filtrar el espacio de características, eliminando palabras o métricas ruidosas que puedan estar induciendo a un sobreajuste incipiente en los modelos base.
2.  **Modelado Avanzado de Grafos:** Se explorará el aprendizaje de representaciones latentes en baja dimensión mediante la implementación de algoritmos específicos como _Node2Vec_, con el objetivo de batir el rendimiento de la línea base actual.

### REFERENCIAS

P. Sen, G. Namata, M. Bilgic, L. Getoor, B. Gallagher, and T. Eliassi-Rad, "Collective Classification in Network Data," _AI Magazine_, vol. 29, no. 3, pp. 93-106, 2008.

---

Este texto está listo para que lo actualicéis en vuestro borrador. ¿Qué te parece si a continuación pasamos a realizar la **Tarea 1.5 (Análisis de correlaciones)** para poder decidir con qué variables nos quedamos y cuáles descartamos?
