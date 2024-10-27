# Lagrangian-Double-Pendulum-Redux-II

## Overview
The Lagrangian Double Pendulum is a simulation tool designed to explore the dynamics of a double pendulum using both manual calculations based on calculus of variations and numerical methods for solving differential equations. This project aims to demonstrate chaotic behavior and simple harmonic motion in the context of a double pendulum system.

## Install Instructions
To set up this project using Anaconda, follow these steps:

1. **Install Anaconda**: If you haven't already, download and install Anaconda from [anaconda.com](https://www.anaconda.com/products/distribution).

2. **Create a New Conda Environment**:
   Open a terminal (Anaconda Prompt on Windows) and create a new environment. Replace `myenv` with your desired environment name:
   ```bash
   conda create -n myenv python=3.x
   conda activate myenv
   conda install numpy matplotlib scipy
   git clone https://github.com/yourusername/Lagrangian-Double-Pendulum-Redux-II.git

## Software Engineering

### Planning and Design
The software engineering process for this project involved several key steps:

#### Requirements Gathering:
- Identified the core functionality needed: simulating a double pendulum, displaying results graphically, and providing numerical data.
- Gathered input from potential users (students and educators) to understand their needs and expectations.

#### Use Cases:
- **Simulation Use Case**: Users can start the simulation, adjust pendulum parameters (length, mass, initial angles), and view results in real-time.
- **Calculation Use Case**: Users can manually compute specific cases using calculus of variations to compare with numerical results.

#### System Design:
- Defined a modular architecture to separate concerns (e.g., physics calculations, numerical methods, user interface).
- Created flowcharts to visualize the simulation process and interaction between components.

#### Documentation:
- Maintained thorough documentation throughout development, including a README file, user manual, and inline comments for code clarity.

### Development Practices
- Utilized version control (Git) to track changes and collaborate with other developers.
- Followed coding standards and conventions to ensure readability and maintainability.

## Testing Script

### Testing Process
Testing is crucial to ensure the simulation behaves as expected. The testing process involves both manual and automated tests. Below are the steps for manual testing:

#### Functionality Testing:
- Verify that the simulation starts correctly without errors.
- Check that all adjustable parameters (length, mass, angles) can be modified.
- Ensure that changes in parameters are reflected in the simulation output.

#### Edge Case Testing:
- Set extreme values for mass and length to test system limits.
- Initialize the pendulum at different angles, including vertical (0° and 180°) and horizontal (90°) positions, and observe the behavior.

#### Comparison Testing:
- Manually calculate expected values for small-angle approximations and compare them with simulation results.
- Analyze the output of the numerical simulation for chaotic behavior by running the same initial conditions multiple times and observing variations.

#### Performance Testing:
- Monitor the simulation's performance for long-running simulations to check for memory leaks or performance degradation.
- Test responsiveness when modifying parameters during a running simulation.

#### Usability Testing:
- Gather feedback from users regarding the interface and overall experience.
- Ensure that the user manual is clear and assists users effectively.

## Requirements

### Software Requirements:
- Anaconda (includes Python 3.x)
- Libraries: NumPy, Matplotlib, SciPy

### Hardware Requirements:
- A computer capable of running Anaconda with a minimum of 4 GB RAM.
- Graphics support for rendering simulations smoothly.

### User Requirements:
- Basic understanding of physics and mathematics, especially mechanics and calculus.
- Familiarity with running Python scripts and adjusting parameters within a user interface.

This detailed approach to software engineering, testing, and installation ensures that the Lagrangian Double Pendulum Redux II is a robust and educational tool for exploring the dynamics of double pendulums.
