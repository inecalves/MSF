import matplotlib.pyplot as plt
import numpy as np

vt = 100/3.6
g = -9.8

x0 = 0
y0 = 3

v0x = 30
v0y = 0 
dt = 0.0001


t1 = np.arange(0,100, dt)
y1 = np.zeros(t1.size)
x1 = np.zeros(t1.size)
vx1 = np.zeros(t1.size)
vy1 = np.zeros(t1.size)


x1[0] = x0
y1[0] = y0
vx1[0] = v0x
vy1[0] = v0y
D = -g/(vt**2)

for i in range(0, t1.size-1):
    v = np.sqrt(vx1[i]**2 + vy1[i]**2)
    ax = -D*vx1[i]*abs(v)
    ay = g-D*vy1[i]*abs(v)
    
    vx1[i+1] = vx1[i] + ax*dt# velocidade no instante
    vy1[i+1] = vy1[i] + ay*dt # velocidade no instante
    x1[i+1] = x1[i] + vx1[i] * dt # posiçao no instante
    y1[i+1] = y1[i] + vy1[i] * dt # posiçao no instante
    if y1[i+1] < 0:
        break

    if 12 < x1[i] < 18.4 and y1[i] > 1: #Verificar se é ponto ou não
        print("PONTO!")
        print(x1[i],y1[i])
        break


t1 = t1[:i+2]
x1 = x1[:i+2]
y1 = y1[:i+2]
vx1 = vx1[:i+2]
vy1 = vy1[:i+2]

plt.plot(x1,y1, label="Com Resistência do ar")
plt.xlabel("x(t) (m)")
plt.ylabel("y(t) (m)")

plt.legend()
plt.grid()

#ALCANCE 
print("Alcance, distância a que a bola cai no solo: " + str(x1[x1.argmax()])) 

plt.show()

