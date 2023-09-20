print("this program will calculate the Microbial Growth Rate based on your parameters, follow the instructions.")
while True :
    start= str(input("Enter the number of cells at the beginning: "))
    end= str(input("Enter the number of cells at the end: "))
    time= str(input("enter the time between start and end: "))
    valid = True
    for i in start:
        if i not in "0123456789.":
            valid = False
            print("insert a valid number")
            break
    if valid:
        break
import math
Growth_rate= (math.log(int(end))-math.log(int(start)))/int(time)
print("This population of cells have a GR of " + str(Growth_rate))
