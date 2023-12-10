#!/usr/bin/python3
""" Module that inserts a line of text to a file """


def append_after(filename="", search_string="", new_string=""):
    """ function that inserts a line of text to a file """
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
