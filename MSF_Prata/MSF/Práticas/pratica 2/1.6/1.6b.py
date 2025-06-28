import numpy as np
import matplotlib.pyplot as plt

dist = np.array([0.0,0.735,1.363,1.739,2.805,3.814,4.458,4.955,5.666,6.329])
tempo =np.array([0,1,2,3,4,5,6,7,8,9])


x = tempo
y = dist
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
m = (n*sxy - sx*sy)/(n*sxx - sx**2) #declive
b = (sxx*sy - sx*sxy)/(n*sxx - sx**2) #ordenada da origem
r2 = (n*sxy - sx*sy)**2/((n*sxx - sx**2)*(n*syy - sy**2))

errom= abs(m)*np.sqrt((1/r2**2-1)/(n-2)) #erro associado ao declive
errob = errom*np.sqrt(sxx/n) #erro associado à ordenada na origem

print("declive m = ", m, "+/-", errom)
print("erro associado ao declive = ",errom)
print("ordenada na origem b = ", b, "+/-",errob)
print("erro associado à ordenada na origem = ",errob)
print("coeficiente de determinação r^2 = ", r2)


# declive m =  0.7188121212121212
# ordenada na origem b =  -0.048254545454544835
# coeficiente de determinação r^2 =  0.9938477355877053