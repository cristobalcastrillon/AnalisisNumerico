from sympy import *
import numpy as np

#Definiendo el símbolo 'x'...
x = Symbol('x')

def serieTaylor(n, a, f, val):
    "Calcula el valor de la serie de Taylor para la función 'f',"
    " teniendo en cuenta la 'n'-ésima derivada ('n'-ésimo término de la serie de Taylor)"
    " alrededor del valor 'a', evaluada en 'val'"
    print("f(x):", f, "\ta:", a, "\tn:", n, "\tEvaluada en:", val)

    for i in range(0, n+1):
        f_prima = f.diff(x, i)
        # print("La ", i, "-ésima derivada de la función ", f, " es igual a ", f_prima)
        taylor = (f_prima.evalf(subs={x: a})*((val-a)**i))/ np.math.factorial(i)
        # print("La aproximación en el", i, "término de la serie es igual a ", taylor)

    return taylor

puntoA = serieTaylor(n = 2, a = 0.05, f = x**(1/2), val = 0.0088)
print(puntoA)

puntoB = serieTaylor(n = 12, a = 0.05, f = x**(1/2), val = 0.0088)
print(puntoB)

# puntoC = serieTaylor(n = ??, a = ??, f = exp(x), val = 2.5)
# print(puntoC)