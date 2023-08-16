#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    '''
    A function that multiplies each element of a list by a specified number using map.
    
    :param my_list: The input list (default is an empty list).
    :param number: The number to multiply each element by (default is 0).
    :return: A new list with elements multiplied by the specified number.
    '''
    return list(map((lambda i: i * number), my_list))
