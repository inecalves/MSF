import numpy as np
import matplotlib.pyplot as plt

v = 30/3.6
m = 75
Cres = 0.9
A = 0.3
par = 1.225
u = 0.004
g = 9.8

#Potencia ciclista = F ciclista * v

Potencia = u*m*g*v + (Cres/2)*A*par*(v**2)*v
print(Potencia)
