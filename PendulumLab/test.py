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
# from visualization import Visualization
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

    # def test_numerical_integration(self):
    #     """Test numerical integration of the pendulum's equations of motion."""
        # initial_conditions = [self.angle1, self.angle2, self.velocity1, self.velocity2]
        # time_span = np.linspace(0, 10, 100)  # 10 seconds, 100 steps
        # result = self.numerical_methods.solve_ode(self.pendulum.equations_of_motion, initial_conditions)

        # # Check if the result is of the expected shape
        # self.assertEqual(result.shape[0], 100)  # 100 time steps
        # self.assertEqual(result.shape[1], 4)    # 4 state variables

    def test_data_logging(self):
        """Test the data logging functionality."""
        test_data = [self.angle1, self.angle2, self.velocity1, self.velocity2]
        self.data_logger.log_state(test_data)
        
        # Check if data is logged correctly
        logged_data = self.data_logger.data
        self.assertEqual(len(logged_data), 1)  # Check if one entry is logged
        self.assertEqual(logged_data[0], test_data)

    # def test_visualization_plot(self):
        # """Test if the visualization can create a plot without errors."""
        # angles1 = [self.angle1]
        # angles2 = [self.angle2]
        # velocities1 = [self.velocity1]
        # velocities2 = [self.velocity2]
        
        # # This will not actually show a plot in a test environment, but will check for errors
        # try:
        #     visualization = Visualization(self.data_logger, self.pendulum, dt=0.01)
        #     visualization.plot_angles_and_velocities(t_max=10, dt=0.01,
        #                                             angles1=angles1,
        #                                             angles2=angles2,
        #                                             velocities1=velocities1,
        #                                             velocities2=velocities2)
        # except Exception as e:
        #     self.fail(f"Visualization plotting failed with exception: {e}")

if __name__ == '__main__':
    unittest.main()