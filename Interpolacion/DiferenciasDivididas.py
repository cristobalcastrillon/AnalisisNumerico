import numpy as np

def diferenciasDivididas(x, y):
    c = []
    for i in range(0, len(x)-1):
        c.append((y[i+1]-y[i])/(x[i+1]-x[i]))
        #La siguiente linea es de prueba
        #print(b[i])

def vector_fx(f, x):
    y = []
    for i in range(0, len(x)):
        y.append(f(x))
    #La siguiente linea es de prueba
    print(y)

f = lambda x: np.log(x)
x1 = [1, 2]

f_x = vector_fx(f, x1)
diferenciasDivididas(x1, f_x)