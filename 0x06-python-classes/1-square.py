#!/usr/bin/python3
"""
This module contains
definitions of the
Square class.
"""


class Square:
    """
    This is the square classs.
    It defines a square based on the provided size.
    """

    def __init(self. size):
        """
        Initialize a new instance of
        the Square class.

        Args:
            size (int):
                The size of Square's sides.
        """

        self.__size = size
        # Private instance sttribute.


"""
1.Note: size attribute is marked as private
    ...(with double underscores Prefix)
2.Control access to it and prevent "external" modifications.
3.Private attributes impliments information hiding and encapsulation,
4.ensuring that the internal state of
    OBJECT is not easily manipulated from outside.
"""
