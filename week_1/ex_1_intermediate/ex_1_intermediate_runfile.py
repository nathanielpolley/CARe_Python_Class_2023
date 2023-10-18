#YOUR CODE FOR EX_1 INTERMEDIATE HERE

MBSpecies = {"Protozoa":57, "Algae":10, "Bacteria":35,"Fungi":5 } #dictionary of diff microbial species

import numpy as np


# for loop to obtain total # of samples
for i in (MBSpecies):
    total_samples = sum(MBSpecies.values())
print(total_samples)

#for loop to find species with counts greater than 15
for i in range(len(MBSpecies)):
    values_list = list(MBSpecies.values())
    newlist = values_list[i]
    if newlist < 15:
        continue
    else:
        print(f"Species index {i}: {newlist}")

#add a new species
MBSpecies = {"Protozoa":57, "Algae":10, "Bacteria":35,"Fungi":5 }
species = input("enter species name!")
numgrowth = int()
counter = 0
counter1 = MBSpecies.values()
def add_species(species,numgrowth):
    newspec = {species: numgrowth}
    MBSpecies.update(newspec)
    if newspec != MBSpecies:
        counter = +1
    else:
        counter1 = +1


#while loop
while True:
    print("Add species please")
    add_species




