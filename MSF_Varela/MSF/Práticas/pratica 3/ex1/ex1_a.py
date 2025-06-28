import numpy as np
import matplotlib.pyplot as plt

#X(t)A = 70t
#X(t)B = t**2

t = np.linspace(0, 25, 100)
va = 70/3.6 
plt.plot(t,va*t)
plt.plot(t,t**2)


plt.xlabel("tempo")
plt.ylabel("posição")
plt.show()

