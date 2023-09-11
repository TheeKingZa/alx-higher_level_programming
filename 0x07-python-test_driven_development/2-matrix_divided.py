#!/usr/bin/python3
"""
Divide all elements of a matrix by a given divisor and round to 2 decimal places.

Parameters:
    matrix (list of lists): A matrix of integers or floats to be divided.
    div (number, int or float): The divisor to divide all elements of the matrix.

Returns:
    list of lists: A new matrix with elements divided by the divisor and rounded to 2 decimal places.

Raises:
    TypeError: If the matrix is not a list of lists of integers or floats,
            if the rows of the matrix have different sizes, or if div is not a number.
    ZeroDivisionError: If div is equal to 0.
"""
    # Function implementation here
def matrix_divided(matrix, div):
    # Check if the matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div, rounding to 2 decimal places
    result_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return result_matrix
