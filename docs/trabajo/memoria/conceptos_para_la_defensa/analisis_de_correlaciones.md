# Análisis de Correlaciones

## Conceptos clave

- Explica las correlaciones de Pearson y Spearman, y cómo se aplican en el análisis de relaciones entre características relacionales y rendimiento de modelos.
  - **Pearson:** mide la relación lineal entre dos variables continuas, asumiendo normalidad y homocedasticidad. Se calcula como la covarianza de las variables dividida por el producto de sus desviaciones estándar. Un valor cercano a 1 o -1 indica una fuerte correlación positiva o negativa, respectivamente, mientras que un valor cercano a 0 indica ausencia de correlación lineal.
  - **Spearman:** es una medida no paramétrica que evalúa la relación monotónica entre dos variables, utilizando los rangos de los datos en lugar de sus valores originales. Es útil cuando los datos no cumplen con los supuestos de Pearson o cuando se sospecha de relaciones no lineales. Un valor de Spearman cercano a 1 o -1 indica una fuerte correlación monotónica positiva o negativa, respectivamente.

`Nota`

> homosticidad: igualdad de varianzas entre grupos o muestras.
> normalidad: distribución de los datos siguiendo una curva de campana (gaussiana).
> varianza: medida de dispersión que indica cuánto se alejan los datos de su media.

### Explica el concepto de chi-cuadrado y su relevancia en la evaluación de relaciones entre características relacionales y rendimiento de modelos.

El estadístico **chi-cuadrado** (representado como $\chi^2$) es una herramienta matemática utilizada en estadística para analizar variables categóricas (datos que se pueden dividir en grupos o categorías, como "color de ojos", "sí/no", "tipo de sangre").

En términos sencillos, el chi-cuadrado mide **la diferencia entre lo que realmente observamos en nuestros datos y lo que esperaríamos observar** si una hipótesis determinada fuera cierta (normalmente, la hipótesis de que no hay relación entre las variables o que los datos siguen una distribución específica).

#### ¿Qué mide exactamente?

El chi-cuadrado se utiliza principalmente para dos tipos de pruebas:

1. **Prueba de Independencia:** Mide si existe una asociación o relación entre dos variables categóricas.

- _Ejemplo:_ ¿Existe relación entre el hábito de fumar (fuma / no fuma) y desarrollar una enfermedad pulmonar (sí / no)? El estadístico te dirá si las diferencias en las tasas de enfermedad entre fumadores y no fumadores son estadísticamente significativas o si podrían deberse al azar.

2. **Prueba de Bondad de Ajuste:** Mide qué tan bien se ajustan los datos observados a una distribución teórica esperada.

- _Ejemplo:_ Si lanzas un dado 60 veces, esperarías que cada número del 1 al 6 salga unas 10 veces. Si el número 6 sale 30 veces, el chi-cuadrado medirá si esa desviación es lo suficientemente grande como para concluir que el dado está trucado.

---

#### ¿Cómo se calcula?

La lógica detrás del estadístico chi-cuadrado es comparar las **Frecuencias Observadas** (los recuentos reales en tus datos) con las **Frecuencias Esperadas** (los recuentos teóricos si no hubiera relación o sesgo).

La fórmula matemática es:

$$\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$$

Donde:

- $O_i$ es la frecuencia **Observada** para una categoría específica.
- $E_i$ es la frecuencia **Esperada** para esa misma categoría.
- $\sum$ significa que debes sumar este cálculo para todas las categorías (todas las celdas de tu tabla).

**El desglose del "por qué" de la fórmula:**

- **Restar $(O_i - E_i)$:** Encuentra la diferencia bruta entre lo real y lo teórico.
- **Elevar al cuadrado $(O_i - E_i)^2$:** Hace que todos los valores sean positivos (para que las diferencias negativas y positivas no se anulen entre sí al sumarlas) y penaliza las diferencias más grandes de manera desproporcionada.
- **Dividir entre $E_i$:** Estandariza la diferencia. Una diferencia de 10 es enorme si solo esperabas 5 casos, pero es insignificante si esperabas 1000 casos. Al dividir por lo esperado, se pone la diferencia en perspectiva.

#### ¿Cómo se interpreta el resultado?

- **Si el valor de $\chi^2$ es cercano a 0:** Significa que tus datos observados son casi idénticos a los esperados. Generalmente, concluyes que **no hay relación** entre las variables (en la prueba de independencia) o que el dado es justo (en la prueba de bondad de ajuste).
- **Si el valor de $\chi^2$ es grande:** Significa que hay una gran diferencia entre lo observado y lo esperado. Concluyes que **es muy probable que exista una relación** entre las variables o que los datos no siguen la distribución teórica.

Para determinar qué se considera un valor "grande", los estadísticos comparan el resultado final de $\chi^2$ con una tabla de distribución teórica basada en los "grados de libertad" (que dependen de cuántas categorías tienes) para obtener un **p-valor**. Si el p-valor es menor a 0.05 (típicamente), el resultado se considera estadísticamente significativo.
