# Queda sem resistência do ar
# Integração numérica de dx/dt = vx, pelo Método de Euler
import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

#parámetros
dt=0.01/10 # passo de tempo intervalo entre cada área calculada
t0=0
tf=3.0
y0=0
vy0=10
g=9.80
vterm=100/3.6
D=9.8/(vterm)**2



#inicialização
n=int((tf-t0)/dt+0.1) # +0.1 para garantir não arredondar para baixo
t=np.zeros(n+1) # n+1 elementos; último índice n
y=np.zeros(n+1)
vy=np.zeros(n+1)
ay=np.zeros(n+1)
desvio=np.zeros(n+1)

vy[0]=vy0
t[0]=t0
y[0]=y0

# b) 
tm=vy0/g
ym=vy0*tm-0.5*g*tm**2
# c)
tsolo=vy0*2/g
print('tm, ym, tsolo = ',tm,ym,tsolo)

# Método de Euler (n+1 elementos)
for i in range(n):
    ay[i] = g - D*vy[i]*abs(vy[i]) # considerando resistência do ar
    y[i+1]=y[i]+vy[i]*dt
    vy[i+1]=vy[i] + ay[i]*dt # atualizar velocidade sabendo aceleração
    t[i+1]=t[i]+dt

plt.plot(t, ay, "y", label="Aceleração")
plt.plot(t, vy, "g", label="Velocidade")
plt.plot(t, y, "b", label="Posição")
plt.xlabel("Tempo (segundos)")
plt.ylabel("Distância (m)")
plt.legend(loc="upper left")
plt.title("Movimento com resistencia")
plt.show()

idx=y.argmax()
ymax=y[idx]
tmax=t[idx]