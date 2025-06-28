'''
Maria Inês Gonçalves
124754
'''

import numpy as np
import matplotlib.pyplot as plt

t0 = 0.0 
tf = 5.5 # tempo s
vi = 0.0 # velocidade inicial do corpo m/s
dt = 0.01 # n passos
g = -9.8 # aceleração gravítica
C = 2.5 # constante C = 2.5 kg/s
m = 50*10**(-3) # massa da bola em kg: 50g = 0.050 kg

t = np.arange(t0, tf, dt)
y = np.empty(np.size(t))
v = np.empty(np.size(t))
a = np.empty(np.size(t))

v[0] = 0
y[0] = 0.30 #posição inicial: 0.30 m

#y1 = 0.30 + 0*T + 0.5*a*T**2 #Valor Teorico

floor = np.zeros(t.size)

#Metodo de Euler
for i in range(np.size(t)-1):
    a[i] = g - C*v[i]/m
    v[i+1] = v[i] + a[i]*dt # velocidade no instante
    y[i+1] = y[i] + v[i] * dt # posiçao no instante

'''
GRÁFICO POSIÇÃO-TEMPO
'''
plt.plot(t,y, 'b-')
plt.xlabel("Tempo, t (s)")
plt.ylabel("Posição, y (m)")
plt.show()

'''
GRÁFICO VELOCIDADE-TEMPO
'''
plt.plot(t,v, 'b-')
plt.xlabel("Tempo, t (s)")
plt.ylabel("Velocidade, v (m/s)")
plt.show()


#b) --> não consegui fazer