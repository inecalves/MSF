'''
Maria Inês Gonçalves
124754
'''

import numpy as np
import matplotlib.pyplot as plt

dt = 0.001
t = np.arange(0,300+dt,dt)

ax = np.zeros(t.size)
vx = np.zeros(t.size)
x = np.zeros(t.size)

u = 0.005               # coeficiente de resistencia de rolamento
Cres = 0.8              # coeficiente de resistencia do ar
area = 0.3              # area frontal [m^2]
Par = 1.225             # densidade do ar [kg/m^3]
m = 75                  # massa do ciclista + bicicleta [kg]
Potencia = 250          # potencia do ciclista [W]
vx[0] = 2               # velocidade inicial dada pelo empurrão [m/s]
g = 9.8
N= m*g                  #N=P = m*g

for i in range(t.size-1):
    Fcic = Potencia/vx[i] 
    FRes = -(Cres/2)*area*Par*vx[i]**2 
    FRol = u*N          #Força de resistencia ao rolamento Frol= u*N=u*m*g
    F = Fcic + FRes - FRol

    ax[i] = F/m  
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i]*dt

# Velocidade Terminal

print("Velocidade Terminal: " + str(vx[vx.argmax()]))

#R: a velocidade terminal é aproximadamente 11.24 m/s

# Tempo para percorrer 3 km
idx_3km = np.where(x >= 3000)[0]
t_3km = t[idx_3km[0]] if len(idx_3km) > 0 else np.nan

print(f"Tempo para percorrer 3 km: {t_3km:.1f} s ({t_3km/60:.1f} min)")

#R: demora aproximadamente 276.5 s (4.6 min) a percorrer 3 km