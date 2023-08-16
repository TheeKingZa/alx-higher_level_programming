def search_replace(my_list, search, replace):
    """
    A function that replaces all occurrences
    of an element by another in a new list
    """
    new_list = []
    # Create an empty list to store the new list with replacements

    for element in my_list:
        # Loop through each element in the input list
        if element == search:
            # Check if the current element matches the search element
            new_list.append(replace)
            # If it matches, add the replacement element to the new list
        else:
            new_list.append(element)
            # If it doesn't match, add the original element to the new list

    return new_list
    # Return the new list with replacements
