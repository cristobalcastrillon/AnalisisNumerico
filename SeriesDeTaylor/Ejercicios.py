import numpy as np
from sympy import *
import SerieTaylor as st

#Definiendo el símbolo 'x'...
x = Symbol('x')

puntoA = st.serieTaylor(n = 2, a = 0.05, f = x**(1/2), val = 0.0088)
print(puntoA)

puntoB = st.serieTaylor(n = 12, a = 0.05, f = x**(1/2), val = 0.0088)
print(puntoB)

puntoC = st.aproxTaylor(f = exp(x), val = 2.5, a = 0, E = 10**-7)
print(puntoC)