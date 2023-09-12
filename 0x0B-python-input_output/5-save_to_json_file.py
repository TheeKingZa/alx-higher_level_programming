#!/usr/bin/python3
"""save_to_json_file module - defines a function to
    ..save an object to a JSON file"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a JSON file using a JSON representation."""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
