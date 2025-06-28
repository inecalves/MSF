'''
Maria Inês Gonçalves
124754
'''

import numpy as np
import matplotlib.pyplot as plt

# Parametros 
t0 = 0.0
tf = 3.0          #[ano]
dt = 0.01
v0 = 2.3 * np.pi  # velocidade inicial [AU/ano]
x0 = 1.0          # posição inicial da terra [AU]

n = int(((tf - t0)/dt))

GM = 4 * np.pi**2

m = 1

t = np.arange(t0, tf, dt)
x = np.zeros(np.size(t))
y = np.zeros(np.size(t))
vx = np.zeros(np.size(t))
vy = np.zeros(np.size(t))
ax = np.zeros(np.size(t))
ay = np.zeros(np.size(t))

x[0] = x0
y[0] = 0
vx[0] = 0
vy[0] = v0
N=len(t)

# método euler-cromer
for i in range(N-1):
    r = np.sqrt(x[i]**2 + y[i]**2)
    ax = -GM * x[i] / r**3
    ay = -GM * y[i] / r**3
    
    vx[i+1] = vx[i] + ax * dt
    vy[i+1] = vy[i] + ay * dt
    x[i+1] = x[i] + vx[i+1] * dt
    y[i+1] = y[i] + vy[i+1] * dt


# NÃO ACABADO
for i in range(n):
        # Calcular a Energia Mecânica (Em = Ec + Ep) :
        vv = np.sqrt(vx[i]**2 + vy[i]**2) # instensidade do vetor velocidade em cada instante

        Ep = -GM*m/x[i] # Energia Potencial
        Ec = 0.5*m*(vv**2) # Energia Cinética

        E = Ec + Ep # Energia Total

        print("A Energia Mecânica no instante {:.1f}s é {:.2f}J".format(t[i], E))

# Plot gráfico Ec-tempo
plt.plot(t, Ec, label="energia cinética")
plt.grid()
plt.xlabel("Tempo (s)")
plt.ylabel("Ec (m)")
plt.legend()
plt.show()
