import numpy as np
import matplotlib.pyplot as plt

'''
Uma bola de ténis é largada de uma altura elevada. Considere a queda livre, sem resistência do ar.
Considere que a aceleração vertical é g = 9.80 m/s2
'''

# a)Construa um programa que determine a posição do objeto, 
#   usando o método de Euler, no intervalo de tempo [0, 4]s .
t0 = 0.0 #tempo inicial
tf = 4.0 #tempo final
x0 = 0.0 #posição inicial
v0 = 0.0 #velocidade inicial
dt = 0.1 #passo

g = 9.8

t = np.arange(t0, tf, dt)
v = np.empty(np.size(t))
x = np.empty(np.size(t))

v[0] = v0
x[0] = x0
for i in range(np.size(t) - 1):  #método de euler
    v[i + 1] = v[i] + g*dt
    x[i + 1] = x[i] + v[i]*dt

# b) Qual a velocidade no instante 3s?
#t3 = v*dt --> v = t3/dt
i3 = int(3.0/dt)
print("v[3] = ", v[i3], "m/s")

# c) Repita as alíneas anteriores, com um passo de tempo 10
#    vezes menor.
dt = 0.01 

t = np.arange(t0, tf, dt)
v = np.empty(np.size(t))
x = np.empty(np.size(t))

v[0] = v0
x[0] = x0
for i in range(np.size(t) - 1):
    v[i + 1] = v[i] + g*dt
    x[i + 1] = x[i] + v[i]*dt

i3 = int(3.0/dt)
print("v[3] = ", v[i3], "m/s")

# d)
#não muda, independentemente do passo

# e) Qual a posição em 3s, se o objeto partiu da posição 0m?
dt = 0.1

t = np.arange(t0, tf, dt)
v = np.empty(np.size(t))
x = np.empty(np.size(t))

v[0] = v0
x[0] = x0
for i in range(np.size(t) - 1):
    v[i + 1] = v[i] + g*dt
    x[i + 1] = x[i] + v[i]*dt

i3 = int(3.0/dt)
print("x[3] = ", x[i3], "m")

# f) Repita a alínea anterior, com um passo 10 vezes menor
dt = 0.01

t = np.arange(t0, tf, dt)
v = np.empty(np.size(t))
x = np.empty(np.size(t))

v[0] = v0
x[0] = x0
for i in range(np.size(t) - 1):
    v[i + 1] = v[i] + g*dt
    x[i + 1]  = x[i] + v[i]*dt

i3 = int(3.0 / dt)
print("x[3] = ", x[i3], "m")

# g)
#depende do passo - aproxima-se do valor real à medida que diminuimos o passo

# h) Calule novamente a posição no instante 2, para vários valores. Faça o gráfico
# do desvio do valor aproximado com o valor exato em função do passo. Como varia
# o erro com o passo?

dt = 0.1

t = np.arange(t0, tf, dt) 
v = np.empty(np.size(t)) 
x = np.empty(np.size(t)) 

v[0] = v0
x[0] = x0
for i in range(np.size(t) - 1):
 v[i + 1] = v[i] + g*dt
 x[i + 1] = x[i] + v[i]*dt

i2 = int(2.0 / dt) 
print("x[2s] com passo 0.1 = ", x[i2], "m")
print("desvio de x[2s] = ", np.abs(x[i2]-19.6), "m")

#------------------------------------------
dt = 0.01

t = np.arange(t0, tf, dt) 
v = np.empty(np.size(t)) 
x = np.empty(np.size(t)) 

v[0] = v0
x[0] = x0
for i in range(np.size(t) - 1):
 v[i + 1] = v[i] + g*dt
 x[i + 1] = x[i] + v[i]*dt

i2 = int(2.0 / dt) 
print("x[2s] com passo 0.01 = ", x[i2], "m")
print("desvio de x[2s] = ", np.abs(x[i2]-19.6), "m")

#------------------------------------------
dt = 0.001

t = np.arange(t0, tf, dt) 
v = np.empty(np.size(t)) 
x = np.empty(np.size(t)) 

v[0] = v0
x[0] = x0
for i in range(np.size(t) - 1):
 v[i + 1] = v[i] + g*dt
 x[i + 1] = x[i] + v[i]*dt

i2 = int(2.0 / dt) 
print("x[2s] com passo 0.001 = ", x[i2], "m")
print("desvio de x[2s] = ", np.abs(x[i2]-19.6), "m")

#-------------------------------------------

dt = 0.0001

t = np.arange(t0, tf, dt) 
v = np.empty(np.size(t)) 
x = np.empty(np.size(t)) 

v[0] = v0
x[0] = x0
for i in range(np.size(t) - 1):
 v[i + 1] = v[i] + g*dt
 x[i + 1] = x[i] + v[i]*dt

i2 = int(2.0 / dt) 
print("x[2s] com passo 0.0001 = ", x[i2], "m")
print("desvio de x[2s] = ", np.abs(x[i2]-19.6), "m")


passos = np.array([0.1, 0.01, 0.001, 0.0001]) #vários valores de passos utilizados
desvios = np.array([0.98, 0.098, 0.0098, 0.00098]) #vários valores dos desvios

plt.loglog(passos, desvios, 'o-')
plt.xlabel("Passo [s]")
plt.ylabel("Desvio da posição [m]")
plt.show()


