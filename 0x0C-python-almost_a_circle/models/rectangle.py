#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Definition of class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of class Rectangle instances"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """to retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """"to retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """to set the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """to get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """to set x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """to get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """to set y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """to return the area"""
        return (self.__width * self.__height)

    def display(self):
        """to display the class"""
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end='')
            for j in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """str representation"""
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format
                (self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """to update"""
        if args is not None and len(args) != 0:
            attr_assigned = ['id', 'width', 'height', 'x', 'y']
        for i in range(len(args)):
            setattr(self, attr_assigned[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """to set the dictionary"""
        new_dict = {}
        new_dict["id"] = self.id
        new_dict["width"] = self.width
        new_dict["height"] = self.height
        new_dict["x"] = self.x
        new_dict["y"] = self.y
        return new_dict
