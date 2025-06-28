import matplotlib.pyplot as plt
import numpy as np

#Constantes
g = 9.8
m = 0.057
r = 0.067/2
PAr = 1.225
vt = 100/3.6
dt = 0.001

t = np.arange(0, 5+dt, dt)
v0= 130/3.6
ang0 = np.radians(10) 
A = np.pi*(r)**2
D = g / vt**2 #coeficiente de resistência do ar

mag = 0.5*A*PAr*r

Rx = np.zeros(t.size)
Ry = np.zeros(t.size)
Rz = np.zeros(t.size)

Vx = np.zeros(t.size)
Vy = np.zeros(t.size)
Vz = np.zeros(t.size)

#Posição inicial
Rx[0] = -10
Ry[0] = 1
Rz[0] = 0

#Velocidade inicial
Vx[0] = v0*np.cos(ang0)
Vy[0] = v0*np.sin(ang0)
Vz[0] = 0.0

#Rotação inicial
Wx = 0
Wy = 0
Wz = 100

#Método de Euler
for i in range(0, t.size-1):
    v = np.sqrt(Vx[i]**2+Vy[i]**2+Vz[i]**2)
    
    #Consoante a rotaçao -> mudar isto
    amagx = - mag * Wz * Vy[i] / m
    amagy = mag * Wz * Vx[i] / m
    amagz = 0
    
    #ha de estar certo para os casos gerais
    ax = -D * Vx[i] * abs(v) + amagx
    ay = - g - D * Vy[i] * abs(v) + amagy
    az = -D * Vz[i] * abs(v) + amagz
    
    Vx[i+1] = Vx[i] + ax * dt
    Vy[i+1] = Vy[i] + ay * dt
    Vz[i+1] = Vz[i] + az * dt
    
    Rx[i+1] = Rx[i] + Vx[i] *dt
    Ry[i+1] = Ry[i] + Vy[i] * dt
    Rz[i+1] = Rz[i] + Vz[i] * dt
    
for i in range(0, t.size-1):   
    #altura máxima
    if(Ry[i+1] < Ry[i]):
        print(Rx[i+1], Ry[i+1], Rz[i+1])
        break

for i in range(0, t.size-1):
    #alcance
    if(Ry[i+1] < 0):
        print(Rx[i+1], Ry[i+1], Rz[i+1])
        break

print(mag)

t = t[:i]
Vx = Vx[:i]
Vy = Vy[:i]
Vz = Vz[:i]

Rx = Rx[:i]
Ry = Ry[:i]
Rz = Rz[:i]

indice = np.argmax(Ry)
y_max = np.max(Ry)
t_ymax = t[indice]
print("Y Maximo:", y_max)
print("Alcance: ",Rx[-2])

plt.plot(Rx,Ry)
plt.legend()
plt.grid()
plt.show()


