import numpy as np
import matplotlib.pyplot as plt

dist = np.array([0.0,0.735,1.363,1.739,2.805,3.814,4.458,4.955,5.666,6.329])
tempo =np.array([0,1,2,3,4,5,6,7,8,9])

#A função polyfit(x,y,n) faz um ajuste
#a um polinómio de grau n, sendo o resultado 
#um vetor com n+1 termos contendo os coeficientes do ajuste.

aprox = np.polyfit(dist, tempo, 1)
print(aprox)
# [1.38262518 0.09440314]
