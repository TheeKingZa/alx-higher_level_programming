#!/usr/bin/python3

# Define a function named "replace_in_list" that takes three parameters:
# my_list: a list of elements
# idx: an index indicating the position where the element should be replaced
# element: the new element to be placed at the specified index
def replace_in_list(my_list, idx, element):
    # Check if the provided index (idx) is less than 0 or greater than the
    # last valid index in the list (len(my_list) - 1).
    if idx < 0 or idx > len(my_list) - 1:
        # If the index is out of bounds, return the original list unchanged.
        return my_list
    else:
        # If the index is within bounds, replace the element at the specified
        # index with the new element provided.
        my_list[idx] = element
        # Return the modified list with the replacement.
        return my_list
