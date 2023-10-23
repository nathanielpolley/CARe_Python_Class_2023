#YOUR CODE FOR EX_1 BEGINNER HERE

Population = [56, 92, 160, 230, 211]
print("The population of cells is", Population)

#Average population.
Average = sum(Population) / len(Population)
print("The average population count is ", Average)

#Max and Min population numbers.
print("The maximum population count is ", max(Population), "and the minimum population count is ",min(Population))

#Days >200 population count.

MinValue = 200

for num in range(len(Population)):
    a = Population[num]
    if a < 200:
        continue
    else:
        print(f"The population on Day {num+1}: {a} exceeded 200")


#Results Obtained
#The population of cells is [56, 92, 160, 230, 211]
#The average population count is  149.8
#The maximum population count is  230 and the minimum population count is  56
#The population on Day 4: 230 exceeded 200
#The population on Day 5: 211 exceeded 200