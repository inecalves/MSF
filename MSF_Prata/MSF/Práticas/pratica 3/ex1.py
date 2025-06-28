#carro A v=v0=70km/h a=0                            x(t) = 70t
#carro Patrulha vo=0km/h a=2   v(t) = vo+at = 2t    x(t) = t**2

import numpy as np
import matplotlib.pyplot as plt

#a)
v=70/3.6
#np.linspace(min,max,n) n é o numero de pontos
t = np.linspace(0, 25, 100)

xA=v*t #carro A
xP=t**2 #carro de patrulha

plt.plot(t,xA)
plt.plot(t,xP)

plt.xlabel("Tempo (s)")
plt.ylabel("Distância (m)")

#Ponto de interseçao xA=xP   vt=t**2   v=t
tI=v
xI = tI**2 #ou v*v
plt.plot(tI,xI,'o')
print('t= ',tI) #tempo onde se encontram
print('x= ',xI) #posição em que se encontram
plt.show()
