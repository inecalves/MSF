import matplotlib.pyplot as plt
import numpy as np
import math

#Movimento oscilatório harmónico forçado

dt = 0.001

indextime1 = int(3/dt)
indextime2 = int(10/dt)
indextime3 = int(11/dt)
indextime4 = int(16/dt)

t = np.arange(0, 20+dt,dt)

#Constantes
k = 2
m = 0.5
b = 0.02
alpha = -0.1
F0 = 7.5
w = math.sqrt(k/m)

v = np.zeros(t.size)
x = np.zeros(t.size)
f = np.zeros(t.size)

x[0] = 1.5    #posicao inicial
v[0] = 0.5     #velocidade inicial

for i in range(t.size-1):
    f[i] =  (-k*x[i]) -3*alpha*x[i]**2 + 4*b*x[i]**3
    a = f[i]/m
    v[i+1] = v[i] + a*dt
    x[i+1] = x[i] + v[i+1]*dt
    

plt.plot(t,x)
plt.xlabel("tempo")
plt.ylabel("x(m)")

firstdivision = x[indextime2:indextime3]
seconddivision = x[indextime3:indextime4]

# print(np.amax(firstdivision))
# print(np.amax(seconddivision))

index1, = np.where(x == np.amax(firstdivision))
index2, = np.where(x == np.amax(seconddivision))


plt.plot(t[index1], np.amax(firstdivision), "bx")
plt.plot(t[index2], np.amax(seconddivision), "bx")

print("Período: tempo entre cristas ->", t[index2]-t[index1])

amplitude = (np.amax(firstdivision) - np.amin(firstdivision))/2
print("Amplitude ->", amplitude)

#calcula a frequencia
frequencia = 1/(t[index2]-t[index1])
print("Frequência ->", frequencia*2*np.pi)





plt.grid()
plt.show()
