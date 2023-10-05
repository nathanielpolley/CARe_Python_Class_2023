#YOUR CODE FOR EX_0 INTERMEDIATE HERE


import math
initial_count = input("Enter initial cell count: ")
final_count = input("Enter final cell count: ")
time_elapsed = input("Enter time elapsed: ")

if initial_count.isdigit() and final_count.isdigit() and time_elapsed.isdigit() and (final_count > initial_count):
    initial_count = int(initial_count)
    final_count = int(final_count)
    time_elapsed = int(time_elapsed)
    if initial_count > 0 and final_count > 0 and time_elapsed > 0:
        growth_rate = (math.log(final_count)-math.log(initial_count)) / time_elapsed
        print("Growth Rate:", growth_rate)
    else:
        print("Please enter a positive value")
else:
    print("Please enter a valid numeric input")
