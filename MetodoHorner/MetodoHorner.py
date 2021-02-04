import numpy as np
from sympy import *

x = Symbol('x')

def crearVectorCoef(n):
    vec = []
    for i in range(0, n+1):
        vec.append(int(input("Ingrese el coeficiente del término " +str(i) +": ")))
    return vec

def formatoPolinomio(n, coeficientes):
    polinomio = 0
    for i in range(0, n+1):
        polinomio += x**i * coeficientes[i]
    return polinomio

def formatoHorner(coeficientes, init, n):
    for i in range(init, n+1):
        if(i != n):
            return coeficientes[init] + x * formatoHorner(coeficientes, i+1, n)
        else:
            return coeficientes[init]