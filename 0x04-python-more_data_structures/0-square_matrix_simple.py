#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """Squares the elements of a matrix.

    Args:
        matrix (list, optional): A list of lists representing a matrix.
            Defaults to an empty list.

    Returns:
        list: A new list of lists containing the squares of the elements
              in the input matrix.
    """

    # Create a new matrix with the same size as the input matrix
    new_matrix = []

    # Iterate over each row in the matrix
    for row in matrix:
        # Compute the square of each element in the row
        new_row = [element**2 for element in row]
        # Add the new row to the new matrix
        new_matrix.append(new_row)

    # Return the new matrix
    return new_matrix
