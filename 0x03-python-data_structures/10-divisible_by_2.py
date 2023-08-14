#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Create an empty list to store the result
    new_list = []
    
    # Iterate through the input list
    for i in range(len(my_list)):
        # Check if the current element is divisible by 2
        if my_list[i] % 2 == 0:
            new_list.append(True)  # Append True to the new list if divisible by 2
        else:
            new_list.append(False) # Append False to the new list if not divisible by 2
    
    # Return the new list
    return new_list
