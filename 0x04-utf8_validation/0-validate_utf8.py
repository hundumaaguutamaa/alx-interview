#!/usr/bin/python3
"""
Write a method that determines if a given data set
represents a valid UTF-8 encoding.
Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else
return False
"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding.
    """
    continuation_bytes_needed = 0

    UTF8_BIT_1 = 1 << 7  # 10000000
    UTF8_BIT_2 = 1 << 6  # 01000000

    for byte in data:
        # Initialize a mask, check for leading 1's in the current byte.
        leading_one_mask = 1 << 7

        if continuation_bytes_needed == 0:
            while leading_one_mask & byte:
                continuation_bytes_needed += 1
                leading_one_mask = leading_one_mask >> 1

            if continuation_bytes_needed == 0:
                continue

            if continuation_bytes_needed == 1 or continuation_bytes_needed > 4:
                return False

        else:
            if not (byte & UTF8_BIT_1 and not (byte & UTF8_BIT_2)):
                return False
            
        continuation_bytes_needed -= 1

    return continuation_bytes_needed == 0
