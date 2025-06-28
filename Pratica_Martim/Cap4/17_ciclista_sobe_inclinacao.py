import numpy as np
import matplotlib.pyplot as plt

# Parâmetros (mesmos do problema anterior)
P = 0.4 * 735.5       # Potência em watts (0.4 cv)
m = 75.0              # Massa do ciclista + bicicleta em kg
CdA = 0.5             # Área de arrasto em m^2
rho = 1.225           # Densidade do ar em kg/m^3
k = 0.5 * rho * CdA   # Termo do coeficiente de arrasto
g = 9.81              # Aceleração da gravidade em m/s^2
theta = np.deg2rad(5) # Inclinação de 5° em radianos
sin_theta = np.sin(theta)

# Função para encontrar velocidade terminal resolvendo P/v = k v^2 + m g sin(theta)
def find_v_terminal(P, k, m, sin_theta):
    f = lambda v: P/v - k*v**2 - m*g*sin_theta
    # Busca binária em [1e-3, 20]
    a, b = 1e-3, 20.0
    fa, fb = f(a), f(b)
    if fa*fb > 0:
        return np.nan
    for _ in range(50):
        mid = 0.5*(a+b)
        fm = f(mid)
        if fa*fm > 0:
            a, fa = mid, fm
        else:
            b, fb = mid, fm
    return 0.5*(a+b)

v_term_colina = find_v_terminal(P, k, m, sin_theta)

# Simulação temporal por Euler explícito
dt = 0.1       # Passo de tempo em s
t_max = 2000   # Máximo tempo para simulação em s

times = np.arange(0, t_max+dt, dt)
velocities = np.zeros_like(times)
distances  = np.zeros_like(times)

# Condição inicial
velocities[0] = 1.0  # Empurrão inicial 1 m/s

# Integração: m dv/dt = P/v - k v^2 - m g sin(theta)
for i in range(1, len(times)):
    v = velocities[i-1]
    dvdt = (P/v - k*v**2 - m*g*sin_theta) / m
    velocities[i] = max(v + dvdt*dt, 0)  # não deixar ficar negativa
    distances[i] = distances[i-1] + velocities[i]*dt
    if distances[i] >= 2000:
        break

t_2km_colina = times[i]

# Plot
plt.figure()
plt.plot(times[:i+1], velocities[:i+1], label='Velocidade')
plt.axhline(v_term_colina, color='r', linestyle='--', label='Velocidade terminal')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.title('Evolução da Velocidade em Colina 5°')
plt.legend()
plt.grid(True)
plt.show()

# Resultados
print(f"Velocidade terminal em colina 5°: {v_term_colina:.2f} m/s")
print(f"Tempo para percorrer 2 km: {t_2km_colina:.1f} s ({t_2km_colina/60:.1f} min)")
