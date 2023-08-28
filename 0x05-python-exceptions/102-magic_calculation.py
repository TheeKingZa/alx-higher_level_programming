#!/usr/bin/python3

def magic_calculation(a, b):
    """
    Performs a specific calculation involving 'a' and 'b'
    with exception handling.

    Args:
        a (int): The first parameter.
        b (int): The second parameter.

    Returns:
        int or float: The result of the calculation.
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += a ** b / i
        except Exception:
            result = b + a
            # If an exception occurs, assign a new value to 'result'
            break
            # Exit the loop
    return (result)
    # Return the final result
