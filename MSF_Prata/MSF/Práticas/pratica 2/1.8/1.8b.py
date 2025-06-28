import numpy as np
import matplotlib.pyplot as plt


temperaturaK = np.array([200,300,400,500,600,700,800,900,1000,1100])
energiaJ= np.array([0.6950,4.363,15.53,38.74,75.08,125.2,257.9,344.1,557.4,690.7])

x = temperaturaK
y = energiaJ

plt.plot(np.log(x),np.log(y),'-')
a = np.polyfit(np.log(x), np.log(y), 1)


t = np.linspace(np.log(temperaturaK[0])*0.9, np.log(temperaturaK[-1])*1.1, 100)
plt.plot(t, a[0]*t+a[1]) #y = cX +b

plt.show()