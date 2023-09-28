# Explain variables and data types
name = "Alice"  # String
age = 30  # Integer
height = 5.8  # Float
is_student = True  # Boolean

# Basic arithmetic operations
x = 10
y = 5

addition = x + y
subtraction = x - y
multiplication = x * y
division = x / y
remainder = x % y

# Display results
print(addition, subtraction, multiplication, division, remainder)

# Input from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Output to the console
print(f"Hello, {name}!")
print(f"You are {age} years old.")

# String creation
text = "Python is fun!"

# Indexing and slicing
first_char = text[0]
substring = text[7:10]
lastLetters = text[::8]

# Display results
print(first_char, substring, lastLetters)

# String methods
text = "Python is fun!"

# String length
length = len(text)

# String methods
uppercase_text = text.upper()
lowercase_text = text.lower()

# Display results
print(length, uppercase_text, lowercase_text)

# Conditional statements
x = 10

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# Logical operators
age = 25
is_student = True

if age >= 18 and is_student:
    print("You are an adult student.")
else:
    print("You are not an adult student.")