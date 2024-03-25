#!/usr/bin/python3
"""
calculates the minimum number of operations to achieve a given
number of characters using only “Copy All” and “Paste” operations.
using copy-paste process
"""
def minOperations(n: int) -> int:
    """ Initialize variables. """
    next_char = 'H'   
    body = 'H'        
    operations = 0    
    
    """ Copy and paste until desired length is reached. """
    while len(body) < n:
        if n % len(body) == 0:
            """ If current length is a factor of n, we can double the content by copying """
            next_char = body
            body += body
            operations += 1
        else:
            """ not a factor of n, simply paste the next character. """

            body += next_char
            operations += 1
    
    if len(body) != n:
        return 0
    
    return operations

n = 9
print("Number of operations:", minOperations(n))
