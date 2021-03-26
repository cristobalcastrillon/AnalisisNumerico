from sympy import symbols

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