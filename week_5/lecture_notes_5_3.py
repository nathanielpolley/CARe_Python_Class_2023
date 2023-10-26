'''
PEP-8 Formatting Style Conventions
'''

# Imports on separate lines
import math
import sys

# Import grouping order
import os
import numpy as np
from my_module import my_function

# Blank lines between import groups

# Indentation
# Use 4 spaces for indentation (not tabs)
def example_function(arg1, arg2):
    if arg1:
        print("This is indented by 4 spaces.")
    else:
        print("So is this.")

def continuation_example():
    long_variable_name = ("This is a very long line with a "  # Wrapped elements
                          "continuation line.")

# Limit lines to 79 characters for code
long_string = "This is a long string that exceeds the recommended " \
              "character limit of 79."

# Limit lines to 72 characters for docstrings and comments
def example_function(arg1, arg2):
    """This is a docstring. It should be limited to 72 characters."""

# Use whitespace around operators and after commas
result = 2 * (3 + 4)
names = ["Alice", "Bob", "Charlie"]

# Avoid extraneous whitespace
example_function( arg1, arg2 )

# Complete sentence comments
# This is a comment explaining the purpose of the following code.

# Indent block comments
def example_function(arg1, arg2):
    """Docstring for this function."""
    # This is a block comment
    # explaining the following code.

# Inline comments separated by spaces
x = 10  # Initialize x to 10

# Function and variable names in lowercase with underscores
def my_function(arg1, arg2):
    my_variable = arg1 + arg2

# Class names follow CapWords (CamelCase)
class MyClass:
    pass

# Constants in uppercase with underscores
MAX_VALUE = 100

# Module-level variables preceded by a single underscore
_private_variable = 42



