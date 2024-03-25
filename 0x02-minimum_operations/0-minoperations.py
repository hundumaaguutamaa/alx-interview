#!/usr/bin/python3

""" Module for 0-minoperations"""


def minOperations(n):
    """ calculates the minimum number of operations to achieve a given
    number of characters using only “Copy All” and “Paste” operations.using copy-paste process
    """
    if n < 2:
        return 0
    
    ops = 0
    body = 2  

    while body <= n:  
        if n % body == 0:  
            ops += body
            n = n // body  
            body -= 1
        body += 1
        
    return ops
