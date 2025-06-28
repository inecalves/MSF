import matplotlib.pyplot as plt
import numpy as np

dt = 0.001
t = np.arange(0,300+dt,dt)

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
P =m*g



def t1500m():
    tmed = 0
    Px=P*np.sin(np.radians(4))
    Py=P*np.cos(np.radians(4))
    N=Py  
    for i in range(t.size-1):
        Fcic = Potencia/vx[i] 
        FRes = -(Cres/2)*area*Par*vx[i]**2 
        FRol = u*m*g          #Força de resistencia ao rolamento Frol= u*N=u*m*g
        F = Fcic + FRes - FRol - Px
        ax[i] = F/m  
        vx[i+1] = vx[i] + ax[i]*dt
        x[i+1] = x[i] + vx[i]*dt
        
        if(x[i] == 1500): #Quando x == 1500m
            tmed= t[np.where(x == x[i])]
            print(t[np.where(x == x[i])])
            break
        
        elif(x[i] > 1500): #Vai buscar o primeiro valor acima de 1500m pega nele e faz media com o anterior
            t1 = t[np.where(x == x[i])]
            t2 = t[np.where(x == x[i-1])]
            tmed = (t1+t2)/2
            print(tmed)
            break
    plt.plot(t,x, label="x")
    plt.show()
    return tmed


tempo1500m = t1500m()
print("Tempo que demora a percorrer 1500m:",tempo1500m)



def t500m():
    tmed = 0
    
    Px=P*np.sin(np.radians(1))
    Py=P*np.cos(np.radians(1))
    N=Py  
    for i in range(t.size-1):
        Fcic = Potencia/vx[i] 
        FRes = -(Cres/2)*area*Par*vx[i]**2 
        FRol = u*m*g      #Força de resistencia ao rolamento Frol= u*N=u*m*g
        F = Fcic + FRes - FRol + Px
        ax[i] = F/m  
        vx[i+1] = vx[i] + ax[i]*dt
        x[i+1] = x[i] + vx[i]*dt

        if(x[i] == 2000): #Quando x == 1500m
            print(t[np.where(x == x[i])])
            break;
        elif(x[i] > 2000): #Vai buscar o primeiro valor acima de 1500m
                                    ## pega nele e faz media com o anterior
            t1 = t[np.where(x == x[i])]
            t2 = t[np.where(x == x[i-1])]
            tmed = (t1+t2)/2
            print(tmed)
            break;
    plt.plot(t,x, label="x")
    plt.show()
    return tmed

tempo500m = t500m()
print("Tempo que demora a percorrer 500m:",tempo500m)

tempototal = tempo1500m + tempo500m
print("Tempo total:",tempototal)







 

