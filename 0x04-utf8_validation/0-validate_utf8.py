#!/usr/bin/python3
"""UTF-8 Validation. """
def is_valid_utf8(data):
    # Counter for the number of bytes in the current UTF-8 character
    remaining_bytes = 0
    
    # Masks to check the most significant bits of each byte
    most_significant_bit_mask = 1 << 7  # 10000000
    second_most_significant_bit_mask = 1 << 6  # 01000000

    for byte in data:
        # Get the 8 least significant bits
        current_byte = byte & 0xFF

        if remaining_bytes == 0:
            # Count the number of leading 1's in the first byte
            leading_one_mask = 1 << 7
            while leading_one_mask & current_byte:
                remaining_bytes += 1
                leading_one_mask = leading_one_mask >> 1
            
            # 1 byte character
            if remaining_bytes == 0:
                continue
            
            # UTF-8 characters can be 1 to 4 bytes long
            if remaining_bytes == 1 or remaining_bytes > 4:
                return False
        else:
            # Check that the byte starts with 10xxxxxx
            if not (current_byte & most_significant_bit_mask and not (current_byte & second_most_significant_bit_mask)):
                return False
        
        remaining_bytes -= 1

    return remaining_bytes == 0


