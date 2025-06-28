

import matplotlib.pyplot as plt
import numpy as np

dt = 0.001
t = np.arange(0,200+dt,dt)

ax = np.zeros(t.size)
vx = np.zeros(t.size)
x = np.zeros(t.size)

u = 0.004
Cres = 0.9
area = 0.3
Par = 1.225
m = 75
Potencia = 294.20
vx[0] = 1
g = 9.8

for i in range(t.size-1):
    Fcic = Potencia/vx[i]
    FRes = -(Cres/2)*area*Par*vx[i]**2
    FRol = u*m*g
    F = Fcic + FRes - FRol
    ax[i] = F/m  
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i]*dt

plt.plot(t,vx, label="velocity")

plt.grid()

print("Vel Terminal: " + str(vx[-1]))
print("90% da Vel Terminal: " + str(vx[-1]*0.9))


#vx = vx - vx[-1]*0.9

#plt.plot(t,vx, label="velocity -90%")

print("Atinge 90% vt aos: ", end="")
for i in range(vx.size-1):
    if(vx[i] == vx[-1]*0.9): ##Quando vx == 90% v terminal
        print(t[np.where(vx == vx[i])])
        break;
    elif(vx[i] > vx[-1]*0.9): ##Vai buscar o primeiro valor acima de 90% da vterminal
                              ## pega nele e faz media com o anterior
        t1 = t[np.where(vx == vx[i])]
        t2 = t[np.where(vx == vx[i-1])]
        tmed = (t1+t2)/2
        print(tmed)
        break;
        

print("Tempo que demora a percorrer 2km: ", end="")
for i in range(x.size-1):
    if(x[i] == 2000): ##Quando vx == 90% v terminal
        print(t[np.where(x == x[i])])
        break;
    elif(x[i] > 2000): ##Vai buscar o primeiro valor acima de 90% da vterminal
                              ## pega nele e faz media com o anterior
        t1 = t[np.where(x == x[i])]
        t2 = t[np.where(x == x[i-1])]
        tmed = (t1+t2)/2
        print(tmed)
        break;
 

plt.legend()