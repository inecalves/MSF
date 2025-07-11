'''
Maria Inês Gonçalves
124754
'''

import numpy as np
import matplotlib.pyplot as plt

# Dados
m = 0.5  # kg
k = 2.0  # N/m
b = 0.2  # kg/s

'''
a) Lei do movimento, quando x0 = 2m com velocidade 2m/s - gráficos posição-tempo e velocidade-tempo
'''

x0 = 2.0
v0 = 2.0

t_inicio = 0
t_fim = 30
dt = 0.01

t = np.arange(t_inicio, t_fim, dt)

x = np.zeros_like(t)
v = np.zeros_like(t)

x[0] = x0
v[0] = v0

for i in range(1, len(t)):
    a = (-k*x[i-1] - b*v[i-1]) / m
    v[i] = v[i-1] + a * dt
    x[i] = x[i-1] + v[i] * dt

plt.figure
plt.plot(t, x)
plt.title('Posição x(t)')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.grid()
plt.show()

plt.figure
plt.plot(t, v)
plt.title('velocidade v(t)')
plt.xlabel('Tempo (s)')
plt.ylabel('velocdidade (m/s)')
plt.grid()
plt.show()

'''
b) Encontrar os primeiros quatro máximos (locais) da posição usando a interpolação pelo polinómio de Lagrange
'''

# Função de interpolação 
def intlagv(xinp, xm1, xm2, xm3, ym1, ym2, ym3):
    xab = xm1 - xm2
    xac = xm1 - xm3
    xbc = xm2 - xm3

    xi1 = xinp - xm1
    xi2 = xinp - xm2
    xi3 = xinp - xm3
    
    a = xi2 * xi3 / (xab * xac)
    b = -xi1 * xi3 / (xab * xbc)
    c = xi1 * xi2 / (xac * xbc)

    yout = a * ym1 + b * ym2 + c * ym3
    return xinp, yout

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

# Encontrar índices aproximados dos extremos locais
extremos_idx = []
for i in range(1, len(x)-1):
    if (x[i] > x[i-1] and x[i] > x[i+1]) or (x[i] < x[i-1] and x[i] < x[i+1]):
        extremos_idx.append(i)

# Refinar os extremos usando a função maxminv
t_extremos = []
x_extremos = []
for idx in extremos_idx:
    # Pegar três pontos ao redor do extremo
    if idx > 0 and idx < len(x)-1:
        xm, ym = maxminv(t[idx-1], t[idx], t[idx+1], x[idx-1], x[idx], x[idx+1])
        t_extremos.append(xm)
        x_extremos.append(ym)

# Plot com os extremos marcados
plt.figure(figsize=(10, 5))
plt.plot(t, x, label='Posição')
plt.scatter(t_extremos, x_extremos, color='red', label='Extremos locais')
plt.title('Posição com extremos locais marcados')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.legend()
plt.grid(True)
plt.show()

print("Primeiros 4 máximos locais:")
i = 0
for te, xe in zip(t_extremos, x_extremos):
    if(xe > 0 and i != 4):
        print(f"Tempo: {te:.2f} s, Posição: {xe:.4f} m")
        i += 1;

#R: os valores dos máximos vão diminuindo.

'''
c) Calcular os tempos entre os máximos e usar o resultado para estimar a frequência de oscilação do corpo
'''
# ???
