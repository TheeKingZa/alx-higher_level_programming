#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    '''
    A function that prints a dictionary in sorted order of keys.

    :param a_dictionary: The input dictionary.
    '''
    keys = list(a_dictionary.keys())
    # Get the keys of the dictionary
    keys.sort()
    # Sort the keys in ascending order

    for key in keys:
        # Iterate through the sorted keys
        print("{}: {}".format(key, a_dictionary[key]))
        # Print the key and its corresponding value
