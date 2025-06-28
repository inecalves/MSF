import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

g = 9.8
vt  = 6.80

t_com=(np.arccosh(10**(20 * g / vt**2)))*vt/g

print("Tempo com resistência do ar =",t_com,"s")

t_sem = np.sqrt(2*20/g)

print("Tempo sem resistência do ar =",t_sem,"s")