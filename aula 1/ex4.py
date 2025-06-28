import numpy as np
import matplotlib.pyplot as plt

N = np.logspace(1,4, num=50, dtype=int)

Ymedia = []
Yerro = []

for i in N:
    X = np.random.normal(10.0,0.5,size=i)
    Xmedia = np.mean(X)
    Xerro = 1/np.sqrt(i)

    Ymedia.append(Xmedia)
    Yerro.append(Xerro)

fig, ax = plt.subplots()  #cria o lugar para gráfico
ax.plot(N, Ymedia)  #preenche o eixo do x, e o eixo do y, respetivamente

ax.plot(N, 10.0-np.array(Yerro), "r--")
ax.plot(N, 10.0+np.array(Yerro), "r--")

plt.xscale("log")  #escala logarítimca
plt.show()  #mostra o gráfico


