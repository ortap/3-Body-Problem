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

class Mass():
    def __init__(self, radius, color):
        self.sphere = sphere(make_trail=True, trail_type = "points", interval = 100, retain = 8000, trail_radius = 0.1)
        self.sphere.color = color
        # self.omega =
        self.sphere.radius = radius
        self.animate([0,0,0])

    def animate(self, r):
        # theta = self.omega*t
        # position = exp(1j*theta)
        self.sphere.pos = vector(r[0],r[1],r[2])

if __name__ == "__main__":
    try:
        m1 = float(input("mass of Planet 1? (default: Mass of Sun - 1.99e30) \n"))
    except ValueError:
        m1 = 1.99e30
    # try:
    #     r1 = float(input("location of Planet 1? (default: Mass of Sun - 1.99e30) \n"))
    # except ValueError:
    #     print(error)
    #     m1 = 1.99e30
    # try:
    #     m1 = float(input("mass of Planet 1? (default: Mass of Sun - 1.99e30) \n"))
    # except ValueError:
    #     print(error)
    #     m1 = 1.99e30

    try:
        m2 = float(input("mass of Planet 2? (default: Mass of Sun - 1.99e30) \n"))
    except ValueError:
        m2 = m1
    try:
        m3 = float(input("mass of Planet 3? (default: 0) \n"))
    except ValueError:
        m3 = 0

    # def GOT_VALUES():
    #     application_window = tk.Tk()
    #     m1 = simpledialog.askinteger("Input","Enter mass 1", parent=application_window,
    #                                  minvalue=0, maxvalue=100)
    # gal = threading.Thread(target=GOT_VALUES)
    # gal.start()
    # print(m1)
    # if m1:
    #     GOT_VALUES = True
    # if GOT_VALUES:
    scene = canvas(title="animation", width = 1000, height = 1000, range = 15)
    # scene.width = 1000
    # scene.height = 1000
    # scene.range = 15
    # scene.title = "Woah! This looks very pretty!
    # start = False
    running = True

    # def Start(a):
    #     global start
    #     start = not start
    #     if start: a.text = "STOP"
    #     else: a.text = "START"

    def Run(b):
        global running
        running = not running
        if running: b.text = "Pause"
        else: b.text = "Run"


    def three_body_problem(m1, m2, m3):

        print(m1, m2, m3)
        # m_1 = winput(bind=three_body_problem, text="1000")
        m1 = m1 #1.99e30
        # print(m1)
        # print(m1, type(m1)) #1.99e30# 1.99e30 # Mass of Sun [kg]
        m2 = m2 #5.97e24 # Mass of Earth [kg]
        m3 = m3 # Mass of Moon [kg]
        G = 6.67e-11 # m^3/kg-s^2

        duration = 10*365.26*24*3600 # s
        h = 2*3600 # s
        num_steps = int(duration / h)
        # print(num_steps)
        times = h*np.array(range(num_steps + 1))
        orbit_v = -1*np.sqrt(G*m1/(2e11))
        # print("orbi_V", orbit_v)
        # three indices: timestep idx, mass idx, xyz
        r = np.zeros([num_steps + 1, 3, 3]) # m
        v = np.zeros([num_steps + 1, 3, 3]) # m/s
        #r[0] = np.array([[-2., 0., 0.], [1., 0., 0.], [0., 0., 1.]]) * 1e11
        r[0] = np.array([[-1., 0., 0.], [1., 0., 0.], [0., 0., 1.]]) * 1e11
        # v[0] = np.array([[0., -1000, 0.], [0., 1000, 0.], [0., 0., 0.]]) * 1e3
        v[0] = np.array([[0., -1*np.sqrt(G*m1/(2e11))/2e3, 0.], [0., np.sqrt(G*m1/(2e11))/2e3, 0.], [0., 0., 0.]]) * 1e3
        # print(r[0][0], v[0])

        def acceleration(r):
            a = np.zeros([3,3])
            a[0] = G*m2/np.linalg.norm(r[0]-r[1])**3*(r[1]-r[0])+G*m3/np.linalg.norm(r[0]-r[2])**3*(r[2]-r[0])
            a[1] = G*m1/np.linalg.norm(r[1]-r[0])**3*(r[0]-r[1])+G*m3/np.linalg.norm(r[1]-r[2])**3*(r[2]-r[1])
            a[2] = G*m1/np.linalg.norm(r[2]-r[0])**3*(r[0]-r[2])+G*m2/np.linalg.norm(r[2]-r[1])**3*(r[1]-r[2])
            return a
        for step in range(num_steps):
            r[step+1] = r[step] + h*v[step]
            v[step+1] = v[step] + h*acceleration(r[step+1])

        return r, v

    # scene.caption = "Enter Mass of Planet 1: \n\n"
    # while 1:
    # m_1 = winput(bind=three_body_problem, text=1000)
    # print(m_1.number)
    # if m_1.number is not None:
    #     break
    # m_1 = winput(bind=three_body_problem)
    # print(m_1.number)
    # b1 = button(text="Start", bind=Start)
    b2 = button(text="Pause", bind=Run)
    # sl = slider(min=0, max=3, value=1.5, length=220, bind=mass_one, right=15)
    # wt = wtext(text='{:1.2f}'.format(sl.value))
    # print(m1, m2, m3)
    r, v = three_body_problem(m1, m2, m3)


    poincare = graph(title="Poincare/Phase Map", xtitle='z', ytitle='z_dot', fast=False, width=1000)
    funct3 = gdots(color=color.red, size=6, label='dots', radius = 1)


    planets = []
    planet1 = Mass(radius = 0.5, color = color.blue)
    planet2 = Mass(radius = 0.5, color = color.blue)
    planet3 = Mass(radius = 0.3, color = color.red)
    planets.append(planet1)
    planets.append(planet2)
    planets.append(planet3)



    t = 0
    while True:
        rate(100)
        if running:
          planet1.animate(r[t,0,:]/1e10)
          planet2.animate(r[t,1,:]/1e10)
          planet3.animate(r[t,2,:]/1e10)
          # funct1.plot( t, 5.0+5.0*cos(-0.2*t)*exp(0.015*t) )
          funct3.plot(r[t,2,2], v[t,2,2])
          t+=1

    userspin  = 1
