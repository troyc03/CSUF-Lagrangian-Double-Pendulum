"""
File name: numerical_methods.py
Author: Troy Chin (CWID: 885586685)
Date: 2024-11-10
Version: 1.0
Description: This script contains the attributes for the double pendulum.

"""

import numpy as np
import csv

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
        self.g - 9.81
        
    def initial_conditions(self, angle1, angle2, velocity1, velocity2):
        self.angle1 = angle1
        self.angle2 = angle2
        self.velocity1 = velocity1
        self.velocity2 = velocity2

    def equations_of_motion(self):
        """
        Compute the equations of motion for the double pendulum.
        """
        theta1_dot = self.velocity1
        theta2_dot = self.velocity2
        theta_ddot1 = 0
        theta_ddot2 = 0
        return [theta1_dot, theta2_dot, theta_ddot1, theta_ddot2]

    
    def Lagrangian(self):
        """
        Return Lagrangian function of the double pendulum.
        """
        T = self.kinetic_energy()
        V = self.potential_energy()
        L = T - V
        return L
    
    def compute_state(self, t):
        pass
    
    def kinetic_energy(self):
        pass
    
    def potential_energy(self):
        pass

    def total_energy(self):
        """
        Calculate total energy of the system.
        """
        
        kinetic_energy = self.kinetic_energy()
        potential_energy = self.potential_energy()
        return kinetic_energy + potential_energy
    
    def reset(self):
        pass