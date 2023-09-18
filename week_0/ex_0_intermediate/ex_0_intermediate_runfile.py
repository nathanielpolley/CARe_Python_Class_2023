print("this program will calculate the Microbial Growth Rate based on your parameters, follow the instructions.")
start= int(input("Enter the number of cells at the beginning: "))
end= int(input("Enter the number of cells at the end: "))
time= int(input("enter the time between start and end: "))
import math
Growth_rate= (math.log(end)-math.log(start))/time
print("This population of cells have a GR of " + str(Growth_rate))
