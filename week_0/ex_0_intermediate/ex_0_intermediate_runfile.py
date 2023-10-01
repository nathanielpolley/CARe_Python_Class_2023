#DE FOR EX_0 INTERMEDIATE HERE
import math
initialcount = (input("Enter the  initialcount: "))
finalcount = (input("Enter the finalcount: "))
time = (input("Enter your time: "))
if  finalcount > initialcount and initialcount.isdigit() and finalcount.isdigit() and time.isdigit():
    GrowthRate = math.log(int(finalcount)) - math.log(int(initialcount)) / int(time)
    print (str(GrowthRate))
else:
    print("invalidinput")