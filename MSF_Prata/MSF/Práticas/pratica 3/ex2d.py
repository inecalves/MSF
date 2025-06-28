import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

g=9.8
vt=6.8

t,yt=sy.symbols('t,yt') 
yt= ((vt**2)/g) * sy.log(sy.cosh(g*t/vt)) 

vy=sy.diff(yt,t)
ay=g-(g/(vt)**2)*vy*abs(vy)

ayplot = sy.lambdify(t,ay,"numpy") 
temp = np.linspace(0, 4, 100) 
plt.plot(temp,ayplot(temp))

plt.show()

#como o gráfico de ay é igual ao de aplot da alínea anterior as acelerações são iguais