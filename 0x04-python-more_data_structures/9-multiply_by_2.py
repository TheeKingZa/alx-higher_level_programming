#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    '''
    A function that creates a new dictionary
    where the values are multiplied by 2.

    :param a_dictionary: The input dictionary.
    :return: A new dictionary with values multiplied by 2.
    '''
    new_dict = {}
    # Create an empty dictionary to store the new values

    for key, value in a_dictionary.items():
        # Iterate through the key-value pairs
        # in the input dictionary
        new_dict.update({key: (value * 2)})
        # Multiply the value by 2 and add to the new dictionary

    return new_dict
    # Return the new dictionary with updated values
