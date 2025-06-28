import numpy as np
import matplotlib.pyplot as plt

'''
Use o seguinte código para gerar 10 valores de X com media esperada 4.5 e devio padrão 0.5,
e calcular a sua media e incerteza.
'''

N=10

X = np.random.normal(4.5,0.5,size=N)
Xmedia = np.mean(X)
Xerro = np.std(X)/np.sqrt(N)

print("Xmedia =", Xmedia)
print("Xerro =", Xerro)

'''
Adapte o código para gerar outro conjunto de valores, Y, com media 10.0 e devio padrão 1.0
'''

Y = np.random.normal(10.0,1.0,size=N)
Ymedia = np.mean(Y)
Yerro = np.std(Y)/np.sqrt(N)

print("Ymedia =", Ymedia)
print("Yerro =", Yerro)

'''
Criar um novo conjunto de valores, Z, que seja a soma de cada par de valores X e Y
'''

Z = X + Y  # soma de cada par de valores
Zmedia = np.mean(Z)  # media dos valores de Z

Zerro_i = np.std(Z)/np.sqrt(N) # incerteza diretamente do desvio padrão dos valores de Z
Zerro_ii = Xerro + Yerro  # incertezas de X e Y para estimar a incerteza de Z 

print("Zmedia =", Zmedia)
print("Zerro_i =", Zerro_i)
print("Zerro_ii =", Zerro_ii)

W = X*Y  # produto de cada par de valores
Wmedia = np.mean(W)

'''
Estimar a incerteza de W das mesmas duas maneiras (agora em ii, deve usar as incertezas relativas)
'''
Werro_i = np.std(W)/np.sqrt(N)
Werro_ii = ((Xerro/Xmedia) + (Yerro/Ymedia))*Wmedia

print("Wmedia =", Wmedia)
print("Werro_i =", Werro_i)
print("Werro_ii =", Werro_ii)


