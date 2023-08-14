#!/usr/bin/python3

# Define a function named "element_at" that takes two parameters:
# my_list: a list of elements
# idx: an index indicating the position of the element to retrieve
def element_at(my_list, idx):
    # Check if the provided index (idx) is less than 0 or greater than the
    # last valid index in the list (len(my_list) - 1).
    if idx < 0 or idx > len(my_list) - 1:
        # If the index is out of bounds, return the string 'None' to indicate
        # that the index is invalid and there is no element at that position.
        return 'None'
    else:
        # If the index is within bounds, return the element from the list
        # at the specified index (idx). This assumes that the list contains
        # elements of any data type.
        return my_list[idx]
