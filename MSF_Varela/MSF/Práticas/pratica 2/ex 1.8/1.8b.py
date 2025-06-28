import numpy as np
import matplotlib.pyplot as plt

T = np.array([0,48,96,144,192,240,288,336,384]) #eixo x
ati = np.array([10.03,7.06,4.88,3.38,2.26,1.66,1.14,0.79,0.58]) #eixo y

x = T
#x = x** delive log-log 
y = ati
npontos = len(T) #ou x.size

x = np.array(T)
y = np.array(E)

plt.plot(np.log(x), np.log(y), "o")
a = np.polyfit(np.log(x), np.log(y), 1)

t = np.linspace(np.log(x[0])*0.9, np.log(x[-1])*1.1, 100)
plt.plot(x, a[0]*x+a[1])

plt.show()