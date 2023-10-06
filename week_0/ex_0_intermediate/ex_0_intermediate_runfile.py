#
import math
initialcount = input("Enter the initial count: ")
finalcount = input("Enter the final count:")
time = input("Enter the time:")
if  initialcount.isdigit() and finalcount.isdigit() and time.isdigit():
    if (int(finalcount) > int(initialcount)):
        GrowthRate = math.log(int(finalcount)) - math.log(int(initialcount)) / int(time)
        print(GrowthRate)
    else:
        print("invalid input")
else:
    print("invalid input")

