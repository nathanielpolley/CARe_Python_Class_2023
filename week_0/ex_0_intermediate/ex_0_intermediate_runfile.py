print("this program will calculate the Microbial Growth Rate based on your parameters, follow the instructions.")
while True :
    start= input("Enter the number of cells at the beginning: ")
    end= input("Enter the number of cells at the end: ")
    time= input("enter the time between start and end: ")
    valid = True
    lst = [start,end,time]
    for i in lst:
        if i.isdigit():
            valid= True
        else:
            valid= False
    if valid:
        break
    else:
        print("please enter a numerical value")
import math
Growth_rate= (math.log(int(end))-math.log(int(start)))/int(time)
print("This population of cells have a GR of " + str(Growth_rate))
