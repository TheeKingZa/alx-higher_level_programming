#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Safely prints a specified number of integer elements from a given list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        int: The number of integer elements successfully printed.
    """
    ret = 0
    # Initialize a counter for successfully printed integer elements
    for i in range(0, x):
        try:
            '''
            Try to print the integer element
            ..at index 'i' using the specified format
            '''
            print("{:d}".format(my_list[i]), end="")
            ret += 1
            # Increment the counter for each successfully printed element
        except (ValueError, TypeError):
            '''
            If a ValueError or TypeError occurs,
            catch the exception and continue to the next iteration
            '''
            # This means that non-integer elements will be skipped
            continue
    print("")
    # Print a newline to separate the output from the next line
    return (ret)
    # Return the total number of integer elements successfully printed
