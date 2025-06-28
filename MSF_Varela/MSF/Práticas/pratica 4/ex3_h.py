import numpy as np
import matplotlib.pyplot as plt
import math

dt=0.01/100     #intervalo entre cada área calculada
t0=0
tf=3.0
y0=0
vy0=0
g=9.80
segundos = 2
#inicialização
n=int((tf-t0)/dt+0.1) # +0.1 para garantir não arredondar para baixo
t=np.zeros(n+1) # n+1 elementos; último índice n
y=np.zeros(n+1)
vy=np.zeros(n+1)
ay=np.zeros(n+1)
desvio = np.zeros(n+1)
dt_listado = np.zeros(n+1)
vy[0]=vy0
dt_listado[0]=dt
t[0]=t0
#x[0]=x0
# Método de Euler (n+1 elementos)
for i in range(n):
    ay[i] = g   # queda livre 
                # (em geral pode ser qualquer função de x[i] e vx[i])
    y[i+1]=y[i]+vy[i]*dt
    vy[i+1]=vy[i] + ay[i]*dt # atualizar velocidade sabendo aceleração
    t[i+1]=t[i]+dt
    desvio[i] = abs(19.6 - y[i])
    dt_listado[i+1] = dt_listado[i] + 0.0001 

indice = int(segundos / dt)

#19.502000000000027 m - passo 0.01
#19.590200000000138 m - passo 0.001
#19.599020000002014 m - passo 0.0001

print((y[indice]),"m")
plt.plot(dt_listado, desvio)
plt.legend()
plt.show()