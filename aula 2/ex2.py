import numpy as np
import matplotlib.pyplot as plt

# a)
# Dados da experiência
L_i = np.array([222.0, 207.5, 194.0, 171.5 , 153.0, 133.0, 113.0, 92.0]) # [cm]
X_i = np.array([2.3, 2.2, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0]) # [cm]

# Fazer o gráfico
plt.scatter(L_i, X_i)
plt.xlabel("Distância da fonte de luz ao alvo, L [cm]")
plt.ylabel("Distância entre máximos luminosos consecutivos, X [cm]")
plt.show()

# b)
# Calcular as quantidades m, b, r2, mm, mb
def minimos_quadrados(x, y):
    N = x.size

    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x ** 2)
    sum_y2 = np.sum(y ** 2)
    sum_xy = np.sum(x * y)

    #Declive
    m = (N * sum_xy - sum_x * sum_y) / (N * sum_x2 - sum_x ** 2)
    #Ordenada na origem
    b = (sum_x2 * sum_y - sum_x * sum_xy) / (N * sum_x2 - sum_x ** 2)
    #Coefiecientes de correlação
    r2 = (N * sum_xy - sum_x * sum_y) ** 2 / ((N * sum_x2 - sum_x ** 2) * (N * sum_y2 - sum_y ** 2))
    #Erro do declive
    dm = np.absolute(m) * np.sqrt((1 / r2 - 1) / (N - 2))
    #Erro da ordenada na origem
    db = dm * np.sqrt((sum_x2) / N)

    return m, b, r2, dm, db

m, b, r2, dm, db = minimos_quadrados(L_i, X_i)

print("m = {0:.4f}".format(m))
print("b = {0:.2f} cm".format(b))
print("r² = {0:.4f}...".format(r2))
print("Δm = {0:.4f}".format(dm))
print("Δb = {0:.2f} cm".format(db))

# c) Representar a reta y = mx + b no gráfico
# Definir dois pontos (x0, y0) e (x1, y1) para representar melhor reta
x = np.array([80.0, 230.0])
y = m * x + b

plt.scatter(L_i, X_i)
plt.plot(x, y)
plt.xlabel("Distância da fonte de luz ao alvo, L [cm]")
plt.ylabel("Distância entre máximos luminosos consecutivos, X [cm]")
plt.show()

# d)
print("X = {0:.2f} cm".format(m * 165.0 + b)) #(L=165.0 cm) - o X está no eixo dos yy

# e)
L_i = np.array([222.0, 207.5, 194.0, 171.5 , 153.0, 133.0, 113.0, 92.0]) # [cm]
X_i = np.array([2.3, 2.2, 2.0, 1.8, 2.0, 1.4, 1.2, 1.0]) 

# Fazer o gráfico
plt.scatter(L_i, X_i)
plt.xlabel("Distância da fonte de luz ao alvo, L [cm]")
plt.ylabel("Distância entre máximos luminosos consecutivos, X [cm]")
plt.show()

# f)
# Calcular as quantidades m, b, r2, mm, mb
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

m, b, r2, dm, db = minimos_quadrados(L_i, X_i)

print("m = {0:.4f}".format(m))
print("b = {0:.2f} cm".format(b))
print("r² = {0:.4f}...".format(r2))
print("Δm = {0:.4f}".format(dm))
print("Δb = {0:.2f} cm".format(db))

# Definir dois pontos (x0, y0) e (x1, y1) para representar melhor reta
x = np.array([80.0, 230.0])
y = m * x + b

# Fazer gráfico
plt.scatter(L_i, X_i)
plt.plot(x, y)
plt.xlabel("Distância da fonte de luz ao alvo, L [cm]")
plt.ylabel("Distância entre máximos luminosos consecutivos, X [cm]")
plt.show()