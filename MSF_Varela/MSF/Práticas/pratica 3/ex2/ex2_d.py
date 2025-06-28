import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

t,yt,vt,at = sy.symbols('t,yt,vt,at')

g = 9.80
vterm = 6.80

yt = ((vterm**2)/g) * sy.log(sy.cosh(g*t/vterm))
vt = sy.diff(yt,t)

at = g - (g/vterm**2)*vt*abs(vt)
at_plot = sy.lambdify(t,at,"numpy")

plt.xlabel("Tempo")
plt.ylabel("Aceleração")

tempo = np.linspace(0, 4, 100)
plt.plot(tempo,at_plot(tempo))
plt.show()