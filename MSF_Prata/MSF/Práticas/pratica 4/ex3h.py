# Queda sem resistência do ar
# Integração numérica de dx/dt = vx, pelo Método de Euler
import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

#parámetros
dt=0.01/100 # passo de tempo intervalo entre cada área calculada
t0=0
tf=3.0
y0=0
vy0=0
g=9.80

#inicialização
n=int((tf-t0)/dt+0.1) # +0.1 para garantir não arredondar para baixo
t=np.zeros(n+1) # n+1 elementos; último índice n
y=np.zeros(n+1)
vy=np.zeros(n+1)
ay=np.zeros(n+1)
desvio=np.zeros(n+1)
dt_listado = np.zeros(n+1)


vy[0]=vy0
t[0]=t0
y[0]=y0
dt_listado[0]=dt
yteorico=9.8*2 #yt=at**2 

# Método de Euler (n+1 elementos)
for i in range(n):
    ay[i] = g # queda livre 
    y[i+1]=y[i]+vy[i]*dt
    vy[i+1]=vy[i] + ay[i]*dt # atualizar velocidade sabendo aceleração
    t[i+1]=t[i]+dt
    dt_listado[i+1] = dt_listado[i] + dt
    desvio[i]=abs(yteorico-y[i])

plt.plot(dt_listado, desvio)
plt.show()