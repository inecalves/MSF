import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

'''
Volante de badmington (aceleração uma função de velocidade)
Um volante de badmington foi largado de uma altura considerável. A lei do movimento é:
y(t) = vt2/g*log(cosh(g*t/vt))
'''

'''
1. Faça o gráfico da lei do movimento y(t) de 0 a 4.0s
'''
y, t, vt, g = sy.symbols('y, t, vt, g')

y = vt**2/g*sy.log(sy.cosh(g*t/vt))

y2 = y.subs([(vt,6.80), (g,9.80)])

y_lam = sy.lambdify(t,y2,"numpy")

t_vals = np.linspace(0, 4, 100)
y_vals = y_lam(t_vals)

plt.plot(t_vals, y_vals)
plt.xlabel("x")
plt.ylabel("y")
plt.title("6.80**2/g*log(cosh(g*t/6.80))")
plt.show()

'''
2. Determine a velocidade instantânea em função do tempo, usando cálculo simbólico (sympy). Faça o gráfico da
velocidade em função do tempo de 0 a 4s, usando o pacote matplotlib. (estamos a usar um bocado do ex1)
'''
g = 9.8
v = sy.integrate(g, t)
print("velocidade instantânea =", v)

v_lam = sy.lambdify(t,v,"numpy")
v_vals = v_lam(t_vals)
plt.plot(t_vals, v_vals)
plt.show()

#3.
'''
3. Determine a aceleração instantânea em função do tempo, usando cálculo simbólico. Faça o gráfico da 
aceleração em função do tempo de 0 a 4s, usando o pacote matplotlib.

a = sy.diff(v, t)
print("acelaração instanânea = ", a)

a_lam = sy.lambdify(t,a,"numpy")
a_vals = a_lam(t_vals)
plt.plot(t_vals, a_vals)
plt.show()                            --> Era suposto dar, mas não dá
'''

'''
4. Mostre que a aceleração é compatível com a forma geral a(t) = g-g/vt2*v*|v|
'''
a2 = g - g/6.8**2*v*abs(v)
a2_lam = sy.lambdify(t, a2, "numpy")
a2_vals = a2_lam(t_vals)
plt.plot(t_vals, a2_vals)
plt.show()
print(a2)

'''
5. Se o volante for largadp de uma altura de 20m, quanto tempo demora a atingir o solo?
Compare com o tempo que demoraria se não houvesse resistência do ar.
'''
h = 20 #m
th = sy.solve(y -h, t)
print(th)