import matplotlib.pyplot as plt
import numpy as np
import math

dt = 0.001

indextime1 = int(3/dt)
indextime2 = int(10/dt)
indextime3 = int(11/dt)
indextime4 = int(16/dt)

t = np.arange(0, 20+dt,dt)

#Constantes
k = 1
m = 1
b = 0.05
F0 = 7.5
w = math.sqrt(k/m)

v = np.zeros(t.size)
x = np.zeros(t.size)
f = np.zeros(t.size)

x[0] = -2 #posicao inicial
v[0] = -4 #velocidade inicial

for i in range(t.size-1):
    f[i] =  (-k*x[i])/m - (b*v[i])/m + (F0*np.cos(w*t[i]))
    a = f[i]/m
    v[i+1] = v[i] + a*dt
    x[i+1] = x[i] + v[i+1]*dt
    

plt.plot(t,x)
plt.xlabel("tempo")
plt.ylabel("x(m)")
plt.show()