#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Create an empty tuple to store the result
    new_tuple = ()

    # Pad both input
    # tuples with zeros to ensure
    # each have at least two elements
    tuple_1 = tuple_a + (0, 0)
    tuple_2 = tuple_b + (0, 0)

    # Calculate the sum of the corresponding elements and create the new tuple
    new_tuple = tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1]

    # Return the new tuple
    return new_tuple
