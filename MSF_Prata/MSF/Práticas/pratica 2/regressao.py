import numpy as np
import matplotlib.pyplot as plt

#alterar valores da lista
L = np.array([222.0, 207.5, 194.0, 171.5, 153.0, 133.0, 113.0, 92.0])
X = np.array([2.3, 2.2, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0])

x = L
y = X
npontos = x.size

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

errom= abs(m)*np.sqrt((1/r2**2-1)/(n-2)) #erro associado ao declive
errob = errom*np.sqrt(sxx/n) #erro associado à ordenada na origem

print("declive m = ", m, "+/-", errom)
print("erro associado ao declive = ",errom)
print("ordenada na origem b = ", b, "+/-",errob)
print("erro associado à ordenada na origem = ",errob)
print("coeficiente de determinação r**2 = ", r2)

