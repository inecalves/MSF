# r = 2t ex + t**2 ey m
# a) v = 2 ex + 2t ey m/s  v(2,2t) m/s

import numpy as np
import matplotlib.pyplot as plt

x0=0
y0=0
t=[1,2,3,4]

# b)
for tempo in t:
    plt.arrow(x0,y0,2*tempo,tempo**2,color='b',width=0.05)

plt.show()


