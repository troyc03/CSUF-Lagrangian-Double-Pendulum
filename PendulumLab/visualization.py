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

class Visualization:
    def __init__(self, logger):
        self.logger = logger
        self.fig, self.ax = plt.subplots()  # Create a figure and axis for the animation
        self.trajectory = []  # To store the trajectory for the animation
        self.line, = self.ax.plot([], [], 'o-', lw=2)  # Line for the pendulum
        self.trace, = self.ax.plot([], [], 'r-', lw=1)  # Trajectory line

    def visualize_motion(self, data):
        """
        Visualizes the motion of the double pendulum.

        Parameters:
            data: A list of states, where each state is a tuple or list containing angles.
        """
        angle1 = [state[0] for state in data]
        angle2 = [state[1] for state in data]
        
        plt.figure(figsize=(12, 6))
        plt.plot(angle1, label="Angle 1")
        plt.plot(angle2, label="Angle 2")
        plt.xlabel("Time")
        plt.ylabel("Angles (radians)")
        plt.title("Double Pendulum Angles Over Time")
        plt.legend()
        plt.show()

    def update_plot(self, frame):
        """
        Updates the plot for each frame of the animation.
        """
        # Get the current state of the pendulum
        x1, y1, x2, y2 = self.logger.data[frame][4:8]  # Assuming positions are stored in the state
        self.line.set_data([0, x1, x2], [0, y1, y2])
        
        # Update the trajectory
        self.trajectory.append((x2, y2))
        self.trace.set_data(*zip(*self.trajectory))

        return self.line, self.trace

    def init_plot(self):
        """
        Initializes the plot for the animation.
        """
        self.line.set_data([], [])
        self.trace.set_data([], [])
        return self.line, self.trace

    def animate(self, frames, dt):
        """
        Creates the animation for the pendulum.
        """
        ani = animation.FuncAnimation(self.fig, self.update_plot, frames=frames,
                                      init_func=self.init_plot, blit=True, interval=dt * 1000)

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
        plt.figure(figsize=(12, 8))  # Adjusted size

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
        plt.plot(np.arange(0, t_max, dt), velocities1, label='Angular Velocity 1')
        plt.plot(np.arange(0, t_max, dt), velocities2, label='Angular Velocity 2')
        plt.xlabel('Time (s)')
        plt.ylabel('Angular Velocity (rad/s)')
        plt.legend()
        plt.title('Double Pendulum Angular Velocities Over Time')
        
        plt.tight_layout()  # Adjusts subplots to fit into figure area.
        plt.show()