#!/usr/bin/python3

def print_reversed_list_integer(my_list=[])


# Iterate over the list in reverse order using a negative step
for i in range(len(my_list) - 1, -1, -1):
    # Print each integer using str.format() to format output
    print("{:d}".format(my_list[i]))
