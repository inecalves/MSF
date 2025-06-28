import matplotlib.pyplot as plt
import numpy as np

xeq = 1.5
dt = 0.01
k = 1

x=np.arange(-5,5+dt,dt)

Ep = 0.5*k*(x**2-xeq**2)**2

plt.ylim([0,10])
plt.xlabel("x (m)")
plt.ylabel("Ep (J)")
plt.plot(x,Ep)
plt.plot([-4,4],[1,1])
plt.show()