#Gaudin-Schumann particle size calculations
#y = (D/D*)^a
# D* is top size of you dsitribution
# a is a constant to be determined accoridng to your curve
#y y = cumulative mass undersize % passing size d

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

