#!/usr/bin/python3
'''
Defines a RECTANGLE class.
'''


class Rectangle:
    '''
    Represents a RECTANGLE.
    '''
    def __init__(self, width=0, height=0):
        '''New RECTANGLE.

        Arguments:
            width(int):
                The width of the new RECTANGLE.
            height (int):
                The height of the new RECTANGLE.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''
        Get or set the width of the rectangle.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an interger")
        if value < 0:
            raise ValueError("with must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''
        Get or set the heightof the rectangle.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
