# Método de Cuadratura Gaussiana

La integración numérica busca aproximar integrales definidas cuando no es posible 
obtener una solución analítica exacta o cuando evaluarla resulta demasiado costoso. 
El método de cuadratura Gaussiana, en particular la cuadratura de Gauss–Legendre, 
es una de las técnicas más eficientes dentro de este campo.


Si queremos aproximar una integral definida de la forma:

\begin{align}
I = \int_a^b f(x)\,dx
\end{align}

La idea de los métodos de cuadratura es aproximar esta integral mediante 
una suma de evaluaciones de la función en ciertos puntos del intervalo:

\begin{align}
I \approx \sum_{i=k}^N w_k \, f(x_k)
\end{align}

donde:

- \(x_k\) son los **puntos de muestreo**,
- \(w_k\) son los **pesos**


Además, para la cuadratura Gaussiana:

  * Los puntos de muestreo se escogen de manera tal que **no son equidistantes**. Esto introduce más grados de libertad para la misma discretización en $N$ subregiones.
  * Es exacta para un polinomio de orden $(2N - 1)$ o menor.

## Polinomios de Legendre
Los polinomios de Legendre ($P_N(x)$) son un sistema de polinomios ortogonales que pueden ser definidos de manera recursiva. Tenemos:
\begin{align}
\forall (M, N) \in\mathbb N^2, \quad \int_{-1}^1 {\rm{d}}x P_N(x)P_M(x) = \frac{2\delta_{MN}}{2N+1}. 
\end{align}

Note que los polinomios están definidos en el intervalo $[-1, 1]$.    

Los se definen empezando con
\begin{align}
P_0(x) = 1 \Rightarrow P_1(x) = x,
\end{align}
tal que los siguientes órdenes se generan con la regla de recursividad
\begin{align}
(N+1)P_{N+1}(x) = (2N+1)xP_N(x) -NP_{N-1}(x).
\end{align}
Alternativamente, los polinomios pueden ser definidos de manera iterativa bajo la regla (fórmula de Rodrigues)
\begin{align}
P_N(x) = \frac1{2^N N!}\frac{d^N}{dx^N}\left[(x^2-1)^N\right].
\end{align}

## Particularidad de la cuadratura Gauss–Legendre

En la **cuadratura Gauss–Legendre**, existe una **regla universal para escoger $w_k$ y $x_k$**. Los pesos y puntos de muestreo se eligen tal que:
  
  * $x_k$ corresponden a las $N$ raíces (ceros) de los polinomios de Legendre de orden $N$.
  * Los pesos se eligen tal que:

      $\displaystyle w_k = \left[\frac{2}{1-x^2}\left(\frac{dP_N}{dx}\right)^{-2}\right]_{x={x_k}}$, con $x_k$ que cumple $P_N(x_k)=0$


Vea también que al estar el método definido en el intervalo $[-1, 1]$ es necesario un cambio de variable a un intervalo arbitrario. En nuestro caso, eso se realizará de manera computacional a patir de una función establecida, por lo que teóricamente no se abordará cómo realizarlo. 


Finalmente, es relevante hablar puntualmente de las ventajas y desventajas del método:

**Ventajas:**

  - La ecuación para evaluar los errores es muy complicada. Sin embargo, la aproximación mejora con un error que decrece por un factor ${\rm{const.}} / N^2$ cuando se incrementa el número de subregiones de discretización en uno.
  - Ejemplo: Pasar de $N=10$ a $N=11$, mejora el resultado de la estimación por un factor de $\approx 100$. Esto indica que la convergencia ocurre con muy pocos puntos de muestreo.
  
**Desventajas:**

  - Sólo funciona bien su la función a integrar es relativamente bien comportada. Si no lo es, se requiren más puntos de muestreo cerca de las regiones problemáticas.
  - Es muy complicado evaluar el error de manera precisa si lo necesitamos.
