#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    '''
    A function that returns a set of elements present in only one of the sets.

    :param set_1: The first input set.
    :param set_2: The second input set.
    :return: A new set containing elements
    present in only one of the input sets.
    '''
    return set_1 ^ set_2
    # Return the symmetric difference of set_1 and set_2
