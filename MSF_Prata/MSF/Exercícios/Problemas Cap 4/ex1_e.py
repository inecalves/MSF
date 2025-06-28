import matplotlib.pyplot as plt
import numpy as np


v0 = 100/3.6
angle = 10/180*np.pi
v0x = v0*np.cos(angle)
v0y = v0*np.sin(angle)
vt = 100/3.6
g = -9.8
x0 = 0
y0 = 0
dt = 0.0001
t = np.arange(0,100, dt)

t1 = np.arange(0,100, dt)
y1 = np.zeros(t.size)
x1 = np.zeros(t.size)
vx1 = np.zeros(t.size)
vy1 = np.zeros(t.size)


x1[0] = x0
y1[0] = y0
vx1[0] = v0x
vy1[0] = v0y
D = -g/(vt**2)

for i in range(0, t1.size-1):
    v = np.sqrt(vx1[i]**2 + vy1[i]**2)
    ax = -D*vx1[i]*abs(v)
    ay = g-D*vy1[i]*abs(v)
    
    vx1[i+1] = vx1[i] + ax*dt# velocidade no instante
    vy1[i+1] = vy1[i] + ay*dt # velocidade no instante
    x1[i+1] = x1[i] + vx1[i] * dt # posiçao no instante
    y1[i+1] = y1[i] + vy1[i] * dt # posiçao no instante
    if y1[i+1] < 0:
        break

t1 = t1[:i+2]
x1 = x1[:i+2]
y1 = y1[:i+2]
vx1 = vx1[:i+2]
vy1 = vy1[:i+2]

#alinea f
t_altura_máxima = np.where(y1 == np.max(y1))
altura_máxima = y1[t_altura_máxima]
print("Altura máxima: ", altura_máxima)
print("Tempo altura maxima: ", t1[t_altura_máxima])

#alinea g
t_alcance = np.where(y1 < 0)
alcance = x1[t_alcance]
print("Alcance: ", alcance)
print("Tempo alcance: ", t1[t_alcance])


plt.plot(x1,y1, label="Com Resistência do ar")
plt.xlabel("x(t) (m)")
plt.ylabel("y(t) (m)")

plt.legend()
plt.grid()
plt.show()