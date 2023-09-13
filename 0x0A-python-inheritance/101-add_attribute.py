#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


# Define a function named add_attribute.
def add_attribute(obj, att, value):
    """
    Add a new attribute to an object if possible.

    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of att.

    Raises:
        TypeError: If the attribute cannot be added.
    """
    # Check if the object has a __dict__ attribute.
    if not hasattr(obj, "__dict__"):
        # If the object does not have __dict__, it cannot have new attributes.
        # Raise a TypeError with the message "can't add new attribute."
        raise TypeError("can't add new attribute")

    # If the object has a __dict__ attribute, it allows adding attributes.
    # Use setattr to add the new attribute with the specified name and value.
    setattr(obj, att, value)
