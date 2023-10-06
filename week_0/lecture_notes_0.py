# Explain variables and data types
name = "Alice"  # String
age = 30  # Integer
height = 5.8  # Float
is_student = True  # Boolean

# Basic arithmetic operations
x = 12
y = 5

addition = x + y
subtraction = x - y
multiplication = x * y
exponents = x ** y
division = x / y
division_no_remainder = x // y
remainder = x % y
scientific = "{:e}".format(exponents)

# Display results
print(addition, subtraction, multiplication, exponents, division, division_no_remainder, remainder, scientific)

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
last_char = text[-1]
substring = text[7:10]
everything_after_fourth_char = text[4::]
every_fourth_char = text[::4]

# Display results
print(first_char, last_char, substring, everything_after_fourth_char, every_fourth_char)

#Strings
text = "Python is fun!"

length = len(text)

# String methods
uppercase_text = text.upper()
lowercase_text = text.lower()
replace_text = text.replace("fun","easy")
find_text_1 = text.find("is")
find_text_2 = text.find("Java")

# Display results
print(length, uppercase_text, lowercase_text, replace_text, find_text_1, find_text_2)

#String concantenation

#Repeat per number of times
line_1 = "Et la trace de leurs vertus "
print(2*line_1)

#Adding strings together
line_2 = "Bien moins jaloux de leur survivre "
print(line_1+line_2)

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

# "and" operator
if age >= 18 and is_student:
    print("You are an adult student.")
else:
    print("You are not an adult student.")

#Bitwise equivalent (AND)
if age >= 18 & is_student:
    print("You are an adult student.")
else:
    print("You are not an adult student.")

# inclusive "or" operator
x = 10
y = 5

if x > 7 or y < 3:
    print("At least one of the conditions is true.")
else:
    print("Neither condition is true.")

#Bitwise equivalent (OR - inclusive OR)
if x > 7 | y < 3:
    print("At least one of the conditions is true.")
else:
    print("Neither condition is true.")

#exclusive "or" operator
x = True
y = False

if (x and not y) or (not x and y):
    print("Exactly one of x or y is true (XOR).")
else:
    print("Neither or both x and y are true.")

#Bitwise equivalent (XOR - exclusive OR)
if x ^ y:
    print("Exactly one of x or y is true (XOR).")
else:
    print("Neither or both x and y are true.")
    
# "not" operator
name = "Maxence"

if not(name == "Anna"):
    print("You are not Anna")
else:
    print("You are Anna")
    
#Bitwise equivalent (NOT)
if name != "Anna":
    print("You are not Anna")
else:
    print("You are Anna")
