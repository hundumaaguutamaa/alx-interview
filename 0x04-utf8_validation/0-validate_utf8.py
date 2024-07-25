#!/usr/bin/python3

def validUTF8(data):
    """Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list of int): List of integers representing bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    
    def is_continuation_byte(byte):
        """Check if the byte is a continuation byte (i.e., starts with '10').

        Args:
            byte (int): A byte value.

        Returns:
            bool: True if byte is a continuation byte, else False.
        """
        return (byte & 0xC0) == 0x80

    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            """Determine the number of bytes for this character
            """ 
            if (byte & 0x80) == 0:
                num_bytes = 0
            elif (byte & 0xE0) == 0xC0:
                num_bytes = 1
            elif (byte & 0xF0) == 0xE0:
                num_bytes = 2
            elif (byte & 0xF8) == 0xF0:
                num_bytes = 3
            else:
                return False
        else:
            if not is_continuation_byte(byte):
                return False
            num_bytes -= 1

    return num_bytes == 0

