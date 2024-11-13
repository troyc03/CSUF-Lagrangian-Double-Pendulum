"""
File name: visualization.py
Author: Troy Chin (CWID: 885586685)
Date: 2024-11-11
Version: 1.2
Description: This script contains the graphical attributes and optimization attributes for the simulation.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Visualization:
    def __init__(self, logger, pendulum):
        self.logger = logger
        self.pendulum = pendulum
        self.fig, self.ax = plt.subplots()  # Create a figure and axis for the animation
        self.line1, = self.ax.plot([], [], 'o-', lw=2, color='blue')  # Line for the first pendulum
        self.line2, = self.ax.plot([], [], 'o-', lw=2, color='red')   # Line for the second pendulum
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 1)
        self.ax.set_aspect('equal')
        self.ax.grid()

    def init_plot(self):
        """
        Initializes the plot for the double pendulum.
        """
        self.line1, = plt.plot([], [], 'b-', label='Pendulum 1')  # Blue line for the first pendulum
        self.line2, = plt.plot([], [], 'r-', label='Pendulum 2')  # Red line for the second pendulum
        plt.xlim(-2, 2)  # Set x limits
        plt.ylim(-2, 2)  # Set y limits
        plt.grid()
        plt.tight_layout()
        plt.legend()  # Add legend here
        return self.line1, self.line2
    
    def update_plot(self, frame):
        """
        Updates the plot for each frame of the animation.
        """
        # Update the pendulum state for the current frame
        self.pendulum.step(self.dt)  # Assuming you have a method to update the pendulum's state
    
        # Get the current angles from the pendulum
        angle1, angle2 = self.pendulum.get_angles()  # Assuming you have a method to get angles
    
        # Calculate positions of the pendulum bobs
        length1 = self.pendulum.length1
        length2 = self.pendulum.length2
    
        x1 = length1 * np.sin(angle1)
        y1 = -length1 * np.cos(angle1)
        x2 = x1 + length2 * np.sin(angle2)
        y2 = y1 - length2 * np.cos(angle2)

        # Update the line data
        self.line1.set_data([0, x1], [0, y1])
        self.line2.set_data([x1, x2], [y1, y2])
        
        return self.line1, self.line2

    def animate(self, frames, dt):
        """
        Creates the animation for the double pendulum.
        """
        # Set the pendulum properties
        self.pendulum.length1 = 1.0  # Set length of the first pendulum arm
        self.pendulum.length2 = 1.0  # Set length of the second pendulum arm
        self.pendulum.mass1 = 1.0    # Set mass of the first pendulum bob
        self.pendulum.mass2 = 1.0    # Set mass of the second pendulum bob
    
        # Create the animation
        FuncAnimation(self.fig, self.update_plot, frames=frames,
                            init_func=self.init_plot, blit=True, interval=dt * 1000)
    
        plt.title("Double Pendulum Simulation")
        plt.xlabel("X Position (m)")
        plt.ylabel("Y Position (m)")
        plt.show()
            
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

    def plot_phase_space(self):
        """
        Plots the phase space of the double pendulum, showing the relationship
        between angles and angular velocities.
        """
        angles1 = [state[0] for state in self.logger.data]
        angles2 = [state[1] for state in self.logger.data]
        velocities1 = [state[2] for state in self.logger.data]
        velocities2 = [state[3] for state in self.logger.data]
    
        plt.figure(figsize=(12, 8))
    
        # Plot phase space for the first pendulum
        plt.subplot(2, 1, 1)
        plt.plot(angles1, velocities1, label='Pendulum 1 Phase Space', color='b')
        plt.title('Phase Space of Pendulum 1')
        plt.xlabel('Angle (rad)')
        plt.ylabel('Angular Velocity (rad/s)')
        plt.grid()
        plt.legend()
    
        # Plot phase space for the second pendulum
        plt.subplot(2, 1, 2)
        plt.plot(angles2, velocities2, label='Pendulum 2 Phase Space', color='r')
        plt.title('Phase Space of Pendulum 2')
        plt.xlabel('Angle (rad)')
        plt.ylabel('Angular Velocity (rad/s)')
        plt.grid()
        plt.legend()
    
        plt.tight_layout()
        plt.show()