import numpy as np
import matplotlib.pyplot as plt

# a)
plt.figure(figsize=(6.5,4.5)) # Preparar a representação gráfica
plt.axis([-5, 3, -4.5, 1.0])

x = 0.0; y = 0.0; theta = 0.0
pos = np.array([[x, y, theta]]) # posicionamento. Robô inicia na orígem com ang=0
plt.arrow(x, y, np.cos(-theta * np.pi / 180), np.sin(-theta * np.pi / 180), color='r',
 width=0.01, head_width=0.1) # representar direção do robô

ang = 45; dist = 3 # instrução 1
theta += ang
x += dist * np.cos(-theta * np.pi / 180)
y += dist * np.sin(-theta * np.pi / 180)
pos = np.append(pos, [[x, y, theta]], 0)
plt.arrow(x, y, np.cos(-theta * np.pi / 180), np.sin(-theta * np.pi / 180), color='r',
 width=0.01, head_width=0.1) # representar direção do robô

ang = 90; dist = 2 # instrução 2
theta += ang
x += dist * np.cos(-theta * np.pi / 180)
y += dist * np.sin(-theta * np.pi / 180)
pos = np.append(pos, [[x, y, theta]], 0)
plt.arrow(x, y, np.cos(-theta * np.pi / 180), np.sin(-theta * np.pi / 180), color='r',
 width=0.01, head_width=0.1) # representar direção do robô

ang = 45; dist = 3 # instrução 3
theta += ang
x += dist * np.cos(-theta * np.pi / 180)
y += dist * np.sin(-theta * np.pi / 180)
pos = np.append(pos, [[x, y, theta]], 0)
plt.arrow(x, y, np.cos(-theta * np.pi / 180), np.sin(-theta * np.pi / 180), color='r',
 width=0.01, head_width=0.1) # representar direção do robô

ang = 45; dist = 2 # instrução 4
theta += ang
x += dist * np.cos(-theta * np.pi / 180)
y += dist * np.sin(-theta * np.pi / 180)
pos = np.append(pos, [[x, y, theta]], 0)
plt.arrow(x, y, np.cos(-theta * np.pi / 180), np.sin(-theta * np.pi / 180), color='r',
 width=0.01, head_width=0.1) # representar direção do robô

ang = 90; dist = 3 # instrução 5
theta += ang
x += dist * np.cos(-theta * np.pi / 180)
y += dist * np.sin(-theta * np.pi / 180)
pos = np.append(pos, [[x, y, theta]], 0)
plt.arrow(x, y, np.cos(-theta * np.pi / 180), np.sin(-theta * np.pi / 180), color='r',
 width=0.01, head_width=0.1) # representar direção do robô

plt.plot(pos[:,0], pos[:,1])
plt.xlabel("Posição do robô, x [m]")
plt.ylabel("Posição do robô, y [m]")
plt.show()


# b)
x_f = x; y_f = y; theta_f = theta
print("As coordenadas finais do robô são:")
print(" r = ({0:.2f}, ".format(x_f), "{0:.2f})".format(y_f))
print(" ang = {0:.2f}".format(theta_f))


# c)
d = np.sqrt(x_f**2 + y_f**2)

plt.figure(figsize=(6.5,4.5))
plt.axis([-4, 2.5, -4, 0.5])

#ang = np.arcsin(-y_f / d) - theta_f # 1. Rotação <= 360 graus
ang = np.remainder(np.arcsin(-y_f / d) - theta_f, 360) # 1. Rotação ângulo arbitrári
dist = d # 2. Avanço
theta += ang
x += dist * np.cos(-theta * np.pi / 180)
y += dist * np.sin(-theta * np.pi / 180)
pos = np.append(pos, [[x, y, theta]], 0)
print("Instrução de retorno:")
print(" dist = ({0:.2f}, ".format(dist))
print(" ang = {0:.2f}".format(ang))
plt.arrow(x, y, np.cos(-theta * np.pi / 180), np.sin(-theta * np.pi / 180), color='r', 
 width=0.01, head_width=0.1)

plt.plot(pos[:,0], pos[:,1])
plt.xlabel("Posição do robô, x [m]")
plt.ylabel("Posição do robô, y [m]")
plt.show()
