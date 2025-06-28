import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
#sympy.diff(y,x) derivada de y em função de x

t,yt,v_funçao_t,a_funçao_t = sy.symbols('t, yt, v_funçao_t, a_funçao_t')

g = 9.80
velocidade_terminal = 6.80

yt = ((velocidade_terminal**2)/g) * sy.log(sy.cosh(g*t/velocidade_terminal))
vt = sy.diff(yt,t)
at = sy.diff(vt,t)

yt_plot = sy.lambdify(t,yt,"numpy")
vt_plot = sy.lambdify(t,vt,"numpy")
at_plot = sy.lambdify(t,at,"numpy")


tempo = np.linspace(0, 4, 100)
plt.plot(tempo,yt_plot(tempo))
plt.plot(tempo,vt_plot(tempo))
plt.plot(tempo,at_plot(tempo))
plt.show()