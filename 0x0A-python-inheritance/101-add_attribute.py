#!/usr/bin/python3
""" ADD attribute Module """


def add_attribute(obj, attribute, value):
    if hasattr(obj, attribute):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
