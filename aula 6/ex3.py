import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constantes
G = 4 * np.pi**2  # Constante gravitacional em unidades astronômicas (AU^3 / ano^2 / massa solar)
M = 1  # Massa do Sol em massas solares
dt = 0.001  # Passo temporal em anos
tf = 10  # Tempo final em anos
n = int(tf / dt)  # Número de passos

# Arrays para posição, velocidade e aceleração
x = np.zeros(n + 1)
y = np.zeros(n + 1)
vx = np.zeros(n + 1)
vy = np.zeros(n + 1)

# Condições iniciais
x[0] = 1  # Posição inicial em AU
y[0] = 0
vx[0] = 0  # Velocidade inicial em AU/ano
vy[0] = 2 * np.pi  # Velocidade inicial em AU/ano

# Método de Euler
for i in range(n):
    r = np.sqrt(x[i]**2 + y[i]**2)  # Distância ao Sol
    ax = -G * M * x[i] / r**3  # Aceleração em x
    ay = -G * M * y[i] / r**3  # Aceleração em y
    
    # Atualizar velocidades
    vx[i + 1] = vx[i] + ax * dt
    vy[i + 1] = vy[i] + ay * dt
    
    # Atualizar posições
    x[i + 1] = x[i] + vx[i+1] * dt
    y[i + 1] = y[i] + vy[i+1] * dt

# Plotar a órbita

fig, ax = plt.subplots() #criar figura
plt.plot(x, y, color='b')
terra = ax.plot(x[0],y[0],'o')[0] #terra, posição inicial
sun = ax.plot(0,0,'o', color="orange", markersize=20)[0]
ax.set(xlim=[-1.6, 1.4], ylim=[-1.4, 1.4]) #fixar os limites dos eixos
def update(frame):
    # atualizar o plot da posição da Terra
    terra.set_xdata([x[frame]])
    terra.set_ydata([y[frame]])
    return terra
#criar a animação
ani = FuncAnimation(fig=fig, func=update, frames=1000, interval=1)


plt.show()