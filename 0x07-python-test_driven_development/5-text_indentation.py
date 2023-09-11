#!/usr/bin/python3
"""
This is a module for formatting text with new lines.
"""


def text_indentation(text):
    """
    Print a text with two new lines after each '.', '?', and ':' character.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    newline = True  # Flag to avoid adding new lines at the beginning

    for char in text:
        if char in ['.', '?', ':']:
            result += char + '\n\n'
            newline = True
        elif char == ' ' and newline:
            continue
        else:
            result += char
            newline = False

    print(result)
