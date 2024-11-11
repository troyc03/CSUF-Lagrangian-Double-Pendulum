# Lagrangian Double Pendulum Lab

This lab explores the motion of a double pendulum using the principles of Lagrangian mechanics, calculus of variations, differential equations, and numerical analysis. The simulation models the chaotic dynamics of the double pendulum system by solving the governing equations both analytically and numerically.

## Project Objectives

- Develop an accurate simulation of a double pendulum using Lagrangian mechanics and numerical analysis techniques.
- Use calculus of variations and differential equations to derive the motion equations both by hand and computationally.
- Implement numerical methods to approximate the solutions to the system's differential equations and visualize the pendulum's motion.

## Tools and Technologies

- **Python**: Main programming language used for this project.
- **MATLAB**: Used for symbolic computation, numerical integration (ODE solvers), and advanced visualizations.
- **Anaconda**: Environment management and package distribution, allowing for easy setup and dependency management.
- **Spyder**: Integrated development environment (IDE) for Python, specifically useful for scientific and engineering computing.

## Key Concepts

- **Lagrangian Mechanics**: Used to derive the equations of motion for the double pendulum. Lagrangian mechanics allows for modeling based on kinetic and potential energy, offering insights into the system's dynamics.
  
- **Calculus of Variations**: Applied to derive the system’s equations by optimizing the action (integral of the Lagrangian), providing a deeper understanding of the physical principles.

- **Differential Equations**: The equations of motion derived are second-order differential equations, which we will solve using both analytical techniques and numerical methods.

- **Numerical Analysis Techniques**: Techniques such as the Euler method and Runge-Kutta methods will be employed to approximate the system's solutions for visualization and data logging purposes.

- **MATLAB Integration**: MATLAB will be used for symbolic math, solving differential equations with built-in solvers, and generating visualizations of the pendulum’s motion for comparison (NOTE: If you cannot properly integrate MATLAB with your Python IDE, then this requirement is optional. You can still run the simulation in Anaconda)

## Installation

1. **Install Anaconda**: Download and install [Anaconda](https://www.anaconda.com/products/distribution) to manage dependencies and environments.
2. **Install MATLAB**: Download and install [MATLAB](https://www.mathworks.com/downloads/) to compare numerical calculations.
3. **Install the following libraries**: You will need these in order for the simulation to properly work on your laptop.
   ```bash
   conda install numpy scipy matplotlib
4. **Open Spyder**: Launch Spyder from the Anaconda Navigator or by running (You can use Jupyter or VSCode if you want to):  
   ```bash
   spyder

## Future Extensions
This lab can be extended to model variations of the double pendulum, such as:
- Introducing external forces.
- Modeling with different damping or friction effects.
- Exploring stability and chaos in similar systems.
- This lab combines theoretical derivation and numerical computing to deepen understanding of chaotic systems, making it ideal for students interested in applied physics, engineering, and computational mathematics.

## Kanban Board (WIP)

# ![image](https://github.com/user-attachments/assets/84fe0ce8-04b4-4bfb-b822-072d7acb52ce)




## Diagrams

Use Case Diagram
```bash
+-----------------------------------+
|          Double Pendulum          |
|        Simulation System          |
+-----------------------------------+
|                                   |
|  +-----------------------------+  |
|  |      User Interface          |  |
|  +-----------------------------+  |
|           /           \           |
|          /             \          |
|   +-------------+  +-------------+ |
|   | Set Initial |  | View Motion | |
|   | Conditions  |  |   Graph     | |
|   +-------------+  +-------------+ |
|                                   |
+-----------------------------------+
```

UML Class Diagram
```bash
+----------------------------+
|        DoublePendulum       |
+----------------------------+
| - mass1: float              |
| - mass2: float              |
| - length1: float            |
| - length2: float            |
| - angle1: float             |
| - angle2: float             |
| - velocity1: float          |
| - velocity2: float          |
+----------------------------+
| + equations_of_motion()     |
| + Lagrangian()              |
| + compute_state()           |
+----------------------------+

        | (has)
        |
        V

+----------------------------+
|     NumericalMethods       |
+----------------------------+
| + euler_method()           |
| + runge_kutta()            |
| + solve_ode()              |
+----------------------------+
```

UML Sequence Diagram
```bash
User              System                NumericalMethods
 |                   |                           |
 |--- Set Conditions ->|                           |
 |                   |--- equations_of_motion() ->|
 |                   |<-- return equations       |
 |--- Start Simulation ->|                       |
 |                   |--- compute_state()        |
 |                   |<-- return new state       |
 |--- Visualize Motion ->|                       |
 |                   |--- plot_motion()          |
```

```bash
+-----------------------+
|  Set Initial Conditions|
+-----------------------+
          |
          V
+-----------------------+
|  Solve Differential   |
|     Equations         |
+-----------------------+
          |
          V
+-----------------------+
|  Visualize Motion     |
+-----------------------+
          |
          V
+-----------------------+
|  Export Data          |
+-----------------------+
```

UML Activity Diagram
```bash
+-----------------------+
|  Set Initial Conditions|
+-----------------------+
          |
          V
+-----------------------+
|  Solve Differential   |
|     Equations         |
+-----------------------+
          |
          V
+-----------------------+
|  Visualize Motion     |
+-----------------------+
          |
          V
+-----------------------+
|  Export Data          |
+-----------------------+
```

UML Swimlane Diagram
```bash
+-------------------------------------------+
|            Double Pendulum Simulation    |
+-------------------------------------------+
|   User   |    System    | NumericalMethods|
+-------------------------------------------+
| Set Initial Conditions ->                 |
|               |                           |
| Start Simulation ->                       |
|               |                           |
| Visualize Motion ->                       |
+-------------------------------------------+
```
