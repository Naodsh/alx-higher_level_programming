#!/usr/bin/python3
""" Module that reads stdin line by line and computes metrics """


import sys


def print_stats(file_sizes, status_codes):
    """ Function to print """
    print(f"File size: {sum(file_sizes)}")
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")


def parse_line(line):
    """ Function that reads stdin line by line and parse """
    parts = line.split()
    if len(parts) > 2:
        file_size = int(parts[-1])
        status_code = parts[-2]
        return file_size, status_code
    return None, None
