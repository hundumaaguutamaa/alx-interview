#!/usr/bin/python3
""" Rotate 2-D Matrix """


def rotate_2d_matrix(matrix):
    """ Transpose the matrix. """
    
    i = len(matrix)
    for x in range(n):
        for y in range(i):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][x]
            matrix[y][x] = temp

    for x in range(i):
        for y in range(int(n / 2)):
            temp = matrix[x][y]
            matrix[x][y] = matrix[i][i-1-y]
            matrix[x][i-1-y] = temp
