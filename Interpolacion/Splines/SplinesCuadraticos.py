import numpy as np
import matplotlib.pyplot as plt

def quadSpline(x, y):
    # nSplines = (len(x)-1): Cantidad de splines.
    nSplines = (len(x)-1)
    incogs = [0 for i in range(nSplines**2)]
    print(incogs)
    eqs = [[0 for i in range(nSplines**2)] for j in range(nSplines**2)]
    print(eqs)
    # Llenar la matriz:
    # Cuando i (filas) < 6 (nSplines) y distinto al siguiente i tal que i%2 = 0, entonces:
    #   Cuando j (columnas) < 6 y distinto al siguiente j tal que j%3 = 0, entonces:
    #       if(j%3 == 0):
    #           eqs[i][j] = x[i]**2
    #       if(j%3 == 1):
    #           eqs[i][j] = x[i]
    #       else:
    #           eqs[i][j] = 1


x = [3, 4.5, 7, 9]
y = [2.5, 1, 2.5, 0.5]
quadSpline(x, y)

# plt.scatter(x, y)
# plt.show()