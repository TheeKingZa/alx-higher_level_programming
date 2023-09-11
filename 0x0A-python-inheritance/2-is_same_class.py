#!/usr/bin/python3
"""is_same_class module - defines a function to check class instance"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a specified class"""
    return type(obj) is a_class
