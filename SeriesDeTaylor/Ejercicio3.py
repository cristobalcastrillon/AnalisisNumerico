import numpy as np
from sympy import *
import SerieTaylor as st

#Definiendo el símbolo 'x'...
x = Symbol('x')

i = 6.0
while(i <= 14.0):
    punto3 = st.serieTaylor(n = 4, a = 10.0, f = -0.0208*x**4 + 0.7917*x**3 - 10.792*x**2 + 64.083*x - 133, val = i)
    print(punto3)
    i += 0.5

while(i <= 20):
    punto3 = st.serieTaylor(n = 4, a = 10.0, f = 0.0208*x**3 - 1.25*x**2 + 22.417*x - 105, val = i)
    print(punto3)
    i += 0.5    