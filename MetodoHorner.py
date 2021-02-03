import numpy as np
from sympy import *

x = Symbol('x')

def crearVectorPol(n):
    vec = []
    for i in range(0, n+1):
        vec.append(i)
    return vec

def crearVectorCoef(n):
    vec = []
    for i in range(0, n+1):
        vec.append(int(input("Ingrese el coeficiente del término " +str(i) +": ")))
    return vec

def formatoPolinomio(grados, coeficientes):
    polinomio = 0
    for i in grados:
        polinomio += x**grados[i] * coeficientes[i]
    return polinomio

def formatoHorner(coeficientes, init):
    for i in range(init, n+1):
        if(i != n):
            return coeficientes[init] + x * formatoHorner(coeficientes, i+1)
        else:
            return coeficientes[init]


n = int(input("Ingrese el grado del polinomio: "))
grados = crearVectorPol(n)
print(grados)

coeficientes = crearVectorCoef(n) 
print(coeficientes)

polinomio = formatoPolinomio(grados, coeficientes)
print("p(x) = ", polinomio)

polinomioHorner = formatoHorner(coeficientes, 0)
print("Ingrese el valor de 'x' con el que evaluar el polinomio: ")
a = float(input())
print(polinomioHorner.evalf(subs = {x: a}))