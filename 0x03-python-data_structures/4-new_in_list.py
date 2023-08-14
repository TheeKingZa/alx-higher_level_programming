#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    # Create a copy of the original list
    copy = my_list.copy()
    # Check if the provided index is out of bounds
    if idx < 0 or idx > len(my_list) - 1:
        # If the index is out of bounds
        # return a copy of the original list (unchanged)
        return my_list.copy()
    else:
        # Update the element at the specified index in the copied list
        copy[idx] = element
        # Return the modified copy of the list
        return copy
