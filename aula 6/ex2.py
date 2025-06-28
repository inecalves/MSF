import numpy as np
import matplotlib.pyplot as plt

# Variáveis
t0 = 0.0 #tempo inicial
tf = 2.0 #tempo final
dt = 0.01 #passo
x0 = 1.0
v0 = 2*np.pi

G = 4*(np.pi**2)
m = 3.003*10**-6

t = np.arange(t0, tf, dt)

x = np.empty(np.size(t))
y = np.empty(np.size(t))
vx = np.empty(np.size(t))
vy = np.empty(np.size(t))
ax = np.empty(np.size(t))
ay = np.empty(np.size(t))

x[0] = x0
y[0] = 0
vx[0] = 0
vy[0] = v0

# Método de Euler-Cromer
for i in range(np.size(t) - 1):
    t[i+1] = t[i] + dt 
    r = np.sqrt(x[i]**2+y[i]**2)
    ax[i] = -G/r**3*x[i]
    ay[i] = -G/r**3*y[i]
    vx[i+1] = vx[i] + ax[i]*dt 
    vy[i+1] = vy[i] + ay[i]*dt
    x[i+1] = x[i] + vx[i+1]*dt
    y[i+1] = y[i] + vy[i+1]*dt  

plt.plot(x, y, 'b-')
plt.xlabel("x(t) [UA]")
plt.ylabel("y(t) [UA]")
plt.show()