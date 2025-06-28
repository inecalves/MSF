import numpy as np
import matplotlib.pyplot as plt

temperaturaK = np.array([200,300,400,500,600,700,800,900,1000,1100])
energiaJ= np.array([0.6950,4.363,15.53,38.74,75.08,125.2,257.9,344.1,557.4,690.7])

x = temperaturaK
y = energiaJ
npontos = x.size

plt.plot(x,y,'-')
plt.plot(x,y,'.')

plt.xlabel("Temperatura (Kelvin)")
plt.ylabel("Energia (Joules)")
plt.show()

#Não é linear