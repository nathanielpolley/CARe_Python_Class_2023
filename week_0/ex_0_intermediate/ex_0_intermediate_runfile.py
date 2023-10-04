import math

initial_count = input("Enter the initial cell count: ")
final_count = input("Enter the final cell count: ")
time = input("Enter the time elapsed: ")

try:
    initial_count = int(initial_count)
    final_count = int(final_count)
    time = float(time)
    if initial_count <= 0 or final_count <= 0 or time <= 0:
        print("You must enter a positive number")

    else:
        growth_rate = (math.log(final_count) - math.log(initial_count)) / time
        print(growth_rate)
except ValueError:
    print("Invalid input, please enter integer values for initial_count and final_count")
