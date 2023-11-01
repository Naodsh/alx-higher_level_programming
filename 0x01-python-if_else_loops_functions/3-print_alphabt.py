#!/usr/bin/python3
for ascii_value in range(ord('a'), ord('z') + 1):
    if chr(ascii_value) not in ('q', 'e'):
        print("{}".format(chr(ascii_value)), end='')
