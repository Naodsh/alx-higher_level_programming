#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
