import numpy as np
from sympy import symbols, simplify
from sympy.plotting import plot
import matplotlib.pyplot as plt
import DiferenciasDivididas as difdivs

#Definiendo el símbolo 'x'...
x = symbols('x')

print("----------------------PUNTO 1----------------------")
f1 = lambda x: np.log(x)
x1 = [1, 2]
f_x = difdivs.calcularVector(f1, x1)
poly1 = difdivs.DiferenciasDivididas(x1, f_x)
print(poly1)
plot(poly1, (x, min(x1), max(x1)))

print("----------------------PUNTO 7.c----------------------")
x2 = [6,8,10,12,14,16,18,20]
y2 = [7,9,12,18,21,19,15,10]
poly2 = difdivs.DiferenciasDivididas(x2, y2)
print("Expresión resultante:\n", poly2, '\n')
print("Expresión simplificada (polinomio de Newton):\n", simplify(poly2), '\n')
#TODO: Sobreponer gráficas (dispersión y curva)
plot(poly2, (x, (min(x2)), (max(x2))))
plt.scatter(x2, y2)
plt.show()

# print("----------------------PRUEBA----------------------")
# f2 = lambda x: x
# x2 = [1,2,3,4]
# f_x2 = difdivs.calcularVector(f2, x2)
# polyPrueba = difdivs.DiferenciasDivididas(x2, f_x2)
# print(polyPrueba)