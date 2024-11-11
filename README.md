
# Lagrangian Double Pendulum Lab

This lab explores the motion of a double pendulum using the principles of Lagrangian mechanics, calculus of variations, differential equations, and numerical analysis. The simulation models the chaotic dynamics of the double pendulum system by solving the governing equations both analytically and numerically.

## Project Objectives

- Develop an accurate simulation of a double pendulum using Lagrangian mechanics and numerical analysis techniques.
- Use calculus of variations and differential equations to derive the motion equations both by hand and computationally.
- Implement numerical methods to approximate the solutions to the system's differential equations and visualize the pendulum's motion.

## Tools and Technologies

- **Python**: Main programming language used for this project.
- **Anaconda**: Environment management and package distribution, allowing for easy setup and dependency management.
- **Spyder**: Integrated development environment (IDE) for Python, specifically useful for scientific and engineering computing.

## Key Concepts

- **Lagrangian Mechanics**: Used to derive the equations of motion for the double pendulum. Lagrangian mechanics allows for modeling based on kinetic and potential energy, offering insights into the system's dynamics.
  
- **Calculus of Variations**: Applied to derive the system’s equations by optimizing the action (integral of the Lagrangian), providing a deeper understanding of the physical principles.

- **Differential Equations**: The equations of motion derived are second-order differential equations, which we will solve using both analytical techniques and numerical methods.

- **Numerical Analysis Techniques**: Techniques such as the Euler method and Runge-Kutta methods will be employed to approximate the system's solutions for visualization and data logging purposes.

## Installation

1. **Install Anaconda**: Download and install [Anaconda](https://www.anaconda.com/products/distribution) to manage dependencies and environments.
2. **Install The Required Libraries**:
   
   ```bash
   conda install numpy scipy matplotlib
3. **Create a New Environment**:
   ```bash
   conda create -n double_pendulum python=3.9
4. **Activate the New Environment**
   ```bash
   conda activate double_pendulum
   
## File Structure

- **`main.py`**: The entry point for running the simulation, where you set initial conditions and execute the full simulation (solving the differential equations, visualizing the motion, logging data, etc.).
- **`pendulum.py`**: Contains the core model of the double pendulum, including the equations of motion derived from Lagrangian mechanics and methods to compute the pendulum's state.
- **`numerical_methods.py`**: Implements numerical methods like the Euler method and Runge-Kutta methods to solve the differential equations.
- **`test.py`**: Contains test cases for verifying the correctness of the system's equations, numerical methods, and integration results.
- **`visualization.py`**: Handles rendering the pendulum’s motion using graphical libraries like Matplotlib.
- **`data_logger.py`**: Manages logging and exporting simulation data such as position and velocity over time into a CSV file for further analysis.

## Future Extensions

This lab can be extended to model variations of the double pendulum, such as:

- Introducing external forces.
- Modeling with different damping or friction effects.
- Exploring stability and chaos in similar systems.

This lab combines theoretical derivation and numerical computing to deepen understanding of chaotic systems, making it ideal for students interested in applied physics, engineering, and computational mathematics.


