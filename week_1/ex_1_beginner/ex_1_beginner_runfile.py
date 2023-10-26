# Definition of the list of microbial population counts over five consecutive days
population_counts = [100, 200, 150, 300, 50]


def calculate_statistics(pop_counts):
    """Function to calculate and display basic statistics on microbial population."""
    # Calculate the average
    average_count = sum(pop_counts) / len(pop_counts)
    # Calculate the maximum
    max_count = max(pop_counts)
    # Calculate the minimum
    min_count = min(pop_counts)

    # Displaying the statistics
    print(f'Average population: {average_count}')
    print(f'Maximum population: {max_count}')
    print(f'Minimum population: {min_count}')


def identify_high_population_days(pop_counts, threshold=200):
    """Function to identify and display days with a population greater than a certain threshold."""
    print(f'Days with a population greater than {threshold}:')
    for day_number, count in enumerate(pop_counts, start=1):  # Day numbering starts at 1
        if count > threshold:
            print(f'Day {day_number}')


# Calling functions with the list of population counts
calculate_statistics(population_counts)
identify_high_population_days(population_counts)
