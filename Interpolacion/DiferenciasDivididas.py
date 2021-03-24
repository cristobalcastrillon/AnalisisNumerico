import numpy as np
#Sympy para imprimir el polinomio de Newton.
#import sympy as sp

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
    print(b)

    #Retornar / Imprimir el polinomio de Newton que interpola los puntos...

def calcularVector(f, vecX):
    vecY = []
    for i in range(len(vecX)):
        vecY.append(f(vecX[i]))
    return vecY

f1 = lambda x: np.log(x)
x1 = [1, 2]

f_x = calcularVector(f1, x1)
DiferenciasDivididas(x1, f_x)

# f2 = lambda x: x
# x2 = [1,2,3,4]

# f_x2 = calcularVector(f2, x2)
# DiferenciasDivididas(x2, f_x2)