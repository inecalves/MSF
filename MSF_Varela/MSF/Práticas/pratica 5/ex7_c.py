import numpy as np
import matplotlib.pyplot as plt

t = [1,2,3,4]
colors = ['b','g','y','r']

for tempo in t:
    plt.arrow(2*tempo,tempo**2,2,2*tempo,color=colors[tempo-1],width=0.05)
    
plt.show()