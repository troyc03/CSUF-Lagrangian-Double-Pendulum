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

    def __init__(self, logger, pendulum):
        """
        Initializes the visualization class.

        Parameters:
            logger: An instance of the data logging class.
            pendulum: An instance of the DoublePendulum class to retrieve state data.
        """
        self.logger = logger
        self.pendulum = pendulum
        self.trajectory = []
        
    def visualize_motion(self, data):
        """
        Visualizes the motion of the double pendulum by plotting angles over time.

        Parameters:
            data: A list of states, where each state contains the angles.
        """
        angle1 = [state[0] for state in data]
        angle2 = [state[1] for state in data]
        
        plt.figure(figsize=(12, 6))
        plt.plot(angle1, label="Angle 1")
        plt.plot(angle2, label="Angle 2")
        plt.xlabel("Time")
        plt.ylabel("Angles (radians)")
        plt.title("Double Pendulum Motion")
        plt.legend()
        plt.show()

    def init_plot(self):
        """
        Initializes the animation plot by setting up figure, axes, and initial line.
        """
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 2)
        self.line, = self.ax.plot([], [], 'o-', lw=2, label="Double Pendulum")
        self.trace, = self.ax.plot([], [], 'r-', lw=1, label="Trace")
        self.ax.legend()
        return self.line, self.trace

    def update_plot(self, frame):
        """
        Updates the plot for each frame of the animation.
        """
        # Get the current state of the pendulum
        x1, y1, x2, y2 = self.pendulum.get_positions()
        self.line.set_data([0, x1, x2], [0, y1, y2])

        # Update the trajectory trace
        self.trajectory.append((x2, y2))
        self.trace.set_data(*zip(*self.trajectory))

        return self.line, self.trace

    def animate(self, frames, dt=0.05):
        """
        Creates the animation for the pendulum.

        Parameters:
            frames: Number of frames to animate.
            dt: Time interval between frames (in seconds).
        """
        ani = animation.FuncAnimation(self.fig, self.update_plot, frames=frames,
                                      init_func=self.init_plot, blit=True, interval=dt * 1000)
        plt.show()  # Show the animation

    def plot_angles_and_velocities(self, t_max, dt, angles1, angles2, velocities1, velocities2):
        """
        Plots the angles and velocities of the double pendulum over time.

        Parameters:
            - t_max: Maximum simulation time.
            - dt: Time step of the simulation.
            - angles1, angles2: Arrays of angles for each pendulum.
            - velocities1, velocities2: Arrays of angular velocities.
        """
        time_array = np.arange(0, t_max, dt)

        plt.figure(figsize=(12, 8))

        # Plot angles
        plt.subplot(2, 1, 1)
        plt.plot(time_array, angles1, label='Angle 1 (rad)')
        plt.plot(time_array, angles2, label='Angle 2 (rad)')
        plt.xlabel('Time (s)')
        plt.ylabel('Angle (rad)')
        plt.title('Double Pendulum Angles Over Time')
        plt.legend()

        # Plot velocities
        plt.subplot(2, 1, 2)
        plt.plot(time_array, velocities1, label='Angular Velocity 1')
        plt.plot(time_array, velocities2, label='Angular Velocity 2')
        plt.xlabel('Time (s)')
        plt.ylabel('Angular Velocity (rad/s)')
        plt.legend()
        plt.title('Double Pendulum Angular Velocities Over Time')
        
        plt.tight_layout()  # Adjust layout to avoid overlap
        plt.show()
