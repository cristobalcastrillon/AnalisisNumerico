from sympy import *
import numpy as np

x = Symbol('x')

def serieTaylor(n, a, f, val):
    "Calcula el valor de la serie de Taylor para la función 'f', teniendo en cuenta la 'n'-ésima derivada ('n'-ésimo término de la serie de Taylor) alrededor del valor 'a', evaluada en 'val'"
    print("f(x):", f, "\ta:", a, "\tn:", n, "\tEvaluada en:", val)

    for i in range(0, n+1):
        f_prima = f.diff(x, i)
        # print("La ", i, "-ésima derivada de la función ", f, " es igual a ", f_prima)
        taylor = (f_prima.evalf(subs = {x: a})*((val-a)**i))/np.math.factorial(i)
        # print("La aproximación en el", i, "término de la serie es igual a ", taylor)

    return taylor

def aproxTaylor(f, val, a, E):
    "Calcula el valor de la serie de Taylor para la función 'f', teniendo en cuenta el error permitido (tolerancia) 'E', alrededor de 'a', evaluada en 'val'"
    print("f(x):", f, "\tEvaluada en:", val, "\tE:", E)

    parada = 1
    i = 0
    while(parada > E):
        f_prima = f.diff(x, i)
        taylor = (f_prima.evalf(subs = {x: a})*((val-a)**i))/np.math.factorial(i)
        print("La aproximación en el", i, "término de la serie es igual a ", taylor)
        i += 1
        parada = taylor

    return taylor