#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Calculates the division of 'a' by 'b',
    handles exceptions, and prints the result.

    Args:
        a (int or float): The numerator.
        b (int or float): The denominator.

    Returns:
        float or None: The division result or None if an exception occurred.
    """
    try:
        div = a / b
        # Attempt the division
    except (TypeError, ZeroDivisionError):
        div = None
        # Set result to None if TypeError or ZeroDivisionError occurs
    finally:
        print("Inside result: {}".format(div))
        # Print the result inside the 'finally' block
    return (div)
    # Return the division result or None
