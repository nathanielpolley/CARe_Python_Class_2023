# Demander à l'utilisateur de saisir les valeurs de population pour cinq jours consécutifs
population_counts = []
for day in range(1, 6):
    count = int(input(f"Enter the population count for Day {day}: "))
    population_counts.append(count)

# Calculer et afficher la moyenne de la population
average_population = sum(population_counts) / len(population_counts)
print(f"Average Population Count: {average_population}")

# Calculer et afficher la population maximale
max_population = max(population_counts)
print(f"Maximum Population Count: {max_population}")

# Calculer et afficher la population minimale
min_population = min(population_counts)
print(f"Minimum Population Count: {min_population}")

# Utiliser une boucle for pour identifier les jours où la population dépasse 200
print("Days with population exceeding 200:")
for day, count in enumerate(population_counts, start=1):
    if count > 200:
        print(f"Day {day}: {count}")