import numpy as np
import matplotlib.pyplot as plt

dist = np.array([0.0,0.735,1.363,1.739,2.805,3.814,4.458,4.955,5.666,6.329])
tempo =np.array([0,1,2,3,4,5,6,7,8,9]) #np.arange(0,10,1)

plt.plot(dist,tempo,'-')
plt.plot(dist,tempo,'.')

plt.xlabel("Tempo (min)")
plt.ylabel("Distância (km)")

plt.show()
