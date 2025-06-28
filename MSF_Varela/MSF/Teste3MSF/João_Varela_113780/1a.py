import numpy as np
from matplotlib import pyplot as plt

m = 1
xeq = 0
k = 1
alpha = 0.05
x = np.arange(-8, 4, 0.1)
Ep = 0.5*k*(x**2)+alpha*(x**3)

plt.plot(x,Ep)


plt.axhline(y=7, color='r', linestyle='-')

plt.grid()
plt.xlabel('x (m)')
plt.ylabel('Energia potencial (J)')
plt.legend()
plt.plot()
plt.show()

#Qual o movimento que o sistema executa se a energia total for 7 J?

#Resposta:
#Como a energia potencial não é simétrica à volta da posição de equilíbrio (x = 0) entre as posições em que a EP <= 7J,
# o movimento oscilatório tem uma posição média (por período) > 0.


#o que acontecerá se a energia total for maior que 8 J?

#Resposta:
#A energia potencial é maior que a energia total, pelo que o movimento não é oscilatório, mas sim de translação.
#com velocidade constante
