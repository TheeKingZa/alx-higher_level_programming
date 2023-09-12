#!/usr/bin/python3
"""read_file module - defines a function to read and print a text file"""


def read_file(filename=""):
    """Reads a text file and prints its content to stdout."""
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
