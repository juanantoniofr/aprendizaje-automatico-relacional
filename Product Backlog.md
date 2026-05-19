# Product Backlog para el Trabajo de Aprendizaje Relacional

| Version | Fecha      | Descripción                           | Autor                       |
| ------- | ---------- | ------------------------------------- | --------------------------- |
| 1.0     | 2024-05-15 | Creación del Product Backlog inicial. | Juan Antonio Fernández Ruiz |

# Introducción

Teniendo de plazo hasta el 9 de junio (aproximadamente 3 semanas) y trabajando dos personas bajo la metodología SCRUM con GitHub, la mejor forma de organizarse es dividir el trabajo en **tres Sprints principales**. A continuación, te presento el **Product Backlog** desglosado y planificado temporalmente para cumplir con todos los requisitos de evaluación.

## Sprint Planning

### Sprint 1: Preparación, Análisis y Extracción de Características (Sugerido: 16 de mayo - 24 de mayo)

_Objetivo:_ Configurar el repositorio, comprender los datos y extraer la información relacional.

- **Tarea 1.1: Configuración del repositorio y entorno.** Inicializar el repositorio en GitHub y configurar el entorno de trabajo en Python con las librerías necesarias, específicamente **NetworkX** y **Scikit-Learn**. Se recomienda usar Jupyter Notebooks o ficheros `.py` y Matplotlib para las visualizaciones.
- **Tarea 1.2: Aprobación formal del profesor.** Aunque el documento rector ya indica el dataset, debéis escribir un correo a palmagro@us.es con el asunto "Trabajo IAIS Relacional (Grupo X)" para confirmar formalmente el conjunto de datos y la tarea de aprendizaje.
- **Tarea 1.3: Análisis Exploratorio de Datos (EDA).** Realizar un análisis inicial de los nodos y sus propiedades nativas.
- **Tarea 1.4: Extracción de características relacionales.** Usar NetworkX para calcular las métricas predictivas basadas en la teoría de grafos. Debéis extraer obligatoriamente información de **centralidad, coeficiente de clustering y detección de comunidades**.
- **Tarea 1.5: Análisis de correlaciones.** Realizar test estadísticos de correlación entre las características extraídas para seleccionar las más útiles antes de modelar.

### Sprint 2: Modelado, Ajuste y Selección (Sugerido: 25 de mayo - 1 de junio)

_Objetivo:_ Entrenar varios modelos, optimizarlos y elegir el definitivo. Dado que somos dos, podemos dividirnos la implementación de distintos algoritmos.

- **Tarea 2.1: Construcción de modelos base.** Implementar y entrenar **al menos tres modelos de clasificación relacionales** distintos, combinando las métricas extraídas con algoritmos estándar como árboles de decisión, kNN o redes neuronales.
- **Tarea 2.2: Validación y ajuste de hiper-parámetros.** Aplicar técnicas de validación sobre un conjunto de evaluación para estimar el rendimiento de los modelos y evitar el sobreajuste (_overfitting_).
- **Tarea 2.3: Evaluación y selección del mejor modelo.** Comparar los modelos construidos usando métricas de error para clasificación y **seleccionar aquel que realice la mejor clasificación y generalice mejor**.
- **Tarea 2.4: Limpieza y verificación de código.** Documentar el código mediante comentarios de calidad. Aseguraros de que el modelo seleccionado final se pueda cargar correctamente y que todo el código se pueda ejecutar en una máquina independiente.

### Sprint 3: Documentación IEEE, Presentación y Entrega (Sugerido: 2 de junio - 8 de junio)

_Objetivo:_ Redactar la memoria, preparar la defensa y empaquetar la entrega.

- **Tarea 3.1: Redacción de la memoria (Alumno 1 y 2).** Escribir un artículo científico de **al menos 6 páginas** en formato de los _IEEE conference proceedings_. Podéis usar LaTeX o un procesador de textos. La memoria no debe contener código fuente y debe dividirse en:
  - **I. Introducción:** Contexto general y objetivos.
  - **II. Preliminares:** Métodos empleados (NetworkX, algoritmos de ML) y trabajo relacionado.
  - **III. Metodología:** Descripción del conjunto de datos, las métricas relacionales y los algoritmos empleados (se puede usar pseudocódigo).
  - **IV. Resultados:** Detalle de la experimentación, validación cruzada, uso de tablas comparativas y análisis de cuál modelo es mejor y las decisiones tomadas.
  - **V. Conclusiones y Referencias:** Resumen del trabajo, ideas de mejora futura y listado bibliográfico referenciado numéricamente.
- **Tarea 3.2: Creación de la presentación.** Diseñar unas diapositivas (PDF, PowerPoint o similar) que resuman la estructura de la memoria, haciendo especial énfasis en los resultados y el análisis crítico.
- **Tarea 3.3: Ensayo de la defensa.** Preparar una presentación oral de **20 minutos**. Es vital ensayar juntos, ya que **ambos miembros del grupo deben participar activamente** en la defensa y la nota final dependerá de vuestra calidad expositiva y de las respuestas a las preguntas del profesor durante los 5 minutos posteriores.
- **Tarea 3.4: Empaquetado final.** El día antes de la entrega (8 de junio), agrupar todo en un **único fichero ZIP** que contenga la memoria en PDF, el código implementado (.py o cuadernos de Jupyter) y el conjunto de datos utilizado.

**Consideraciones clave durante todos los Sprints:**

- **Originalidad:** Subid periódicamente vuestros avances a GitHub, pero tened extremo cuidado de no incluir código ni texto copiado de internet sin referenciar. Cualquier detección de plagio se evalúa automáticamente con un cero en la asignatura.
