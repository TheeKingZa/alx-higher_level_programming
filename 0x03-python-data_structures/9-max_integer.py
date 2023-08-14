#!/usr/bin/python3

def max_integer(my_list=[]):
    # Check if the list is empty
    if len(my_list) == 0:
        return "None"
    else:
        # Initialize max with the first element of the list
        max = my_list[0]

        # Iterate through the list to find the maximum element
        for i in range(len(my_list)):
            if my_list[i] > max:
                max = my_list[i]

        # Return the maximum element
        return max
