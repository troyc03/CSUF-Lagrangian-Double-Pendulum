"""
File name: data_logger.py
Author: Troy Chin (CWID: 885586685)
Date: 2024-11-10
Version: 1.0
Description: This script will handle any data logging from the user.

"""

#Import models here.
import csv

class DataLogger:
    def __init__(self):
        self.data = []

    def log_state(self, state):
        self.data.append(state)

    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Angle 1", "Angle 2", "Velocity 1", "Velocity 2"])  # Header
            writer.writerows(self.data)
