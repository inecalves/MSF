import numpy as np
import matplotlib.pyplot as plt

xi = 0
xf = 2
dx = np.array([0.2,0.1,0.02,0.002])
logD = np.log(dx)

def regLin(x,y):
    #calcula a regressão linear de uma função
    x2=x**2
    y2=y**2
    xy=x*y
    n=x.size

    sx=x.sum()
    sy=y.sum()
    sxy=xy.sum()
    sx2=x2.sum()
    sy2=y2.sum()

    m=(n*sxy-sx*sy)/(n*sx2-(sx**2))
    b=(sx2*sy-sx*sxy)/(n*sx2-(sx**2))
    
    r2n=n*sxy-sx*sy
    r2d1=n*sx2-(sx**2)
    r2d2=n*sy2-(sy**2)
    r2=(r2n**2) / (r2d1*r2d2)
    
    varM=abs(m)*np.sqrt( ((1/r2)-1)/(n-2) )
    varB = varM*np.sqrt(sx2/n)
    return m,b,r2,varM,varB

def f(x):
    f = (x**3)/4
    return f

def aproxTrap(f,n,dx):
    return dx*(0.5*(f[0]+f[n])+np.sum(f[1:n]))

integral = np.empty(len(dx))
erros = np.empty(len(dx))

logE = np.log(erros)

for i in range(len(dx)):
    n = int((xf-xi)/dx[i])
    x = np.linspace(xi,xf,n+1)

    value = aproxTrap(f(x),n,dx[i])
    erro = abs(1-value)

    integral[i] = value
    erros[i] = erro

reg = regLin(logD,logE)
m = reg[0]

print("Declive:", m)

plt.xlabel("log(dx)")
plt.ylabel("log(erro)")
plt.plot(logD, logE, "o")
plt.show()