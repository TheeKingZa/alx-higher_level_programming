#!/usr/bin/python3
'''Defines a RECTANGLE class.
'''


class Rectangle:
    """RECTANGLE CLASS.
    """

    def __init__(self, width=0, height=0):
        '''NEW RECTANGLE.

        Args:
            width:(int)
                The width of the new rectangle.
            height:(int)
                The height of the new rectangle.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        get or set the width of the rectangle.
        """
        return __self.width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        get or set the height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Return the area of rectangle.
        """
        return (self.__width * self.__height)

    def perimeeter(self):
        """
        REturn the perimeter of rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self._width * 2) + (self.__height * 2))
