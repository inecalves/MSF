import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

t = np.linspace(0, 4, 100)
g=9.8
vt=6.8

yt= ((vt**2)/g) * np.log(np.cosh(g*t/vt))

plt.plot(t,yt)
plt.show()