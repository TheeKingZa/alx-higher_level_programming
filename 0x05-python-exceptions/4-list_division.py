#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divides two lists element by element and handles exceptions.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        list: A new list of length list_length containing all the divisions.
    """
    new_list = []  # Initialize an empty list to store division results
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            # Attempt to perform the division
        except TypeError:
            print("wrong type")
            # Handle TypeError (e.g., non-numeric values in lists)
            div = 0
            # Assign a default value if division cannot be performed
        except ZeroDivisionError:
            print("division by 0")
            # Handle ZeroDivisionError (dividing by zero)
            div = 0
            # Assign a default value if division cannot be performed
        except IndexError:
            print("out of range")
            # Handle IndexError (index out of range)
            div = 0
            # Assign a default value if division cannot be performed
        finally:
            new_list.append(div)
            # Append the division result (or default) to the new_list
    return (new_list)
    # Return the new_list containing division results
