import numpy as np
import matplotlib.pyplot as plt

valores = [0.00,0.735,1.363,1.739,2.805,3.814,4.458,4.955 ,5.666,6.329]

minutos = [0,1,2,3,4,5,6,7,8,9]

x = np.array(minutos)
y=np.array(valores)

plt.xlabel("Tempo (min)")
plt.ylabel("Distância (km)")

plt.scatter(x,y)
plt.show()

