import numpy as np
import matplotlib.pyplot as plt

atividade = np.array([9.676 , 6.355, 4.261, 2.729, 1.862, 1.184, 0.7680, 0.4883, 0.3461, 0.2119])
tempo = np.arange(0, 50, 5)

x = atividade
y = tempo
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

errom= np.abs(m)*np.sqrt(((1/r2)-1)/(n-2)) #erro associado ao declive
errob = errom*np.sqrt(sxx/n) #erro associado à ordenada na origem

print("declive m = ", m, "+/-", errom)
print("erro associado ao declive = ",errom)
print("ordenada na origem b = ", b, "+/-",errob)
print("erro associado à ordenada na origem = ",errob)
print("coeficiente de determinação r**2 = ", r2)

# mostrar o gráfico com os pontos e a reta da regressão linear
equacao=m*x+b
plt.plot(x, equacao, label="Reta de regressao linear") # reta
plt.scatter(x, y, marker='o', color='m', label="Pontos") # pontos
plt.xlabel("Tempo (dias)")
plt.ylabel("Atividade (mCi)")
plt.legend()
plt.show()

#a) como se pode observar, a relação entre o tempo e a atividade
#não é linear (também é perceptivel através do r2 ser == 0.80)