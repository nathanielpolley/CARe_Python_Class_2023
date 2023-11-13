import math
initial_count=(input("enter the initial cell number:"))
final_count=(input("enter the final cell count:"))
time=(input("enter the time:"))

if initial_count.isdigit()and final_count.isdigit() and time.isdigit():
    print('good input')
    initial_count = int(initial_count)
    final_count = int(final_count)
    time = int(time)
    if initial_count<final_count:
        print('The growth rate is:')
        print((math.log(final_count) - math.log(initial_count)) / time)
    else:
        print('Conditions are wrong: initial count needs to be smaller than final count')
else:
    print('wrong input, please enter positive number values')

#Converting into int to calculate





