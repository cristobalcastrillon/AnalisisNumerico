# -------------------------MODELOS-------------------------
# ----------------Susceptible - Infectado------------------
def modelo_SI(s, i, N, tasaInfec, tiempoMax):
  t = 0
  sus = []
  inf = []
  prob = []
  while (t < tiempoMax):
    s, i = s - tasaInfec * ((s * i / N)), i + tasaInfec * ((s * i) / N)
    p = tasaInfec * (i / N)

    sus.append(s)
    inf.append(i)
    prob.append(p)
    t += 1

    # Prueba
    # print(s, i, p)

  return([sus, inf, prob])

# ----------Susceptible - Infectado - Recuperado-----------
def modelo_SIR(y, tasaInfec, tasaRecup, tiempoMax):
  # s: Población susceptible
  # i: Población infectada
  # r: Población recuperada
  # n: (implícito) conjunto de s, i, r (s+i+r)
  s, i, r = y
  dS_dt = -tasaInfec * s * i / (s + i + r)
  dI_dt = tasaInfec * s * i / (s + i + r) - (tasaRecup * i)
  dR_dt = tasaRecup * i
  return([dS_dt, dI_dt, dR_dt])

# ------------------Depredaror - Presa---------------------
def modelo_DP(valsIni, tiempoMax, params):
  # x: Población inicial de presas
  # y: Población inicial de depredadores
  x, y = valsIni
  alpha, beta, delta, gamma = params
  dx_dt = alpha * x - beta * x * y
  dy_dt = delta * x * y - gamma * y
  return([dx_dt, dy_dt])

# -------------------------DATOS--------------------------
# COVID-19 - Casos Confirmados en la ciudad de Bogotá:
# https://datosabiertos.bogota.gov.co/dataset/numero-de-casos-confirmados-por-el-laboratorio-de-covid-19-bogota-d-c

# ---------------BIBLIOGRAFÍA Y REFERENCIAS---------------
# The Coronavirus Curve - Numberphile:
# https://www.youtube.com/watch?v=k6nLfCbAzgo

# Ordinary Differential Equations (ODE) in Python:
# https://towardsdatascience.com/ordinal-differential-equation-ode-in-python-8dc1de21323b

# View of Mathematical models and the coronavirus, COVID-19:
# https://colombiamedica.univalle.edu.co/index.php/comedica/article/view/4277/4761

# Lotka-Volterra Equations (Predator - Prey Model):
# https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations

# Python Code for Predator-Prey Model:
# https://www.youtube.com/watch?v=2f5aRTBmm10