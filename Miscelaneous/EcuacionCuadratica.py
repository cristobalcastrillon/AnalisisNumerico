import math
import cmath

def evaluarCuadratica(a, b, c):
    "Función que calcula los posibles resultados [x1, x2] (arreglo)"
    "de un polinomio de la forma a*x^2 + b*x + c."
    exprInterna = ((b**2)-4*a*c)
    if(exprInterna < 0):
        return [(-b + cmath.sqrt(exprInterna))/(2*a), (-b - cmath.sqrt(exprInterna))/(2*a)]
    else:
        return [(-b + math.sqrt(exprInterna))/(2*a), (-b - math.sqrt(exprInterna))/(2*a)]

print("Ingrese el valor de 'a': ")
a = float(input())
print("Ingrese el valor de 'b': ")
b = float(input())
print("Ingrese el valor de 'c': ")
c = float(input())

r = evaluarCuadratica(a, b, c)
x1 = r[0]
print("x1 =", x1)
x2 = r[1]
print("x2 =", x2)