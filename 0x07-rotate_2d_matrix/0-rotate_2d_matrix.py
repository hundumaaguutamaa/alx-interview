#!/usr/bin/python3
""" Function that Rotate 2-D Matrix
"""


def rotate_2d_matrix(matrix):
    """ Rotate the matrix. 
       Return:None 
    """
    
    n = len(matrix)  # Correct variable name
    for x in range(n):
        for y in range(n):  # Correct loop variable
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][x]
            matrix[y][x] = temp

    for x in range(n):
        for y in range(int(n / 2)):
            temp = matrix[x][y]
            matrix[x][y] = matrix[x][n-1-y]  # Correct index
            matrix[x][n-1-y] = temp
