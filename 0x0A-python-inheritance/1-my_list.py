#!/usr/bin/python3
"""
This module defines the MyList class
    a subclass of the built-in list class.

The MyList class provides a method
    to print the list in sorted (ascending) order.
"""


# Define the MyList class as a subclass of the built-in list class.
class MyList(list):
    """a subclass of list"""

    # Initialize the MyList object.
    def __init__(self):
        """initializes the object"""
        # Call the constructor of the base class (list)
        # to initialize the object.
        super().__init__()

    # Define a method to print the sorted list.
    def print_sorted(self):
        """prints the sorted list"""
        # Use the sorted function
        # to create a sorted copy
        # of the list and print it.
        print(sorted(self))
