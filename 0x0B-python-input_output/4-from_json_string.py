#!/usr/bin/python3
"""from_json_string module - defines a function to
    convert a JSON string to an object"""


import json


def from_json_string(my_str):
    """Converts a JSON string to a Python object and returns it."""
    return json.loads(my_str)
