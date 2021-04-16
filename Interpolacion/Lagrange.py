#https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.lagrange.html
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
import numpy as np
from sympy.plotting import plot
from numpy.polynomial import chebyshev
import math

#Punto 6:
def funTan(x):
  return 0.4069*(x**6)-7.2587*(x**5)+53.119*(x**4)-203.35*(x**3)+427,26*(x**2)-462,5*x+0.999

coeffs_cheb = [1] * 11 # Solo queremos el elemento 11 de la serie
T11 = chebyshev.Chebyshev(coeffs_cheb, [(2*math.pi/3), (4*math.pi/3)])
xp_ch = T11.roots()
print(xp_ch)

#Punto 7:
def funcion1(x):
  return np.exp(x)

def funTaylor(x):
  return 0.28*(x**3)+0.4192*(x**2)+1.0192*x+0.999

def dividirPaso(x1, x2, nSteps):
  stepLength = (x2 - x1)/nSteps
  x_array = [x1]
  punto = x1
  while(punto < x2):
    punto += stepLength
    x_array.append(punto)
  return x_array

def puntoSiete(x1, x2):
  i = 1
  error = 0
  while(error < 10**(-5)):
    x_array = dividirPaso(x1, x2, i)
    poly = lagrange(x_array, np.exp(x_array))
    for j in x_array:
      error_array = []
      error_array.append(funTaylor(j) - poly(j))
      error = max(error_array)
    i += 1
    #print(i)
  return lagrange(dividirPaso(x1, x2, i), np.exp(dividirPaso(x1, x2, i)))

print(puntoSiete(0, 1))
plot(puntoSiete(0, 1), (x, (x1, x2)))