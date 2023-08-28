#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_function(fct, *args):
    """
    Executes a given function with provided arguments, handles exceptions,
    and prints an error message to standard error if an exception occurs.

    Args:
        fct (function): The function to execute.
        *args: Variable number of arguments to pass to the function.

    Returns:
        Any:
            * The result of the function execution,
            * or None if an exception occurs.
    """
    try:
        res = fct(*args)
        # Execute the provided function with the provided arguments
    except Exception as e:
        '''
        * If an exception occurs,
        catch it and print an error message to standard error
        '''
        print("Exception: {}".format(e), file=sys.stderr)
        return (None)
        # Return None to indicate that an exception occurred
    else:
        # If no exception occurs, return the result of the function execution
        return (res)
