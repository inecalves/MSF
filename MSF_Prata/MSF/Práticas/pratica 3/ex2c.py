import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

g=9.8
vt=6.8

t,yt=sy.symbols('t,yt') 

yt= ((vt**2)/g) * sy.log(sy.cosh(g*t/vt)) 
print(yt)

ytplot = sy.lambdify(t,yt,"numpy") 
temp = np.linspace(0, 4, 100) 
vt=sy.symbols('vt')
vt=sy.diff(yt,t)
vtplot=sy.lambdify(t,vt,"numpy") 

a=sy.symbols('a')
a=sy.diff(vt,t)
aplot=sy.lambdify(t,a,"numpy")

plt.plot(temp,aplot(temp))
plt.xlabel("Tempo (s)")
plt.ylabel("Aceleração (m/s**2)")

print("A aceleração instantânea em função do tempo é dada pela expressão ",aplot)
plt.show()
