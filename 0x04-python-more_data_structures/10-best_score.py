#!/usr/bin/python3

def best_score(a_dictionary):
    '''
    A function that returns the key
    with the largest integer value in a dictionary.

    :param a_dictionary: The input dictionary.
    :return: The key with the largest integer value.
    '''
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        # Get the keys of the dictionary
        score = 0
        # Initialize a variable to store the largest score
        leader = ""
        # Initialize a variable to store the key with the largest score

        for i in my_list:
            # Iterate through the keys in the dictionary
            if a_dictionary[i] > score:
                # Check if the value associated with the key
                # is greater than the current largest score
                score = a_dictionary[i]
                # Update the largest score
                leader = i
                # Update the leader key

        return leader
        # Return the key with the largest integer value
