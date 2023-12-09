#!/usr/bin/python3
""" Module that  implementation of the MyInt class that inherits from
int and inverts the == and != operators:"""


class MyInt(int):
    """ Myint Class """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
