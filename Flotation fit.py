#Add variations of kinectic flotatation models

import numpy as np
import matplotlib.pyplot as plt

while True:
    regression_type = input("Select regression type add later ").strip().lower() #Regression method to be selected

    if regression_type == "1 comp":
        # Inputs for the model
        comp1_data_points = int(input("Enter number of data points: ").strip())
        comp1_time = int(input("Enter time of each datapoint (seconds): ").strip())
        comp1_mass = int(input("Enter mass of each datapoint (g): ").strip())
        comp1_mass = int(input("Enter grade of each datapoint (%): ").strip())

        #Calculations
        metal_content1 = []
        cummulative_metal1 = []

        
    #elif regression_type == "2 comp":

    #elif regression_type == "3 comp":

    #elif regression_type == "Rectangular":
        
