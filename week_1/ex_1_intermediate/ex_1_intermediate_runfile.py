microbial_species = {"Bacteria": 20, "Archaea": 15, "Fungi": 10}
total_samples = 0

for species, samples in microbial_species.items():
    total_samples += samples
    if samples > 15:
        print(f'Species greater than 15: {species}')

print(f'Number of samples in all species: {total_samples}')

def add_species(species_dict, new_species):
    if new_species in species_dict:
        species_dict[new_species] += 1
    else:
        species_dict[new_species] = 1

while True:
    new_species_name = input("Enter a new species name (or 'continue' to exit): ")

    if new_species_name.lower() == 'continue':
        break

    add_species(microbial_species, new_species_name)
    print(f'{new_species_name} has been added or incremented.')

print("Final Microbial Species Dictionary:")
for species, samples in microbial_species.items():
    print(f'{species}: {samples} samples')
