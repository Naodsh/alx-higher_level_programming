#!/usr/bin/python3
"""
Moudle Returns True if obj is exactly an instance of the specified class;
"""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of the specified class;
    otherwise False."""
    return type(obj) is a_class
