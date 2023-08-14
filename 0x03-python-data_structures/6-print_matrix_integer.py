#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            # Print each element of the matrix
            # ..using str.format()
            # Add a space after each element if
            # ..it's not the last in row
            print("{:d}".format(col), end=" " if col != row[-1] else "")

        # Print a newline character at the end of each row
        print()
