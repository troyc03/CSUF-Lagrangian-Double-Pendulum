"""
File name: pendulum.py
Author: Troy Chin (CWID: 885586685)
Date: 2024-11-11
Version: 1.2
Description: This script simulates the motion of a double pendulum using the DoublePendulum class.
"""

import numpy as np
import matplotlib.pyplot as plt

class DoublePendulum:
    def __init__(self, mass1: float, mass2: float, length1: float, length2: float, 
                 angle1: float, angle2: float, velocity1: float, velocity2: float):
        self.mass1 = mass1
        self.mass2 = mass2
        self.length1 = length1
        self.length2 = length2
        self.angle1 = angle1
        self.angle2 = angle2
        self.velocity1 = velocity1
        self.velocity2 = velocity2
        self.g = 9.81  # Corrected assignment for gravity

    def initial_conditions(self, angle1: float, angle2: float, velocity1: float, velocity2: float):
        """Set the initial conditions for the pendulum."""
        self.angle1 = angle1
        self.angle2 = angle2
        self.velocity1 = velocity1
        self.velocity2 = velocity2

    def equations_of_motion(self) -> list:
        """
        Compute the equations of motion for the double pendulum.
        Returns:
            list: A list containing angular velocities and accelerations.
        """
        theta1_dot = self.velocity1
        theta2_dot = self.velocity2
        
        # Placeholder for angular accelerations (to be calculated)
        theta_ddot1 = -self.g * (2 * self.mass1 + self.mass2) * np.sin(self.angle1) / (self.length1 * (self.mass1 + self.mass2))
        theta_ddot2 = -self.g * self.mass2 * np.sin(self.angle2) / (self.length2 * self.mass2)

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
        

    def compute_state(self, dt: float):
        """Compute the state of the system after a time step dt."""
        theta1_dot, theta2_dot, theta_ddot1, theta_ddot2 = self.equations_of_motion()
        
        # Update velocities
        self.velocity1 += theta_ddot1 * dt
        self.velocity2 += theta_ddot2 * dt
        
        # Update angles
        self.angle1 += theta1_dot * dt
        self.angle2 += theta2_dot * dt

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