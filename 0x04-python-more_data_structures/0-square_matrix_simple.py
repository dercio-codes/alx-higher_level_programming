def square_matrix_simple(matrix=[]):
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
