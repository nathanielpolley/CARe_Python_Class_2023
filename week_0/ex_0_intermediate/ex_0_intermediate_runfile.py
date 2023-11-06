#All homeworks will be due next week! (arithmetic from last week skills and then what we do this week)

#1. Microbial Growth Rate Calculator (Variables and Input/Output):
#- Write a Python program that calculates the growth rate of a microbial culture based on user input for initial
# and final cell counts and the time elapsed.
#- Prompt the user to input the initial count, final count, and time.
#- Calculate and display the growth rate using the formula: Growth Rate = (ln(final count) - ln(initial count)) / time.
#- Ensure that the program handles invalid input gracefully.

#order of code changed!
import math
def MBgrowthrate(initial,final,time):
    if initial.isdigit() and final.isdigit() and time.isdigit():
        initial = int(input("Enter Initial Bacteria Count: "))
        final = int(input("Enter Final Bacteria Count: "))
        time = int(input("Enter Amount of Time Growth Has Occurred For: "))
        if final > initial:
            growth = (math.log(final)) - (math.log(initial)/time)
        print(growth)
    else:
        print("Enter a valid input please! :-)")















