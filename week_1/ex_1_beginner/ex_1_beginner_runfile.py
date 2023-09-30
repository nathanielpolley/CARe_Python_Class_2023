#YOUR CODE FOR EX_1 BEGINNER HERE
lst= [100,200,150,300,50]
average = 0
for i in lst:
    average += i
average = average/5
min = min(lst)
max = max(lst)
print("average= "+ str(average) +" Min= "+ str(min)+ " Max= "+ str(max))