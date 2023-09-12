#!/usr/bin/python3
"""to_json_string module - defines a function to
    convert an object to a JSON string"""


import json


def to_json_string(my_obj):
    """Converts an object to a JSON string and returns it."""
    return json.dumps(my_obj)
