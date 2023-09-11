#!/usr/bin/python3
"""
Define
attribute of an object.
lookup function
"""


def lookup(obj):
    '''
    Return a list of an available attributes of an object
    '''
    return(dir(obj))
