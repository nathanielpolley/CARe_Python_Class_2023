#YOUR CODE FOR EX_0 INTERMEDIATE HERE
import math

initial_count = float(input("write the initial cell count: "))
final_count: float = float(input("write the final cell count: "))
time = float(input('write the time: '))
def GrowthRate(initial_count, final_count, time):
    growth_rate = (math.log(final_count) - math.log(initial_count)) / time
    return growth_rate

result = GrowthRate(initial_count, final_count, time)
print('Growth Rate:', result)