import matplotlib.pyplot as plt
import numpy as np
dt = 0.01 
t = np.arange(0, 7+dt, dt)

t0 = 0              #tempo inicial em s

x0 = 0
y0 = 3
z0 = 0

vx0 = 30
vy0 = 0
vz0 = 0

m = 0.057           #massa da bola em kg
r = 0.034           #raio da bola em m
A = np.pi*(r)**2    #area da bola em m^2
PAr = 1.225         #densidade do ar em kg/m^3
g = 9.8
vterminal = 20/3.6

D = g/(vterminal**2) #coeficiente para resistencia do ar
mag = 0.5*A*PAr*r    #Força de Magnus sem wxv

Rx = np.zeros(t.size)
Ry = np.zeros(t.size)
Rz = np.zeros(t.size)

Vx = np.zeros(t.size)
Vy = np.zeros(t.size)
Vz = np.zeros(t.size)

#Posição inicial
Rx[0] = x0
Ry[0] = y0
Rz[0] = z0

#Velocidade inicial 
Vx[0] = vx0
Vy[0] = vy0
Vz[0] = vz0

# W(0,0,-60)
Wx = 0
Wy = 0
Wz = -60

for i in range(0,t.size-1):
    v = np.sqrt(Vx[i]**2+Vy[i]**2+Vz[i]**2) #modulo da velocidade
    
    amagx = mag* np.cross([Wx,Wy,Wz],[Vx[i],Vy[i],Vz[i]])[0] / m 
    amagy = mag* np.cross([Wx,Wy,Wz],[Vx[i],Vy[i],Vz[i]])[1] / m 
    amagz = mag* np.cross([Wx,Wy,Wz],[Vx[i],Vy[i],Vz[i]])[2] / m 
    
    ax = -D * Vx[i] * abs(v) + amagx
    ay = -g - D * Vy[i] * abs(v) + amagy
    az = -D * Vz[i] * abs(v) + amagz
    
    Vx[i+1] = Vx[i] + ax * dt
    Vy[i+1] = Vy[i] + ay * dt
    Vz[i+1] = Vz[i] + az * dt
    
    Rx[i+1] = Rx[i] + Vx[i] *dt
    Ry[i+1] = Ry[i] + Vy[i] * dt
    Rz[i+1] = Rz[i] + Vz[i] * dt

    if 12 < Rx[i] < 18.4 and Ry[i] > 1: #Verificar se é ponto ou não
        print("Ponto!")
        print(Rx[i], Ry[i], Rz[i])
        break
    #Como a condiçao nao se verifica nao foi ponto

    if Rx[i]>20:
        print(Ry[i]," Altura da bola")
        break


plt.plot(t, Rx, label="x(t)")
plt.plot(t, Ry, label="y(t)")
plt.plot(t, Rz, label="z(t)")
plt.legend()
plt.grid()

#ALCANCE 
print("Alcance, distância a que a bola cai no solo: " + str(Rx[Rx.argmax()])) 

plt.show()
