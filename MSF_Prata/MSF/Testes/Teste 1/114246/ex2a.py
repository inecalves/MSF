import matplotlib.pyplot as plt
import numpy as np

v0 = 15
angle = 30/180*np.pi
v0x = v0*np.cos(angle)
v0y = v0*np.sin(angle)
vt = 20
g = -9.8
x0 = 0
y0 = 2
dt = 0.001


t = np.arange(0,20, dt)
x = np.zeros(t.size)
y = np.zeros(t.size)
vx = np.zeros(t.size)
vy = np.zeros(t.size)


x[0] = x0
y[0] = y0
vx[0] = v0x
vy[0] = v0y

#metodo de Euler
for i in range(0, t.size-1):
    D = -g/(vt**2)  
    vx[i+1] = vx[i]# velocidade no instante
    vy[i+1] = vy[i] + (g-D*vy[i]*abs(vy[i]))*dt # velocidade no instante
    x[i+1] = x[i] + vx[i] * dt # posiçao no instante
    y[i+1] = y[i] + vy[i] * dt # posiçao no instante
    if y[i+1] < 0:
        break

t = t[:i+2]
x = x[:i+2]
y = y[:i+2]
vx = vx[:i+2]
vy = vy[:i+2]



plt.plot(x,y, label = "Com Res")
plt.xlabel("Distância percorrida (m)")
plt.ylabel("Altura (m)")
plt.title("Gráfico da trajetória, altura em função da distância percorrida")
plt.legend()
plt.show()