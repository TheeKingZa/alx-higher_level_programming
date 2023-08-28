#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """
    Prints an integer using the "{:d}".format() formatting,
    handles exceptions,

    and prints an error message to standard error
    if a ValueError occurs.

    Args:
        value (int): The integer to print.

    Returns:
        bool:
          *  True if printing is successful,
          * False if a TypeError or ValueError occurs.
    """
    try:
        print("{:d}".format(value))
        # Try to print the integer using the specified format
        return (True)
        # Return True if printing is successful
    except (TypeError, ValueError):
        '''
        * If a TypeError or ValueError occurs during printing,
        catch the exception
        '''
        '''
        * Print an error message to standard error,
        including the exception message
        '''
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
        # Return False to indicate that printing was not successful
