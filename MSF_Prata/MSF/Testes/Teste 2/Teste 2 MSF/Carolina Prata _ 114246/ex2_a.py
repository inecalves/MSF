import matplotlib.pyplot as plt
import numpy as np

dt = 0.001
t = np.arange(0,100+dt,dt)

ax = np.zeros(t.size)
vx = np.zeros(t.size)
x = np.zeros(t.size)

u = 0.04                #coeficiente de resistencia de um piso liso
Cres = 0.25             #coeficiente de resistencia do ar
area = 2                #area frontal
Par = 1.225             #densidade do ar
m = 2000                #massa do eletrico
Potencia = 40*10**3     #potencia 
vx[0] = 1               #velocidade inicial dada pelo empurrão m/s 
g = 9.8
P= m*g 
Px=P*np.sin(np.radians(5))
Py=P*np.cos(np.radians(5))
N=P

for i in range(t.size-1):
    Fcic = Potencia/vx[i] 
    FRes = -(Cres/2)*area*Par*vx[i]**2 
    FRol = u*N          #Força de resistencia ao rolamento Frol= u*N=u*m*g
    F = Fcic + FRes - FRol - Px
    ax[i] = F/m  
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i]*dt


plt.plot(t,x, label="Posição")
plt.plot(t,vx, label="Velocidade")
plt.legend()

plt.title("Evolução temporal da posição e da velocidade")
plt.grid()
plt.show()