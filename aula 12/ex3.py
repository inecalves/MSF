import numpy as np
import matplotlib.pyplot as plt

# Dados do sistema (Exercício 1)
k = 1       # N/m
k_ = 0.5    # N/m
m = 1       # kg
xAeq = 1.0  # m
xBeq = 2.0  # m

# Frequências naturais (modo simétrico e modo antissimétrico)
w1 = np.sqrt(k / m)                          # modo 1: oscilação simétrica
w2 = np.sqrt((k + 2 * k_) / m)              # modo 2: oscilação antissimétrica

# Tempo de simulação
T = 100      # Período total para análise de Fourier
dt = 0.1     # Intervalo de tempo
t = np.arange(0, T, dt)

# Três casos iniciais do exercício 3
condicoes_iniciais = {
    "i":  (xAeq + 0.3, xBeq + 0.3),
    "ii": (xAeq + 0.3, xBeq - 0.3),
    "iii":(xAeq + 0.3, xBeq - 0.1)
}

# Função de Fourier reaproveitada (mesma da imagem 2)
def abfourier(tp, xp, it0, it1, nf):
    dt = tp[1] - tp[0]
    per = tp[it1] - tp[it0]
    ome = 2 * np.pi / per

    s1 = xp[it0] * np.cos(nf * ome * tp[it0])
    s2 = xp[it1] * np.cos(nf * ome * tp[it1])
    st = xp[it0 + 1:it1] * np.cos(nf * ome * tp[it0 + 1:it1])
    soma = np.sum(st)

    q1 = xp[it0] * np.sin(nf * ome * tp[it0])
    q2 = xp[it1] * np.sin(nf * ome * tp[it1])
    qt = xp[it0 + 1:it1] * np.sin(nf * ome * tp[it0 + 1:it1])
    somq = np.sum(qt)

    integra = ((s1 + s2) / 2 + soma) * dt
    af = 2 / per * integra
    integq = ((q1 + q2) / 2 + somq) * dt
    bf = 2 / per * integq
    return af, bf

# Função para simular movimento dos corpos com condições iniciais
def simular_movimento(xA0, xB0, t):
    # Decomposição nas coordenadas normais
    q1_0 = (xA0 - xAeq + xB0 - xBeq) / 2   # modo simétrico
    q2_0 = (xA0 - xAeq - (xB0 - xBeq)) / 2 # modo antissimétrico

    q1 = q1_0 * np.cos(w1 * t)
    q2 = q2_0 * np.cos(w2 * t)

    xA = xAeq + q1 + q2
    xB = xBeq + q1 - q2
    return xA, xB

# Parâmetros para Fourier
it0 = 0
it1 = int(T / dt) - 1  # evitar ultrapassar o limite do vetor
n_vals = np.arange(1, 31)
omega = 2 * np.pi / T
frequencias = omega * n_vals

# Armazenar resultados
resultados = {}

# Calcular para cada caso
for nome, (xA0, xB0) in condicoes_iniciais.items():
    xA, xB = simular_movimento(xA0, xB0, t)

    aA, bA = [], []
    for n in n_vals:
        a, b = abfourier(t, xA, it0, it1, n)
        aA.append(a)
        bA.append(b)

    resultados[nome] = {
        "frequencias": frequencias,
        "a_n": aA,
        "b_n": bA
    }

# Plotar os gráficos dos coeficientes de Fourier para cada caso
for nome, dados in resultados.items():
    plt.figure()
    plt.title(f'Coeficientes de Fourier | Caso {nome}')
    plt.stem(dados["frequencias"], dados["a_n"], linefmt='b-', markerfmt='bo', basefmt=' ', label="an")
    plt.stem(dados["frequencias"], dados["b_n"], linefmt='#ff69b4', markerfmt='o', basefmt=' ', label='bn')
    plt.xlabel('Frequência ωₙ [rad/s]')
    plt.ylabel('Coeficientes aₙ (azul) e bₙ (vermelho)')
    plt.grid(True)
    plt.tight_layout()

plt.show()
