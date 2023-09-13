#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


# Define a new class MyInt that inherits
#    from the built-in int class.
class MyInt(int):
    """Invert int operators == and !=."""

    # Override the == operator to invert its behavior.
    def __eq__(self, value):
        """Override == operator with != behavior."""
        # Compare the real value of the MyInt
        # ..instance with the provided value.
        # If they are not equal,
        # Return True (inverted behavior).
        return self.real != value

    # Override the != operator to invert its behavior.
    def __ne__(self, value):
        """Override != operator with == behavior."""
        # Compare the real value of the MyInt instance with the provided value.
        # If they are equal, return True (inverted behavior).
        return self.real == value
