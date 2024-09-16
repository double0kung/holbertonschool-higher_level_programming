#!/usr/bin/python3
"""Module to divide all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number
    Args:
        matrix (list of lists): Matrix of integers or floats
        div (int or float): Number to divide by
    Returns:
        A new matrix with all elements divided by div
    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if each row of the matrix doesn't have the same size,
                   or if div is not a number
        ZeroDivisionError: If div is zero
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(isinstance(ele, (int, float)) for row in matrix
               for ele in row):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(ele / div, 2) if div != float('inf') else 0.0
             for ele in row] for row in matrix]
