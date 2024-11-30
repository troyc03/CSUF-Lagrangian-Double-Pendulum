"""
File name: numerical_methods.py
Author: Troy Chin (CWID: 885586685)
Date: 2024-11-13
Version: 1.4
Status: Ready to deliver to customers
Description: This script contains the numerical methods implemented in this lab.
"""

# Import numerical methods here.

import matplotlib.pyplot as plt

class NumericalMethods:
    
    def __init__(self, dt=0.01):
        self.dt = dt

    def euler_method(self, func, y0):
        """Function for solving ODEs using Euler's Method."""
        dydt = func(0, y0)
        return [yi + self.dt * dyi for yi, dyi in zip(y0, dydt)]

    def runge_kutta(self, func, y0):
        """Function for solving ODEs using Runge-Kutta Method (of Order 4)."""
        k1 = func(0, y0)
        k2 = func(0, [yi + 0.5 * self.dt * k1i for yi, k1i in zip(y0, k1)])
        k3 = func(0, [yi + 0.5 * self.dt * k2i for yi, k2i in zip(y0, k2)])
        k4 = func(0, [yi + self.dt * k3i for yi, k3i in zip(y0, k3)])
        return [yi + (self.dt / 6) * (k1i + 2 * k2i + 2 * k3i + k4i) for yi, k1i, k2i, k3i, k4i in zip(y0, k1, k2, k3, k4)]

    def adaptive_runge_kutta(self, func, y0, tolerance=1e-6):
        """Function for solving ODEs using Adaptive Runge-Kutta Method."""
        h = self.dt
        y = y0
        error = tolerance + 1

        while error > tolerance:
            k1 = func(0, y)
            k2 = func(0, [yi + 0.25 * h * k1i for yi, k1i in zip(y, k1)])
            k3 = func(0, [yi + (3/32) * h * k1i + (9/32) * h * k2i for yi, k1i, k2i in zip(y, k1, k2)])
            k4 = func(0, [yi + (1932/2197) * h * k1i - (7200/2197) * h * k2i + (7296/2197) * h * k3i for yi, k1i, k2i, k3i in zip(y, k1, k2, k3)])
            k5 = func(0, [yi + (439/216) * h * k1i - 8 * h * k2i + (3680/513) * h * k3i - (845/4104) * h * k4i for yi, k1i, k2i, k3i, k4i in zip(y, k1, k2, k3, k4)])
            k6 = func(0, [yi - (8/27) * h * k1i + 2 * h * k2i - (3544/2565) * h * k3i + (1859/4104) * h * k4i - (11/40) * h * k5i for yi, k1i, k2i, k3i, k4i, k5i in zip(y, k1, k2, k3, k4, k5)])

            y4 = [yi + h * ((25/216) * k1i + (1408/2565) * k3i + (2197/4104) * k4i - (1/5) * k5i) for yi, k1i, k3i, k4i, k5i in zip(y, k1, k3, k4, k5)]
            y5 = [yi + h * ((16/135) * k1i + (6656/12825) * k3i + (28561/56430) * k4i - (9/50) * k5i + (2/55) * k6i) for yi, k1i, k3i, k4i, k5i, k6i in zip(y, k1, k3, k4, k5, k6)]

            error = max(abs(y5i - y4i) for y5i, y4i in zip(y5, y4))
            if error > tolerance:
                h *= 0.9 * (tolerance / error) ** 0.2
            else:
                y = y5

        return y

    def midpoint_method(self, func, y0):
        """Function for solving ODEs using the Midpoint Method."""
        dydt = func(0, y0)
        y_mid = [yi + 0.5 * self.dt * dyi for yi, dyi in zip(y0, dydt)]
        dydt_mid = func(0, y_mid)
        return [yi + self.dt * dyi_mid for yi, dyi_mid in zip(y0, dydt_mid)]

    def solve_ode(self, func, y0, method='runge_kutta', tolerance=1e-6):
        if method == 'euler':
            return self.euler_method(func, y0)
        elif method == 'runge_kutta':
            return self.runge_kutta(func, y0)
        elif method == 'adaptive_runge_kutta':
            return self.adaptive_runge_kutta(func, y0, tolerance)
        elif method == 'midpoint':
            return self.midpoint_method(func, y0)
        else:
            raise ValueError("Unknown method. Choose 'euler', 'runge_kutta', 'adaptive_runge_kutta', or 'midpoint'.")

#Example implementation            

def main():
    def simple_ode(t, y):
        """Simple linear ODE."""
        return [3 * yi for yi in y]
    
    # Create an instance of NumericalMethods
    nm = NumericalMethods(dt=0.1)
    y0 = [1.0]  # Initial condition
    time_steps = 10  # Number of time steps
    methods = ['euler', 'runge_kutta', 'adaptive_runge_kutta', 'midpoint']  # List of methods to solve ODE

    # List to store solutions for each method
    solutions = {method: [y0] for method in methods}
    
    # Solve the ODE for each method
    for i in range(time_steps):
        for method in methods:
            y_next = nm.solve_ode(simple_ode, solutions[method][-1], method=method)
            solutions[method].append(y_next)

            # Print the solution at each step for each method
            print(f"Method: {method}, Step {i}: {y_next}")
    
    # Print final results for each method
    for method in methods:
        print(f"Final solution for {method} after {time_steps} steps: {solutions[method][-1]}")

    # Plot the results for each method
    times = [i * nm.dt for i in range(time_steps + 1)]  # Time array
    plt.figure(figsize=(10, 6))

    for method in methods:
        solution_values = [result[0] for result in solutions[method]]  # Extract the first (and only) element of each result
        plt.plot(times, solution_values, label=f'{method.capitalize()} Solution')

    plt.xlabel('Time')
    plt.ylabel('Solution (y)')
    plt.title('ODE Solutions over Time for Different Methods')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()

