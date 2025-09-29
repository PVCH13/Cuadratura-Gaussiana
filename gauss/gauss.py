def gaussxw(N):
    """Genera los puntos de muestreo y pesos de la cuadratura Gauss–Legendre en [-1,1].

    Examples:
        >>> gaussxw(4)
        (array([-0.86113631, -0.33998104,  0.33998104,  0.86113631]), array([0.34785485, 0.65214515, 0.65214515, 0.34785485]))

    Args:
        N (int): número de puntos de cuadratura.

    Returns:
        x (ndarray): arreglo de NumPy que contiene los puntos.
        w (ndarray): arreglo de Numpy que contiene los pesos.

    """

    x, w = np.polynomial.legendre.leggauss(N)
    
    return x, w

def gaussxwab(a, b, x, w):
    """Transforma puntos y pesos de [-1,1] al intervalo [1,3].

    Examples:
        >>> puntos, pesos = gaussxw(4)
        >>> gaussxwab(1, 3, puntos, pesos)
        (array([1.13886369, 1.66001896, 2.33998104, 2.86113631]), array([0.34785485, 0.65214515, 0.65214515, 0.34785485]))

    Args:
        a (int or float): límite inferior.
        b (int or float): límite superior.
        x (ndarray): puntos en [-1,1].
        w (ndarray): pesos en [-1,1].
    
    Returns:
        (tuple): arreglos transformados al intervalo [1,3].

    """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

def integrando(varInd):
    """Función de prueba: f(x) = x^6 - x^2 sin(2x).

    Examples:
        >>> integrando(1.0)
        np.float64(0.09070257317431829)

    Args:
        varInd (float or int): variable independiente.

    Returns:
         (float): valor de la función evaluada.

    """
    return varInd**6 - varInd**2 * np.sin(2*varInd)

