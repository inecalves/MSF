
from maxminv import maxminv, abfourier
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

plt.rcParams['interactive'] == True
dt = 0.01
m = 1
xeq = 0
g = 9.8

k = 1
b = 0.05
a = 0.002
F0 = 7.5
VForc = 1

t = np.arange(0,600+dt,dt)

x = np.zeros(t.size)
v = np.zeros(t.size)
x[0] = 3
v[0] = 0

for i in range(t.size-1):
    Fx = -k*x[i]*(1+2*a*(x[i]**2))
        
    Fforc = F0*np.cos(VForc*t[i])
    
    Famort = -b*v[i]
    
    ax = (Fx+Fforc+Famort)/m
    
    v[i+1] = v[i] + ax*dt
    x[i+1] = x[i] + v[i+1]*dt
plt.plot(t[55500:], x[55500:])
ind_peaks = find_peaks(x)[0]
n = np.arange(0,11,1)
Aaf = np.zeros(n.size)
Abf = np.zeros(n.size)
tmax = np.zeros(ind_peaks.size)
angmax = np.zeros(ind_peaks.size)

for i in range(tmax.size):
    k = ind_peaks[i]
    tmax[i], angmax[i] = maxminv(t[k-1],t[k],t[k+1],x[k-1],x[k],x[k+1])
    
Ang_Num = angmax[-1]
T_Num = (tmax[-1]-tmax[-2])
print("\nA amplitdue é {:0.5f}º".format(Ang_Num))
print("\nO periodo é {:0.5f}s".format(T_Num))
for i in range(n.size):
    Aaf[i],Abf[i] = abfourier(t, x, ind_peaks[-2], ind_peaks[-1], i)

print("\n{:^15}{:^15}{:^15}{:^15}".format("n","an","bn","sqrt(an^2+bn^2)"))
for i in range(n.size):
    print("{:^15}{:^15.5f}{:^15.5f}{:^15.5f}".format(n[i],Aaf[i],Abf[i],np.sqrt(Aaf[i]**2+Abf[i]**2)))
values = np.zeros(t.size)