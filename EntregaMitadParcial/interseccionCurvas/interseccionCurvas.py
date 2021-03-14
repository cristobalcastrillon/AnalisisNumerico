import numpy as np
import math 

def interseccionCurvas(a, b, tol, f):
    tramo = abs(b-a)
    while(tramo > tol):        
        c = b - (f(b) * (a - b))/(f(a) - f(b))
        if(np.sign(f(c)) == np.sign(f(a))):
            tramo = abs(c-a)
            a = c
        else:
            tramo = abs(b-c)
            b = c
        print("APROX.=[{:0.10f}] | ERROR=[{}]".format(c,tramo))

#f: expresión hallada para la intersección entre las dos curvas.
f = lambda x: -3*x**3 + 60*x + 57 - 300*x**-1 
#Intervalos basado en solución de Wolfram Alpha:
a1 = 1
b1 = 3

a2 = 3
b2 = 4.6

tol = 2**(-16)

interseccionCurvas(a1, b1, tol, f)
print('----------------------------------------')
interseccionCurvas(a2, b2, tol, f)
        