"""
File name: test.py
Author: Troy Chin (CWID: 885586685)
Date: 2024-11-10
Version: 1.0
Description: Unit tests for the double pendulum simulation components.
"""

import unittest
import numpy as np
from numerical_methods import NumericalMethods
from data_logger import DataLogger
from pendulum import DoublePendulum

#Import any test models here.

class TestSimulation(unittest.TestCase):
    
    def setUp(self):
        """Set up the test environment before each test."""
        # Initialize parameters for the double pendulum
        self.mass1 = 1.0
        self.mass2 = 1.0
        self.length1 = 1.0
        self.length2 = 1.0
        self.angle1 = np.pi / 4  # 45 degrees
        self.angle2 = np.pi / 6  # 30 degrees
        self.velocity1 = 0.0
        self.velocity2 = 0.0
        self.g = 9.81

        # Create instances of the classes
        self.pendulum = DoublePendulum(
            self.mass1, self.mass2, self.length1, self.length2,
            self.angle1, self.angle2, self.velocity1, self.velocity2, self.g
        )
        self.numerical_methods = NumericalMethods(dt=0.01)
        self.data_logger = DataLogger()

    def test_double_pendulum_initialization(self):
        """Test if the double pendulum initializes with correct parameters."""
        self.assertEqual(self.pendulum.mass1, self.mass1)
        self.assertEqual(self.pendulum.mass2, self.mass2)
        self.assertEqual(self.pendulum.length1, self.length1)
        self.assertEqual(self.pendulum.length2, self.length2)
        self.assertAlmostEqual(self.pendulum.angle1, self.angle1)
        self.assertAlmostEqual(self.pendulum.angle2, self.angle2)

    def test_data_logging(self):
        """Test the data logging functionality."""
        test_data = [self.angle1, self.angle2, self.velocity1, self.velocity2]
        self.data_logger.log_state(test_data)
        
        # Check if data is logged correctly
        logged_data = self.data_logger.data
        self.assertEqual(len(logged_data), 1)  # Check if one entry is logged
        self.assertEqual(logged_data[0], test_data)
        
class TestNumericalMethods(unittest.TestCase):
    
    def setUp(self):
        """Set up the test environment before each test."""
        self.dt = 0.01
        self.methods = NumericalMethods(dt=self.dt)
        self.initial_state = [1.0]  # Initial condition for y(0) = 1
        self.tolerance = 1e-6

    def linear_ode(self, t, y):
        """Linear ODE function: dy/dt = -y."""
        return [-yi for yi in y]

    def test_euler_method(self):
        """Test Euler's Method for solving the linear ODE."""
        result = self.methods.solve_ode(
            self.linear_ode, self.initial_state, method='euler'
            )
        expected = [self.initial_state[0] * (1-self.dt)] #Analytical solution
        self.assertAlmostEqual(result[0], expected[0], delta=1e-3)
        
    def test_runge_kutta(self):
        """Test Runge-Kutta method for solving the linear ODE."""
        result = self.methods.solve_ode(
            self.linear_ode, self.initial_state, method='runge_kutta'
            )
        expected = [self.initial_state[0] * np.exp(-self.dt)]  # Analytical solution
        self.assertAlmostEqual(result[0], expected[0], delta=1e-6)
        
    def test_adaptive_runge_kutta(self):
        """Test Adaptive Runge-Kutta method for solving the linear ODE."""
        result = self.methods.solve_ode(
            self.linear_ode, self.initial_state, method='adaptive_runge_kutta'
            )
        expected = [self.initial_state[0] * np.exp(-self.dt)] #Analytical solution
        self.assertAlmostEqual(result[0], expected[0], delta=1e-6)
        
    def test_midpoint(self):
        result = self.methods.solve_ode(
            self.linear_ode, self.initial_state, method='midpoint'
            )
        expected = [self.initial_state[0] * np.exp(-self.dt)] #Analytical solution
        self.assertAlmostEqual(result[0], expected[0], delta=1e-6)

class TestVisualization(unittest.TestCase):
    pass
        
if __name__ == '__main__':
    unittest.main()

