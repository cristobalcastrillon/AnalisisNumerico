#https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.lagrange.html
from scipy.interpolate import lagrange
import numpy as np

#Punto 6:

#Punto 7:
def funTaylor(x):
  return 0.28*(x**3)+0.4192*(x**2)+1.0192*x+0.999

def dividirPaso(x1, x2, nSteps):
  stepLength = (x2 - x1)/nSteps
  x_array = [x1]
  punto = x1
  while(punto < x2):
    punto += stepLength
    x_array.append(punto)
  print("Longitud del paso: ", stepLength)
  return x_array

def puntoSiete(x1, x2):
  i = 1
  error = 0
  poly = ''
  while(error < 10**(-5)):
    x_array = dividirPaso(x1, x2, i)
    poly = lagrange(x_array, np.exp(x_array))
    error_array = []
    for j in x_array:
      error_array.append(funTaylor(j) - poly(j))
    error = max(error_array)
    i += 1
    print("Cantidad de puntos a interpolar: ", len(x_array), '\n')
  return poly

print(puntoSiete(0, 1))