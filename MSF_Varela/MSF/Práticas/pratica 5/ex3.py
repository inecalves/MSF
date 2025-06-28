import numpy as np
import matplotlib.pyplot as plt

y0 = 0
x0 = 0
x = 3
y = 4

plt.arrow(x0,y0,3,4,color='b',width=0.05)
plt.arrow(0,0,4,-3,color='r',width=0.05)
plt.axis('square')
plt.show()