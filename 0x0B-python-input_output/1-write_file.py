#!/usr/bin/python3
"""
Writes a string to a text file (UTF8) and returns the
number of characters written.

"""


def write_file(filename="", text=""):
    """Function that write string to text file"""

    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
