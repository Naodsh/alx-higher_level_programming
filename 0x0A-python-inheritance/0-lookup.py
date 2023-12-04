#!/usr/bin/python3
""" Module that return attributes and methods of an object."""


def lookup(obj):
    """Returns a list of available attributes and methods of an object."""
    return dir(obj)
