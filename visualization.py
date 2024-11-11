"""
File name: visualization.py
Author: Troy Chin (CWID: 885586685)
Date: 2024-11-10
Version: 1.0
Description: This script contains the graphical attributes and optimization attributes for the simulation.

"""

import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

#Import any models here.
class Visualization():
    """
    Parameters:
        - pendulum: The DoublePendulum instance containing mass, length, and angle data
        - dt: Time step for the simulation (default is 0.01)
    """
    def __init__(self, pendulum, dt=0.01):
        self.pendulum = pendulum
        self.dt = dt
        self.fig, self.ax = plt.subplots()
        self.line = self.ax.plot([],[], 'o-', lw=2)
        self.trace = self.ax.plot([],[], color='gray', alpha=0.5)

    def init_plot(self):
        """
        Initializes the plot area and lines for the animation.
        """
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 2)
        self.ax.set_aspect('equal')
        return self.line, self.trace

