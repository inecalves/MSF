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
dt = 0.00001


#a)

t = np.arange(0,100, dt)
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
    vx[i+1] = vx[i]# velocidade no instante
    vy[i+1] = vy[i] + g*dt # velocidade no instante
    x[i+1] = x[i] + vx[i] * dt # posiçao no instante
    y[i+1] = y[i] + vy[i] * dt # posiçao no instante
    if y[i+1] < 0:
        break

t = t[:i+2]
x = x[:i+2]
y = y[:i+2]
vx = vx[:i+2]
vy = vy[:i+2]


print("Altura máxima: " ,max(y))   #altura maxima
t_ymax = np.where(y == max(y))
print("Tempo para altura máxima: ",t[t_ymax])  #tempo para altura maxima


t_final = np.where(y < 0)
print("Alcance: ", x[t_final])  #alcance 
print("Tempo para alcance final ", t[t_final])  #tempo para distancia maxima




plt.plot(x,y, label = "Sem Resistência do ar")
#grelha no grafico
plt.grid(True)
plt.show()