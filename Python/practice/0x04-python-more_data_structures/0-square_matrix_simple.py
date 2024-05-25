def square_matrix_simple(matrix=[]):
    # Create a new matrix of the same size with squared values
    new_matrix = []
    for row in matrix:
        new_row = [x**2 for x in row]
        new_matrix.append(new_row)
    return new_matrix

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(square_matrix_simple(matrix))
# Output: [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
