# import numpy as np
from sympy import *
import MetodoHorner as mh

x = Symbol('x')

n = int(input("Ingrese el grado del polinomio: "))

coeficientes = mh.crearVectorCoef(n) 
print(coeficientes)

polinomio = mh.formatoPolinomio(n, coeficientes)
print("p(x) = ", polinomio)

polinomioHorner = mh.formatoHorner(coeficientes, 0, n)
print(polinomioHorner)

print("Ingrese el valor de 'x' con el que evaluar el polinomio: ")
a = float(input())
print(polinomioHorner.evalf(subs = {x: a}))