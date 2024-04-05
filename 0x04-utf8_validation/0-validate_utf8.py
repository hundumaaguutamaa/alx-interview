#!/usr/bin/python3
""" UTF-8 validation """


def validUTF8(data)
	""" Validation function"""
        counter = 0
 
        mask1 = 1 << 7
 
        mask2 = 1 << 6
        for num in data:
 
            mask = 1 << 7
            if counter == 0:
                while mask & num:
                    counter += 1
                    mask >>= 1
 
                if counter == 0:
                    continue
 
                if counter == 1 or counter > 4:
                    return False
            else:
 
                if not (num & mask1 and not (num & mask2)):
                    return False
                counter -= 1
 
        return counter == 0

