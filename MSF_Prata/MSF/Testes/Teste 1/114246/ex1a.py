import numpy as np
import matplotlib.pyplot as plt

t = np.array([0,48,96,144,192,240,288,336,384]) #eixo x
atividade = np.array([10.03,7.06,4.88,3.38,2.26,1.66,1.14,0.79,0.58]) #eixo y

x = t
y = atividade
npontos = len(x)

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

print("declive m = ", m, "+/-", errom) #m=-0.0229 +/- 0.0034
print("erro associado ao declive = ",errom)
print("ordenada na origem b = ", b, "+/-",errob) #b=7.9184 +/- 0.7846
print("erro associado à ordenada na origem = ",errob)
print("coeficiente de determinação r**2 = ", r2) #r**2= 0,8635

equacao=m*x+b
plt.plot(x, equacao, label="Reta de regressão linear") # reta
plt.scatter(x, y, marker='o', color='m',label="Pontos") # pontos
plt.xlabel("t (horas)")
plt.ylabel("atividade (mBq)")
plt.title("Gráfico da atividade em função do tempo")
plt.legend()
plt.show()

#O coeficiente de determinação r**2 é de 0,8635
#A relação não é linear, pois o coeficiente não é muito próximo de 1, caso fosse estaríamos perante uma relação linear
