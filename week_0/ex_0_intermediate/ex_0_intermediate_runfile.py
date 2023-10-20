import math

x = input("Initial Number of Cells: ")
y = input("Final Number of Cells: ")
z = input("Time Taken: ")

if x.isdigit() and y.isdigit() and z.isdigit():
    initial = int(x)
    final = int(y)
    time = int(z)

    if y > x:
        print("Running Formula")
        growth_rate = (math.log(final) - math.log(initial)) / time
        print("Microbial Growth Rate:", growth_rate)
    else:
        print("Error: The Final count must be greater than the Initial count.")
else:
    print("Error: Please enter non-negative and non-decimal numeric values.")