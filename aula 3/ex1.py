import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

x,y,m,b = sy.symbols('x, y, m, b')  # Definir variáveis simbólicos

y = m*x**2 + b  # Definir uma expressão

y2 = y.subs([(m,0.01),(b,0.0)])  # Impor valores específicos para variáveis

y_em_1 = y2.evalf(subs={x:1})  # Avaliar y2 num determinado valor de x com o método evalf

y_lam = sy.lambdify(x,y2,"numpy")  # Se quiseremos avaliar múltiplas vezes

y_lam(x)

#Usar a função y_lam para fazer um plot de y em valores de x de 0 até 2
x_vals = np.linspace(0, 2, 100)
y_vals = y_lam(x_vals)

plt.plot(x_vals, y_vals)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = 0.01x**2')
plt.show()


'''
Outras funções úteis:
sympy.diff(y,x) --> derivada de y em função de x
sympy.integrate(y,x) --> integral de y em função de x
sympy.nsolve(y,x,x0) --> encontrar solução x numérica para y=0, com valor inicial x0
'''
