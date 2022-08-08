#!/usr/bin/python3
"""Define class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The clss Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing from Rectangle module"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """to get the size"""
        return self.width

    @size.setter
    def size(self, value):
        """to set the values"""
        self.width = value
        self.height = value

    def __str__(self):
        """to get the str rep"""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """to update"""
        if args is not None and len(args) != 0:
            attr_assigned = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attr_assigned[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """to get the dictionary"""
        new_dict = {}
        new_dict["id"] = self.id
        new_dict["size"] = self.size
        new_dict["x"] = self.x
        new_dict["y"] = self.y
        return new_dict
