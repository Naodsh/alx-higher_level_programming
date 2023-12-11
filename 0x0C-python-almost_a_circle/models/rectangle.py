#!/usr/bin/python3
""" Recrangle Module """


from models.base import Base


class Rectangle(Base):
    """ Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError("x  must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError("y  must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area function """
        return self.__width * self.__height

    def display(self):
        """ function to display rectangle """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ string function """
        return "[Rectangle] ({}) {}/{} - {}/{}" .format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ function to update """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ function json to dictionary """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
            }
