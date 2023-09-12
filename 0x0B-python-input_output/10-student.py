#!/usr/bin/python3
"""Student module - defines a Student class"""


class Student:
    """Student class to represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance with
        @ first_name
        @ last_name
        @ age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of
        A Student instance with specified attributes."""
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}
