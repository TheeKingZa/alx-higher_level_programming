#!/usr/bin/python3
"""inherits_from module - defines a function to check class inheritance"""


def inherits_from(obj, a_class):
    """Checks if an object is an
    instance of a class inherited from a specified class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
