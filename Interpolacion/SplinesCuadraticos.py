import numpy as np
import matplotlib.pyplot as plt

def quadSpline(x, y):
    # nSplines = (len(x)-1): Cantidad de splines.
    nSplines = (len(x)-1)
    incogs = [0 for i in range(nSplines**2)]
    print(incogs)
    eqs = [[0 for i in range(nSplines**2)] for j in range(nSplines**2)]
    print(eqs)

    for i in range(nSplines**2):
        for j in range(nSplines**2):
            if(j == 0 and i == 0):
                #a_1 = 0:
                eqs[i][j] = 0
            # else:
                #¿Por qué la primera fila de la matriz queda así (ejemplo)?


x = [3, 4.5, 7, 9]
y = [2.5, 1, 2.5, 0.5]
quadSpline(x, y)

# plt.scatter(x, y)
# plt.show()