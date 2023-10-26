# Demander à l'utilisateur de saisir la liste de données pour les populations sur 5 jours
population_counts = []
for day in range(1, 6):
    count = int(input(f"Enter the population for the day {day}: "))
    population_counts.append(count)

# Calculate and print the average population count
average_count = sum(population_counts) / len(population_counts)
print("Average Population Count:", average_count)

# Calculate and print the maximum population count
max_count = max(population_counts)
print("Maximum Population Count:", max_count)

# Calculate and print the minimum population count
min_count = min(population_counts)
print("Minimum Population Count:", min_count)

# Use a for loop to iterate through the population counts and identify days when the population exceeds 200
days_exceeding_200 = []
for day, count in enumerate(population_counts, 1):
    if count > 200:
        days_exceeding_200.append(day)

if days_exceeding_200:
    print("Days when the population exceeds 200:", days_exceeding_200)
else:
    print("No day exceeded a population of 200.")
