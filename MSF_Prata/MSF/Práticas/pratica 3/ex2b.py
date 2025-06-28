import numpy as np
import matplotlib.pyplot as plt
import sympy as sy #biblioteca que permite fazer cálculos simbólicos em python

g=9.8
vt=6.8

t,yt=sy.symbols('t,yt') #definir variáveis simbólicos

yt= ((vt**2)/g) * sy.log(sy.cosh(g*t/vt)) #definir uma expressão
print(yt)

ytplot = sy.lambdify(t,yt,"numpy") #transformar uma expressão sympy numa lambda function numpy
temp = np.linspace(0, 4, 100) #intervalo de 0 a 4s com 100 pontos no eixo do x

vt=sy.symbols('vt')
vt=sy.diff(yt,t)
vtplot=sy.lambdify(t,vt,"numpy") #vtplot é uma função de t que pode ser chamada vt(t), velocidade em funçao do tempo
plt.plot(temp,vtplot(temp))

print("A velocidade instantânea em função do tempo é dada pela expressão ",vt)
plt.show()



