import numpy as np
import matplotlib.pyplot as plt

'''
2. 4 esferas com 1 levantada inicialmente.
'''
t0 = 0.0 # condição inicial, tempo [s]
tf = 5.0 # limite do domínio, tempo final [s]
dt = 0.001 # passo [s]

# inicializar domínio temporal [s]
t = np.arange(t0, tf, dt)
Nt = np.size(t)

# Parametros
N = 4 # Numero de esferas
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
v_arr[:, 0] = np.zeros(N) # Velocidades iniciais [m/s]

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
3. 5 esferas com 2 levantadas inicialmente
'''
N = 5

x0 = np.arange(0, N, 1) * d # posições de equilibrio [m]

# inicializar das granzedas físicas
x_arr = np.zeros((N, Nt)) # posição das esferas i=0...N-1 [m]
v_arr = np.zeros((N, Nt)) # velocidades [m/s]
a_arr = np.zeros((N, Nt)) # aceleraçoes [m/s2]

# Condicoes iniciais
x_arr[:, 0] = x0 # Posiçoes de equilibrio [m]
x_arr[0, 0] = - 5 * d # Esferas levantadas
x_arr[1, 0] = - 4 * d # Esferas levantadas
v_arr[:, 0] = np.zeros(N) # Velocidades iniciais [m/s]

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

