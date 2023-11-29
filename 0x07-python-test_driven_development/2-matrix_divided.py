#!/usr/bin/python3
"""
This is the "2-matrix_divided.py" module.
The 2-matrix_divided module supplies one function,matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):
    """
    Returns:
    - list of lists: New matrix with elements divided by div, \
            rounded to 2 decimal places.
    """

    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(row, list) and all(isinstance(x, (int, float))
       for x in row) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return result_matrix
