import matplotlib.pyplot as plt
import numpy as np

dt = 0.01 
t = np.arange(0, 0.5+dt, dt)
t0 = 0              #tempo inicial em s
m = 0.45            #massa da bola em kg
r = 0.11            #raio da bola em m
A = np.pi*(r)**2    #area da bola em m^2
PAr = 1.225         #densidade do ar em kg/m^3
g = 9.8
vterminal = 100/3.6
D = g/(vterminal**2) #coeficiente para resistencia do ar
mag = 0.5*A*PAr*r    #Força de Magnus sem wxv
Rx = np.zeros(t.size)
Ry = np.zeros(t.size)
Rz = np.zeros(t.size)

Vx = np.zeros(t.size)
Vy = np.zeros(t.size)
Vz = np.zeros(t.size)

#Posição inicial (0,0,23.8)
Rz[0] = 23.8

#Velocidade inicial (25,5,-50)
Vx[0] = 25
Vy[0] = 5
Vz[0] = -50

# w(0,0,400)
Wy = 400

for i in range(0,t.size-1):
    v = np.sqrt(Vx[i]**2+Vy[i]**2+Vz[i]**2) #modulo da velocidade
    
    amagx = mag * Wy * Vz[i] / m 
    amagz = - mag * Wy * Vx[i] / m
    
    ax = -D * Vx[i] * abs(v) + amagx
    ay = -g - D * Vy[i] * abs(v)
    az = -D * Vz[i] * abs(v) + amagz
    
    Vx[i+1] = Vx[i] + ax * dt
    Vy[i+1] = Vy[i] + ay * dt
    Vz[i+1] = Vz[i] + az * dt
    
    Rx[i+1] = Rx[i] + Vx[i] *dt
    Ry[i+1] = Ry[i] + Vy[i] * dt
    Rz[i+1] = Rz[i] + Vz[i] * dt


plt.plot(t, Rx, label="x(t)")
plt.plot(t, Ry, label="y(t)")
plt.plot(t, Rz, label="z(t)")
plt.legend()
plt.grid()
plt.show()

#3D plot
plt.figure(figsize=(8,8))
ax = plt.axes(projection='3d')
ax.plot3D(Rx[Rx>=0],-Rz[Rx>=0],Ry[Rx>=0], 'r')

goalx = [0,0,0,0]
goaly = [0,2.4,2.4,0]
goalz = [-3.66,-3.66,3.66,3.66]

ax.plot3D(goalx,goalz,goaly, 'k')
ax.set_xlim3d(0, 5)
ax.set_ylim3d(-25, 5)
ax.set_zlim3d(0, 5)
ax.set_box_aspect((2,6,2))
ax.set_xlabel('x')
ax.set_ylabel('z')
ax.set_zlabel('y')
plt.show()