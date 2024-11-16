"""
File name: setup.py
Author: Troy Chin (CWID: 885586685)
Date: 2024-11-10
Version: 1.0
Description: This is a test file to properly integrate MATLAB's API Engine to Python.
"""

try:
    import matlab.engine
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "ERROR: The MATLAB Engine API module is not installed. Please ensure the MATLAB Engine API for Python is installed and properly integrated with your Python environment."
    )

def setup_engine():
    try:
        eng = matlab.engine.start_matlab()
        return eng
    except Exception as e:
        raise RuntimeError(
            f"ERROR: Failed to start the MATLAB Engine. Ensure MATLAB is installed and configured correctly. Details: {e}"
        )

# Initialize the MATLAB Engine
try:
    boot = setup_engine()
    print("MATLAB Engine successfully started.")
except ModuleNotFoundError as e:
    print(e)
except RuntimeError as e:
    print(e)
