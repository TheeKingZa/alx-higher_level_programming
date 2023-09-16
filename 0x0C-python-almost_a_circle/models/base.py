#!/usr/bin/python3
"""
Module containing the Base class
"""


class Base:
    """Base class for managing id attributes
    in other classes.
    """

    # Private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize
        Constructor for Base instance with an id.
        Args:
            id (int):
                The ID of the instance.
            if None:
                it will auto-generated.
        """
        if id is not None:
            # If an ID is provided.
            self.id = id
            # assign it to instance id attribute.
        else:
            # If id is not provided, increment __nb_objects and assign it
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

# defines the base class.
# will be used as the base classs for other classes.
# Provides a way to manage and generate IDs for instances.
