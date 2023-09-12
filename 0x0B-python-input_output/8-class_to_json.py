#!/usr/bin/python3
"""class_to_json module - defines a function for JSON
    ..serialization of an object"""


def class_to_json(obj):
    """Returns a dictionary description of an object for JSON serialization."""
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    return obj
