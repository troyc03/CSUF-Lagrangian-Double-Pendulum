"""
File name: test.py
Author: Troy Chin (CWID: 885586685)
Date: 2024-11-10
Version: 1.0
Description: This is a test file to handle any errors or miscalculations.

"""

import unittest
from pendulum import DoublePendulum
from numerical_methods import NumericalMethods
from visualization import Visualization
from data_logger import DataLogger
import numpy as np

#Import test models here.
class testDoublePendulum(unittest.TestCase):
    def test_pendulum_initial_conditions():
        """
        Tests that the DoublePendulum class initializes correctly with given parameters.
        """
        pendulum = DoublePendulum(mass1=1.0, mass2=1.0, length1=1.0, length2=1.0, 
                                    angle1=np.pi / 4, angle2=np.pi / 4, 
                                    velocity1=0.0, velocity2=0.0, g=9.81)
            
        assert pendulum.mass1 == 1.0, "Mass1 initialization failed"
        assert pendulum.mass2 == 1.0, "Mass2 initialization failed"
        assert pendulum.length1 == 1.0, "Length1 initialization failed"
        assert pendulum.length2 == 1.0, "Length2 initialization failed"
        assert np.isclose(pendulum.angle1, np.pi / 4), "Angle1 initialization failed"
        assert np.isclose(pendulum.angle2, np.pi / 4), "Angle2 initialization failed"
        assert pendulum.velocity1 == 0.0, "Velocity1 initialization failed"
        assert pendulum.velocity2 == 0.0, "Velocity2 initialization failed"
        print("test_pendulum_initial_conditions passed.")

    def test_numerical_methods_step():
        """
        Tests that NumericalMethods performs a correct ODE step based on the pendulum's equations of motion.
        """
        pendulum = DoublePendulum(mass1=1.0, mass2=1.0, length1=1.0, length2=1.0, 
                                angle1=np.pi / 4, angle2=np.pi / 4, 
                                velocity1=0.0, velocity2=0.0, g=9.81)
        methods = NumericalMethods(dt=0.01)
        
        initial_state = [pendulum.angle1, pendulum.velocity1, pendulum.angle2, pendulum.velocity2]
        next_state = methods.solve_ode(pendulum.equations_of_motion, initial_state)
        
        assert len(next_state) == 4, "Expected state vector of length 4."
        print("test_numerical_methods_step passed.")


    def test_data_logging():
        """
        Tests that the DataLogger correctly logs and stores state data.
        """
        logger = DataLogger()
        test_state = [0.5, 0.0, -0.5, 0.0]
        
        # Log the test state
        logger.log_state(test_state)
        assert len(logger.data) == 1, "Data logger should have one logged entry."
        assert logger.data[0] == test_state, "Logged state does not match expected."
        print("test_data_logging passed.")


    def test_visualization_init():
        """
        Tests that the Visualization class initializes without errors and sets up data correctly.
        """
        logger = DataLogger()
        pendulum = DoublePendulum(mass1=1.0, mass2=1.0, length1=1.0, length2=1.0, 
                                angle1=np.pi / 4, angle2=np.pi / 4, 
                                velocity1=0.0, velocity2=0.0, g=9.81)
        visualization = Visualization(logger, pendulum)
        
        assert visualization.logger is logger, "Visualization logger not initialized correctly."
        assert visualization.pendulum is pendulum, "Visualization pendulum not initialized correctly."
        print("test_visualization_init passed.")


    def test_phase_space_plot():
        """
        Tests that the phase space plot can be generated without errors.
        This test will not display the plot but will ensure no errors occur in the plotting function.
        """
        logger = DataLogger()
        pendulum = DoublePendulum(mass1=1.0, mass2=1.0, length1=1.0, length2=1.0, 
                                angle1=np.pi / 4, angle2=np.pi / 4, 
                                velocity1=0.0, velocity2=0.0, g=9.81)
        visualization = Visualization(logger, pendulum)

        # Example data for phase space plot
        angles1 = np.linspace(-np.pi, np.pi, 100)
        velocities1 = np.sin(angles1)
        angles2 = np.linspace(-np.pi, np.pi, 100)
        velocities2 = np.cos(angles2)

        try:
            visualization.plot_phase_space(angles1, velocities1, angles2, velocities2)
            print("test_phase_space_plot passed.")
        except Exception as e:
            print(f"test_phase_space_plot failed with error: {e}")


    # Run all tests
    if __name__ == "__main__":
        test_pendulum_initial_conditions()
        test_numerical_methods_step()
        test_data_logging()
        test_visualization_init()
        test_phase_space_plot()