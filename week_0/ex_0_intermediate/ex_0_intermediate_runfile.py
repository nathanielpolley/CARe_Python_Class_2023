#YOUR CODE FOR EX_0 INTERMEDIATE HERE
import math

x = input("Enter the initial count of cells as an integer only.")
y = input("Enter the final count of cells as an integer only")
t = input("Enter the amount of time in minutes")


if x.isdigit() and y.isdigit() and t.isdigit() and y > x:
    print("Thank you")


    a = math.log(int(y)) - math.log(int(x))/ int(t)
    print("Microbial growth is ", round(a, 2))

else:
    print("Please enter only integer values and ensure the final count is greater than the initial count of cells")