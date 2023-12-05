#!/usr/bin/python3
"""Converts an instance of a class to a JSON serializable dictionary"""


def class_to_json(obj):
    """Converts an instance of a class to a JSON serializable dictionary"""
    # Get all attributes of the object
    attributes = obj.__dict__

    # Filter out any private attributes
    serializable_attrs = {
        key: value for
        key, value in attributes.items() if not key.startswith('_')
    }

    # Convert attributes to a dictionary
    return serializable_attrs
