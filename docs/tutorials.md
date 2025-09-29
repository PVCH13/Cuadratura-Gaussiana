# Tutorial de uso

En este ejemplo se aplica la **cuadratura Gauss–Legendre** para aproximar la integral

\[
f(x) = x^6 - x^2 \sin(2x), \quad x \in [1,3]
\]

## Implementación en Python

```python
import numpy as np
from scipy.special import legendre


# Definición de la función a integrar
def integrando(varInd):
    return varInd**6 - varInd**2 * np.sin(2*varInd)

# Generación de puntos y pesos en [-1,1]
def gaussxw(N):
    x, w = np.polynomial.legendre.leggauss(N)  
    return x, w

# Transformación de intervalo [-1,1] -> [a,b]
def gaussxwab(a, b, x, w):
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

# Intervalo de integración
a, b = 1, 3
```
## Uso

Una vez hayan sido implementadas las funciones mostradas anteriormente, para realizar el cálculo de la integral se deben realizar los siguientes pasos.

1. Invocar la función **gaussxw(N)** y reemplazar $N$ por el número que se desee trabajar, asignando sus valores de retorno a dos variables, donde la primera contendrá los puntos y la segunda los pesos. 
2. Redefinir las variables definidas en el paso **1.** mediante la función **gaussxwab**, que toma como argumentos: el límite de integración inferior, el límite de integración inferior, los puntos (**1.**), los pesos (**1.**). Esto permite realizar el cambio de variable para obtener los puntos y los pesos en el intervalo definido. 

    Note que $a$ y $b$ fueron definidos en la integración del código, en cualquier caso usted podría cambiar estos valores al darle los argumentos a la función si desea otro intervalo de integración. Además, puede no redefinir las variables, sino crear unas nuevas, lo importante es ser consistente en el paso **3.**

3. Realice e imprima la suma de los productos de los pesos con la función **integrando** que toma como variable los puntos. Puede hacerlo usando $np.sum$, tal y como se muestra a continuación en el ejemplo.

El ejemplo utiliza un $foor loop$ para evidenciar el resultado con distintos valores de $N$.  



```python
# En este caso, a partir de N=4 se cumple que 2N - 1 > 6, por lo que para 4 o números mayores se obtiene un resultado exacto. 
for N in [2, 3, 4, 5]:
    puntos, pesos = gaussxw(N)
    puntos, pesos = gaussxwab(a, b, puntos, pesos)
    integral = np.sum(pesos * integrando(puntos))
    print("N = {} → aproximación = {}".format(N, integral))
```
```text
N = 2 → aproximación = 306.8199344959197
N = 3 → aproximación = 317.264151733829
N = 4 → aproximación = 317.3453903341579
N = 5 → aproximación = 317.34422672196956
```
