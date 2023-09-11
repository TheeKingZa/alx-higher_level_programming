#!/usr/bin/python3
"""
Define a function named is_same_class that takes,
two arguments, obj and a_class.
"""
def is_same_class(obj, a_class):
    # Check if the type of obj is equal to a_class.
    if type(obj) == a_class:
        # If they are the same, return True.
        return True
    # If they are not the same, return False.
    return False
