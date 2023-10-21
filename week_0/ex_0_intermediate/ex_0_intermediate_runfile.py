# Matias Medina Tanco: EX_0 INTERMEDIATE

# Asks for input of each of the relevant variables (initial and final cell counts, time elapsed)
# If an invalid value is given for a variable the program asks again until a valid value is given


# import the relevant library
import math

# start loop to repeatedly ask for inputs until they are all correct

while True:
    # Ask for the initial and final cell counts, as well as time elapsed
    while True:
        try:
            initial = int(input("Enter the initial cell count: "))
            if initial <= 0:
                print("Please enter a value greater than 0.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    while True:
        try:
            final = int(input("Enter the final cell count: "))
            if final <= 0 or final < initial:
                print("Please enter a final count value greater than 0 and larger than the initial count value.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    while True:
        try:
            time = int(input("Enter the time elapsed: "))
            if time <= 0:
                print("Please enter a value greater than 0.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    # Check if the inputs are valid. If they are not valid then program will ask again for the inputs
    if (final > initial):
        # Calculates growth rate and prints out result
        initial = int(initial)
        final = int(final)
        time = int(time)

        # Check if time is greater than 0 to prevent an error in the formula (the .isdigit() method
        # allows zeroes to pass through)
        if time > 0:
            GrowthRate = (math.log(final) - math.log(initial)) / time
            print("The growth rate of the microbial culture is: ", GrowthRate)
            # Get out of loop to end program
            break
        else:
            print("Please enter valid inputs.")

    else:
        print("Please enter valid inputs.")