import numpy as np
import matplotlib.pyplot as plt
import time

y0 = 0
x0 = 0
t = [1,2,3,4]
colors = ['b','g','y','r']


for tempo in t:
    plt.arrow(x0,y0,2*tempo,tempo**2,color=colors[tempo-1],width=0.05)
    
    
plt.show()


