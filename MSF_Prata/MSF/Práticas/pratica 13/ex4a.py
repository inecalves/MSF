
import matplotlib.pyplot as plt
import numpy as np

#Oscilador quártico forçado e amortecido

dt = 0.001
m = 1
xeq = 0 #posição de equilíbrio
g = 9.8

k = 1
b = 0.05
a = 0.002
F0 = 7.5 #Força externa
VForc = 1

t = np.arange(0,200+dt,dt)

x = np.zeros(t.size)
v = np.zeros(t.size)

x[0] = 3 #posição inicial
v[0] = 0 #velocidade inicial


for i in range(t.size-1):
    Fx = -k*x[i]*(1+2*a*(x[i]**2))
        
    Fforc = F0*np.cos(VForc*t[i])
    
    Famort = -b*v[i]
    
    ax = (Fx+Fforc+Famort)/m
    
    v[i+1] = v[i] + ax*dt
    x[i+1] = x[i] + v[i+1]*dt
    
plt.plot(t,x)
plt.grid()
plt.show()