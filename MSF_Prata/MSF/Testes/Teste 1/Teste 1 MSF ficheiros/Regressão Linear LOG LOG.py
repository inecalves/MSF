import numpy as np
import matplotlib.pyplot as plt

#alterar valores da lista e nome das variáveis
L = np.array([])
X = np.array([])
x = L
y = X
npontos = x.size

x = np.log(x) # transformar em log(x) e log(y)
y = np.log(y) #Gráfico LOG-LOG

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

print("declive m = ", m, "+/-", errom)
print("erro associado ao declive = ",errom)
print("ordenada na origem b = ", b, "+/-",errob)
print("erro associado à ordenada na origem = ",errob)
print("coeficiente de determinação r**2 = ", r2)

# mostrar o gráfico com os pontos e a reta da regressão linear
equacao=m*x+b
plt.plot(x, equacao,label="Reta de regressao linear") # reta
plt.scatter(x, y, marker='o', color='m',label="Pontos") # pontos
plt.xlabel("")
plt.ylabel("")
plt.legend()
plt.show()

