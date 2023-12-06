#!/usr/bin/python3
""" Module of Geometry """


class BaseGeometry:
    """ Class of BaseGeometry """
    def area(self):
        """ Area function """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Integer validator function """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
