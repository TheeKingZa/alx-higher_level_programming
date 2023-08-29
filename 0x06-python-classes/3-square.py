#!/usr/bin/python3
"""
This module contains the definition of the Square class.
"""


class Square:
    """
    This is the Square class.
    It defines a square based on the provided size.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.
        Args:
            size (int, optional):
                The size of the square's sides. Defaults to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Computes and returns the current square's area.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2


'''
Note: The class now includes a public instance method
    'area' that calculates and returns
# the area of the square based on the size attribute.
'''
