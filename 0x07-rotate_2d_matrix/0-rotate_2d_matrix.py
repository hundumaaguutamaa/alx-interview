#!/usr/bin/python3
""" Rotate 2-D Matrix """


def rotate_2d_matrix(matrix):
    i = len(matrix)
    
    """ Transpose the matrix. """
    for x in range(i):
        for y in range(x, i):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
    
    """ Reverse each row. """
    for row in matrix:
        row.reverse()

""" Matrix uusage. """
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)
print(matrix)
