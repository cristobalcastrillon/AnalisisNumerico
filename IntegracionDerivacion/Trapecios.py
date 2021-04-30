import numpy as np
from scipy import integrate
#'integrate' for calculating absolute error between methods

def trapecio(a, b, f, n):
  h = (b-a)/n
  s = 0 
  for i in range(1, n):
    s += f(a+(i*h))
  res = (f(a) + f(b) + (s*2)) * (h/2)
  return res

f = lambda x: np.sqrt(x) * np.sin(x)

print(trapecio(0, 2, f, 5))
print(trapecio(0, 2, f, 10))
print(trapecio(0, 2, f, 100))
print('\n')
  
g = lambda x: 1/(1+x)

print(trapecio(0, 1, g, 5))
print(trapecio(0, 1, g, 10))
print(trapecio(0, 1, g, 100))
print(trapecio(0, 1, g, 1000))
print(trapecio(0, 1, g, 10000))
print('\n')

f1 = lambda x: np.sin(x)

print(trapecio(0, np.pi, f1, 3))
print(trapecio(0, np.pi, f1, 5))
print(trapecio(0, np.pi, f1, 8))
print(trapecio(0, np.pi, f1, 11))
print(trapecio(0, np.pi, f1, 14))
print(trapecio(0, np.pi, f1, 17))
print(trapecio(0, np.pi, f1, 20))
print(trapecio(0, np.pi, f1, 22732))
