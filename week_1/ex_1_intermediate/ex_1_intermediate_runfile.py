# Matias Medina Tanco: EX_1 INTERMEDIATE

# Define dictionary
microbeDict = {
    "Bacteria" : 20,
    "Archaea" : 15,
    "Fungi" : 10,
}

# Define the totalSamples variable (for adding up the total number of samples in the dictionary)
totalSamples = 0

# Add up the numbers of samples for all species in the dictionary
for val in microbeDict.values():
    totalSamples = totalSamples + val

# Print out the result
print("A total of ", totalSamples, " samples have been collected from all species.")

# Use a list comprehension to create a list of microbial species with sample counts greater than 15.
listSpecies = [k for (k,v) in microbeDict.items() if v>15]
print("List of species with more than 15 collected samples: ", listSpecies)

# Create a function that takes the species dictionary and a new species name as input
def speciesFunction(dict, species):
    # Check if species exists within the dictionary
    if dict.__contains__(species):
        # If the species exists within the dictionary, add 1 to the collected samples count
        print(species, " found within dictionary, adding one collected sample to species...")
        dict[species] = dict[species]+1
        print("There are now ", dict[species], " samples of ", species)
    else:
        # If the species doesn't exist within the dictionary, add it to dictionary and set sample count to 1
        print(species, " NOT found within dictionary, creating a new entry...")
        dict[species] = 1
        print("There are now ", dict[species], " samples of ", species)

# Establish while loop to continuously prompt the user for new species names to add to the dictionary until
# they choose to stop
while True:
    # Ask for user choice on whether or not to continue
    print("Do you want to register a species sample? (y/n)")
    choice = input()

    # If user's choice was affirmative, continue
    if choice == "y":
        print("Understood.")
    # If user's choice was negative, terminate program
    elif choice == "n":
        print("Terminating program.")
        break
    # Elegantly and empathetically deal with clever users
    else:
        print("Weird input, assuming you want to enter a species.")

    # Ask for the species name
    speciesInput = input("Please enter your species: ")

    # Call forth the speciesFunction function defined earlier
    speciesFunction(microbeDict, speciesInput)