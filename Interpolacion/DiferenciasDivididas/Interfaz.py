import numpy as np
from sympy import symbols
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
print(poly2)
plot(poly2, (x, (min(x2)), (max(x2))))
plt.scatter(x2, y2)
plt.show()
# Polinomio de grado seis (Symbolab): -0.00023...x^6+0.018305x^5-0.58648x^4+9.62244x^3-84.89164x^2+382.47568x-681.7328

# print("----------------------PRUEBA----------------------")
# f2 = lambda x: x
# x2 = [1,2,3,4]
# f_x2 = difdivs.calcularVector(f2, x2)
# polyPrueba = difdivs.DiferenciasDivididas(x2, f_x2)
# print(polyPrueba)