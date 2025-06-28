import matplotlib.pyplot as plt
import numpy as np

#QUEDA LIVRE DE UM CORPO SEM RESISTÊNCIA DO AR
vi = 100/3.6 * np.cos(10) # m/s
dt = 0.01 #n passos
vt = 60.0
g = -9.8

T = np.arange(0,20, dt)
v = np.zeros(T.size)
y = np.zeros(T.size)
ay = np.zeros(T.size)

v[0] = 0
y[0] = 800 #posição inicial do corpo em queda livre

D = -g/(vt**2)    

#y1 = 800 + 0*T + 0.5*g*T**2 Valor Teorico
# aceleraçao inicial

floor = np.zeros(T.size)

#Metodo de Euler
for i in range(0, T.size-1):
        ay[i]=g
        v[i+1] = v[i] + (g-D*v[i]*abs(v[i]))*dt # velocidade no instante
        y[i+1] = y[i] + v[i] * dt # posiçao no instante

#Valor aproximado consultado no variable Explorer quando y ~ 0
print("Velocidade de embate ", abs(v[1755]))
print("Tempo aquando o embate ", T[1755])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_xlabel('tempo (s)')
ax.set_ylabel('Y (m)')
ax.plot(T, floor, label="Y = 0")
ax.plot(T, y, label="Metodo de Euler")
#ax.plot(T, y1, label="Exato")

plt.legend()