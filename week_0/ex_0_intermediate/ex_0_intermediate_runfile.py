# Import the math module to access the natural logarithm function
import math

# Function to get float input from the user
def get_float_input(prompt):
    while True:
        try:
            # Attempt to convert user input to a float
            return float(input(prompt))
        except ValueError:
            # If conversion fails, display an error message
            print("Invalid input. Please enter a numeric value.")

# Function to interpret the growth rate with subtle humor
def interpret_growth_rate(growth_rate):
    if growth_rate <= 0:
        return "No growth. Maybe they're on a coffee break?"
    elif 0 < growth_rate <= 0.2:
        return "Slow and steady. Like a sloth, but less cute."
    elif 0.2 < growth_rate <= 1:
        return "Moderate growth. Neither sprinting nor crawling."
    elif 1 < growth_rate <= 3:
        return "Quite speedy. They must have deadlines too."
    else:
        return "Growing like they're in a Silicon Valley startup."

# Main function
def main():
    # Prompt the user for the initial cell count
    initial_count = get_float_input("Enter the initial cell count: ")
    # Prompt the user for the final cell count
    final_count = get_float_input("Enter the final cell count: ")
    # Prompt the user for the time elapsed
    time_elapsed = get_float_input("Enter the time elapsed (in hours): ")

    # Validate that the inputs are greater than zero
    if initial_count <= 0 or final_count <= 0 or time_elapsed <= 0:
        print("Invalid values. All values must be greater than zero.")
        return

    # Calculate the growth rate using the given formula
    growth_rate = (math.log(final_count) - math.log(initial_count)) / time_elapsed

    # Round the growth rate to 4 decimal places
    growth_rate = round(growth_rate, 4)

    # Display the calculated growth rate
    print(f"The growth rate is: {growth_rate}")

    # Provide a subtle, humorous interpretation of the growth rate
    print(interpret_growth_rate(growth_rate))

# Run the main function if this script is executed as the main program
if __name__ == "__main__":
    main()
