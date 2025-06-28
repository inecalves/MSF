import matplotlib.pyplot as plt
import numpy as np

vi = 0 # velocidade inicial do corpo m/s
dt = 0.01 #n passos
g = -9.8 #aceleração gravítica

T = np.arange(0,20, dt)
v = np.zeros(T.size)
y = np.zeros(T.size)
ay = np.zeros(T.size)

v[0] = 0
y[0] = 4 #posição inicial do corpo em queda livre
  
y1 = 4 + 0*T + 0.5*g*T**2 #Valor Teorico usando  y(t)=y0+v0t+1/2at**2

floor = np.zeros(T.size)

#Metodo de Euler
for i in range(0, T.size-1):
        ay[i]=g
        v[i+1] = v[i] + ay[i]*dt # velocidade no instante
        y[i+1] = y[i] + v[i]*dt # posiçao no instante


print("Velocidade : ", v)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_xlabel('tempo (s)')
ax.set_ylabel('Y (m)')
ax.plot(T, floor, label="Y = 0")
ax.plot(T, y, label="Metodo de Euler")
ax.plot(T, y1, label="Metodo Exato")
plt.legend()
plt.show()
