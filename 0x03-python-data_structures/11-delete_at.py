#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # Check if the index is out of bounds
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        # Delete the element at the specified index using 'del'
        del my_list[idx]

    # Return the modified list (if an element was deleted) or..
    # ..the original list (if index was out of bounds)
    return my_list
