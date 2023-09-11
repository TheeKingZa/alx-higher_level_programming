#!/usr/bin/python3
"""BaseGeometry module - defines a base geometry class"""


class BaseGeometry:
    """Base geometry class"""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value, raising appropriate exceptions if invalid"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
