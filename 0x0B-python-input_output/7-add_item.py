#!/usr/bin/python3
"""add_item module - defines a script to
    ..add items to a list and save them to a JSON file"""

import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# Check if the JSON file exists
if path.exists("add_item.json"):
    # Load the existing list from the JSON file
    my_list = load_from_json_file("add_item.json")
else:
    # Create an empty list if the JSON file doesn't exist
    my_list = []

# Add command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(my_list, "add_item.json")
