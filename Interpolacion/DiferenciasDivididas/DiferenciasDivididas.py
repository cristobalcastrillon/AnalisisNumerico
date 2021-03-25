import numpy as np
#Sympy para imprimir el polinomio de Newton.
from sympy import *
import FormatoPolinomio as fp

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

    #Imprimiendo el polinomio de Newton que interpola los puntos...
    x = Symbol('x')
    nwtnPoly = fp.formatoPolinomio(len(vecX), b[0])
    print(nwtnPoly)

def calcularVector(f, vecX):
    vecY = []
    for i in range(len(vecX)):
        vecY.append(f(vecX[i]))
    return vecY

print("----------------------PUNTO 1----------------------")
f1 = lambda x: np.log(x)
x1 = [1, 2]

f_x = calcularVector(f1, x1)
DiferenciasDivididas(x1, f_x)

print("----------------------PUNTO 7.c----------------------")
x2 = [14,14.5,15,15.5,16,16.5,17,17.5,18,18.5,19,19.5,20]
y2 = [20.9132,20.6454,20.205,19.6076,18.8688,18.0042,17.0294,15.96,14.8116,13.5998,12.3402,11.0484,9.74]
DiferenciasDivididas(x2, y2)

# print("----------------------PRUEBA----------------------")
# f2 = lambda x: x
# x2 = [1,2,3,4]

# f_x2 = calcularVector(f2, x2)
# DiferenciasDivididas(x2, f_x2)