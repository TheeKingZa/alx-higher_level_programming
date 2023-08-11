#!/usr/bin/python3
""" Importing the function from add_0.py """

if __name__ == "__main__":
    """sum of 1 and 2"""
    from add_0 import add

    a = 1
    b = 2
    """ Calling the add function and printing the result """
    print("{} + {} = {}".format(a, b, add(a, b)))
