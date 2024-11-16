"""
File name: main.py
Author: Troy Chin (CWID: 885586685)
Date: 2024-11-12
Version: 1.3
Status: Ready for submission and delivery to customers
Description: This script is the main entry point for the program.
"""

from pendulum import DoublePendulum
from numerical_methods import NumericalMethods
from visualization import Visualization
from data_logger import DataLogger
import numpy as np

def main():
    # Define initial conditions
    mass1, mass2 = 1.0, 1.0
    length1, length2 = 1.0, 0.5
    angle1, angle2 = np.pi / 3, np.pi / 6  # Initial angles in radians
    velocity1, velocity2 = 1.0, 1.0  # Initial angular velocities in radians per second
    g = 9.81

    # Initialize the double pendulum and numerical methods
    pendulum = DoublePendulum(mass1, mass2, length1, length2, angle1, angle2, velocity1, velocity2, g)
    methods = NumericalMethods(dt=0.01)

    # Set up data logger
    logger = DataLogger()

    # Run simulation
    time_steps = 1000
    dt = 0.01
    for t in range(time_steps):
        # Call compute_state correctly
        current_state = pendulum.compute_state()  # Get the current state of the pendulum
        logger.log_state(current_state)  # Log the current state

        # Update the pendulum state
        pendulum.step(dt)  # Update the state using your existing step method

        # Use the current state as the initial conditions for the ODE solver
        next_state = methods.solve_ode(pendulum.equations_of_motion, current_state)

        # Log the next state if needed or print it
        print(next_state)

    # Prepare data for visualization
    angles1 = [state[0] for state in logger.data]
    angles2 = [state[1] for state in logger.data]
    velocities1 = [state[2] for state in logger.data]
    velocities2 = [state[3] for state in logger.data]

    # Create visualization instance and animate
    visualization = Visualization(logger, pendulum, dt)
    visualization.animate(frames=len(logger.data))  # Adjust frames as needed

    # Plot angles and velocities
    visualization.plot_angles_and_velocities(t_max=time_steps * dt, dt=dt,
                                            angles1=angles1,
                                            angles2=angles2,
                                            velocities1=velocities1,
                                            velocities2=velocities2)

    # Plot phase space of pendulum
    visualization.plot_phase_space()
    
    # Save logged data to CSV
    logger.save_to_csv('double_pendulum_data.csv')

if __name__ == "__main__":
    main()