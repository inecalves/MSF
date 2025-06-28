import matplotlib.pyplot as plt
import numpy as np

dt = 0.0001
g = 9.8
v0 = 100/3.6
ang = 10/180*np.pi
m = 57/1000
t = np.arange(0,15+dt,dt)

x0 = 0
y0 = 0
vx0 = v0*np.cos(ang)
vy0 = v0*np.sin(ang)

Em0 = m*g*y0 + 0.5*m*v0**2

vt = 100/3.6 #velocidade terminal
D = g / vt**2 #coeficiente de resistência do ar

x = np.zeros(t.size)
y = np.zeros(t.size)
vx = np.zeros(t.size)
vy = np.zeros(t.size)
Em = np.zeros(t.size)
W  = np.zeros(t.size)
x[0] = x0
y[0] = y0
vx[0] = vx0
vy[0] = vy0
Em[0] = Em0
W[0] = 0
f = np.zeros(t.size)

ind1, ind2 = round(0.4/dt), round(0.8/dt) #indice nos pontos 0.4 e 0.8

print("No instante: Inicial -> Em: " + str(Em0))
#metodo de Euler
for i in range(0, t.size-1):
    v = np.sqrt(vx[i]**2+vy[i]**2)
    
    ax = - D * vx[i] * v
    ay = - D * vy[i] * v
    f[i] = m*(ax*vx[i]+ay*vy[i]) 
    
    ay = ay - g
    vx[i+1] = vx[i] + ax * dt # velocidade no instante
    vy[i+1] = vy[i] + ay * dt # velocidade no instante
    x[i+1] = x[i] + vx[i] * dt # posiçao no instante
    y[i+1] = y[i] + vy[i] * dt # posiçao no instante
    v = np.sqrt(vx[i+1]**2+vy[i+1]**2)
    
    Em[i+1] = m*g*y[i+1] + 0.5*m*v**2
    
    
    W[i] = -m*g*(y[i]-y0) #0.5*m*(v-v0)**2 
    #print("No instante: " + str(i+1) + " -> Em: " + str(Em[i+1]))
    if y[i+1] < 0:
        break
 
t = t[:i+2]
x = x[:i+2]
y = y[:i+2]
vx = vx[:i+2]
vy = vy[:i+2]
Em = Em[:i+2]
 
 
plt.xlim([0,1])
plt.plot(t, Em)
plt.xlabel("Tempo")
plt.ylabel("Energia Mecanica")
 
#Energia mecânica nos instantes t = 0, 0.4 e 0.8
print("em t0:", str(Em[np.where(t == 0)]))
print("em t1:", str(Em[np.where(t == 0.4)]))
print("em t2:", str(Em[np.where(t == 0.8)]))


Wres1 = (0.5*(f[0]+f[ind1])+np.sum(f[1:ind1]))*dt
Wres2 = (0.5*(f[0]+f[ind2])+np.sum(f[1:ind2]))*dt

print(Wres1)
print(Wres2)
#vv = np.sqrt(vx**2 + vy**2)
#W0 = float(0.5*m*(vv[np.where(t == 0)]-v0)**2)
#print("{:.02f}".format(W0))

#W1 = float(0.5*m*(vv[np.where(t == 0.4)]-v0)**2)
#print("{:.02f}".format(W1))


plt.grid()
plt.legend()
plt.show()