#!/usr/bin/python3
"""
This is a module for adding two integers.
"""


def add_integer(a, b=98):
    """
    Add two integers or floats.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast to integers if inputs are floats
    a = int(a)
    b = int(b)

    return a + b
