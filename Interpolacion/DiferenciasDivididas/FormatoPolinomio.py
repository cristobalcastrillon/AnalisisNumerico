from sympy import *
x = Symbol('x')

def formatoPolinomio(n, coeficientes):
    polinomio = 0
    for i in range(0, n+1):
        polinomio += x**i * coeficientes[i]
    return polinomio