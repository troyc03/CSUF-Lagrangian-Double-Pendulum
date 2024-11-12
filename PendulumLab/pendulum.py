"""
File name: pendulum.py
Author: Troy Chin (CWID: 885586685)
Date: 2024-11-12
Version: 1.2
Description: This script handles the attributes necessary to build the double pendulum.
"""

import numpy as np

class DoublePendulum:
    def __init__(self, mass1, mass2, length1, length2, angle1, angle2, velocity1, velocity2, g):
        self.mass1 = mass1
        self.mass2 = mass2
        self.length1 = length1
        self.length2 = length2
        self.angle1 = angle1
        self.angle2 = angle2
        self.velocity1 = velocity1
        self.velocity2 = velocity2
        self.g = g  # Gravitational constant

    def initial_conditions(self, angle1: float, angle2: float, velocity1: float, velocity2: float):
        """Set the initial conditions for the pendulum."""
        self.angle1 = angle1
        self.angle2 = angle2
        self.velocity1 = velocity1
        self.velocity2 = velocity2

    def equations_of_motion(self, t, state) -> list:
        """
        Compute the equations of motion for the double pendulum.
        Args:
            t (float): Time variable.
            state (list): A list containing [theta1, theta2, theta1_dot, theta2_dot].

        Returns:
            list: A list containing angular velocities and accelerations.
        """
        theta1, theta2, theta1_dot, theta2_dot = state
        
        # Example usage of `t` if there's a time-dependent external force (this is just hypothetical)
        external_force = np.cos(t)  # Hypothetical time-dependent force for demonstration

        # Compute angular accelerations based on the current state and external force
        theta_ddot1 = -self.g * (2 * self.mass1 + self.mass2) * np.sin(theta1) / (self.length1 * (self.mass1 + self.mass2)) + external_force
        theta_ddot2 = -self.g * self.mass2 * np.sin(theta2) / (self.length2 * self.mass2) + external_force

        return [theta1_dot, theta2_dot, theta_ddot1, theta_ddot2]



    def Lagrangian(self) -> float:
        """
        Return the Lagrangian function of the double pendulum.
        Returns:
            float: The Lagrangian of the system.
        """
        T = self.kinetic_energy()
        V = self.potential_energy()
        L = T - V
        return L

    def get_angles(self) -> tuple:
       """
       Return the current angles of the pendulum.
       """
       return self.angle1, self.angle2

    def get_velocities(self) -> tuple:
       """
       Return the current angular velocities of the pendulum.
       """
       return self.velocity1, self.velocity2

    def get_positions(self) -> tuple:
       """
       Calculate and return the (x, y) positions of the pendulum masses.
       """
       x1 = self.length1 * np.sin(self.angle1)
       y1 = -self.length1 * np.cos(self.angle1)
       x2 = x1 + self.length2 * np.sin(self.angle2)
       y2 = y1 - self.length2 * np.cos(self.angle2)
       return x1, y1, x2, y2
        

    def compute_state(self, t):
        # Define the current state here as a list [theta1, theta2, theta1_dot, theta2_dot]
        state = [self.angle1, self.angle2, self.velocity1, self.velocity2]
        
        # Pass both 't' and 'state' to equations_of_motion
        theta1_dot, theta2_dot, theta_ddot1, theta_ddot2 = self.equations_of_motion(t, state)
        
        # Update the angles and velocities based on the computed accelerations
        # (Your update logic would go here)
        
        return theta1_dot, theta2_dot, theta_ddot1, theta_ddot2

    def kinetic_energy(self) -> float:
        """Calculate the kinetic energy of the system."""
        # Calculate the velocities of the masses
        v1 = self.length1 * self.velocity1  # Linear velocity of mass1
        v2 = self.length2 * self.velocity2  # Linear velocity of mass2
        T1 = 0.5 * self.mass1 * v1**2
        T2 = 0.5 * self.mass2 * v2**2
        return T1 + T2

    def potential_energy(self) -> float:
        """Calculate the potential energy of the system."""
        # Calculate the heights of the masses
        h1 = self.length1 * (1 - np.cos(self.angle1))  # Height of mass1
        h2 = self.length2 * (1 - np.cos(self.angle2))  # Height of mass2
        V1 = self.mass1 * self.g * h1
        V2 = self.mass2 * self.g * h2
        return V1 + V2

    def total_energy(self) -> float:
        """
        Calculate the total energy of the system.
        Returns:
            float: The total energy (kinetic + potential).
        """
        kinetic_energy = self.kinetic_energy()
        potential_energy = self.potential_energy()
        return kinetic_energy + potential_energy

    def reset(self):
        """Reset the pendulum to its initial state."""
        self.initial_conditions(0, 0, 0, 0)  # Reset to default initial conditions