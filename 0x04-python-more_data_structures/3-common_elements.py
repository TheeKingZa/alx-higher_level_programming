#!/usr/bin/python3

def common_elements(set_1, set_2):
    '''
    A function that returns a set of common elements between two sets.

    :param set_1: The first input set.
    :param set_2: The second input set.
    :return: A new set containing common elements from both input sets.
    '''
    return set_1 & set_2  # Return the intersection of set_1 and set_2
