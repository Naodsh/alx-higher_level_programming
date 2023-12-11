#!/usr/bin/python3
""" Square Module """


from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}" .format(
                self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
