# Lagrangian Double Pendulum Lab

## Table of Contents
- [Project Description](#project-description)
- [Tools and Technologies](#tools-and-technologies)
- [Key Concepts](#key-concepts)
- [Kanban Board](#kanban-board)
- [Installation](#installation)
- [Diagrams](#diagrams)
- [Known Issues](#known-issues)
- [To-Do Items](#to-do-items)

## Project Description
This lab explores the motion of a double pendulum using the principles of Lagrangian mechanics, calculus of variations, differential equations, and numerical analysis. The simulation models the chaotic dynamics of the double pendulum system by solving the governing equations both analytically and numerically. In order to conduct this lab, please make sure to download the appropriate software in the [Installation](#installation) section.

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

- **MATLAB Integration**: MATLAB will be used for symbolic math, solving differential equations with built-in solvers, and generating visualizations of the pendulum’s motion for comparison (NOTE: If you cannot properly integrate MATLAB with your Python IDE, then this requirement is optional. You can still run the simulation in Anaconda and treat MATLAB as a separate environment to compare your calculations)

## Installation

1. **Install Anaconda**: Download and install [Anaconda](https://www.anaconda.com/products/distribution) for the primary numerical and scientific calculations performed in this laboratory.
2. **Install MATLAB**: Download and install [MATLAB](https://www.mathworks.com/products/matlab.html) to compare numerical calculations.
3. **Install the following libraries**: You will need these in order for the simulation to properly work on your laptop.
   ```bash
   conda install numpy scipy matplotlib
4. **Open Spyder**: Launch Spyder from the Anaconda Navigator or by running this command in the Anaconda Command Prompt (You can also use Jupyter or VSCode if you want):  
   ```bash
   spyder

## Kanban Board (Updated November 13, 2024)

![image](https://github.com/user-attachments/assets/a3924d1e-369e-4e1b-a109-c7222f10591c)


* [Kanban User Stories/Requirements Models](https://docs.google.com/document/d/1SGqSKioedVcLIY1T7fengTqAkcT4FvSXmw4P1XDdrbs/edit?tab=t.0)
* [Kanban Task List (All tasks listed will be added to the Kanban Board weekly)](https://docs.google.com/document/d/1vBFQM8tplh93Y_LbmWPhZ9SYO8kH2StDEvxj4FI_ibQ/edit?tab=t.0)


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
|        DoublePendulum      |
+----------------------------+
| - mass1: float             |
| - mass2: float             |
| - length1: float           |
| - length2: float           |
| - angle1: float            |
| - angle2: float            |
| - velocity1: float         |
| - velocity2: float         |
| - g: float                 |  <- gravity
+----------------------------+
| + __init__()               |
| + set_initial_conditions() |
| + equations_of_motion()    |
| + Lagrangian()             |
| + compute_state(t)         |
| + calculate_kinetic_energy()|
| + calculate_potential_energy()|
| + calculate_total_energy() |
| + reset()                  |
+----------------------------+

        | (uses)
        |
        V

+----------------------------+
|     NumericalMethods       |
+----------------------------+
| - dt: float                |  <- time step
+----------------------------+
| + euler_method()           |
| + runge_kutta()            |
| + solve_ode(ode, init)     |
| + adaptive_runge_kutta()   |
| + midpoint_method()        |
+----------------------------+
```

UML Sequence Diagram
```bash
User              System                NumericalMethods
 |                   |                           |
 |--- Set Initial Conditions ->                 |
 |                   |--- set_initial_conditions() |
 |                   |<-- Return success        |
 |--- Start Simulation ->                       |
 |                   |--- equations_of_motion() ->|
 |                   |<-- Differential eqns     |
 |                   |--- runge_kutta()         |
 |                   |--- calculate_total_energy()|
 |                   |<-- New state, energy     |
 |                   |--- log_data()            |
 |                   |                           |
 |--- Visualize Motion ->                       |
 |                   |--- plot_motion()         |
 |                   |<-- Display graph         |
 |                   |                           |
 |--- Export Data ->                            |
 |                   |--- save_to_csv()         |
 |                   |<-- CSV export complete   |
```

UML State Diagram 

```bash
+-----------------------+
|  Set Initial Conditions|
+-----------------------+
          |
          V
+-----------------------+
|  Solve Differential   |
|     Equations         |
| - Define ODEs         |
| - Apply Runge-Kutta   |
| - Calculate Energy    |
+-----------------------+
          |
          V
+-----------------------+
|  Log and Visualize    |
|     Simulation        |
| - Plot motion         |
| - Save CSV            |
| - Calculate Total Energy |
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
| - Define ODEs         |
| - Apply Runge-Kutta   |
| - Calculate Energy    |
+-----------------------+
          |
          V
+-----------------------+
|  Log and Visualize    |
|     Simulation        |
| - Plot motion         |
| - Save CSV            |
| - Calculate Total Energy |
+-----------------------+

```

UML Swimlane Diagram
```bash
+-------------------------------------------------------------+
|            Double Pendulum Simulation                       |
+-------------------------------------------------------------+
|   User        |    System               | NumericalMethods  |
+-------------------------------------------------------------+
| Set Initial   |                         |                   |
| Conditions -> | set_initial_conditions()|                   |
|               | Compute ODEs ->         | Euler/Runge-Kutta |
|               | Update State            |                   |
|               | calculate_total_energy()|                   |
|               | Visualize Motion        |                   |
| Export Data ->| save_to_csv()           |                   |
+-------------------------------------------------------------+

```

## Known Issues

- **MATLAB Integration**: Some users may experience compatibility issues when integrating MATLAB and Python. For this reason, integration is optional.
- **Chaotic Instability**: The nature of the double pendulum system leads to highly unstable and divergent results if precise initial conditions are not maintained.

## To-Do Items

- Reimplement code into MATLAB (or integrate MATLAB API to Python if possible)
- Implement unit and integration testing to the Python laboratory to account for miscalculations and error handling in case MATLAB is not integrated correctly.

#### Credits
Troy Chin (Kanban Team Leader/Head DevOps Coordinator)

##### License

This project is free for anyone to access and distribute to other users.
[https://www.gnu.org/licenses/gpl-3.0.en.html](https://www.gnu.org/licenses/gpl-3.0.en.html)
