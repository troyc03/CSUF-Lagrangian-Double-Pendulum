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

    def plot_angles_and_velocities(self, t_max, dt, angles1, angles2, velocities1, velocities2):
        """
        Plots the angles and velocities of the double pendulum over time.

        Parameters:
            - t_max: The maximum time for the simulation.
            - dt: The time step for the simulation.
            - angles1: The angles of the first pendulum.
            - angles2: The angles of the second pendulum.
            - velocities1: The velocities of the first pendulum.
            - velocities2: The velocities of the second pendulum.
        """
        plt.figure(figsize=(12, 6))

        # Plot angles
        plt.subplot(2, 1, 1)
        plt.plot(np.arange(0, t_max, dt), angles1, label='Angle 1 (rad)')
        plt.plot(np.arange(0, t_max, dt), angles2, label='Angle 2 (rad)')
        plt.title('Double Pendulum Angles Over Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Angle (rad)')
        plt.legend()

        # Plot velocities
        plt.subplot(2, 1, 2)
        plt.plot(np.arange(0, t_max, dt), velocities1, label='Velocity 1 (rad/s)')
        plt.plot(np.arange(0, t_max, dt), velocities2, label='Velocity 2 (rad/s)')
        plt.title('Double Pendulum Velocities Over Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Velocity (rad/s)')
        plt.legend()

        plt.tight_layout()
        plt.show()