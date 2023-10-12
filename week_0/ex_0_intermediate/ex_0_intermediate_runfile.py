#YOUR CODE FOR EX_0 INTERMEDIATE HERE

import math


ICount = float(input("Input the initial count : \n"))
FCount = float(input("Input the final count : \n"))
Time = float(input("Input the time : \n"))
GRate = (math.log(FCount) - math.log(ICount)) / Time

print("The growth rate is : ", GRate)
