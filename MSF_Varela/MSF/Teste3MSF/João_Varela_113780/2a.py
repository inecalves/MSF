

import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 1
alpha = 0.15

x0 = 2
v0 = 0
b = 0.02

F_0 = 7.5
omega_f = 0

dt = 0.001
t0 = 0
tf = 20

oscillator = lambda x: -k * x -3*(alpha*x**2)# Change me
accel = lambda t, x, v:  oscillator(x)/m - (b/m)*v + (F_0/m)*np.cos(omega_f * t)


n = int((tf-t0) / dt + 0.1)

t = np.zeros(n + 1) 
x = np.zeros(n + 1) 
v = np.zeros(n + 1) 
Em = np.zeros(n + 1) 
Ep = np.zeros(n + 1) 


# Valores inicias
v[0] = v0
t[0] = t0
x[0] = x0


def runge_kutte4(t,x,vx,acelera,dt):
  ax1=acelera(t,x,vx)
  c1v=ax1*dt
  c1x=vx*dt

  ax2=acelera(t+dt/2.,x+c1x/2.,vx+c1v/2.)
  c2v=ax2*dt
  c2x=(vx+c1v/2.)*dt 

  ax3=acelera(t+dt/2.,x+c2x/2.,vx+c2v/2.)
  c3v=ax3*dt
  c3x=(vx+c2v/2.)*dt

  ax4=acelera(t+dt,x+c3x,vx+c3v)
  c4v=ax4*dt
  c4x=(vx+c3v)*dt

  xp=x+(c1x+2.*c2x+2.*c3x+c4x)/6.
  vxp=vx+(c1v+2.*c2v+2.*c3v+c4v)/6.
  return xp,vxp

for i in range(n):
  mx, vx = runge_kutte4(t[i], x[i], v[i], accel, dt)

  v[i + 1] = vx
  x[i + 1] = mx
  t[i + 1] = t[i] + dt
  Ep[i + 1] = 0.5*k*x[i]**2 + alpha*x[i]**3
  Em[i + 1] = Ep[i] + 0.5*mx*v[i]**2 



x_temp = x[t >0]
t_temp = t[t > 0]
v_temp = v[t > 0] 


plt.plot(t, x)
plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.title("Oscilador Quártico Met Runge-Kutta 4ºordem")
plt.xlim(0,20)
plt.ylim(0,5)
plt.grid()
plt.show()
