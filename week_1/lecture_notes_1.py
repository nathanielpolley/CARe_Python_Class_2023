# List creation
fruits = ["apple", "banana", "cherry"]

# Indexing and slicing
first_fruit = fruits[0]  # Access the first item (indexing starts at 0)
subset = fruits[1:3]    # Extract a subset (slicing)

# List methods
fruits.append("orange")  # Add an element to the end of the list
fruits.remove("banana")  # Remove an element by value

# Display results
print(f"First fruit: {first_fruit}")
print(f"Subset of fruits: {subset}")

# List concatenation
all_fruits = fruits + ["grape", "kiwi"]
print(all_fruits)

#List repitition
repeated_fruits = ["apple"] * 3
print(repeated_fruits)

#List length
num_fruits = len(fruits)
print(num_fruits)

# Tuple creation
dimensions = (10, 20)
print(dimensions)

#Tuple unpacking to variables
width, height = dimensions
print(width, height)

# Dictionary creation
student = {"name": "Alice", "age": 25}
print(student)

# Accessing values
student_name = student["name"]  # Accessing a dictionary value by key
print(student_name)

# Dictionary manipulation
student["grade"] = "A"   # Add a new key-value pair
student["age"] = 26      # Update an existing value
del student["age"]       # Delete a key-value pair

# Using a for loop
squares = []
for x in range(1, 6):
    squares.append(x * x)

# Using list comprehension
squares_comp = [x ** 2 for x in range(1, 6)]

# Display results
print(f"Squares: {squares}")
print(f"Squares (list comprehension): {squares_comp}")

#Conditional list comprehension
even_squares = [x * x for x in range(1, 6) if x % 2 == 0]
print(f"Even squares: {even_squares}")

#Nested list comprehension (2-dimensional lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
flattened_matrix = [element for row in matrix for element in row]
print(flattened_matrix)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#Range function for loops
for i in range(5):  # Equivalent to range(0, 5)
    print(i)

#Enumerating lists
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Function definition
def greet(name):
    return f"Hello, {name}!"

# Function call
message = greet("Alice")
print(message)

#Function with multiple parameters
def greet(name, greeting):
    return f"{greeting}, {name}!"

message = greet(name="Alice", greeting="Goodbye")
print(message)

# Reading a file
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Writing to a file
with open("output.txt", "w") as file:
    file.write("Hello, World!")

#Exception handling
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")