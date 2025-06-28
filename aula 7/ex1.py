import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

'''
1. Faça uma simulação do movimento da bola usadando o método de Euler-Cromer
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
# y(x) = 0.1 - 0.05*x para x < 2, de outra forma y(x) = 0
def y_func(x: float) -> float:
    return 0.1 - 0.05 * x if x < 2.0 else 0.0

# Derivada de y em ordem a x
# dy/dx = -0.05 para x < 2, de outra forma dy/dx = 0
def dydx_func(x: float) -> float:
    return -0.05 if x < 2.0 else 0.0

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

plt.plot(y, vx, 'b-')
plt.xlabel("t")
plt.ylabel("v")
plt.show()

'''
2. Encontre a velocidade final e o tempo em que a bola atinge x = 2.5 m
'''

x1 = x
y1 = y
vx1 = vx
i2_5 = np.size(x[x<=2.5])
v2_5 = vx[i2_5]
t2_5 = t[i2_5]
print("Quando x = 2.5 m, v = {0:.5f} m/s**2".format(v2_5))
print("Quando x = 2.5 m, t = {0:.5f} s".format(t2_5))

'''
3. Podemos comparar os resultados com os obtidos através da conservação da
energia. Calcule a potencial inicial (Epi) e daí a energia cinética final (Ecf).
   Qual é a velocidade final? Concorda com os resultados obtidos na simulação?


    Epi = Ecf  <=>  m*g*y = 1/2*m*v**2  <=>  v = sqrt(2*g*y)
'''
v = np.sqrt(2*g*0.1)
print("A velocidade final é", v)

'''
Faça uma animação do movimento da bola para cada forma da pista
'''

fig = plt.figure()
ax = plt.axes(xlim=(-0.1, 2.6), ylim=(-0.05, 0.15))
bola = ax.plot([], [], 'ro', [], [], 'bo')[0] # bola, posição inicial

def update(frame):
    # atualizar o plot da posição da bola
    bola.set_xdata([x1[frame]])
    bola.set_ydata([y1[frame]])
    return bola

nframes = 100
total_frames = np.size(t)
iframes = np.arange(0, total_frames, total_frames // nframes)
ani = FuncAnimation(fig=fig, func=update, frames=iframes, interval=100)

plt.show()