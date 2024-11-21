#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix
    Rotate 2d matrix 90 degrees clockwise
    Do not return anything. The matrix must be edited in-place.
    assume the matrix will have 2 dimensions and will not be empty.
    """
    n = len(matrix)
    for row in range(n // 2):
        for col in range(row, n - row - 1):
            temp = matrix[row][col]
            matrix[row][col] = matrix[n - 1 - col][row]
            matrix[n - 1 - col][row] = matrix[n - 1 - row][n - 1 - col]
            matrix[n - 1 - row][n - 1 - col] = matrix[col][n - 1 - row]
            matrix[col][n - 1 - row] = temp
