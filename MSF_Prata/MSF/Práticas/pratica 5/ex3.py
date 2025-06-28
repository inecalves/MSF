
import numpy as np
import matplotlib.pyplot as plt

#representação de vetor
# v=(3,4) x0,y0 ponto inicial do vetor
x0=0
y0=0
x=3
y=4
plt.arrow(x0,y0,x,y,color='b',width=0.05)
plt.arrow(x0,y0,4,-3,color='r',width=0.05)
plt.axis('square')
plt.show()