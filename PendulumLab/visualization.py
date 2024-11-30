"""
File name: visualization.py
Author: Troy Chin (CWID: 885586685)
Date: 2024-11-11
Version: 1.3
Status: Ready to deliver to customers. 
Description: This script contains the graphical attributes and optimization attributes for the simulation.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Visualization:
    
    def __init__(self, logger, pendulum, dt):
        """Initialize graphical attributes of the visualization system."""
        self.logger = logger
        self.pendulum = pendulum
        self.dt = dt  # Store dt for use in update_plot
        self.fig, self.ax = plt.subplots()  # Create a figure and axis for the animation
        self.line1, = self.ax.plot([], [], 'o-', lw=2, color='blue')  # Line for the first pendulum
        self.line2, = self.ax.plot([], [], 'o-', lw=2, color='red')   # Line for the second pendulum
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 2)
        self.ax.set_aspect('equal')
        self.ax.grid()

    def init_plot(self):
        """Initialize conditions of the graphical interface."""
        self.line1.set_data([], [])
        self.line2.set_data([], [])
        return self.line1, self.line2
    
    def update_plot(self, frame):
        """Update the pendulum state per frame."""
        # Update the pendulum state for the current frame
        self.pendulum.step(self.dt)  # Update the pendulum's state
    
        # Get the current angles from the pendulum
        angle1, angle2 = self.pendulum.get_angles()  # Get angles in radians
    
        # Calculate positions of the pendulum bobs
        length1 = self.pendulum.length1
        length2 = self.pendulum.length2
    
        # Ensure the lengths are valid
        if length1 <= 0 or length2 <= 0:
            print("Pendulum lengths must be greater than zero.")
            return
    
        x1 = length1 * np.sin(angle1)
        y1 = -length1 * np.cos(angle1)
        x2 = x1 + length2 * np.sin(angle2)
        y2 = y1 - length2 * np.cos(angle2)
    
        # Update the line data
        self.line1.set_data([0, x1], [0, y1])
        self.line2.set_data([x1, x2], [y1, y2])
    
        # Print the positions for debugging
        print(f"Frame: {frame} | Pendulum 1 Position: x1={x1}, y1={y1}")
        print(f"Frame: {frame} | Pendulum 2 Position: x2={x2}, y2={y2}")
    
        return self.line1, self.line2
        return self.line1, self.line2

    def animate(self, frames):
        """Begin animation for the pendulum system."""
        # Initialize the plot before starting the animation
        self.init_plot()
    
        # Create the animation
        ani = FuncAnimation(self.fig, self.update_plot, frames=frames,
                            blit=True, interval=self.dt * 1000)
    
        # Set titles and labels
        self.ax.set_title("Pendulum Movement", fontsize=14)
        self.ax.set_xlabel("X Position (m)", fontsize=12)
        self.ax.set_ylabel("Y Position (m)", fontsize=12)
    
        # Show the plot
        plt.show()
            
    def plot_angles_and_velocities(self, t_max, dt, angles1, angles2, velocities1, velocities2):
        """Plot angles and velocities of the pendulum system."""
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
        
    def plot_phase_space(self):
        """
        Plots the phase space of the double pendulum, showing the relationship
        between angles and angular velocities.
        """
        angles1 = [state[0] for state in self.logger.data]
        angles2 = [state[1] for state in self.logger.data]
        velocities1 = [state[2] for state in self.logger.data]
        velocities2 = [state[3] for state in self.logger.data]
        
        plt.figure(figsize=(12, 6))
    
        # Plot phase space for first pendulum
        plt.subplot(1, 2, 1)
        plt.plot(angles1, velocities1, label='Pendulum 1', color='blue')
        plt.title('Phase Space of Pendulum 1')
        plt.xlabel('Angle (rad)')
        plt.ylabel('Angular Velocity (rad/s)')
        plt.grid()
        plt.axhline(0, color='black', lw=0.5, ls='--')
        plt.axvline(0, color='black', lw=0.5, ls='--')
        plt.legend()
    
        # Plot phase space for second pendulum
        plt.subplot(1, 2, 2)
        plt.plot(angles2, velocities2, label='Pendulum 2', color='red')
        plt.title('Phase Space of Pendulum 2')
        plt.xlabel('Angle (rad)')
        plt.ylabel('Angular Velocity (rad/s)')
        plt.grid()
        plt.axhline(0, color='black', lw=0.5, ls='--')
        plt.axvline(0, color='black', lw=0.5, ls='--')
        plt.legend()
    
        plt.tight_layout()
        plt.show()