#!/usr/bin/python3
""" def pascal_triangle(n): """


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n

    Args:
        n (number): number of rows in the pascal triangle
    """

    if n <= 0:
        return []

    pascal_list = []
    for i in range(0, n):
        row = []

        for j in range(0, i + 1):
            if j == 0 or j == i:
                row.append(1)
                continue

            prevRow = pascal_list[i - 1]
            row.append(prevRow[j] + prevRow[j - 1])

        pascal_list.append(row)

    return pascal_list
