import math
def calculate_growth_rate():
    try:
        initial_count = int(input("Enter the initial cell count: "))
        final_count = int(input("Enter the final cell count: "))
        time = int(input("Enter the time elapsed: "))

        if time < 0:
            print("Only positive numbers for the time are allowed.")
        else:
            growth_rate = (math.log(final_count) - math.log(initial_count)) / time
            print(f"The growth rate is: {growth_rate}")
    except ValueError:
        print("Invalid input. You need a number of cells that is greater than or equal to 0.")


calculate_growth_rate()