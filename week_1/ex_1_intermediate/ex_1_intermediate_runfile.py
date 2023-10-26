# Étape 1 : Définissez un dictionnaire vide pour stocker les espèces microbiennes et leurs comptes d'échantillons.
microbial_species = {}

# Étape 2 : Mise en place d'une boucle pour calculer et imprimer le nombre total d'échantillons collectés.
total_samples = 0
for count in microbial_species.values():
    total_samples += count

# Étape 3 : Utilisez une compréhension de liste pour créer une liste d'espèces avec des comptes d'échantillons supérieurs à 15.
species_greater_than_15 = [species for species, count in microbial_species.items() if count > 15]

# Étape 4 : Créez une fonction pour ajouter de nouvelles espèces au dictionnaire avec le nombre d'échantillons.
def add_species(species_dict, new_species, sample_count):
    if new_species in species_dict:
        species_dict[new_species] += sample_count
    else:
        species_dict[new_species] = sample_count

# Étape 5 : Mise en place d'une boucle while pour demander continuellement à l'utilisateur les noms de nouvelles espèces et le nombre d'échantillons.
while True:
    new_species_name = input("Entrez le nom d'une nouvelle espèce (ou 'stop' pour quitter) : ")
    if new_species_name.lower() == 'stop':
        break
    try:
        sample_count = int(input(f"Entrez le nombre d'échantillons pour {new_species_name}: "))
        add_species(microbial_species, new_species_name, sample_count)
    except ValueError:
        print("Veuillez entrer un nombre valide pour le nombre d'échantillons.")

# Étape 6 : Imprimez le dictionnaire complet, y compris les modifications apportées par l'utilisateur, ainsi que le nombre d'échantillons pour chaque espèce.
print("Dictionnaire des espèces microbiennes :")
for species, count in microbial_species.items():
    print(f"{species}: {count} échantillons")

# Étape 7 : Calculez et imprimez à nouveau le nombre total d'échantillons, en tenant compte des modifications apportées par l'utilisateur.
total_samples = sum(microbial_species.values())
print(f"Total des échantillons collectés : {total_samples} échantillons")

# Étape 8 : Comptez le nombre total d'espèces dans le dictionnaire.
total_species = len(microbial_species)
print(f"Nombre total d'espèces : {total_species}")
