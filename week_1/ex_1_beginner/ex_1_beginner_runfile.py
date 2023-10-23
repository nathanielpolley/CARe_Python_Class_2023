# Define a list of microbial population counts for five consecutive days
population_counts = [100, 200, 150, 300, 50]

# Calculate and print the average population count
average_population = sum(population_counts) / len(population_counts)
print(f"Average population count: {average_population}")

# Calculate and print the maximum population count
max_population = max(population_counts)
print(f"Maximum population count: {max_population}")

# Calculate and print the minimum population count
min_population = min(population_counts)
print(f"Minimum population count: {min_population}")

# Use a for loop to iterate through the population counts and identify days when the population exceeds 200
days_above_200 = []
for day, count in enumerate(population_counts, start=1):
    if count > 200:
        days_above_200.append(day)

# Print out the day numbers when the population exceeds 200
if days_above_200:
    print(f"Days when population exceeds 200: {', '.join(map(str, days_above_200))}")
else:
    print("No days with population exceeding 200")

# Results:
# Average population count: 160.0
# Maximum population count: 300
# Minimum population count: 50
# Days when population exceeds 200: 4