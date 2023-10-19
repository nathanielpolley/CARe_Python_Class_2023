import math

initial_count = input("Enter the initial cell count:")
final_count = input("Enter the final cell count:")
time = input("Enter the time elapsed ( in hours):")

initial_count = float(initial_count)
final_count = float(final_count)
time = float(time)

growth_rate = (math.log(final_count) - math.log(initial_count)) / time

if growth_rate is not None :
    print(f"The growth rate of the microbial culture is : {growth_rate} per hours")
else :
    print("Invalid input")