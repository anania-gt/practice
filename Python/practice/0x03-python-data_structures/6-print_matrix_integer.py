def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in row:
            print("{:d}".format(column), end=" ")
        print()

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer(matrix)
