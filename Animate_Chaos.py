import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint
from vpython import *
import tkinter as tk
from tkinter import simpledialog
import string
import threading
from scipy.optimize import brentq
import numpy as np
from tempfile import TemporaryFile
from numpy import loadtxt
#Load the saved data that you want to animate, make sure it's in the same folder
zz1=loadtxt('rpoints2t.txt',float)
zz2=loadtxt('rpoints3t.txt',float)
class Mass():
    def __init__(self, radius, color):
        self.sphere = sphere(make_trail=True, retain = 10000, trail_color= vector(1,0,0))
        self.sphere.color = color
        self.sphere.radius = radius
        self.animate([0,0,0])

    def animate(self, r):
        self.sphere.pos = vector(r[0],r[1],r[2])

if __name__ == "__main__":
    m1 = 1.99e30
    scene = canvas(title="animation", width = 2000, height = 2000, range = 15, background=color.white)
    duration = 1000
    h = 1e-2 # s

    planets = []
    planet1 = Mass(radius = 1,color = color.blue)
    planet2 = Mass(radius = 1, color = color.red)
    planets.append(planet1)

    t = 0
    while True:
        rate(1000) #Speed of animation
        planet1.animate((0,0,zz1[t,0]))#)
        planet2.animate((0,0,zz2[t,0]))
        t+=1

    userspin  = 1
