#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    # Create an empty list to store the new matrix

    for col in matrix:
        # Loop through each column in the input matrix
        result = list(map(lambda x: x ** 2, col))
        '''
        For each column, use the map function to apply the lambda function
        * that calculates the square of each element.
        * The result is a list of squared
          values for the current column.
        '''

        new_matrix.append(result)
        '''
        * Append the squared values of
        the current column to the new_matrix list.
        * This effectively creates a new row in the new matrix.
        '''

    return new_matrix
    # Return the new matrix containing squared values
