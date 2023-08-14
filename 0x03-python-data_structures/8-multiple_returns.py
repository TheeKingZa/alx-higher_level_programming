#!/usr/bin/python3

def multiple_returns(sentence):
    # Create an empty tuple to store the result
    my_tuple = ()
    
    # Check if the sentence is empty
    if len(sentence) == 0:
        # If the sentence is empty, create a tuple with 0 and "None"
        my_tuple = 0, "None"
    else:
        # If the sentence is not empty, create a tuple with the length and the first character
        my_tuple = len(sentence), sentence[0]
    
    # Return the created tuple
    return my_tuple
