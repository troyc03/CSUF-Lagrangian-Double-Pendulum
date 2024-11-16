"""
File name: pendulum.py
Author: Troy Chin (CWID: 885586685)
Date: 2024-11-12
Version: 1.3
Status: Ready to deliver to customers
Description: This script handles the attributes necessary to build the double pendulum.
"""
import numpy as np

class DoublePendulum:
    def __init__(self, mass1, mass2, length1, length2, angle1, angle2, velocity1, velocity2, g=9.81):
        self.mass1 = mass1
        self.mass2 = mass2
        self.length1 = length1
        self.length2 = length2
        self.angle1 = angle1
        self.angle2 = angle2
        self.velocity1 = velocity1
        self.velocity2 = velocity2
        self.g = g  # Gravitational constant
    
    def initial_conditions(self, mass1, mass2, length1, length2, angle1, angle2, velocity1, velocity2):
        self.mass1 = mass1
        self.mass2 = mass2
        self.length1 = length1
        self.length2 = length2
        self.angle1 = angle1
        self.angle2 = angle2
        self.velocity1 = velocity1
        self.velocity2 = velocity2
        
    def get_angles(self):
        """
        Returns the current angles of the pendulum.
        """
        return self.angle1, self.angle2
    
    def compute_state(self):
        return [self.angle1, self.angle2, self.velocity1, self.velocity2]

    def equations_of_motion(self, t, state):
        angle1, angle2, velocity1, velocity2 = state
        
        delta_theta = angle2 - angle1
        
        # Denominators for the angular acceleration calculations
        den1 = (self.mass1 + self.mass2) * self.length1 - self.mass2 * self.length1 * np.cos(delta_theta)**2
        den2 = (self.length2 / self.length1) * den1

        # Angular accelerations
        theta1_ddot = ((self.mass2 * self.length1 * velocity1**2 * np.sin(delta_theta) * np.cos(delta_theta) +
                         self.mass2 * self.g * np.sin(angle2) * np.cos(delta_theta) +
                         self.mass2 * self.length2 * velocity2**2 * np.sin(delta_theta) -
                         (self.mass1 + self.mass2) * self.g * np.sin(angle1)) / den1)

        theta2_ddot = ((-self.mass2 * self.length2 * velocity2**2 * np.sin(delta_theta) * np.cos(delta_theta) +
                         (self.mass1 + self.mass2) * self.g * np.sin(angle1) * np.cos(delta_theta) -
                         (self.mass1 + self.mass2) * self.length1 * velocity1**2 * np.sin(delta_theta) -
                         (self.mass1 + self.mass2) * self.g * np.sin(angle2)) / den2)

        return [velocity1, theta1_ddot, velocity2, theta2_ddot]

    def step(self, dt):
        derivatives = self.equations_of_motion(0, self.compute_state())
        self.angle1 += derivatives[0] * dt
        self.velocity1 += derivatives[1] * dt
        self.angle2 += derivatives[2] * dt
        self.velocity2 += derivatives[3] * dt

    def get_positions(self) -> tuple:
        x1 = self.length1 * np.sin(self.angle1)
        y1 = -self.length1 * np.cos(self.angle1)
        x2 = x1 + self.length2 * np.sin(self.angle2)
        y2 = y1 - self.length2 * np.cos(self.angle2)
        return x1, y1, x2, y2

    def kinetic_energy(self) -> float:
        v1 = self.length1 * self.velocity1
        v2 = self.length2 * self.velocity2
        T1 = 0.5 * self.mass1 * v1**2
        T2 = 0.5 * self.mass2 * v2**2
        return T1 + T2

    def potential_energy(self) -> float:
        h1 = self.length1 * (1 - np.cos(self.angle1))
        h2 = self.length2 * (1 - np.cos(self.angle2))
        V1 = self.mass1 * self.g * h1
        V2 = self.mass2 * self.g * h2
        return V1 + V2

    def total_energy(self) -> float:
        return self.kinetic_energy() + self.potential_energy()
    
    
    def reset(self):
        self.initial_conditions(0, 0, 0, 0)  # Reset to default initial conditions
