#!/usr/bin/python3
"""
0-add module

This module provides a simple addition function.
"""


def add(a, b):
    """
    Add two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of a and b.
    """
    return (a + b)


if __name__ == "__main__":
    a = 1
    b = 2
    result = add(a, b)
    print(f"{a} + {b} = {result}")
