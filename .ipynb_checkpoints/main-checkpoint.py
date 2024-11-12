"""
File name: main.py
Author: Troy Chin (CWID: 885586685)
Date: 2024-11-10
Version: 1.0
Description: This script is the main entry point for the program.
"""

import numpy as np
import matplotlib.pyplot as plt
from pendulum import DoublePendulum
from numerical_methods import NumericalMethods

def main():
    mass1, mass2 = 1.0
    length1, length2 = 1.0
    angle1, angle2 = np.pi / 4, np.pi / 6 # Initialize angles
    velocity1, velocity2 = 0.0, 0.0 # Initialize velocity 

    dt = 0.01 # Time step
    t_max = 10 # Max simulation time
    time_steps = int(t_max / dt) 

    pendulum = DoublePendulum(mass1, mass2, length1, length2, angle1, angle2, velocity1, velocity2)
    numerical_methods = NumericalMethods(dt, time_steps)

    #Simulation arrays
    pass