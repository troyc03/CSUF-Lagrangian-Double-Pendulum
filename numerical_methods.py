"""
File name: numerical_methods.py
Author: Troy Chin (CWID: 885586685)
Date: 2024-11-11
Version: 1.2
Description: This script contains the numerical methods implemented in this lab.

"""

import numpy as np
from scipy.integrate import odeint

class NumericalMethods():
    """
    A class to implement various numerical methods for solving ODEs.
    """

    def __init__(self, dt):
        self.dt = dt  # Time step
        
    def euler_method(self, f, y0):
        """
        Compute Euler's method for solving ODEs.
        
        Parameters:
        f : callable
            The function that defines the ODE.
        y0 : array_like
            Initial condition.
        
        Returns:
        t : ndarray
            Time points.
        y : ndarray
            Solution at each time point.
        """
        t = np.arange(0, 10, self.dt)
        y = np.zeros((len(t), len(y0)))  # Corrected initialization
        y[0] = y0
        for i in range(1, len(t)):
            y[i] = y[i-1] + self.dt * f(t[i-1], y[i-1])
        return t, y
    
    def runge_kutta(self, f, y0):
        """
        Compute Runge-Kutta Method of Order Four for solving ODEs.
        
        Parameters:
        f : callable
            The function that defines the ODE.
        y0 : array_like
            Initial condition.
        
        Returns:
        t : ndarray
            Time points.
        y : ndarray
            Solution at each time point.
        """
        t = np.arange(0, 10, self.dt)
        y = np.zeros((len(t), len(y0)))  # Corrected initialization
        y[0] = y0
        for i in range(1, len(t)):
            k1 = self.dt * f(t[i-1], y[i-1])
            k2 = self.dt * f(t[i-1] + self.dt / 2, y[i-1] + k1 / 2)
            k3 = self.dt * f(t[i-1] + self.dt / 2, y[i-1] + k2 / 2)
            k4 = self.dt * f(t[i-1] + self.dt, y[i-1] + k3)
            y[i] = y[i-1] + 1/6 * (k1 + 2*k2 + 2*k3 + k4) 
        return t, y

    def solve_ode(self, f, y0, method='runge_kutta'):
        """
        Solves the ODE using the specified method.
        
        Parameters:
        f : callable
            The function that defines the ODE.
        y0 : array_like
            Initial condition.
        method : str
            The method to use for solving the ODE ('euler', 'runge_kutta', 'odeint').
        
        Returns:
        t : ndarray
            Time points.
        y : ndarray
            Solution at each time point.
        """
        if method == 'euler':
            return self.euler_method(f, y0)
        elif method == 'runge_kutta':
            return self.runge_kutta(f, y0)
        elif method == 'odeint':
            t = np.arange(0, 10, self.dt)
            y = odeint(f, y0, t)
            return t, y
        else:
            raise ValueError('ERROR: Unsupported method.')