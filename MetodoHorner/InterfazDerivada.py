from sympy import *
import MetodoHorner as mh

x = Symbol('x')

def comillasDer(y):
    comillas = ""
    for i in range(0, y):
        comillas += "'"
    return comillas

n = int(input("Ingrese el grado del polinomio: "))

coeficientes = mh.crearVectorCoef(n) 
print(coeficientes)

grados = mh.crearVectorGrados(n)
print(grados)

polinomio = mh.formatoPolinomio(n, coeficientes)
print("p(x) = ", polinomio)

y = int(input("Por favor ingrese el grado de diferenciación que desea para el polinomio: "))
polinomiodx = polinomio.diff(x, y)
print("p" + comillasDer(y) + "(x) =", polinomiodx)

mh.calcularVectores(y, coeficientes, grados)

polinomioHorner = mh.formatoHorner(coeficientes, 0, n)
print(polinomioHorner)

print("Ingrese el valor de 'x' con el que evaluar el polinomio: ")
a = float(input())
print(polinomioHorner.evalf(subs = {x: a}))