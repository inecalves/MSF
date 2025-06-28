import numpy as np
import matplotlib.pyplot as plt

'''
Regressão linear pelo método dos mínimos quadráticos
'''

def minimos_quadrados(x, y):
    N = x.size

    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x ** 2)
    sum_y2 = np.sum(y ** 2)
    sum_xy = np.sum(x * y)

    # Declive
    m = (N * sum_xy - sum_x * sum_y) / (N * sum_x2 - sum_x ** 2)
    # Ordenada na origem
    b = (sum_x2 * sum_y - sum_x * sum_xy) / (N * sum_x2 - sum_x ** 2)
    # Coefiecientes de correlação
    r2 = (N * sum_xy - sum_x * sum_y) ** 2 / ((N * sum_x2 - sum_x ** 2) * (N * sum_y2 - sum_y ** 2))
    # Incerteza do declive
    dm = np.absolute(m) * np.sqrt((1 / r2 - 1) / (N - 2))
    # Incerteza da ordenada na origem
    db = dm * np.sqrt((sum_x2) / N)

    return m, b, r2, dm, db

# a)
# Dados da experiência
D = np.array([0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0]) # [Dias] -- eixo x
A = np.array([9.676, 6.355, 4.261, 2.729, 1.862, 1.184, 0.7680, 0.4883, 0.3461, 0.2119]) # [mCi] -- eixo y

# Fazer o gráfico
plt.scatter(D, A)
plt.xlabel("Dias, D")
plt.ylabel("Atividade Radioativa, A [mCi]")
plt.show()

# A relação é uma lei exponencial

# b)
plt.semilogy(D, A)
plt.xlabel("Dias, D")
plt.ylabel("ln Atividade Radioativa, A [mCi]")
plt.show()

# O logaritmo da atividade é linear com o tempo - lei exponencial

# c)
X_i = D
Y_i = np.log(A)

# Calcular melhor reta
m, b, r2, dm, db = minimos_quadrados(X_i, Y_i)

# Imprimir resultados
print("m = {0:.4f}".format(m))
print("b = {0:.2f} cm".format(b))
print("r² = {0:.4f}...".format(r2))
print("Δm = {0:.4f}".format(dm))
print("Δb = {0:.2f} cm".format(db))

# Gerar valores do tempo e espaço percorrido para representação da reta
x = np.linspace(0.0, 45.0, 2)
y = m * x + b

# Fazer gráfico
plt.scatter(X_i, Y_i)
plt.plot(x, y)
plt.xlabel("Dias, D")
plt.ylabel("ln Atividade Radioativa, A [mCi]")
plt.show()

print("semivida do isótopo = ", -np.log(2)/m)