#!/usr/bin/python3
""" Student Module """


class Student:
    """ Student Class """
    def __init__(self, first_name, last_name, age):
        """ init function """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__

        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result
