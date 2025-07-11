import matplotlib.pyplot as plt
import numpy as np

dt = 0.001 
t = np.arange(0, 1+dt, dt)
t0 = 0              #tempo inicial em s
ang = np.radians(16)
vi = 100/3.6
vx0 = vi*np.cos(ang)
vy0 = vi*np.sin(ang)

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

#Posição inicial (0,0,0)


#Velocidade inicial (25,5,-50)
Vx[0] = vx0
Vy[0] = vy0

# w(0,400,0)
#Wy = 400

for i in range(0,t.size-1):
    v = np.sqrt(Vx[i]**2+Vy[i]**2+Vz[i]**2) #modulo da velocidade
    
    ax = -D * Vx[i] * abs(v) 
    ay = -g - D * Vy[i] * abs(v)
    az = -D * Vz[i] * abs(v) 
    
    Vx[i+1] = Vx[i] + ax * dt
    Vy[i+1] = Vy[i] + ay * dt
    Vz[i+1] = Vz[i] + az * dt
    
    Rx[i+1] = Rx[i] + Vx[i] *dt
    Ry[i+1] = Ry[i] + Vy[i] * dt
    Rz[i+1] = Rz[i] + Vz[i] * dt

    if Rx[i] > 20 and 0 < Ry[i] < 2.4 and -3.75 < Rz[i] < 3.75:
        print("Golo! Neymar é o maior")


    if Rx[i]>20:
        print(Ry[i]," Altura da bola")
        break

        

plt.plot(t, Rx, label="x(t)")
plt.plot(t, Ry, label="y(t)")
plt.plot(t, Rz, label="z(t)")
plt.legend()
plt.grid()
plt.show()
