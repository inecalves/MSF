import numpy as np
import matplotlib.pyplot as plt

'''
Regressão linear pelo método dos mínimos quadráticos
'''

# a)
# Dados da experiência
T = np.array([200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1100.0]) # [K]
E = np.array([0.6950, 4.363, 15.53, 38.74, 75.08, 125.2, 257.9, 344.1, 557.4, 690.7]) # [J]

# Fazer o gráfico
plt.scatter(T, E)
plt.xlabel("Temperatura, T [K]")
plt.ylabel("Energia, E [J]")
plt.show()

# Não é linear

# b)
# Gráfico semilogy() - log-linear:
plt.semilogy(T, E)
plt.xlabel("Temperatura, T [K]")
plt.ylabel("Energia, E [J]")
plt.show()

# Gráfico loglog() - log-log
plt.loglog(T, E)
plt.xlabel("Temperatura, T [K]")
plt.ylabel("Energia, E [J]")
plt.show()

# c) uma lei de potência

# d)
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

X_i = np.log(T)
Y_i = np.log(E)

# Calcular melhor reta
m, b, r2, dm, db = minimos_quadrados(X_i, Y_i)

# Imprimir resultados
print("m = {0:.4f}".format(m))
print("b = {0:.2f} cm".format(b))
print("r² = {0:.4f}...".format(r2))
print("Δm = {0:.4f}".format(dm))
print("Δb = {0:.2f} cm".format(db))

# Definir dois pontos (x0, y0) e (x1, y1) para representar a melhor reta
x = np.array([5.25, 7.0])
y = m * x + b

# Fazer gráfico
plt.scatter(X_i, Y_i)
plt.plot(x, y)
plt.xlabel("X = ln(T)")
plt.ylabel("Y = ln(P)")
plt.show()
print("n = m = ", m)
print("c = exp(b) = ", np.exp(b))

# O valor de r2 é 0.9973...

# e)
# P = 4.0**(-10) * T**4.0



