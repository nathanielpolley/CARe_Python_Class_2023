#YOUR CODE FOR EX_0 INTERMEDIATE HERE

import math

initial_count = int(input("Type the initial cell count: "))
final_count = int(input("Type the final cell count: "))
time = int(input("Type the time: "))


def GrowthRate(initial_count, final_count, time):
    growth_rate = (math.log(final_count) - math.log(initial_count)) / time
    return growth_rate
if (final_count > initial_count>0) and (time>0) and (isinstance(initial_count,int)) and (isinstance(final_count,int)) and (isinstance(time,int)):
    result = GrowthRate(initial_count, final_count, time)
    print("Growth Rate:", result)
else:
    print("error ! remember : - your final count need to be higher than the initial count"
          "        - time and initial count have to be positive"
          "        - you need to enter a int")

#done


