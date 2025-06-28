import numpy as np
import matplotlib.pyplot as plt


#X(t)A = va * t
#X(t)B = vb * t**2

t = np.linspace(0, 25, 100)
va = 70/3.6
plt.plot(t,va*t)
plt.plot(t,t**2)


plt.xlabel("tempo")
plt.ylabel("posição")

#segundo as equações va = t

plt.plot(va,va*va,'o')
print(va,va**2)
plt.show()

