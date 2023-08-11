#!/usr/bin/python3
if __name == "__main__":
    """Print the calculations of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    # Printing the results
    print("{a} + {b} = {}".format(a, b, add(a, b)))
    print("{a} - {b} = {}".format(a, b, sub(a, b)))
    print("{a} * {b} = {}".format(a, b, mul(a, b)))
    print("{a} / {b} = {}".format(a, b, div(a, b)))
