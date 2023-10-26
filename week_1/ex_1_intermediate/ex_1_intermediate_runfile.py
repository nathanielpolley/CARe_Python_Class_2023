# Define a dictionary to hold microbial species and their sample counts.
# Key: Species name, Value: Number of samples collected for that species
microbial_species = {"Bacteria": 20, "Archaea": 15, "Fungi": 10}

# Calculate the total number of samples collected across all species.
# Use the 'values' method to get the sample counts and sum them up.
total_samples = sum(microbial_species.values())
print(f"Total number of samples collected: {total_samples}")

# Use list comprehension to filter species with sample count greater than 15.
# 'items' method gives us key-value pairs to loop through.
species_gt_15 = [species for species, count in microbial_species.items() if count > 15]
print(f"Species with more than 15 samples: {species_gt_15}")


# Function to add a new species to the dictionary.
# Takes the existing species dictionary and a new species name as arguments.
def add_species(species_dict, new_species):
    # Check if the species already exists in the dictionary.
    if new_species in species_dict:
        # If exists, increment the sample count by 1.
        species_dict[new_species] += 1
    else:
        # If not, add the species to the dictionary with initial sample count of 1.
        species_dict[new_species] = 1


# Loop to continuously add new species.
# The loop will run until the user decides to stop.
while True:
    # Prompt the user for a new microbial species name.
    new_species = input("Enter a new microbial species (or type 'stop' to exit): ")

    # Check if the user wants to stop adding new species.
    if new_species.lower() == "stop":
        break

    # Use the function to add the new species to the dictionary.
    add_species(microbial_species, new_species)

    # Display the updated dictionary.
    print(microbial_species)
