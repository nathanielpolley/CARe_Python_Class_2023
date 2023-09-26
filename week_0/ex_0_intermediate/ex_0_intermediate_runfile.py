# Matias Medina Tanco: EX_0 INTERMEDIATE

# Asks for input of each of the relevant variables (initial and final cell counts, time elapsed)
# If an invalid value is given for a variable the program asks again until a valid value is given


# import the relevant library
import math

# Ask for initial cell count
while True:
    try:
        initial = int(input("Enter the initial cell count: "))
    except ValueError:
        print("Please enter a valid, whole number.")
    else:
        break

# Ask for final cell count
while True:
    try:
        final = int(input("Enter the final cell count: "))
    except ValueError:
        print("Please enter a valid, whole number.")
    else:
        break

# Ask for time elapsed
while True:
    try:
        time = int(input("Enter the time elapsed: "))
    except ValueError:
        print("Please enter a valid, whole number.")
    else:
        break

# Calculates growth rate and prints out result
GrowthRate = (math.log(final) - math.log(initial)) / time

print("The growth rate of the microbial culture is: ", GrowthRate)

