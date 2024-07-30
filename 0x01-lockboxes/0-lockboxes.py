#!/usr/bin/python3
"""
Module to determine if all boxes can be unlocked.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    :param boxes: List of lists, where each sublist contains keys to other boxes
    :return: True if all boxes can be opened, False otherwise
    """
    if not boxes:
        return False

    n = len(boxes)   
    unlocked = [False] * n   
    unlocked[0] = True   
    keys = [0]   

    while keys:
        current_key = keys.pop()   
        for key in boxes[current_key]:   
            if key < n and not unlocked[key]:   
                unlocked[key] = True   
                keys.append(key)   

    return all(unlocked)   


