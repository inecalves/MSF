
import matplotlib.pyplot as plt
import numpy as np

#Constantes
g = 9.8
m = 0.057
r = 0.067/2
PAr = 1.225
vt = 100/3.6
dt = 0.01

t = np.arange(0, 5+dt, dt)
v0= 130/3.6
ang0 = 10/180*np.pi ##PASSAR DE RADIANOS A GRAUS

A = np.pi*(r)**2
D = g / vt**2
mag = 0.5*A*PAr*r

Rx = np.zeros(t.size)
Ry = np.zeros(t.size)
Rz = np.zeros(t.size)

Vx = np.zeros(t.size)
Vy = np.zeros(t.size)
Vz = np.zeros(t.size)


Rx[0] = -10
Ry[0] = 1
Rz[0] = 0

Vx[0] = v0*np.cos(ang0)
Vy[0] = v0*np.sin(ang0)
Vz[0] = 0.0

Wx = 0
Wy = 0
Wz = 100

#metodo de Euler
for i in range(0, t.size-1):
    v = np.sqrt(Vx[i]**2+Vy[i]**2+Vz[i]**2)
    
    #Consoante a rotacao -> mudar isto
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
    
    if(Ry[i] < 0):
        break;

t = t[:i+2]
Vx = Vx[:i+2]
Vy = Vy[:i+2]
Vz = Vz[:i+2]

Rx = Rx[:i+2]
Ry = Ry[:i+2]
Rz = Rz[:i+2]


indice = np.argmax(Ry)
y_max = np.max(Ry)
t_ymax = t[indice]
print("Y Maximo:", y_max)
print("Alcance: ",Rx[i])

plt.plot(Rx,Ry)
plt.show()