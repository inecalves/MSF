import matplotlib.pyplot as plt
import numpy as np

dt = 0.001
t = np.arange(0,205+dt,dt)

ax = np.zeros(t.size)
vx = np.zeros(t.size)
x = np.zeros(t.size)

u = 0.01                #coeficiente de resistencia de um piso liso
Cres = 0.9              #coeficiente de resistencia do ar
area = 0.5              #area frontal
Par = 1.225             #densidade do ar
m = 72                  #massa da pessoa + trotinete
Potencia = 0.48*735.5   #294.20 potencia passado de hp para w
vx[0] = 0.5             #velocidade inicial dada pelo empurrão
g = 9.8
N= m*g                  #N=P = m*g

for i in range(t.size-1):
    Fcic = Potencia/vx[i] 
    FRes = -(Cres/2)*area*Par*vx[i]**2 
    FRol = u*N          #Força de resistencia ao rolamento Frol= u*N=u*m*g
    F = Fcic + FRes - FRol
    ax[i] = F/m  
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i]*dt

    print("Tempo que demora a percorrer 2000m:")
    if(x[i] == 2000): ##Quando x == 2000m
        print(t[np.where(x == x[i])])
        break;
    elif(x[i] > 2000): ##Vai buscar o primeiro valor acima de 2000m
                              ## pega nele e faz media com o anterior
        t1 = t[np.where(x == x[i])]
        t2 = t[np.where(x == x[i-1])]
        tmed = (t1+t2)/2
        print(tmed)
        break;

plt.plot(t,vx, label="velocity")
plt.grid()
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (m/s)")
plt.title("Gráfico da velocidade em função do tempo")
plt.legend()
plt.show()




 

