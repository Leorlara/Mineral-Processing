import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import linregress

#Gaudin-Schumann particle size calculations
#y = (D/D*)^a
# D* is top size of you dsitribution
# a is a constant to be determined accoridng to your curve
#y y = cumulative mass undersize % passing size d
while True:
    Top_Size_unit=input("Enter the unit to be used (mm or µm): ")
    Sizes = []
    Passing = []
    Data_points = int(input("Enter the number of data points: "))

    for z in range(Data_points):
        size = float(input(f"Enter the size (from biggest to smallest) {z+1}: "))
        Sizes.append(size)
        passing = float(input(f"Enter the % passing {z+1}: "))
        Passing.append(passing)

    Cumulative_Retained = []
    cumulative_sum = 0

    for passing in Passing:
        cumulative_sum += passing
        Cumulative_Retained.append(cumulative_sum)

    Cumulative_passing = []
    current_passing = 100 - Passing[0]  # Start with 100 - the first passing value
    Cumulative_passing.append(current_passing)

    for i in range(1, len(Passing)):
        current_passing -= Passing[i]
        Cumulative_passing.append(current_passing)

    log_Sizes = np.log10(Sizes)
    log_CumPassing = np.log10(Cumulative_passing)

    slope, intercept, r_value, p_value, std_err = linregress(log_Sizes, log_CumPassing)

    print(f"Fitted Line: log(Cumulative Passing) = {slope:.4f} * log(Size) + {intercept:.4f}")
    print(f"R-squared value: {r_value**2:.4f}")

    fitted_line = slope * log_Sizes + intercept

    plt.scatter(log_Sizes, log_CumPassing, label="Log-Log Data", color="red")
    plt.plot(log_Sizes, fitted_line, label="Fitted Line", color="blue")
    plt.xlabel("Log(Size)")
    plt.ylabel("Log(Cumulative Passing)")
    plt.legend()
    plt.title("Log-Log Fit of Gaudin-Schumann Distribution")
    plt.show()
    Again_GS = input("Do you want to enter a new set of data points? (yes/no): ").strip().lower()
    if Again_GS != "yes":
        print("End of program")
        break

#rosin rammler particle size calculations
#y = exp[-(x/xi)^b]
# xi is the size parameter  (x at which y=63.2%)
# b is a constant to be determined accoridng to your curve

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

    Again_RR = input("Do you want to enter a new set of data points? (yes/no): ").strip().lower()
    if Again_RR != "yes":
        print("End of program")
        break