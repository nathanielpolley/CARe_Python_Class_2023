#YOUR CODE FOR EX_1 BEGINNER HERE


import statistics #import of stats library to access mean, min, and max functions
MBPopCount = [50,150,750,500,225] #creation of list with values for each day of 5 day period

for i in MBPopCount: #for loop to find mean, min, and max
        average = statistics.mean(MBPopCount)
        minimum = min(MBPopCount)
        maximum = max(MBPopCount)
print(average,minimum,maximum)

#pairing day with population using enumerate
for index, population in enumerate (MBPopCount):
       print(f"day {index}: {population}")


#finding days where microbial population exceeds 200
for i in range(len(MBPopCount)):
      popbyday = MBPopCount[i]
      if popbyday < 200:
             continue
      else:
             print(f"Population at day{i}: {popbyday}")