#!/usr/bin/python3
"""
calculates the minimum number of operations to achieve a given
number of characters using only “Copy All” and “Paste” operations.
using copy-paste process
"""
def minOperations(n: int) -> int:
    """ Initialize variables. """
    next_op = 'H'   
    body = 'H'        
    opr = 0    

 while (len(body) < n):
        if n % len(body) == 0:
            opr += 2
            next_op = body
            body += body
        else:
            opr += 1
            body += next_op
    if len(body) != n:
        return 0
    return opr
