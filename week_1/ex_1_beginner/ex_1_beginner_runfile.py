# Matias Medina Tanco: EX_1 BEGINNER

# Imports the mean function to calculate the average of values within a list
from statistics import mean

# Defines the list with microbial population counts for 5 consecutive days
microbialPop = [100, 200, 150, 300, 50]

# Calculate the average, maximum and minimum values of the list
average = mean(microbialPop)
maximum = max(microbialPop)
minimum = min(microbialPop)

# Prints out the results
print("The average microbial population count is: ", average)
print("The maximum microbial population count is: ", maximum)
print("The minimum  microbial population count is: ", minimum)


# Iterate through the microbialPop list to find days in which the population was greater than 200
for i in range(len(microbialPop)):

    # Define variable valueCheck which is assigned the value of day i in the microbialPop list
    valueCheck = microbialPop[i]

    # Check if on day i the population count is greater than 200. If so, print out the day's number
    if valueCheck > 200:
        print("On day ", i, " the microbial population exceeded 200 (Note: the first day is considered day 0).")