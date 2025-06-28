import numpy as np
import matplotlib.pyplot as plt

'''
1. Simule o movimento de duas esferas sujeitas às forças descritas
na página anterior. Use o método de Euler-Cromer. Tenha cuidado com a escolha de
'''

t0 = 0.0 # condição inicial, tempo [s]
tf = 5.0 # tempo final [s]
dt = 0.001 # passo [s]

# inicializar domínio temporal [s]
t = np.arange(t0, tf, dt)
Nt = np.size(t)

# Parametros
N = 2 # Numero de esferas
d = 0.1 # Diametro das esferas [m]
l = 10 * d # Comprimento das cordas
m = 0.3 # Massa das esferas [kg]
g = 9.8 # aceleração gravítica [m/s^2]
k = 1e7 # constante de forca elastica [N/m^2]
x0 = np.arange(0, N, 1) * d # posições de equilibrio [m]

# inicializar das granzedas físicas
x_arr = np.zeros((N, Nt)) # posição das esferas i=0...N-1 [m]
v_arr = np.zeros((N, Nt)) # velocidades [m/s]
a_arr = np.zeros((N, Nt)) # aceleraçoes [m/s2]

# Condicoes iniciais
x_arr[:, 0] = x0 # Posiçoes de equilibrio [m]
x_arr[0, 0] = - 5 * d # Esferas levantadas
v_arr[:, 0] = np.zeros(N) # Velocidade iniciais [m/s]

def acc_toque(dx):
    #calcular a aceleração de uma esfera devido ao contacto com a esfera à sua direita
    if dx < d:
        a = k * abs(dx - d)**2 / m
    else:
        a = 0.0
    return a

def acc_i(i, x):
    a = 0

    if i > 0: # a primeira esfera não tem vizinho à sua esquerda
        a += acc_toque(x[i] - x[i - 1])
    if i < (N - 1): # a última esfera não tem vizinho à sua direita
        a -= acc_toque(x[i + 1] - x[i])

    # aceleração de gravidade, afeta todas as esferas
    a -= g * (x[i] - d * i) / l
    return a

# Método de Euler-Cromer
for j in range(np.size(t) - 1): # loop no tempo
    for i in range(0, N): # loop nas esferas
        a_arr[i, j] = acc_i(i, x_arr[:, j])

    v_arr[:, j + 1] = v_arr[:, j] + a_arr[:, j] * dt
    x_arr[:, j + 1] = x_arr[:, j] + v_arr[:, j + 1] * dt

# Representação grafica da posição
for i in range(0, N): # loop nas esferas
    plt.plot(t, x_arr[i, :])

plt.xlabel("t [s]")
plt.ylabel("posição [m]")
plt.show()

'''
2. Calcule o momento total em cada instante, e apresentar os
resultados num gráfico

momento: P = m*v
'''

# Calculo do momento linear
p_arr = m * v_arr
p_tot = p_arr[0, :] + p_arr[1, :]

# Representação grafica do momento
plt.plot(t, p_arr[0, :], 'b-', t, p_arr[1, :], 'r-', t, p_tot, 'k-')
plt.xlabel("Tempo decorrido, t [s]")
plt.ylabel("Posição, x [m]")
plt.show()


'''
3. Calcule a energia cinética e a energia potencial em cada instante,
e apresentar os resultados num gráfico.
'''
# Energia cinética
E_c = p_tot**2 / (2 * m)

# Energia potencial
#E_p = np.zeros(np.size(E_c))
E_p = m * g * (x_arr[0, :] - x0[0])**2 / (2 * l)
E_p += m * g * (x_arr[1, :] - x0[1])**2 / (2 * l)

# Representação das energias cinetica e potencial
plt.plot(t, E_c, 'b-', t, E_p, 'r-')
plt.xlabel("Tempo decorrido, t [s]")
plt.ylabel("Energia [J]")
plt.show()
