"""
File name: main.py
Author: Troy Chin (CWID: 885586685)
Date: 2024-11-12
Version: 1.2
Description: This script is the main entry point for the program.
"""

from pendulum import DoublePendulum
from numerical_methods import NumericalMethods
from visualization import visualize_motion
from data_logger import DataLogger

def main():
    # Define initial conditions
    mass1, mass2 = 1.0, 1.0
    length1, length2 = 1.0, 1.0
    angle1, angle2 = 1.0, 0.5  # Initial angles in radians
    velocity1, velocity2 = 0.0, 0.0  # Initial angular velocities in radians per second
    g = 9.81

    # Initialize the double pendulum and numerical methods
    pendulum = DoublePendulum(mass1, mass2, length1, length2, angle1, angle2, velocity1, velocity2, g)
    methods = NumericalMethods(dt=0.01)

    # Set up data logger
    logger = DataLogger()

    # Run simulation
    time_steps = 100
    for t in range(time_steps):
        # Compute the current state of the pendulum
        current_state = pendulum.compute_state(t * methods.dt)
        logger.log_state(current_state)

        # Use the current state as the initial conditions for the ODE solver
        next_state = methods.solve_ode(pendulum.equations_of_motion, current_state)

        # Log the next state if needed or print it
        print(next_state)

    # Visualize the motion
    visualize_motion(logger.data)

    # Save logged data to CSV
    logger.save_to_csv('double_pendulum_data.csv')

if __name__ == "__main__":
    main()
