import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import linregress

#Gaudin-Schumann particle size calculations
#y = (D/D*)^a
# D* is top size of you dsitribution
# a is a constant to be determined accoridng to your curve
#y y = cumulative mass undersize % passing size d

while True:
    regression_type = input("Select regression type: Gaudin-Schumann (GS) or Rosin-Rammler (RR): ").strip().lower() #Regression method to be selected

    if regression_type == "gs":
        while True:
            Top_Size_unit=input("Enter the unit to be used (mm or µm): ")
            Sizes = [] #array that gets the sieves information
            Passing = [] #array that collects the retained mass
            Data_points = int(input("Enter the number of data points: ")) #hHow many inpputs you have

            for z in range(Data_points): #loop to enter the avaibale information
                size = float(input(f"Enter the size (from biggest to smallest) {z+1}: "))
                Sizes.append(size)
                passing = float(input(f"Enter the % passing {z+1}: "))
                Passing.append(passing)

            Cumulative_Retained = [] #array to calculate the cumulative retained mass
            cumulative_sum = 0

            for passing in Passing: #loop to calciulate the cumulative retained mass
                cumulative_sum += passing
                Cumulative_Retained.append(cumulative_sum)

            Cumulative_passing = [] #array to calculate the cumulative passing mass
            current_passing = 100 - Passing[0]  # Start with 100 - the first passing value
            Cumulative_passing.append(current_passing)

            for i in range(1, len(Passing)): #loop to calculate the cumulative passing mass
                current_passing -= Passing[i]
                Cumulative_passing.append(current_passing)

            log_Sizes = np.log10(Sizes) #threse two lines are to calculate the log of the sizes and the cumulative passing (linerarizing)
            log_CumPassing = np.log10(Cumulative_passing)

            slope, intercept, r_value, p_value, std_err = linregress(log_Sizes, log_CumPassing)
            Top_Size_GS = 10**(((np.log10(100))-intercept)/slope) #calculation of the D* in the GS method (which is the passing at 100%)
            fitted_line = slope * log_Sizes + intercept

            print(f"Fitted Line: log(Cumulative Passing) = {slope:.4f} * log(Size) + {intercept:.4f}") #information on the linear fit
            print(f"R-squared value: {r_value**2:.4f}")
            print(f"D* parameter = {Top_Size_GS:.2f}") #GS parameter
            print(f"a parameter = {slope:.4f}") #GS parameter

            plt.scatter(log_Sizes, log_CumPassing, label="Log-Log Data", color="red")
            plt.plot(log_Sizes, fitted_line, label="Fitted Line", color="blue")
            plt.xlabel("Log(Size)")
            plt.ylabel("Log(Cumulative Passing)")
            plt.legend()
            plt.title("Log-Log Fit of Gaudin-Schumann Distribution")
            plt.show()
            # Again_GS = input("Do you want to enter a new set of data points? (yes/no): ").strip().lower()
            # if Again_GS != "no":
            #     print("End of program")
            #     break

        #rosin rammler particle size calculations
        #y = exp[-(x/xi)^b]
        # xi is the size parameter  (x at which y=63.2%)
        # b is a constant to be determined accoridng to your curve
    if regression_type == "rr":
        while True:
            Top_Size_unit_RR=input("Enter the unit to be used (mm or µm): ")
            Sizes_RR = []
            Passing_RR = []
            Data_points_RR = int(input("Enter the number of data points: "))
            for z in range(Data_points_RR):
                size_RR = float(input(f"Enter the size (from biggest to smallest) {z+1}: "))
                Sizes_RR.append(size_RR)
                passing_RR = float(input(f"Enter the % passing {z+1}: "))
                Passing_RR.append(passing_RR)

            Cumulative_Retained_RR = []
            cumulative_sum_RR = 0

            for passing_RR in Passing_RR:
                cumulative_sum_RR += passing_RR
                Cumulative_Retained_RR.append(cumulative_sum_RR)

            Cumulative_passing_RR = []
            current_passing_RR = 100 - Passing_RR[0]  # Start with 100 - the first passing value
            Cumulative_passing_RR.append(current_passing_RR)

            for i in range(1, len(Passing_RR)):
                current_passing_RR -= Passing_RR[i]
                Cumulative_passing_RR.append(current_passing_RR)

            log_Sizes_RR = np.log(Sizes_RR)
            natural_passing = []
            log_natural_passing = []

            for i in range(len(Cumulative_passing_RR)):
                 value = 1 / (1 - (Cumulative_passing_RR [i] / 100))  
                 log_value = np.log(np.log(value))        
                 natural_passing.append(value)           
                 log_natural_passing.append(log_value)   

            slope_RR, intercept_RR, r_value_RR, p_value_RR, std_err_RR = linregress(log_Sizes_RR, log_natural_passing)
            fitted_line_RR = slope_RR * log_Sizes_RR + intercept_RR

            print(f"Fitted Line: ln(-ln(1 - Passing)) = {slope_RR:.4f} * ln(Size) + {intercept_RR:.4f}")
            print(f"R-squared value: {r_value_RR**2:.4f}")
            x_rr = np.log(intercept_RR/slope_RR)

            print(f"m parameter = {slope_RR:.2f}") #RR parameter
            print(f"b parameter = {intercept_RR:.4f}") #RR parameter
            print(f"D* parameter = {x_rr:.2f}") #RR parameter


            plt.scatter(log_Sizes_RR, log_natural_passing, label="Log-Log Data", color="red")
            plt.plot(log_Sizes_RR, fitted_line_RR, label="Fitted Line", color="blue")
            plt.xlabel("ln(Size)")
            plt.ylabel("ln(ln(1/(1-Passing)))")
            plt.legend()
            plt.title("Rosin-Rammler Distribution Fit")
            plt.show()

            Again_RR = input("Do you want to enter a new set of data points? (yes/no): ").strip().lower()
            if Again_RR != "yes":
                print("End of program")
                break