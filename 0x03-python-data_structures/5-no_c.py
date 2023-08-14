#!/usr/bin/python3

def no_c(my_string):
    # Create a translation table that maps
    # 'c' and 'C' to None (effectively removing them)
    translation_table = {ord('c'): None, ord('C'): None}
    # Use the translate method to create a new string with characters removed
    new_string = my_string.translate(translation_table)
    return new_string
