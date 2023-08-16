#!/usr/bin/python3

def uniq_add(my_list=[]):
    '''
    A function that sums up unique elements in a list.

    :param my_list: The input list containing elements.
    :return: The sum of unique elements in the list.
    '''
    new_list = []
    # Create an empty list to store unique elements
    sum = 0
    # Initialize the sum to 0

    for num in my_list:
        # Loop through each element in the input list
        if num not in new_list:
            # Check if the element is not already in the new_list
            sum += num
            # If the element is unique, add it to the sum
            new_list.append(num)
            # Add the element to the new_list to track its uniqueness

    return sum
    # Return the sum of unique elements
