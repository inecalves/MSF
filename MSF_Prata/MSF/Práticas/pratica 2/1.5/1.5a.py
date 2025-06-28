import numpy as np
import matplotlib.pyplot as plt

xs = [222.0,207.7,194,171.5,153,133,113,92]
ys=[2.3,2.2,2,1.8,1.6,1.4,1.2,1]

X = np.array(xs)
Y = np.array(ys)

plt.plot(X,Y,'-')
plt.plot(X,Y,'.')
plt.show()