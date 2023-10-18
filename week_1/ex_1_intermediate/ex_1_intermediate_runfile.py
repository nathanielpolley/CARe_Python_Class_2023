# Initialize an empty dictionary to store the microbial species and their sample counts
microbial_species = {}

# Function to add or update a species in the dictionary
def add_species(species_dict, species_name, sample_count):
    if species_name in species_dict:
        species_dict[species_name] += sample_count
    else:
        species_dict[species_name] = sample_count

# Ask the user for the initial sample counts for each species
print("Enter the initial sample counts for each species:")
while True:
    species_name = input("Species name (or 'done' to finish): ")
    if species_name.lower() == 'done':
        break
    sample_count = int(input(f"Sample count for {species_name}: "))
    add_species(microbial_species, species_name, sample_count)

# Calculate and print the total number of samples collected across all species
total_samples = sum(microbial_species.values())
print(f"Total Number of Samples Collected: {total_samples}")

# Use a list comprehension to create a list of species with sample counts greater than 15
high_count_species = [species for species, count in microbial_species.items() if count > 15]
print("Species with Sample Counts Greater than 15:", high_count_species)

# Implement a while loop to interactively add new species to the dictionary
while True:
    species_name = input("Enter a new species name (or 'stop' to quit): ")
    if species_name.lower() == 'stop':
        break
    sample_count = int(input(f"Sample count for {species_name}: "))
    add_species(microbial_species, species_name, sample_count)

# Print the updated dictionary
print("Updated Microbial Species Dictionary:")
for species, count in microbial_species.items():
    print(f"{species}: {count}")