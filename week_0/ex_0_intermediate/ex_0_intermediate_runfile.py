import math

def calculate_growth_rate(initial_count, final_count, time):
    try:
        initial_count = float(initial_count)
        final_count = float(final_count)
        time = float(time)

        if initial_count <= 0 or final_count <= 0 or time <= 0:
            raise ValueError("All values must be greater than zero.")

        growth_rate = (math.log(final_count) - math.log(initial_count)) / time
        return growth_rate
    except ValueError as e:
        return None

def main():
    print("Microbial Culture Growth Rate Calculator")
    initial_count = input("Enter the initial cell count: ")
    final_count = input("Enter the final cell count: ")
    time = input("Enter the time elapsed (in hours): ")

    growth_rate = calculate_growth_rate(initial_count, final_count, time)

    if growth_rate is not None:
        print(f"The growth rate of the microbial culture is: {growth_rate:.2f} per hour")
    else:
        print("Invalid input. Please enter positive numeric values for initial count, final count, and time.")

if __name__ == "__main__":
    main()