def magic_calculation(a, b):
    # Import functions 'add' and 'sub' from the module 'magic_calculation_102'
    from magic_calculation_102 import add, sub
    
    # Compare a and b
    if a < b:
        # Call the 'add' function and store the result in 'c'
        c = add(a, b)
        
        # Iterate through a range of values [4, 5]
        for i in range(4, 6):
            # Call the 'add' function with arguments 'c' and 'i', update 'c'
            c = add(c, i)
    else:
        # Call the 'sub' function and return the result
        return sub(a, b)
    
    # Return the final value of 'c'
    return c
