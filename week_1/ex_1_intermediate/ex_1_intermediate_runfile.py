#YOUR CODE FOR EX_1 INTERMEDIATE HERE
#YOUR CODE FOR EX_0 INTERMEDIATE HERE

# User input
import math

x = input("Enter the initial number of cells as an integer only.")
y = input("Enter the final number of cells as an integer only")
t = input("Enter the amount of time in minutes")


#User error correction
if x.isdigit() and y.isdigit() and t.isdigit():
    print("Thank you")

 # microbial growth rate calculator
    a = math.log(int(y)) - math.log(int(x)) / int(t)
    a = round(a, 2)
    print("Microbial growth is ", a)

else:
    print("Please enter only integer values")
