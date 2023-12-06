#!/usr/bin/python3
""" Module of Rectangle Class inherited from Geometry Class """


class BaseGeometry:
    """ BaseGeometry Class """
    def area(self):
        """ Area function """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Integer validator function """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ Class of Rectangle inherited from Geometry Class """
    def __init__(self, width, height):
        """ init function """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
