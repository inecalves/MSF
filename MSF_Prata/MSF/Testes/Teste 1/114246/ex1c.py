import numpy as np

m= -0.0075 # declive do ex 1 b)
errom= 6.3306**(-5)

meiavida= -np.log(2)/m
erromeiavida = errom/m

print(meiavida)
print(erromeiavida)

#O valor de t1/2 é de 92.4196 com um erro de -0.0131