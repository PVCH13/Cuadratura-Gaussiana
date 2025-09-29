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
