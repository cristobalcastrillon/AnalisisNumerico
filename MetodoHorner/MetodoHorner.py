import numpy as np
from sympy import *

x = Symbol('x')

def crearVectorCoef(n):
    vec = []
    for i in range(0, n+1):
        vec.append(int(input("Ingrese el coeficiente del término " +str(i) +": ")))
    return vec

def crearVectorGrados(n):
    vec = []
    for i in range(0, n+1):
        vec.append(i)
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

def recalcularVectores(y, coeficientes, grados):
    "Recalcula los vectores de coeficientes y grados de un polinomio después de cada iteración correspondiente a la diferenciación"
    for i in range(0, y):
        for j in range(0, len(coeficientes)):
            coeficientes[j] *= grados[j]
            if(grados[j]-1 > 0):
                grados[j] -= 1
            else:
                grados[j] = 0