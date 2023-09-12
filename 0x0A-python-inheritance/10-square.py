#!/usr/bin/python3
"""Square module - defines a Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle"""

    def __init__(self, size):
        """Initializes a Square instance with size."""
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)  # Call the parent class constructor with size for width and height

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2
