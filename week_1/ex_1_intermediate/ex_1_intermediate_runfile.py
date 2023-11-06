#YOUR CODE FOR EX_1 INTERMEDIATE HERE

MBSpecies = {} #dictionary of diff microbial species

# for loop to obtain total # of samples
for i in (MBSpecies):
    total_samples = sum(MBSpecies.values())
print(f"Total number of samples collected: {total_samples}")

#List comprehension to obtain list of microbial species with value greater than 15
for i in range(len(MBSpecies)):
    values_list = list(MBSpecies.values())
    newlist = values_list[i]
    if newlist < 15: #if statement to print
        continue
    else:
        print (f"Species at index {i}, {newlist}")

# function to keep enter new species to dictionary
species = input("Enter species name!")
numgrowth = int(input('value'))

def add_species(MBSpecies, species, numgrowth):
    if species in MBSpecies:
        MBSpecies[species] += numgrowth
    else:
        MBSpecies[species] = numgrowth


# While loop to add new species to dictionary + print updated version!

while True:
    species = input("Enter a new species name" or "finish operation")
    if species == MBSpecies.keys:
        break
    else:
        numgrowth = int(input(f"sample count for species {species}: "))
        add_species(MBSpecies, species, numgrowth)

for species, count in MBSpecies.items():
    print(f"{species}: {count}")



