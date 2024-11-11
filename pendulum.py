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
        self.g 
        
    def initial_conditions(self, mass1, mass2, length1, length2, angle1, angle2, velocity1, velocity2):
        self.mass1 = mass1
        self.mass2 = mass2
        self.length1 = length1
        self.length2 = length2
        self.angle1 = angle1
        self.angle2 = angle2
        self.velocity1 = velocity1
        self.velocity2 = velocity2

    def equations_of_motion():
        """
        Compute the equations of motion for the double pendulum.
        """
        pass
    
    def Lagrangian(self):
        pass
    
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