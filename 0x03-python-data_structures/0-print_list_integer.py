#!/usr/bin/python3

# Prototype
def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        '''list the range of length at index i'''
        print("{:d}".format(my_list[i]))
