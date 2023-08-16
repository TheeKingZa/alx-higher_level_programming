#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    '''
    A function that deletes a key from a dictionary.

    :param a_dictionary: The input dictionary.
    :param key: The key to be deleted (default is an empty string).
    :return: The modified dictionary after deletion (if the key exists).
    '''
    if key in a_dictionary:
        # Check if the key exists in the dictionary
        del a_dictionary[key]
        # If the key exists, delete it

    return a_dictionary
    # Return the modified dictionary
