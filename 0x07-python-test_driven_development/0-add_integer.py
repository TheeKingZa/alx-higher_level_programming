#!/usr/bin/python3

def add_integer(a, b=98):
    """
    This function adds two integers.

    :param a: The first integer.
    :param b: The second integer (default is 98).
    :return: The sum of a and b as an integer.
    """
    '''
    Check if a and b are either integers or floats,
    otherwise raise an exception.
    '''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast a and b to integers if they are floats.
    a = int(a)
    b = int(b)

    # Calculate the sum of a and b and return it.
    result = a + b
    return (result)
