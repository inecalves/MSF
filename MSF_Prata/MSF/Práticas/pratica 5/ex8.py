import numpy as np
import matplotlib.pyplot as plt

r=0.11              #m
densidadear = 1.225 #kg/m***3
A= np.pi * r**2

# VETOR 1
a = 5
b = 2
c = 10 
v1 = [a,b,c]

# VETOR 2
m = 1
n = 4
o = -7
v2=[m,n,o]

produto_vetorial = np.cross(v1,v2)

fmagnus = 1/2 * A * densidadear * r * produto_vetorial

print(fmagnus)
