import pandas as pd

# Basic list comprehension
squares = [x * x for x in range(1, 6)]

# Conditional list comprehension
even_squares = [x * x for x in range(1, 6) if x % 2 == 0]

# Using a for loop with an if statement
fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    fruit = fruits[i]
    if fruit == "banana":
        continue
    else:
        print(f"Fruit at index {i}: {fruit}")

# Generator function
def square_numbers(n):
    for i in range(n):
        yield i * i

# Using a generator
squares = square_numbers(5)

#Function recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Program to find the first even number and skip odd numbers in a list

numbers = [1, 3, 5, 6, 8, 9, 10, 12]

# Using a for loop with break and continue
found_even = False  # A flag to track if an even number is found

for num in numbers:
    if num % 2 == 0:  # Check if the number is even
        print(f"Found the first even number: {num}")
        found_even = True
        break  # Exit the loop as we found an even number
    else:
        print(f"Skipping odd number: {num}")
        continue  # Skip to the next iteration if the number is odd

if not found_even:
    print("No even numbers found in the list.")


# Function to calculate the area of a rectangle and return the result

def calculate_rectangle_area(length, width):
    if length <= 0 or width <= 0:
        return None  # Return None for invalid input

    area = length * width
    return area


# Calculate the area of a rectangle
length = 5
width = 4

area = calculate_rectangle_area(length, width)

if area is not None:
    print(f"The area of the rectangle is: {area}")
else:
    print("Invalid input. Please provide positive values for length and width.")

# Calculate and print Fibonacci numbers up to a specified limit
limit = 10
for i in range(limit):
    result = fibonacci(i)
    print(f"Fibonacci({i}) = {result}")

# Enumerate with for loop
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Zip with for loop
names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 88]
for name, score in zip(names, scores):
    print(f"Name: {name}, Score: {score}")

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 22],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston']
}

df = pd.DataFrame(data)

# Displaying the DataFrame
print("DataFrame created from a dictionary:")
print(df)
print("\n")

# Reading a CSV file into a DataFrame
csv_file = 'sample_data.csv'
df_from_csv = pd.read_csv(csv_file)

# Displaying the DataFrame from the CSV file
print("DataFrame read from a CSV file:")
print(df_from_csv)
print("\n")

# Filtering the DataFrame
filtered_df = df_from_csv[df_from_csv['Age'] > 30]

print("Filtered DataFrame (Age > 30):")
print(filtered_df)
print("\n")

# Grouping and aggregating data
grouped_df = df_from_csv.groupby('City').agg({'Age': 'mean'})

print("Grouped and aggregated DataFrame (mean age by city):")
print(grouped_df)
print("\n")

# Writing a DataFrame to a CSV file
output_csv_file = 'output_data.csv'
filtered_df.to_csv(output_csv_file, index=False)

print("Filtered DataFrame written to a CSV file.")