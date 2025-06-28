import numpy as np
import matplotlib.pyplot as plt
x0=0
y0=0
t=[1,2,3,4]

# c)
for tempo in t:
    plt.arrow(2*tempo,tempo**2,2,2*tempo,color='b',width=0.05)

plt.show()