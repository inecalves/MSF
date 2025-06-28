import numpy as np
import matplotlib.pyplot as plt

# Constantes do sistema
m = 1.0        # massa (kg)
k = 0.2        # constante elástica (N/m)
alpha = 1.0    # termo não linear (N/m^3)
b = 0.01       # amortecimento (kg/s)
F0 = 5.0       # força externa (N)
omega_f = 0.6  # frequência angular (rad/s)

# Passo de tempo e vetor tempo
dt = 0.01
t = np.arange(0, 50, dt)

# Condições iniciais
x0 = 1.0
v0 = 0.0

# Função de aceleração
def acelera(t, x, v):
    return (F0 * np.cos(omega_f * t) - b * v - k * x - 4 * alpha * x**3) / m

# a) Lei do movimento 
# Método de Runge-Kutta 4ª ordem
def rk4_step(x, v, t, dt):
    def dxdt(v): return v
    def dvdt(t, x, v): return acelera(t, x, v)

    k1x = dxdt(v)
    k1v = dvdt(t, x, v)

    k2x = dxdt(v + 0.5 * dt * k1v)
    k2v = dvdt(t + 0.5 * dt, x + 0.5 * dt * k1x, v + 0.5 * dt * k1v)

    k3x = dxdt(v + 0.5 * dt * k2v)
    k3v = dvdt(t + 0.5 * dt, x + 0.5 * dt * k2x, v + 0.5 * dt * k2v)

    k4x = dxdt(v + dt * k3v)
    k4v = dvdt(t + dt, x + dt * k3x, v + dt * k3v)

    x_new = x + (dt / 6) * (k1x + 2*k2x + 2*k3x + k4x)
    v_new = v + (dt / 6) * (k1v + 2*k2v + 2*k3v + k4v)

    return x_new, v_new

# Integração da equação do movimento
x_vals = [x0]
v_vals = [v0]

x, v = x0, v0
# Aplica rk4_step a cada instante de 
# tempo para simular o movimento.
for ti in t[:-1]:
    x, v = rk4_step(x, v, ti, dt)
    x_vals.append(x)
    v_vals.append(v)

x_vals = np.array(x_vals)
v_vals = np.array(v_vals)

# Gráfico da posição em função do tempo
plt.figure(figsize=(8, 4))
plt.plot(t, x_vals)
#Mostra as oscilações do sistema. 
# Como é não linear, vemos comportamento caótico (não periódico, difícil de prever).
plt.xlabel("t (s)")
plt.ylabel("x(t) (m)")
plt.title("Movimento do oscilador não harmónico forçado (x(t))")
plt.grid(True)
plt.tight_layout()
plt.show()

# O gráfico da posição mostra oscilações não periódicas e irregulares 
# — o que já é um indício de comportamento caótico.

# Parte (b) – testar diferentes valores de dt para avaliar estabilidade dos resultados
dt_values = [0.05, 0.02, 0.01, 0.005]
t_max = 50

results_b = {}

for dt_test in dt_values:
    t_test = np.arange(0, t_max, dt_test)
    x, v = 1.0, 0.0
    x_list = [x]

    for ti in t_test[:-1]:
        x, v = rk4_step(x, v, ti, dt_test)
        x_list.append(x)

    results_b[dt_test] = np.array(x_list)

# Gráficos dos resultados da parte (b)
plt.figure(figsize=(10, 6))
for dt_test in dt_values:
    plt.plot(np.arange(0, t_max, dt_test), results_b[dt_test], label=f"dt = {dt_test}")
plt.xlabel("t (s)")
plt.ylabel("x(t)")
plt.title("Comparação da solução para diferentes valores de Δt")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# d) 
# Gráfico da trajetória no espaço de fase
plt.figure(figsize=(6, 6))
plt.plot(x_vals, v_vals)
plt.xlabel("x(t) (m)")
plt.ylabel("v(t) (m/s)")
plt.title("Espaço de fase: v(t) vs x(t)")
plt.grid(True)
plt.tight_layout()
plt.show()

# O gráfico no espaço de fase forma um padrão denso, 
# com laços irregulares.
# Isto não é uma órbita fechada (como num oscilador harmónico), 
# mas sim um atrator estranho — típico de sistemas caóticos.
