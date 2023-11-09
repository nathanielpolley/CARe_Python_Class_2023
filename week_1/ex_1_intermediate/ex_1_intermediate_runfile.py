#YOUR CODE FOR EX_1 INTERMEDIATE HERE

"""-Create a Python script that defines a dictionary where the keys represent different microbial species
        (e.g., "Bacteria", "Archaea", "Fungi") and the values represent the number of samples collected for each species
        (e.g., {"Bacteria": 20, "Archaea": 15, "Fungi": 10}).
-Implement a loop to calculate and print the total number of samples collected across all species.
-Use a list comprehension to create a list of microbial species with sample counts greater than 15.
-Create a function that takes the species dictionary and a new species name as input. The function should add the new
        species to the dictionary with an initial count of 1 if the species is not already present. If the species is
        already in the dictionary, increase its count by 1.
-Implement a while loop to continuously prompt the user for new species names to add to the dictionary until they
        choose to stop it.
-Print out to the console the entirety of the dictionary including the changes made by the user.
-Please provide the Python runfile with comments explaining each step and the results of your calculations
        in the submit file."""

# Create a dictionary representing microbial species and their sample counts
dic = {
    "Bacteria": 20,
    "Archaea": 15,
    "Fungi": 10}

# Calculate and print the total number of samples
total_samples = 0
for i in dic.values():
    total_samples += i

print("Total number of samples collected across all species:", total_samples)


# Use a list comprehension to create a list of species with sample counts greater than 15
species_gt_15 = [species for species, count in dic.items() if count > 15]
print("Species with sample counts greater than 15:", species_gt_15)

# Create a function to add new species to the dictionary
def add_new_species(species_dict, new_species):
    if new_species in species_dict:
        species_dict[new_species] += 1
    else:
        species_dict[new_species] = 1

# Implement a while loop to continuously prompt the user for new species names
while True:
    new_species_name = input("Enter a new species name (or 'stop' to finish): ")
    if new_species_name.lower() == "stop":
        break
    add_new_species(dic, new_species_name)

# Print the updated dictionary
print("Updated dictionary of species and sample counts:", dic)

