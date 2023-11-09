#Python Layout Guidelines
'''This is a module-level docstring.

It provides information about the purpose of this module.

We will be demonstrating standard layout of a Python file here
'''

# Standard library imports
import os
import sys

# Third-party library imports
import numpy as np
import scipy as sp
import matplotlib as plt

# Local application imports
from my_module import my_function

#Global constraints
MAX_VALUE = 100
DEFAULT_NAME = "Guillaume Dupont"

#Function and Class definitions
def calculate_average(numbers):
    '''Calculate the average of a list of numbers.'''
    total = sum(numbers)
    count = len(numbers)
    return total / count

class Student:
    def __init__(self, name, age):
        '''Initialize a Student object with a name and age.'''
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hi, I am {self.name} and {self.age} years old.")

#Main Code (Code to execute when the script is run)
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    avg = calculate_average(numbers)
    print("Average:", avg)
    # Create an instance of Student object and call its "introduce" method
    student_1=Student(DEFAULT_NAME, "31")
    student_1.introduce()
    # Call of my_function from my_module.py module
    print(my_function(5, 6))




