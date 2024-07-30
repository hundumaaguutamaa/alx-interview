#!/usr/bin/python3
"""  Pascal's Triangle  """


def pascal_triangle(n):
  """ Returns a list of lists of integers
        represens lis of integers. 

  """

    if n <= 0:
        return []

    triangle = [[1]]  

    for i in range(1, n):
        row = [1]  
        last_row = triangle[-1]

        """ Compute values in the middle of the row"""
        for j in range(1, len(last_row)):
            row.append(last_row[j - 1] + last_row[j])

        row.append(1) 
        triangle.append(row)

    return triangle

