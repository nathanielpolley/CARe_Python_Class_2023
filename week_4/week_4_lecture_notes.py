import matplotlib.pyplot as plt

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio import Align
from Bio import Phylo

#Circle object example
class Circle:
    def __init__(self, radius = 3, color = "blue"):
        self.radius = radius
        self.color = color
    def add_radius(self,r):
        self.radius = self.radius + r
        return(self.radius)
    def drawCircle(self):
        circle = plt.Circle((0,0), radius = self.radius, fc = self.color)
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()

RedCircle = Circle(10,"red")
dir(RedCircle)
RedCircle.radius
RedCircle.color

RedCircle.radius = 1
RedCircle.radius

RedCircle.drawCircle()

print("Radius of object: ", RedCircle.radius)
RedCircle.add_radius(2)
print("Radius of object after add_radius(2): ", RedCircle.radius)
RedCircle.add_radius(5)
print("Radius of object after add_radius(5): ", RedCircle.radius)
RedCircle.drawCircle()

BlueCircle = Circle(radius = 100)
BlueCircle.radius
BlueCircle.color
BlueCircle.drawCircle()

#Rectangle object example
class Rectangle(object):
    def __init__(self, width = 2, height = 3, color = 'r'):
        self.height = height
        self.width = width
        self.color = color
    def drawRectangle(self):
        rectangle = plt.Rectangle((0, 0), width=self.width, height=self.height, fc = self.color)
        plt.gca().add_patch(rectangle)
        plt.axis("scaled")
        plt.show()

SkinnyBlueRectangle = Rectangle(2,3,"blue")

SkinnyBlueRectangle.drawRectangle()

FatYellowRectangle = Rectangle(20,5,"yellow")
FatYellowRectangle.drawRectangle()

#Example of object inheritance
# Superclass (Parent Class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        pass

# Subclass (Child Class)
class Dog(Animal):
    def speak(self):
        return f"{self.name} the {self.species} barks: Woof!"

# Subclass (Child Class)
class Cat(Animal):
    def speak(self):
        return f"{self.name} the {self.species} meows: Meow!"

# Create instances of the subclasses
dog = Dog("Buddy", "Dog")
cat = Cat("Whiskers", "Cat")

# Call the speak method on the instances
print(dog.speak())  # Output: Buddy the Dog barks: Woof!
print(cat.speak())  # Output: Whiskers the Cat meows: Meow!

#Example of object polymorphism
# Base class (abstract class)
class Shape:
    def area(self):
        pass

# Subclass 1
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1415 * self.radius * self.radius

# Subclass 2
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Function to calculate the area of any shape (polymorphism)
def calculate_area(shape):
    return shape.area()

# Create instances of the subclasses
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calculate and print the areas of different shapes
print("Area of the circle:", calculate_area(circle))       # Output: Area of the circle: 78.5375
print("Area of the rectangle:", calculate_area(rectangle)) # Output: Area of the rectangle: 24

#BioPython

# Creating a sequence
my_sequence = Seq("AGTACACTGGT")

# Slicing a sequence
sub_sequence = my_sequence[2:5]

# Reverse complement
reverse_complement = my_sequence.reverse_complement()

# Reading a sequence file
# with open("sequences.fasta") as file:
#     records = SeqIO.parse(file, "fasta")
#
# # Writing a sequence to a file
# with open("output.fasta", "w") as output_file:
#     SeqIO.write(records, output_file, "fasta")

# Define the path to the FASTA file
fasta_file = "sequences.fasta"

# Read the FASTA file
records = list(SeqIO.parse(fasta_file, "fasta"))

# Print sequence information
for record in records:
    print("Sequence ID:", record.id)
    print("Sequence description:", record.description)
    print("Sequence length:", len(record.seq))
    print("Sequence:", record.seq)
    print()

# Accessing specific sequences
sequence_2 = records[1]  # Indexing is zero-based
print("Sequence 2 ID:", sequence_2.id)
print("Sequence 2 length:", len(sequence_2.seq))

# Sequence manipulation
sequence_1 = records[0]
reverse_complement = sequence_1.seq.reverse_complement()
print("Reverse Complement of Sequence 1:", reverse_complement)

#Sequence Alignment
alignment = Align.PairwiseAligner()
score = alignment.score("AGTACACTGGT", "AGTGCACAGTA")

print(score)

# Reading a tree from a Newick file
tree = Phylo.read("tree.nwk", "newick")

# Visualizing the tree
Phylo.draw_ascii(tree)

#Error Exception Handling

#Arithmetic Error
try:
    result = 10 / 0
except ArithmeticError as e:
    print(f"Caught an ArithmeticError: {e}")

#Lookup Errors (IndexError and KeyError)
try:
    my_list = [1, 2, 3]
    value = my_list[5]
except IndexError as e:
    print(f"Caught an IndexError: {e}")

try:
    my_dict = {"name": "Alice"}
    value = my_dict["age"]
except KeyError as e:
    print(f"Caught a KeyError: {e}")

#Type Error
try:
    result = "5" + 10
except TypeError as e:
    print(f"Caught a TypeError: {e}")

#Value Error
try:
    num = int("abc")
except ValueError as e:
    print(f"Caught a ValueError: {e}")

#Keyboard Interrupt
try:
    input("Press Enter to continue...")
except KeyboardInterrupt:
    print("Caught a KeyboardInterrupt (Ctrl+C pressed)")