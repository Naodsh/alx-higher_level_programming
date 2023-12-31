#!/usr/bin/python3
""" Square Module """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ init function """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str function """
        return "[Square] ({}) {}/{} - {}" .format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {
            'id': self.id,
            'x': self.x,
            'size': self.width,
            'y': self.y
        }
