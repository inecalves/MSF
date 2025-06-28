'''
Maria Inês Gonçalves
124754
'''

import numpy as np
import matplotlib.pyplot as plt

# Dados
k = 2.0
k_prime = 0.5
m = 1.0

# Dei valores às posições de equilíbrio para se poder visualizar - mas independentemente da posição,
# o movimento é o mesmo.
xA_eq= 1.0
xB_eq = 1.0

'''
a) Encontre a lei de movimento dos dois corpos numereicamente, através de vários casos
'''

def derivatives(y):
    xA, vA, xB, vB = y

    F_A = -k*(xA - xA_eq) - k_prime*(xA-xB)
    F_B = -k_prime*(xB - xA_eq) - k*(xB - xB_eq)

    aA = F_A / m
    aB = F_B / m

    return np.array([vA, aA, vB, aB])

def euler_integrate(y0,t,dt):
    n = len(t)
    y = np.zeros((n,4))
    y[0] = y0

    for i in range(1,n):
        y[i] = y[i-1] + dt * derivatives(y[i-1])
    return y

dt = 0.01
t_max = 30.0
t = np.arange(0, t_max, dt)

# Casos
cases = [
    {'name': 'Caso i)', 'xA0': xA_eq, 'xB0': xB_eq, 'vA0': 0.2, 'vB0': -0.3},
    {'name': 'Caso ii)', 'xA0': xA_eq, 'xB0': xB_eq, 'vA0': 0.2, 'vB0': -0.2},
    {'name': 'Caso iii)', 'xA0': xA_eq, 'xB0': xB_eq, 'vA0': 0.3, 'vB0': 0.3}
]

plt.figure(figsize=(15, 10))

for i, case in enumerate(cases):
    y0 = np.array([case['xA0'], case['vA0'], case['xB0'], case['vB0']])

    solution = euler_integrate(y0, t, dt)
    xA = solution[:, 0]
    xB = solution[:, 2]

    plt.subplot(3, 1, i + 1)
    plt.plot(t, xA, label='xA', color='blue')
    plt.plot(t, xB, label='xB', color='orange')
    plt.title(case['name'])
    plt.xlabel('Tempo (s)')
    plt.ylabel('Posição (m)')
    plt.legend()
    plt.grid()

plt.tight_layout()
plt.show()

'''
b) Como caracteriza o movimento dos corpos em cada um dos 3 casos?
'''
# R: o movimentos dos corpos em cada um dos casos é um movimento periódico harmónico

