import numpy as np
import matplotlib.pyplot as plt

#N = int(input('Número de medições: '))

xs = [222.0,207.7,194,171.5,153,133,113,92]
ys=[2.3,2.2,2,1.8,1.6,1.4,1.2,1]
N = len(xs)
x = np.array(xs)
somamulti = 0
xquadrado = 0
yquadrado = 0

for i in range (N):
    somamulti+= xs[i]*ys[i]
    xquadrado += xs[i]**2
    yquadrado += ys[i]**2

denominador = 0
m = N * somamulti
denominador += xquadrado * N

denominador -= sum(xs)**2

m = m - ( sum(xs) * sum(ys))

m = m / denominador

b = (xquadrado*sum(ys) - sum(xs)*somamulti)/denominador

r2 = ((N*somamulti - ( sum(xs) * sum(ys)))**2)/((N*xquadrado - sum(xs)**2)*(N*yquadrado - sum(ys)**2))

print ('declive (m) = ',m)
print('ordenada na origem (b) = ',b)
print('coeficiente de determinação (r2) = ',r2)










