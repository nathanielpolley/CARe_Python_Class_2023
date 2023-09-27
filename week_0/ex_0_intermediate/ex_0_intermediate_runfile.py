#YOUR CODE FOR EX_0 INTERMEDIATE HERE
x = 60 #initial count
y = 1000 #final count
z = 24 #time
print(x,y,z)

import math
a=print(math.log(x,10)) #log10 of initial count
b=print(math.log(y,10)) #log10 of final count

w=math.log(y,10)-math.log(x,10) #substraction of log10 of final and initial counts
print(w)

t=w/z #Growth Rate
print(t)
