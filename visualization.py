"""
File name: visualization.py
Author: Troy Chin (CWID: 885586685)
Date: 2024-11-11
Version: 1.2
Description: This script contains the graphical attributes and optimization attributes for the simulation.

"""

import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from pendulum import DoublePendulum
from numerical_methods import NumericalMethods

# Import any models here.
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
        self.line, = self.ax.plot([], [], 'o-', lw=2)
        self.trace, = self.ax.plot([], [], color='gray', alpha=0.5)
        self.trajectory = []

    def init_plot(self):
        """
        Initializes the plot area and lines for the animation.
        """
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 2)
        self.ax.set_aspect('equal')
        return self.line, self.trace

    def update_plot(self, frame):
        """
        Updates the plot for each frame of the animation.
        """
        # Get the current state of the pendulum
        x1, y1, x2, y2 = self.pendulum.get_positions()  # Assuming this method exists
        self.line.set_data([0, x1, x2], [0, y1, y2])
        
        # Update the trajectory
        self.trajectory.append((x2, y2))
        self.trace.set_data(*zip(*self.trajectory))

        return self.line, self.trace

    def animate(self, frames):
        """
        Creates the animation for the pendulum.
        """
        ani = animation.FuncAnimation(self.fig, self.update_plot, frames=frames,
                                      init_func=self.init_plot, blit=True, interval=self.dt * 1000)
        # Plotting the results

