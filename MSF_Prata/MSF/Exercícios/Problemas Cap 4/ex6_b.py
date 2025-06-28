import numpy as np
import matplotlib.pyplot as plt

k = 1
m = 1
v0 = 0
x0 = 4
w = np.sqrt(k/m)

ti = 0
tf = 20
dt = 0.001

t = np.arange(0,50,dt)

x=np.zeros(t.size)
v=np.zeros(t.size)
a=np.zeros(t.size)
x[0]=x0
v[0]=v0

for i in range(0, t.size-1):
    a[i]=-k/m*x[i]
    v[i+1]=v[i]+a[i]*dt
    x[i+1]=x[i]+v[i+1]*dt


v_analitico = -4*w*np.sin(w*t)

plt.xlabel("t (s)")
plt.ylabel("v (m/s)")

plt.plot(t,v,label="Euler",color="red")
plt.plot(t,v_analitico,label="Analítico",color="blue")

plt.show()