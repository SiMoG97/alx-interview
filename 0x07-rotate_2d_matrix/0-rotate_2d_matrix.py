#!/usr/bin/python3
"""Rotation of a 2D matrix by 90 deg clockwise"""


def transpose(matrix):
    """transposes the matrix
    which means the columns become the rows and vise versa

    Args:
        matrix (_type_): list of lists
    """

    n = len(matrix[0])
    for i in range(0, n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverseList(arr):
    """Reverses the given list

    Args:
      arr (_type_): the list
    """

    for i in range(0, len(arr) // 2):
        arr[i], arr[-i - 1] = arr[- i - 1], arr[i]


def rotate_2d_matrix(matrix):
    """Rotates the matrix by 90 deg clockwise

    Args:
        matrix (_type_): list of lists
    """

    transpose(matrix)
    for i in range(0, len(matrix[0])):
        reverseList(matrix[i])
