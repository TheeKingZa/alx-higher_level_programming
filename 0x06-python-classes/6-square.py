#!/usr/bin/python3
"""
This module contains the definition of the Square class.
"""


class Square:
    """
    This is the Square class.
    It defines a square based on the provided size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.
        Args:
            size (int, optional):
                The size of the square's sides. Defaults to 0.
            position (tuple, optional):
                The position of the square. Defaults to (0, 0).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for the size attribute.
        Returns:
            int: The size of the square's sides.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.
        Args:
            value (int): The size of the square's sides.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for the position attribute.
        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.
        Args:
            value (tuple): The position of the square.
        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes and returns the current square's area.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' characters.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
