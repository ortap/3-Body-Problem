# -*- coding: utf-8 -*-
"""Phase_Portrait.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K5i8hI3LW1AgXiSryEfahJKwOX9ru7tJ
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq
duration = 100#365.26*24*3600 # s
h = 1e-1 # s

#Function to run RK4 for various initial conditions r0
def RUN(r0):
  e=0.57
  def f(r,t):
    z=r[0]
    v=r[1]
    dzdt=v
    def nle(u):
      return -u+e*np.sin(u)+t
    root= brentq(nle, 0, 2e9)
    r_=.5*(1-e*np.cos(root))
    dvdt=-z/(z**2+r_**2)**(3/2)

    return np.array([dzdt,dvdt],float)

  rpoints= []
  r=r0

  tpoints= np.arange(0,duration,h)
  for t in tpoints:
      neww=r.copy()
      rpoints.append(neww)

      k1 = h*f(r,t)
      k2 = h*f(r+0.5*k1,t+0.5*h)
      k3 = h*f(r+0.5*k2,t+0.5*h)
      k4 = h*f(r+k3,t+h)

      r += (k1+2*k2+2*k3+k4)/6
      rpoints2=np.stack(rpoints)
  return rpoints2 

#Make a list of initial conidtions to plot on the Phae Portrait
initials = np.linspace(-1.7885,1.7885,10)
IC =[]
for i in range(len(initials)):
  Z=RUN(np.array([initials[i],0],float)) #Run the function for each IC.Here the velocity is set to zero
  axes = plt.gca()
  axes.set_xlabel('z')
  axes.set_ylabel('z_dot')
  axes.plot(Z[:, 0], Z[:, 1], label="Planet 1")