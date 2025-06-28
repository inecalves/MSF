import numpy as np
import matplotlib.pyplot as plt

valores = [0.00,0.735,1.363,1.739,2.805,3.814,4.458,4.955 ,5.666,6.329]

minutos = [0,1,2,3,4,5,6,7,8,9]

x = np.array(minutos)
y=np.array(valores)

xy = x*y
xx = x**2
yy = y**2

sx = x.sum()
sy = y.sum()
sxy = xy.sum()
sxx = xx.sum()
syy = yy.sum()

n = x.size
m = (n*sxy - sx*sy)/(n*sxx - sx**2)
b = (sxx*sy - sx*sxy)/(n*sxx - sx**2)
r2 = (n*sxy - sx*sy)**2/((n*sxx - sx**2)*(n*syy - sy**2))

print("declive m = ", m)
print("ordenada na origem b = ", b)
print("regressão linear r^2 = ", r2)