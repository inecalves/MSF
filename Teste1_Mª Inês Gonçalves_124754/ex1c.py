'''
Maria Inês Gonçalves
124754
'''

import numpy as np
import matplotlib.pyplot as plt

'''
R:
Através dos gráficos anteriores, é possível conlcuir que se pode aplicar uma
relação como uma lei de potência aos dados, ou seja, y = c*x^n
'''

C = np.array([1.2, 4.2, 11, 20, 22, 37, 45]) #eixo x  --> comprimento do fémur (cm)
M = np.array([0.03, 0.54, 9.1, 38, 57, 230, 480]) #eixo y --> massa (kg)

x = np.log(C)
y = np.log(M)

npontos = len(C)

xy = x*y
xx = x**2
yy = y**2

sx = x.sum()
sy = y.sum()
sxy = xy.sum()
sxx = xx.sum()
syy = yy.sum()

n = npontos
m = (n*sxy - sx*sy)/(n*sxx - sx**2)
b = (sxx*sy - sx*sxy)/(n*sxx - sx**2)
r2 = (n*sxy - sx*sy)**2/((n*sxx - sx**2)*(n*syy - sy**2))

errom= np.abs(m)*np.sqrt(((1/r2)-1)/(n-2)) #erro associado ao declive
errob = errom*np.sqrt(sxx/n) #erro associado à ordenada na origem

c = np.exp(b)
n = m

plt.plot(x, c*x**n, label = "Reta com lei de potência")
plt.xlabel("Comprimento de Fêmur (cm)")
plt.ylabel("Massa (kg)")
plt.legend()
plt.show()