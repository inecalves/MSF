import numpy as np
import matplotlib.pyplot as plt

# Função para encontrar o máximo por interpolação com 3 pontos
def maxminv(xm1, xm2, xm3, ym1, ym2, ym3):
    xab = xm1 - xm2
    xac = xm1 - xm3
    xbc = xm2 - xm3

    a = ym1 / (xab * xac)
    b = -ym2 / (xab * xbc)
    c = ym3 / (xac * xbc)

    xmla = (b + c) * xm1 + (a + c) * xm2 + (a + b) * xm3
    xm = 0.5 * xmla / (a + b + c)

    xta = xm - xm1
    xtb = xm - xm2
    xtc = xm - xm3

    ymax = a * xtb * xtc + b * xta * xtc + c * xta * xtb
    return xm, ymax

# Constantes
g = 9.8
L = 1.0
dt = 0.01
T = 10
n = int(T / dt)

# Método de Euler-Cromer
def euler_cromer(theta0, omega0=0):
    theta = np.zeros(n)
    omega = np.zeros(n)
    t = np.linspace(0, T, n)

    theta[0] = theta0
    omega[0] = omega0

    for i in range(1, n):
        omega[i] = omega[i-1] - (g/L) * np.sin(theta[i-1]) * dt
        theta[i] = theta[i-1] + omega[i] * dt

    return t, theta

# Função para medir período usando interpolação Lagrange em dois máximos
def medir_periodo(t, theta):
    # Procurar os índices dos máximos locais
    maximos = []
    for i in range(1, len(theta)-1):
        if theta[i-1] < theta[i] and theta[i] > theta[i+1]:
            maximos.append(i)

    # Usar os dois primeiros máximos para medir o período
    if len(maximos) < 2:
        raise ValueError("Menos de dois máximos detectados!")

    i1, i2 = maximos[0], maximos[1]

    # Obter pontos ao redor dos máximos
    xm1, xm2, xm3 = t[i1-1], t[i1], t[i1+1]
    ym1, ym2, ym3 = theta[i1-1], theta[i1], theta[i1+1]
    t1, _ = maxminv(xm1, xm2, xm3, ym1, ym2, ym3)

    xm1, xm2, xm3 = t[i2-1], t[i2], t[i2+1]
    ym1, ym2, ym3 = theta[i2-1], theta[i2], theta[i2+1]
    t2, _ = maxminv(xm1, xm2, xm3, ym1, ym2, ym3)

    return t2 - t1

# Simulação e cálculo para um ângulo inicial
theta0 = 0.1  # rad
t, theta = euler_cromer(theta0)
T_medido = medir_periodo(t, theta)
T_teorico = 2 * np.pi * np.sqrt(L / g)

# Resultados
print(f"Período numerico: {T_medido:.4f} s")
print(f"Período teórico: {T_teorico:.4f} s")
print(f"Erro relativo: {abs(T_medido - T_teorico) / T_teorico * 100:.2f}%")

# Gráfico opcional
plt.plot(t, theta)
plt.title(f'Pêndulo: θ₀ = {theta0} rad')
plt.xlabel('Tempo (s)')
plt.ylabel('Ângulo θ (rad)')
plt.grid(True)
plt.show()
