from sympy import *
import numpy as np

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

#def formatoHorner(grados, coeficientes, polinomio):
    #La idea es hacer una matriz de grados en que la primera fila corresponda a los grados del polinomio
    #la segunda fila corresponda a lo anterior -1 (excepto cuando el valor es 0: 0 - 1 = 0)

n = int(input("Ingrese el grado del polinomio: "))
grados = crearVectorPol(n)
print(grados)

coeficientes = crearVectorCoef(n) 
print(coeficientes)

polinomio = formatoPolinomio(grados, coeficientes)
print("p(x) = ", polinomio)

formatoHorner(grados, coeficientes, polinomio)