#!/usr/bin/python3

"""
 function def island_perimeter(grid):
 that returns the perimeter of the island described in grid
"""


def island_perimeter(matrix):
    if not matrix or not matrix[0]:
        return 0

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    total_perimeter = 0

    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col] == 1:
                if row == 0 or matrix[row-1][col] == 0:
                    total_perimeter += 1
                if row == num_rows-1 or matrix[row+1][col] == 0:
                    total_perimeter += 1
                if col == 0 or matrix[row][col-1] == 0:
                    total_perimeter += 1
                if col == num_cols-1 or matrix[row][col+1] == 0:
                    total_perimeter += 1

    return total_perimeter

