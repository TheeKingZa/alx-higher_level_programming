#!/usr/bin/python3

def print_reversed_list_integer(my_list=[])


# Check if the input list is not empty
if my_list:
    # Reverse the elements of the list in-place
    my_list.reverse()

    # Iterate over the indices of the reversed list
    for i in range(len(my_list)):
        # Print the current element in the reversed list
        print("{:d}".format(my_list[i]))
