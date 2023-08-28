#!/usr/bin/python3

def safe_print_integer(value):
    """
    Safely prints an integer using the "{:d}".format() formatting.

    Args:
        value (int): The integer to print.

    Returns:
        bool:
        True if printing is successful,
        False if a TypeError or ValueError occurs.
    """
    try:
        print("{:d}".format(value))
        # Try to print the integer using the specified format
        return (True)
        # Return True if printing is successful
    except (TypeError, ValueError):
        '''
        If a TypeError or ValueError occurs during printing,
        catch the exception
        '''
        # and return False to indicate that printing was not successful
        return (False)
