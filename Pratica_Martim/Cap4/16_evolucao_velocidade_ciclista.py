import numpy as np
import matplotlib.pyplot as plt

# Parâmetros (ajustar conforme necessário)
P = 0.4 * 735.5       # Potência em watts (0.4 cv)
m = 75.0              # Massa do ciclista + bicicleta em kg
CdA = 0.5             # Área de arrasto em m^2
rho = 1.225           # Densidade do ar em kg/m^3
k = 0.5 * rho * CdA   # Termo do coeficiente de arrasto

# Cálculo analítico da velocidade terminal
v_term = (P / k) ** (1/3)

# Parâmetros de integração temporal
dt = 0.1              # Passo de tempo em segundos
t_max = 500           # Tempo máximo de simulação em segundos

# Arrays para tempo, velocidade e distância
times = np.arange(0, t_max + dt, dt)
velocities = np.zeros_like(times)
distances = np.zeros_like(times)

# Condição inicial
velocities[0] = 1.0   # Empurrão inicial de 1 m/s

# Integração da EDO: m dv/dt = P/v - k v^2
for i in range(1, len(times)):
    v = velocities[i - 1]
    dvdt = (P / v) / m - (k * v**2) / m
    velocities[i] = v + dvdt * dt
    distances[i] = distances[i - 1] + velocities[i] * dt

# Tempo para atingir 90% da velocidade terminal
t_90 = times[np.where(velocities >= 0.9 * v_term)[0][0]]

# Tempo para percorrer 2 km
idx_2km = np.where(distances >= 2000)[0]
t_2km = times[idx_2km[0]] if len(idx_2km) > 0 else np.nan

# Gráfico da evolução da velocidade
plt.figure()
plt.plot(times, velocities, label='Velocidade')
plt.axhline(v_term, color='r', linestyle='--', label='Velocidade terminal')
plt.axvline(t_90, color='g', linestyle=':', label='90% v_term')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.title('Evolução Temporal da Velocidade')
plt.legend()
plt.grid(True)
plt.show()

# Resultados impressos
print(f"Velocidade terminal (analítica): {v_term:.2f} m/s")
print(f"Tempo para atingir 90% de v_term: {t_90:.1f} s")
print(f"Tempo para percorrer 2 km: {t_2km:.1f} s ({t_2km/60:.1f} min)")


# Print results
print(f"Velocidade terminal (analítica): {v_term:.2f} m/s")
print(f"Tempo para atingir 90% de v_term: {t_90:.1f} s")
print(f"Tempo para percorrer 2 km: {t_2km:.1f} s ({t_2km/60:.1f} min)")
