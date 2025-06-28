import matplotlib.pyplot as plt
import numpy as np


dt = 0.001

t = np.arange(0, 20+dt,dt)
k = 1
m = 1
omega = np.sqrt(k/m)
EM = np.zeros(t.size)
Ep = 0.75
xeq = 1.5
v = np.zeros(t.size)
x = np.zeros(t.size)

f = np.zeros(t.size)
EP = np.zeros(t.size)
v[0] = 0
x[0] = np.sqrt(xeq**2+np.sqrt(2*Ep/k))

for i in range(t.size-1):
    f[i] = -2*k*(x[i]**2-xeq**2)*x[i]
    a = f[i]/m
    v[i+1] = v[i] + a*dt
    x[i+1] = x[i] + v[i+1]*dt

plt.plot(t,x)

ind1 = np.where(t == 2.7)
ind1 = ind1[0][0]

ind2 = np.where(t == 5.0)
ind2 = ind2[0][0]

ind3 = np.where(t == 7.2)
ind3 = ind3[0][0]

plt.plot([t[ind1], t[ind1]],[1,2])
plt.plot([t[ind2], t[ind2]],[1,2])
plt.plot([t[ind3], t[ind3]],[1,2])

intervalo1 = x[ind1:ind2]
intervalo2 = x[ind2:ind3]

pontomax1, = np.where(x == np.max(intervalo1)) #usado 2 valores para comparar se nao ha nenhumme erro
pontomax2, = np.where(x == np.max(intervalo2))

pontomin1, = np.where(x == np.min(intervalo1))  #usado 2 valores para comparar se nao ha nenhumme erro
pontomin2, = np.where(x == np.min(intervalo2))

print(pontomax1[0],pontomax2[0])

periodo = t[pontomax2[0]] - t[pontomax1[0]]

print("Ponto alto", x[pontomax1[0]])
print("Ponto Baixo", x[pontomin1[0]])
print("Amplitude", x[pontomax1[0]] - x[pontomin1[0]])

print("Periodo", periodo)
print("Frequencia", (1/periodo))

plt.show()