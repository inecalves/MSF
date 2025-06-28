import numpy as np
import matplotlib.pyplot as plt

# a), b), c) --> no caderno
'''
d) Resolva a alínea a), conseiderando a resistência do ar,
    usando o método de Euler. A velocidade terminal da bola 
    no ar é de 100km/h.
'''
t0 = 0.0
tf = 3.0
y0 = 0.0
v0 = 10.0 #(m/s)
vt = 27.7 #(m/s)
dt = 0.0001 #passo (s) --> quanto menor = melhor

g = 9.8
D = g/vt ** 2

t = np.arange(t0, tf, dt)
y = np.empty(np.size(t))
v = np.empty(np.size(t))
a = np.empty(np.size(t))

y[0] = y0
v[0] = v0

for i in range(np.size(t) - 1):
    a[i] = -g - D * v[i] * np.abs(v[i])
    v[i + 1] = v[i] + a[i] * dt
    y[i + 1] = y[i] + v[i] * dt

plt.plot(t, y, 'b-')
plt.plot(t, y0 + v0*t - 0.5*g*t**2, 'r-')
plt.xlabel("t [s]")
plt.ylabel("y [m]")
plt.show()

'''
e) Repita as alíneas b) e c) nas condições da alínea d).
Deve encontrar uma maneira numérica de estimar os instantes
da altura máxima e do retorno à posição inicial.
'''
imax = np.argmax(y)  #maior y - maior altura 'registada'
tmax = t[imax]  #instante da altura máxima
print("Instante da Altura máxima = ", tmax, "s")
print("Altura máxima, ymax = ", y[imax], "m")
#---------------------
izero = np.size(y) - np.size(y[y<0])  #posição em que volta a ser 0
tzero = t[izero]  #tempo que demora
print("Tempo que demora para voltar a passar na origem = ", tzero, "s")

