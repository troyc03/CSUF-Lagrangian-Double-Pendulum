"""
File name: numerical_methods.py
Author: Troy Chin (CWID: 885586685)
Date: 2024-11-10
Version: 1.0
Description: This script contains various numerical methods used for this lab.
"""

# PLEASE make sure to compute manual calculations before writing this program.

import numpy as np
from scipy.integrate import odeint

class NumericalMethods():
    #Import numerical methods here.
    
    def __init__(self, dt):
        self.dt = dt # Time step
        
    def euler_method(self, f, y0):
        """
        Compute Euler's method for solving ODEs.
        """
        t = np.arange(0, 10, self.dt)
        y = np.zeros(len(t), len(y0))
        y[0] = y0
        for i in range(1, len(t)):
            y[i] = y[i-1] + self.dt * f(t[i-1], y[i-1])
        return t, y
    
    def runge_kutta(self, f, y0):
        """
        Compute Runge-Kutta Method of Order Four for solving ODEs.
        """
        t = np.arange(0, 10, self.dt)
        y = np.zeros((len(t), len(y0)))
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
        Use any of the given methods to solve  manually.
        """
        if method == 'euler':
            return self.euler_method(f, y0)
        elif method == 'runge_kutta':
            return self.runge_kutta(f, y0)
        elif method == 'odeint':
            return odeint(f, y0)
        else:
            raise ValueError('ERROR: Unsupported method.')
    



    
    
