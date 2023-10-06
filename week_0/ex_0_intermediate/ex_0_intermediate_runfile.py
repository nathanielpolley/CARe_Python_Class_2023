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


# Code Error
import math


# Function to calculate growth rate
def calculate_growth_rate(initial_count, final_count, time):
    try:
        # Ensure all inputs are positive
        if initial_count <= 0 or final_count <= 0 or time <= 0:
            raise ValueError("All inputs must be positive values.")

        # Growth rate formula
        growth_rate = (math.log(final_count) - math.log(initial_count)) / time
        return growth_rate

    except ValueError as e:
        return str(e)


# User Input
try:
    initial_count = float(input("Enter initial cell count: "))
    final_count = float(input("Enter final cell count: "))
    time = float(input("Enter time elapsed: "))

    growth_rate = calculate_growth_rate(initial_count, final_count, time)

    if isinstance(growth_rate, float):
        print(f"Growth Rate: {growth_rate:.4f}")
    else:
        print("Error:", growth_rate)

except ValueError:
    print("Invalid input. Please enter positive numeric values for initial count, final count, and time.")