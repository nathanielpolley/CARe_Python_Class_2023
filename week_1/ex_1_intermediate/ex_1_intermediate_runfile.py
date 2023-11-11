#YOUR CODE FOR EX_1 INTERMEDIATE HERE
#-Create a Python script that defines a dictionary where the keys represent different microbial species
samples= {'Bacteria': 20,
          'Archaea': 15,
          'Fungi': 10}
#-Implement a loop to calculate and print the total number of samples collected across all species.
samples_val= samples.values()
total_samples= 0
for i in samples_val:
    total_samples += i
print(total_samples)
#-Use a list comprehension to create a list of microbial species with sample counts greater than 15.
dict_15_minimum={}
for key,value in samples.items():
    if value >15:
        dict_15_minimum.update({key:value})
print(dict_15_minimum.items())
#-Create a function that takes the species dictionary and a new species name as input. The function should add the new
#species to the dictionary with an initial count of 1 if the species is not already present. If the species is
#already in the dictionary, increase its count by 1.
def dictionary_addition(dict):
    name= str(input('Enter the name of the species to add: ').lower().capitalize())
    if name in dict:
        dict[name] += 1
    else:
        dict[name] = 1
    return dict
#dictionary_addition(samples)
#print(samples.items())

#-Implement a while loop to continuously prompt the user for new species names to add to the dictionary until they
#choose to stop.it the Python runfile with comments explaining each step and the results of your calculations in the submit file.
def multiple_dictionary_addition(dict):
    while True:
        more= True
        name= str(input('Enter the name of the species to add: ').lower().capitalize())
        if name in dict:
            dict[name] += 1
        else:
            dict[name] = 1
        x= input("Do you wish to add another sample Y/N: ").upper()
        if x !="Y":
            break
multiple_dictionary_addition(samples)
print(samples.items())