# -*- coding: utf-8 -*-
"""Sitnikov_Simplectic_shai.ipynb


Original file is located at
    https://colab.research.google.com/drive/1Wp_HTXGh_HhfXaT-NFKRzZhNJp3Ohb67
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

from scipy.integrate import odeint

m1 = 1.99e30 # 1.99e30 # Mass of Sun [kg]
m2 = 1.99e30 #5.97e24 # Mass of Earth [kg]
m3 = 0 # Mass of Moon [kg]
G = 6.67e-11 # m^3/kg-s^2

duration = 10*365.26*24*3600 # s
h = 2*3600 # s
num_steps = int(duration / h)
print(num_steps)
times = h*np.array(range(num_steps + 1))

def three_body_problem():
    orbit_v = -1*np.sqrt(G*m1/(2e11))
    print("orbi_V", orbit_v)
    # three indices: timestep idx, mass idx, xyz
    r = np.zeros([num_steps + 1, 3, 3]) # m
    v = np.zeros([num_steps + 1, 3, 3]) # m/s
    r[0] = np.array([[-1., 0., 0.], [1., 0., 0.], [0., 0., 1.]]) * 1e11
    v[0] = np.array([[0., -1*np.sqrt(G*m1/(1e11))/2e3, 0.], [0., np.sqrt(G*m1/(1e11))/2e3, 0.], [0., 0., 0.]]) * 1e3
    print(r[0][0], v[0])
    
    def acceleration(r):
        a = np.zeros([3,3])
        a[0] = G*m2/np.linalg.norm(r[0]-r[1])**3*(r[1]-r[0])+G*m3/np.linalg.norm(r[0]-r[2])**3*(r[2]-r[0])
#         print(a[0].shape)
        a[1] = G*m1/np.linalg.norm(r[1]-r[0])**3*(r[0]-r[1])+G*m3/np.linalg.norm(r[1]-r[2])**3*(r[2]-r[1])
        a[2] = G*m1/np.linalg.norm(r[2]-r[0])**3*(r[0]-r[2])+G*m2/np.linalg.norm(r[2]-r[1])**3*(r[1]-r[2])
        return a
## Used simplectic euler - https://en.wikipedia.org/wiki/Semi-implicit_Euler_method

    for step in range(num_steps):      
        r[step+1] = r[step] + h*v[step]
        v[step+1] = v[step] + h*acceleration(r[step+1]) 
        print(r[step])
    return r, v

r, v = three_body_problem()

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(r[:, 0, 0], r[:, 0, 1], r[:, 0, 2], label="Sun")
ax.plot(r[:, 1, 0], r[:, 1, 1], r[:, 1, 2], label="Earth")
ax.plot(r[:, 2, 0], r[:, 2, 1], r[:, 2, 2], label="Moon")
ax.legend()
ax.set_xlabel('x in m')
ax.set_ylabel('y in m')
ax.set_zlabel('z in m')
ax.axis('equal')

#########################################################
# Plot 2 D
#########################################################
axes2 = plt.gca()
axes2.set_xlabel('x in m')
axes2.set_ylabel('y in m')
axes2.plot(r[:, 0, 0], r[:, 0, 1], label="Sun")
axes2.plot(r[:, 1, 0], r[:, 1, 1], label="Earth")
axes2.plot(r[:, 2, 0], r[:, 2, 1], label="Moon")
plt.axis('equal')
plt.legend()

#########################################################
# Plot 1-D wrt time
#########################################################
axes3 = plt.gca()
axes3.set_xlabel('time')
axes3.set_ylabel('z3')
axes3.plot( times,r[:, 2, 2], label="Moon")



