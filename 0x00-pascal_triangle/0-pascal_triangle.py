#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal’s triangle of n:
    """

    if n <= 0:
        return []

    """ Initialize the triangle with the first row. """
    triangle = [[1]]

    for i in range(1, n):
        row = [1]   
        last_row = triangle[-1]

        """ Compute the values in the middle of the row """
        for j in range(1, len(last_row)):
            row.append(last_row[j - 1] + last_row[j])

        row.append(1)   
        triangle.append(row)

    return triangle
  
