import numpy as np
from sympy import *

x = Symbol('x')

def crearVectorPol(n):
    vec = []
    for i in range(0, n+1):
        vec.append(i)
    return vec

def crearMatrizPol(n, vec):
    matriz = []
    for i in range(0, n):
        matriz.append(vec)
        # Imprimir la matriz si es necesario:
        # print(vec)
        for j in range(0, n+1):
            if((vec[j] - 1) > 0):
                vec[j] -= 1
            else:
                vec[j] = 0
    return matriz

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
#AVERIGUAR: Si se puede hacer una copia que no necesariamente sea el mismo obj. (como en C++)
gradosCopia = crearVectorPol(n)
print(grados)

matrizHorner = crearMatrizPol(n, grados)
print(gradosCopia)

coeficientes = crearVectorCoef(n) 
print(coeficientes)

polinomio = formatoPolinomio(grados, coeficientes)
print("p(x) = ", polinomio)