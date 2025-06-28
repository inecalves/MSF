import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

'''
2. Faça uma simulação do movimento da bola usadando o método de Euler-Cromer
com as seguintes condições iniciais:
        x0 = 0
        vx0 = 0
    simule o movimento até x = 2.5m
'''

t0 = 0.0        # condição inicial, tempo [s]
tf = 4.0        # limite do domínio, tempo final [s]
dt = 0.001      # passo [s]
vx0 = 0.0       # condição inicial, módulo da velocidade inicial [m/s]
x0 = 0.0        # condição inicial, coordenada x da posição inicial [m]
y0 = 0.1        # condição inicial, coordenada y da posição inicial [m]
g = 9.8         # aceleração gravitacional [m/s^2]

# Trajetória y(x)
# y(x) = 0.025 * (x - 2)**2 para x < 2, de outra forma y(x) = 0
def y_func(x: float) -> float:
    return 0.025 * (x - 2)**2 if x < 2.0 else 0.0

# Derivada de y em ordem a x
# dy/dx = 0.05 * (x - 2) para x < 2, de outra forma dy/dx = 0
def dydx_func(x: float) -> float:
    return 0.05 * (x - 2) if x < 2.0 else 0.0

# domínio [ano]
t = np.arange(t0, tf, dt)

# posição [m]
x = np.zeros(np.size(t))
y = np.zeros(np.size(t))
x[0] = x0
y[0] = y0

# velocidade [m/s]
vx = np.zeros(np.size(t))
vx[0] = vx0

# aceleração [m/s^2]
ax = np.zeros(np.size(t))

for i in range(np.size(t) - 1):
    # aceleração
    ax[i] = -g * dydx_func(x[i])

    # Método de Euler-Cromer
    vx[i + 1] = vx[i] + ax[i] * dt
    x[i + 1] = x[i] + vx[i + 1] * dt
    y[i + 1] = y_func(x[i+1])

fig, ax1 = plt.subplots()
color = 'tab:blue'             # --> posição do x
ax1.set_xlabel('time (s)')
ax1.set_ylabel('x', color=color)
ax1.plot(t[x<2.5], x[x<2.5], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx() # partilhar eixo horizontal

color = 'tab:red'              # --> posição do y
ax2.set_ylabel('y', color=color)
ax2.plot(t[x<2.5], y[x<2.5], color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()
plt.show()

'''
3. Quanto tempo é que a bola demora a atingir x = 2.5m? Foi mais rápido ou
mais devagar do que no exercício 1?
'''

x2 = x
y2 = y
vx2 = vx
i25 = np.size(x[x<=2.5])
v25 = vx[i25]
t25 = t[i25]
print("Quando x = 2.5 m, v = {0:.5f} m/s²".format(v25))
print("Quando x = 2.5 m, t = {0:.5f} s".format(t25))

# A velocidade final é a mesma, mas a bola da trajetória parabólica
# chega ao destino mais rapidamente

'''
Faça o gráfico da velocidade vx em função da altura y para cada forma da pista
'''
plt.plot(y, vx, 'b-')
plt.xlabel("t")
plt.ylabel("v")
plt.show()

'''
Faça uma animação do movimento da bola para cada forma da pista
'''

fig = plt.figure()
ax = plt.axes(xlim=(-0.1, 2.6), ylim=(-0.05, 0.15))
bola = ax.plot([], [], 'ro', [], [], 'bo')[0] # bola, posição inicial

def update(frame):
    # atualizar o plot da posição da bola
    bola.set_xdata([x2[frame]])
    bola.set_ydata([y2[frame]])
    return bola

nframes = 100
total_frames = np.size(t)
iframes = np.arange(0, total_frames, total_frames // nframes)
ani = FuncAnimation(fig=fig, func=update, frames=iframes, interval=100)

plt.show()