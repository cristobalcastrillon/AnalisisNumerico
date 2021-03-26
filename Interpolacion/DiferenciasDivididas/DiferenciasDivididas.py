import numpy as np
from sympy import symbols
from sympy.plotting import plot
import matplotlib.pyplot as plt

#Definiendo el símbolo 'x'...
x = symbols('x')

def DiferenciasDivididas(vecX, vecY):
    """
    Función que calcula un polinomio de Newton que interpola las coordenadas [vecX, vecY].
    """
    n = len(vecX)+1
    b = []
    #Creando la matriz necesaria para efectuar las operaciones del método...
    for i in range(len(vecX)):
        c = [0 for z in range(n)]
        b.append(c)
        n -= 1

    #Poblando la matriz con los valores correspondientes...
    for j in range(len(vecX)):
        for i in range(len(vecX)):
            if(j == 0):
                b[i][j] = vecX[i]
            elif(j == 1):
                b[i][j] = vecY[i]

    #Calculando la matriz (tabla) de diferencias divididas...
    iVar = 1
    jVar = 2
    n = len(vecX)-1
    for j in range(2, len(vecX)):
        for i in range(n):
            b[i][j] = (b[i + 1][j - 1] - b[i][j - 1]) / (b[i + iVar][j - jVar] - b[i][j - jVar])
        iVar += 1
        jVar += 1
        n -= 1
    # La siguiente línea es de prueba (imprime la tabla de diferencias divididas):
    # print(b)

    #Retornando el polinomio de Newton que interpola los puntos...
    nwtnPoly = formatoPolinomio(len(vecX), b[0], vecX)
    return nwtnPoly

def calcularVector(f, vecX):
    vecY = []
    for i in range(len(vecX)):
        vecY.append(f(vecX[i]))
    return vecY

def formatoPolinomio(n, coeficientes, vecX):
    polinomio = 0
    for i in range(1, n):
        multi = 1
        for j in range(0, i-1):
            multi *= (x-vecX[j])
        polinomio += (coeficientes[i] * multi)
    return polinomio

print("----------------------PUNTO 1----------------------")
f1 = lambda x: np.log(x)
x1 = [1, 2]
f_x = calcularVector(f1, x1)
poly1 = DiferenciasDivididas(x1, f_x)
print(poly1)
plot(poly1, (x, min(x1), max(x1)))

print("----------------------PUNTO 7.c----------------------")
x2 = [6,8,10,12,14,16,18,20]
y2 = [7,9,12,18,21,19,15,10]
poly2 = DiferenciasDivididas(x2, y2)
print(poly2)
plot(poly2, (x, (min(x2)), (max(x2))))
plt.scatter(x2, y2)
plt.show()

# print("----------------------PRUEBA----------------------")
# f2 = lambda x: x
# x2 = [1,2,3,4]
# f_x2 = calcularVector(f2, x2)
# polyPrueba = DiferenciasDivididas(x2, f_x2)
# print(polyPrueba)