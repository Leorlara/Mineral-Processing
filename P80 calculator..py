# A possible idea for to improve this code would be to detected the over and under sieves from a csv file (as the new input) and calculate the P80% from it

import numpy as np

method = input("Would you like to use a linear of logarithmic method? (li/ln) ").strip().lower()

if method == "li":

    # Mandatory inputs to calculate the P80%
    sieve_over_linear = float(input("Enter the closest sieve size above 80%: ")) 
    sieve_under_linear = float(input("Enter the closest sieve size under 80%: "))  
    cum_passing_over_linear = float(input("Enter the cumulative passing from the size above 80%: ")) / 100 
    cum_passing_under_linear = float(input("Enter the cumulative passing from the size under 80%: ")) / 100 

    # Calculating P80% using linear interpolation
    P80_linear = ((0.8 - cum_passing_over_linear) / (cum_passing_under_linear - cum_passing_over_linear)) * (sieve_under_linear - sieve_over_linear) + sieve_over_linear
    print(f"The P80% is {P80_linear}")

elif method == "ln":

    # The following inputs are mandatory to calculate the P80%
    sieve_over_logarithmic = float(input("Enter the closest sieve size over 80%: "))
    sieve_under_logarithmic = float(input("Enter the closest sieve size under 80%: "))
    cum_passing_over_logarithmic = float(input("Enter the cumulative passing from the size over 80% ")) / 100
    cum_passing_under_logarithmic = float(input("Enter the cumulative passing from the size under 80% ")) / 100

    ln_size_over = np.log(sieve_over_logarithmic)
    ln_size_under = np.log(sieve_under_logarithmic)
    ln_cum_passing_over = np.log(-np.log(cum_passing_over_logarithmic))
    ln_cum_passing_under = np.log(-np.log(cum_passing_under_logarithmic))

    # The calculations start here
    P80_ln = ((-1.4994 - ln_cum_passing_over) / (ln_cum_passing_under - ln_cum_passing_over)) * (ln_size_under - ln_size_over) + ln_size_over #the P80 is calculated here
    P80_logarithmic = np.exp(P80_ln) #We are leaving the logarithmic scale and going back to the linear scale here
    print(f"The P80% is {P80_logarithmic}")

    #Overall this was a very simple code to write, and I only did it to practice, I still find easier to this process through Excel, specially when you have to obtain multiple P80%s




