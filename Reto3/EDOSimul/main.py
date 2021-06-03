import modelos as mod
import numpy as np
import csv
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.integrate import solve_ivp

# ----------Susceptible - Infectado - Recuperado---------
# Datos iniciales:
# N: Población de Bogotá D.C. (2018) según el DANE:
# https://sitios.dane.gov.co/cnpv/#!/donde_estamos
N = 7149540
I0 = 1
# S0: N (población de Bogotá) - I0 (primer infectado)
S0 = N - I0 
# R0: Número inicial de Recuperados (NO CONFUNDIR CON NÚMERO DE REPRODUCCIÓN)
R0 = 0

# Tasas de modelo pronóstico:
# Manrique-Abril, et al.
# tasaInfec ≠ porcentaje
tasaInfec = 1.5
tasaRecup = 0.022

# t: 60 días (2 meses)
# Tercer parámetro total de muestras en el rango 0 - 60 (parámetro 2)
tSIR = np.linspace(0, 60, 60)

# Solución con MÉTODO: Función ODEInt (Adams o BDF)
sol_SIR = odeint(mod.modelo_SIR, [S0, I0, R0], tSIR, args=(tasaInfec, tasaRecup))
sol_SIR = np.array(sol_SIR)

# Gráfica
"""
plt.figure(figsize = [6, 4])
plt.plot(tSIR, sol_SIR[:, 0], label = "S(t)")
plt.plot(tSIR, sol_SIR[:, 1], label = "I(t)")
plt.plot(tSIR, sol_SIR[:, 2], label = "R(t)")
plt.grid()
plt.legend()
plt.xlabel("Tiempo")
plt.ylabel("No. Individuos")
plt.show()
"""

# Guardando datos en CSV...
with open('sir_ODEInt.csv', mode='w') as sir_ODEInt:
  row_writer = csv.writer(sir_ODEInt, delimiter=';')
  row_writer.writerow(['Dia','Susceptibles','Infectados','Recuperados'])
  for i in range(len(tSIR)):
    row_writer.writerow([i + 1, sol_SIR[i, 0], sol_SIR[i, 1], sol_SIR[i, 2]])

# Solución con MÉTODO: Runge-Kutta de Orden 4
# Basado en:
# http://acme.byu.edu/wp-content/uploads/2020/09/SIR2020.pdf
def ode_SIR(t, y):
  return np.array([-tasaInfec*y[0]*y[1]/N, (tasaInfec*y[0]*y[1]/N)-tasaRecup*y[1], tasaRecup*y[1]])

sol_SIR2 = solve_ivp(ode_SIR, [tSIR[0], tSIR[-1]], [S0, I0, R0], method = "RK45", t_eval = tSIR)

# Gráfica
"""
plt.figure(figsize = [6, 4])
plt.plot(sol_SIR2.t, sol_SIR2.y[0], label = "S(t)")
plt.plot(sol_SIR2.t, sol_SIR2.y[1], label = "I(t)")
plt.plot(sol_SIR2.t, sol_SIR2.y[2], label = "R(t)")
plt.grid()
plt.legend()
plt.xlabel("Tiempo")
plt.ylabel("No. Individuos")
plt.show()
"""

# Guardando datos en CSV...
with open('sir_RK45.csv', mode='w') as sir_ODEInt:
  row_writer = csv.writer(sir_ODEInt, delimiter=';')
  row_writer.writerow(['Dia','Susceptibles','Infectados','Recuperados'])
  for i in range(len(tSIR)):
    row_writer.writerow([i+1, sol_SIR2.y[0][i], sol_SIR2.y[1][i], sol_SIR2.y[2][i]])

# ----------------Susceptible - Infectado--------------
sus = [] # Array Infectados
inf = [] # Array Susceptibles
prob = [] # Probabilidad de Infección en tiempo T
sol = [sus, inf, prob]

# t: 60 días (2 meses)
tSI = 60
# Reutilizando los valores iniciales del modelo SIR...
sol = mod.modelo_SI(S0, I0, N, tasaInfec, tSI)

# Gráfica
"""
figure = plt.figure()
figure.canvas.set_window_title('Modelo SI')
figure.add_subplot(211)
inf_line, = plt.plot(sol[0], label = 'S(t)')

sus_line, = plt.plot(sol[1], label = 'I(t)')
plt.legend(handles = [inf_line, sus_line])

ax = figure.add_subplot(212)
prob_line = plt.plot(sol[2], label = 'p(t)')
plt.legend(handles = prob_line)
plt.xlabel('T')
plt.ylabel('p')
plt.show()
"""

# Guardando datos en CSV...
with open('si_Numerico.csv', mode='w') as sir_ODEInt:
  row_writer = csv.writer(sir_ODEInt, delimiter=';')
  row_writer.writerow(['Dia','Susceptibles','Infectados'])
  for i in range(tSI):
    row_writer.writerow([i + 1, sol[0][i], sol[1][i]])

# Solución con MÉTODO: Runge-Kutta de Orden 4
# Basado en:
# http://acme.byu.edu/wp-content/uploads/2020/09/SIR2020.pdf
def ode_SI(t, y):
  return np.array([-tasaInfec*y[0]*y[1]/N, (tasaInfec*y[0]*y[1]/N)])

sol_SI2 = solve_ivp(ode_SI, [tSIR[0], tSIR[-1]], [S0, I0], method = "RK45", t_eval = tSIR)

# Gráfica
"""
plt.figure(figsize = [6, 4])
plt.plot(sol_SI2.t, sol_SI2.y[0], label = "S(t)")
plt.plot(sol_SI2.t, sol_SI2.y[1], label = "I(t)")
plt.grid()
plt.legend()
plt.xlabel("Tiempo")
plt.ylabel("No. Individuos")
plt.show() 
"""

# Guardando datos en CSV...
with open('si_RK45.csv', mode='w') as sir_ODEInt:
  row_writer = csv.writer(sir_ODEInt, delimiter=';')
  row_writer.writerow(['Dia','Susceptibles','Infectados'])
  for i in range(tSI):
    row_writer.writerow([i + 1, sol_SI2.y[0][i], sol_SI2.y[1][i]])

# ---------------Depredador - Presa----------------
# Datos tomados de Predator-Prey Modeling/Shaza Hussein/University of South Florida
# https://scholarcommons.usf.edu/cgi/viewcontent.cgi?article=4818&context=ujmm

y0 = [1000, 100] # [Presa, Depredador] Vals. iniciales
# t: 1 año
tDP = np.linspace(0, 365, 365) 

# Parámetros reales positivos que describen la interacción de las dos especies
# Presa: Conejos
alpha = 0.2    # Tasa de natalidad presa
beta = 0.001   # Tasa de muerte presa
# Depredador: Zorros
delta = 0.001   # Tasa de natalidad depredador
gamma = 0.5     # Tasa de muerte depredador

params = [alpha, beta, delta, gamma]

sol_DP = odeint(mod.modelo_DP, y0, tDP, args=(params,))
sol_DP = np.array(sol_DP)

# Gráfica
"""
plt.figure(figsize = [6, 4])
plt.plot(tDP, sol_DP[:, 0], label = "Conejos")
plt.plot(tDP, sol_DP[:, 1], label = "Zorros")
plt.grid()
plt.legend()
plt.xlabel("Tiempo")
plt.ylabel("No. de Individuos")
plt.show()
"""

# Amplitud de cada función
maxConejo = max(sol_DP[:, 0])
minConejo = min(sol_DP[:, 0])

amplitudConejo = abs(maxConejo - minConejo) / 2

maxZorro = max(sol_DP[:, 1])
minZorro = min(sol_DP[:, 1])

amplitudZorro = abs(maxZorro - minZorro) / 2

#print(amplitudConejo)
#print(amplitudZorro)

# Conejos
# Periodo 365/(8+1/4) = 44.24 días
# Frecuencia 1/T = 0.001984 días^-1

# Zorros
# Periodo 365/(8+1/2) = 42.94 días
# Frecuencia 1/T = 0.023288 días^-1