#Babylonian Square Root:
#Algoritmo para calcular la raíz cuadrada 'y' de un número 'n' 
#con un error permitido (tolerancia) 'E' y brindando un valor aproximado inicial 'x'.

import math

def truncate(number, decimals=0):
    """
    Returns a value truncated to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor
#Link de referencia a la anterior función: https://kodify.net/python/math/truncate-decimals/#:~:text=With%20Python's%20math.,certain%20number%20of%20decimal%20places.

def babylonianSqRt(n, E, x):
    "Esta función calcula la raíz cuadrada de 'n' con un error permitido 'E' y brindando un valor aproximado inicial 'x'"
    
    #Orden de convergencia
    # vecError = []
    # i = 0

    diferencia = 1
    y = x
    while(diferencia > E):
        y = 0.5 * (x + (n/x))
        diferencia = abs(x - y)
        #Orden de convergencia
        # vecError[i]
        x = y
        #Orden de convergencia
        # i += 1
    return y

print('Por favor, escriba el número cuya raíz cuadrada desea calcular: ')
n = float(input())

print('Por favor, escriba cuántos números después de la coma o punto desea (precisión): ')
p = int(input())

#Se calcula el error permitido con base en la precisión 'p'
E = 10**-p

print('Por favor, escriba un valor que usted crea aproximado a la raíz cuadrada de ' + str(n))
x = float(input())

#Llamada a la función 'babylonianSqRt'
print(truncate(babylonianSqRt(n, E, x), p))

#Tabla para orden de convergencia
# print()