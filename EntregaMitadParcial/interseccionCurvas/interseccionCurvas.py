import numpy as np
import math 

def interseccionCurvas(a, b, tol, f, g):
    #'f' y 'g' son funciones 'lambda' igualadas a '0' (e.g. f = lambda x,y: x**2 + x*y - 10 —función original: f(x) = x**2 + x*y = 10)
    h = lambda x,y: f - g
    tramo = abs(b-a)
    while(tramo > tol):        
        c = b - (f(b) * (a - b))/(f(a) - f(b))
        if(np.sign(f(c)) == np.sign(f(a))):
            tramo = abs(c-a)
            a = c
        else:
            tramo = abs(b-c)
            b = c
        #print("n=[{}] | APROX.=[{:0.10f}] | ERROR=[{}]".format(n,c,tramo))

f = lambda x,y: x**2 + x*y - 10
g = lambda x,y: y + 3*x*y**2 - 57
a = -1
b = 2
tol = 2**(-16)

interseccionCurvas(a, b, tol, f, g)
        