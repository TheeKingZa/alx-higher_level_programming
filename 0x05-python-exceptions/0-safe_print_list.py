#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Safely prints a specified number of elements from a given list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        int: The number of elements printed.
    """
    ret = 0
    # Initialize a counter to keep track of printed elements
    for i in range(x):
        try:
            # Try to print the element at index 'i' from 'my_list'
            print("{}".format(my_list[i]), end="")
            ret += 1
            # Increment the counter for each successfully printed element
        except IndexError:
            # If IndexError occurs, it means 'i' is out of range for 'my_list'
            # Break the loop to stop printing and handling elements
            break
    print("")
    # Print a newline to separate the output from the next line
    return (ret)
    # Return the total number of elements printed
