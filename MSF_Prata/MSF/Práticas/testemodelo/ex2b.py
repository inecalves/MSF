import matplotlib.pyplot as plt
import numpy as np
import math

#Movimento oscilatório harmónico forçado

dt = 0.001

indextime1 = int(685/dt)
indextime2 = int(704/dt)
indextime3 = int(705/dt)
indextime4 = int(710/dt)

t = np.arange(0, 800+dt,dt)

#Constantes
k = 1
m = 1
b = 0.05
F0 = 7.5
w = 1.4

v = np.zeros(t.size)
x = np.zeros(t.size)
f = np.zeros(t.size)

x[0] = -3 #posicao inicial
v[0] = -4 #velocidade inicial

beta =  0.001


for i in range(t.size-1):
    if t[i] >= 400:
        w = 1.37

    f[i] =  (-k*x[i]*(1+2*beta*x[i]**2)) - (b*v[i]) + (F0*np.cos(w*t[i]))
    a = f[i]/m
    v[i+1] = v[i] + a*dt
    x[i+1] = x[i] + v[i+1]*dt


    

plt.plot(t,x)
plt.xlabel("tempo")
plt.ylabel("x(m)")

firstdivision = x[indextime1:indextime2]
seconddivision = x[indextime3:indextime4]

print(np.amax(firstdivision))
print(np.amax(seconddivision))

index1, = np.where(x == np.amax(firstdivision))
index2, = np.where(x == np.amax(seconddivision))

print(index1)
print(index2)

plt.plot(t[index1], np.amax(firstdivision), "bx")
plt.plot(t[index2], np.amax(seconddivision), "bx")

print("Período: tempo entre cristas ->", t[index2]-t[index1])

amplitude = (np.amax(firstdivision) - np.amin(firstdivision))/2
print("Amplitude ->", amplitude)

plt.show()