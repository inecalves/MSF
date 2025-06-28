
import numpy as np
import matplotlib.pyplot as plt

dt = 0.001  # passo temporal, intervalo entre cada área calculada
tf = 4.0  # instante final
t0 = 0  # instante inicial
n = int((tf - t0) / dt + 0.1)  # numero de passos, numero de areas "retangulos"
vterm= 20 #alterar valor da velocidade terminal
D=9.8/(vterm)**2

# iniciar os arrays com o tempo, a velocidade, a posição e aceleraçao
t = np.zeros(n + 1)
vy = np.zeros(n + 1)
y = np.zeros(n + 1)
ay= np.zeros(n + 1)

# condições iniciais
g = 9.8  # aceleração gravítica sem resistencia do ar
t[0] = 0  # instante inicial
vy[0] = 0  # velocidade inicial eixo y
y[0] = 0  # posição inicial eixo y

# Método de Euler
for i in range(n):
    ay[i] = g - D*vy[i]*abs(vy[i]) # considerando resistência do ar
    #ay[i]=g sem resistência do ar
    t[i + 1] = t[i] + dt  # alterar o instante
    vy[i + 1] = vy[i] + g * dt  # alterar a velocidade
    y[i + 1] = y[i] + vy[i] * dt  # alterar a posição

# print gráfico da posição em função do tempo
plt.plot(t, y, color='m')
plt.ylabel("Posição (m)")
plt.xlabel("Tempo (s)")
plt.show()
# print gráfico da velocidade em função do tempo
plt.plot(t, vy, color='m')
plt.ylabel("Velocidade (m/s)")
plt.xlabel("Tempo (s)")
plt.show()
# print gráfico da aceleraçao em função do tempo
plt.plot(t, ay, color='m')
plt.ylabel("Aceleração (m/s**2)")
plt.xlabel("Tempo (s)")
plt.show()

#ALTURA MAXIMA
idx=y.argmax()
ymax=y[idx]
tmax=t[idx]
print("A altura maxima foi de {} no instante{}".format(ymax,tmax))

#Verificar em que instantes o valor da posiçao é 0
idxs = np.where(np.isclose(y,0,atol=0.005))[0]
idx = idxs[1]
tRet = t[idx]
print("Volta á posição inicial no instante {} no instante".format(tRet))

