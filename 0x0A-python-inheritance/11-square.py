#!/usr/bin/python3
""" Module of Square inherited from  Rectangle Class
the Rectangle Class is inherited from Geometry Class """


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

    def __str__(self):
        """ str function """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """ Area Function """
        return self.__width * self.__height


class Square(Rectangle):
    """ Class of Square inherted from Rectangle Class"""
    def __init__(self, size):
        """ init function """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ str function """
        return f"[Square] {self.__size}/{self.__size}"
