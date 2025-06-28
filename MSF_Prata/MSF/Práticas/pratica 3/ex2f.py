import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

t,yt,vt,at = sy.symbols('t,yt,vt,at')

g = 9.80
vterm = 6.80

yt = ((vterm**2)/g) * sy.log(sy.cosh(g*t/vterm))

t_com=(np.arccosh(10**(20 * g / vterm**2)))*vterm/g #tempo a chegar ao solo

vt = sy.diff(yt,t)
vt_plot = sy.lambdify(t,vt,"numpy")

at=sy.diff(vt,t)
at_plot = sy.lambdify(t,at,"numpy")

print("Velocidade:", vt_plot(t_com), "m/s.")
print("Aceleração:", at_plot(t_com), "m/s^2.")
