"""
File name: main.py
Author: Troy Chin (CWID: 885586685)
Date: 2024-11-10
Version: 1.0
Description: This script is the main entry point for the program.
"""

import numpy as np
import matplotlib.pyplot as plt
from pendulum import DoublePendulum
from numerical_methods import NumericalMethods
from visualization import Visualization

def main():
    """
    Main function to simulate the motion of a double pendulum.
    Initializes parameters and runs the simulation.
    """
    # Initialize parameters
    masses = (1.0, 1.0)  # Masses of the pendulums
    lengths = (1.0, 1.0)  # Lengths of the pendulums
    angles = (np.pi / 4, np.pi / 6)  # Initial angles
    velocities = (0.0, 0.0)  # Initial velocities

    dt = 0.01  # Time step
    t_max = 10  # Max simulation time
    time_steps = int(t_max / dt)

    # Create pendulum and numerical methods instances
    pendulum = DoublePendulum(*masses, *lengths, *angles, *velocities)
    numerical_methods = NumericalMethods(dt)

    # Initialize arrays to store simulation results
    angles1 = np.zeros(time_steps)
    angles2 = np.zeros(time_steps)
    velocities1 = np.zeros(time_steps)
    velocities2 = np.zeros(time_steps)

    # Run the simulation (assuming a method exists in NumericalMethods)
    for i in range(time_steps):
        # Update the pendulum stateUpda
        angles1[i], angles2[i] = pendulum.get_angles()  # Assuming this method returns current angles
        velocities1[i], velocities2[i] = pendulum.get_velocities()  # Assuming this method returns current velocities

if __name__ == "__main__":
    main()