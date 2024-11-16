"""
File name: setup.py
Author: Troy Chin
Date: 15 November 2024
Version: 1.0
Purpose: This is the setup file to integrate MATLAB's API Engine to Python.

"""

#Import models here.

import matlab.engine

def setup_engine(options='-desktop'):
    try:
        eng = matlab.engine.start_matlab(options)
        print("MATLAB Engine initiated successfully.")
        return eng
    except Exception as e:
        print(f"ERROR: Initiation failed. Details: {e}")
        return None
 
eng = setup_engine()

if eng:
    print("MATLAB Engine is running.")
else:
    print("Failed to start MATLAB Engine.")

