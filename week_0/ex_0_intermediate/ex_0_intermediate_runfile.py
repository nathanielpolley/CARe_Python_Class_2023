import math
def calculate_growth_rate():

        initial_count = int(input("Enter the initial cell count: "))
        final_count = int(input("Enter the final cell count: "))
        time = int(input("Enter the time elapsed: "))
        if int(time) < 0:
                return print('Only positive numbers for the time' )

        growth_rate = (math.log(final_count) - math.log(initial_count)) / time

        print(f"The growth rate is: {growth_rate}")

calculate_growth_rate()

