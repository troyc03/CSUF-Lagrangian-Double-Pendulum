"""
File name: main.py
Author: Troy Chin (CWID: 885586685)
Date: 2024-11-12
Version: 1.2
Description: This script is the main entry point for the program.
"""

from pendulum import DoublePendulum
from numerical_methods import NumericalMethods
from visualization import Visualization
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
    time_steps = 1000
    dt = 0.01
    for t in range(time_steps):
        # Call compute_state correctly
        current_state = pendulum.compute_state()  # or compute_state(t * methods.dt) if modified
        logger.log_state(current_state)

        # Update the pendulum state
        pendulum.step(dt)  # Update the state using your existing step method

        # Use the current state as the initial conditions for the ODE solver
        next_state = methods.solve_ode(pendulum.equations_of_motion, current_state)

        # Log the next state if needed or print it
        print(next_state)

    # After collecting data in logger, you can visualize and animate it as follows:
    visualization = Visualization(logger, pendulum)

    # Animate the double pendulum's movement
    visualization.animate(frames=len(logger.data), dt=0.05)  # Adjust frames and dt as needed

    # Plot angles and velocities
    visualization.plot_angles_and_velocities(t_max=time_steps * dt, dt=dt,
                                            angles1=[state[0] for state in logger.data],
                                            angles2=[state[1] for state in logger.data],
                                            velocities1=[state[2] for state in logger.data],
                                            velocities2=[state[3] for state in logger.data])
    
    # Plot phase space
    visualization.plot_phase_space()  # Call the new phase space plotting function
    
    # Save logged data to CSV
    logger.save_to_csv('double_pendulum_data.csv')

if __name__ == "__main__":
    main()