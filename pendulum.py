"""
File name: numerical_methods.py
Author: Troy Chin (CWID: 885586685)
Date: 2024-11-10
Version: 1.0
Description: This script contains the attributes for the double pendulum.

"""

import numpy as np

class DoublePendulum():
    # Import class attributes here.
    def __init__(self, mass1, mass2, length1, length2, angle1, angle2, velocity1, velocity2):
        self.mass1 = mass1
        self.mass2 = mass2
        self.length1 = length1
        self.length2 = length2
        self.angle1 = angle1
        self.angle2 = angle2
        self.velocity1 = velocity1
        self.velocity2 = velocity2

    def Lagrangian(self):
        """
        Return the Lagrangian function of the double pendulum.
        """
        T = self.kinetic_energy()
        V = self.potential_energy()
        return T - V

    def equations_of_motion():
        """
        Return Euler-Lagrange equations of the double pendulum.
        """
        pass

    def compute_state():
        """
        Compute the state of the system (angles, velocities, positions) at a given time t.
        """
        pass

    def kinetic_energy(self):
        """
        Compute the total kinetic energy of the double pendulum system.
        """
        # Using the formula T = (1/2) * m * v^2 for both pendulums
        v1 = self.velocity1
        v2 = self.velocity2
        T = 0.5 * self.mass1 * (self.length1 * v1)**2 + 0.5 * self.mass2 * (self.length2 * v2)**2
        return T

    def potential_energy(self):
        """
        Compute the total potential energy of the double pendulum system.
        """
        g = 9.81  # gravitational acceleration
        h1 = self.length1 * (1 - np.cos(self.angle1))
        h2 = self.length2 * (1 - np.cos(self.angle2))
        V = self.mass1 * g * h1 + self.mass2 * g * h2
        return V

    def position(self):
        """
        Calculate the position of the pendulum masses (x, y) at any given time.
        """
        x1 = self.length1 * np.sin(self.angle1)
        y1 = -self.length1 * np.cos(self.angle1)
        x2 = self.length2 * np.sin(self.angle2)
        y2 = -self.length2 * np.cos(self.angle2)
        return (x1, y1), (x2, y2)
    
    def check_energy_conservation():
        pass
