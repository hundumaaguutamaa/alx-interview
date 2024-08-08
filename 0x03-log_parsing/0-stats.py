#!/usr/bin/python3
"""   Log parsing """

import sys
import signal

"""Initialize variables"""
total_file_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Prints the current statistics"""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

def signal_handler(sig, frame):
    """Handles keyboard interruption (CTRL + C)"""
    print_stats()
    sys.exit(0)

"""Register the signal handler"""
signal.signal(signal.SIGINT, signal_handler)

"""Process input line by line"""
try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue
        try:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            total_file_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
        except (ValueError, IndexError):
            continue

        line_count += 1
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

print_stats()

