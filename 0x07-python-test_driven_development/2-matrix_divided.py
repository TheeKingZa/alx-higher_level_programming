#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    :param matrix: A list of lists containing integers or floats.
    :param div: The number to divide all elements by
        (integer or float).
    :return: A new matrix with elements rounded to 2 decimal places.
    """
    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list)
    or not all(isinstance(row, list) for row in matrix)
    or not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("""
        matrix must be a matrix (list of lists)
        of integers/floats""")

    # Check if all rows of the matrix have the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and round to 2 decimal places
    result_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return (result_matrix)
