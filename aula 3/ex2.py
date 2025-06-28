import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

'''
Um avião arranca do repouco e acelera com acelaração constante a = 3m/s2 até atingir a velocidade de descolagem de 250 km/h
'''

'''
1. Escreve a função que descreve o movimento do avião (lei do movimento) x(t). Faça o gráfico da lei do movimento.
'''
x, x0, t, v0, a = sy.symbols('x, x0, t, v0, a')

x = x0 + v0*t + 1/2*a*t**2

x2 = x.subs([(x0,0.0),(v0,0.0),(a,3.0)])

x_lam = sy.lambdify(t,x2,"numpy")

x_lam(t)

t_vals = np.linspace(0, 2, 100)
x_vals = x_lam(t_vals)

plt.plot(t_vals, x_vals)
plt.xlabel('t')
plt.ylabel('x')
plt.title('y = 1/2*3*t**2')
plt.show()

'''
2. Em que instante e qual a distância percorrida pelo avião quando atinge a velocidade de descolagem?
Encontre a solução com cálculo analítico
'''
#250 km/h --> 250*1000/3600 
v = 250*1000/3600
a = 3

td = v/a   #v = m/s, a = m/s*s, fica só segundo, ou seja, o tempo
print(td)  #aqui o tempo
print(x_lam(td))  #aqui descobrimos a posição

'''
3. Use sympy.integrate() para integrar a aceleração em função do tempo duas vezes, para obter a velocidade e a
posição do avião como funções (simbólicos) de tempo. Está de acordo com o que se esperava?
'''
vf = sy.integrate(a, t)  #como a velocidade incial é zero, não se adiciona nada

d = sy.integrate(v, t)

print("velocidade simbólica = ",vf)
print("posição simbólica = ",d)

'''
4. Use sympy.nsolve() para encontrar o tempo e a posição de descolagem. 
'''
tempo = sy.nsolve(v - vf, 0.0)
print("tempo = ",tempo)

print("distancia = ", x_lam(tempo))

