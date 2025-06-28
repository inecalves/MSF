import matplotlib.pyplot as plt
import numpy as np

dt = 0.0001 
t = np.arange(0, 0.5+dt, dt)
t0 = 0              #tempo inicial em s
m = 57/1000         #massa da bola em kg
r = (67/2)/1000            #raio da bola em m
A = np.pi*(r)**2    #area da bola em m^2
PAr = 1.225         #densidade do ar em kg/m^3
g = 9.8
vterminal = 100/3.6
D = g/(vterminal**2) #coeficiente para resistencia do ar
mag = 0.5*A*PAr*r    #Força de Magnus sem w*v
Rx = np.zeros(t.size)
Ry = np.zeros(t.size)
Rz = np.zeros(t.size)

Vx = np.zeros(t.size)
Vy = np.zeros(t.size)
Vz = np.zeros(t.size)

#Posição inicial (-10,1,0)
Rx[0] = -10
Ry[0] = 1
Rz[0] = 0


#Velocidade inicial (25,5,-50)
v=130/3.6
angle = 10/180*np.pi
Vx[0] = v*np.cos(angle)
Vy[0] = v*np.sin(angle)
Vz[0] = 0


Wx = 0
Wy = 0
Wz = -100


for i in range(0,t.size-1):
    v = np.sqrt(Vx[i]**2+Vy[i]**2+Vz[i]**2) #modulo da velocidade
    
    amagx = mag* np.cross([Wx,Wy,Wz],[Vx[i],Vy[i],Vz[i]])[0] / m 
    amagy = mag* np.cross([Wx,Wy,Wz],[Vx[i],Vy[i],Vz[i]])[1] / m 
    amagz = -mag* np.cross([Wx,Wy,Wz],[Vx[i],Vy[i],Vz[i]])[2] / m 
    
    ax = -D * Vx[i] * abs(v) + amagx
    ay = -g - D * Vy[i] * abs(v) 
    az = -D * Vz[i] * abs(v) + amagz
    
    Vx[i+1] = Vx[i] + ax * dt
    Vy[i+1] = Vy[i] + ay * dt
    Vz[i+1] = Vz[i] + az * dt
    
    Rx[i+1] = Rx[i] + Vx[i] *dt
    Ry[i+1] = Ry[i] + Vy[i] * dt
    Rz[i+1] = Rz[i] + Vz[i] * dt



altura_max = np.max(Ry)
print("Altura máxima: ", altura_max)

plt.plot(t, Rx, label="x(t)")
plt.plot(t, Ry, label="y(t)")
plt.plot(t, Rz, label="z(t)")
plt.legend()
plt.grid()
plt.show()
