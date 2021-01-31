from sympy import *
import numpy as np

#Definiendo el símbolo 'x'...
x = Symbol('x')

def serieTaylor(n, a, f, val):
    "Calcula el valor de la serie de Taylor para la función 'f',"
    " teniendo en cuenta la 'n'-ésima derivada ('n'-ésimo término de la serie de Taylor)"
    " alrededor del valor 'a', evaluada en 'val'"

    for i in range(0, n+1):
        f_prima = f.diff(x, i)
        taylor = (f_prima.evalf(subs={x: a})*((val-a)**n))/ np.math.factorial(i)

    return taylor

print(serieTaylor(n = 2, a = 0.05, f = x**(1/2), val = 0.0088))
print(serieTaylor(n = 12, a = 0.05, f = x**(1/2), val = 0.0088))