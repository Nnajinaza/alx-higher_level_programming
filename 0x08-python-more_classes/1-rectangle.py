#!/usr/bin/python3


'''Define a class of rectangle'''


class Rectangle:
    height = True
    width = True

    '''the initialization of the class'''
    def __init__(self, width=0, height=0):
        """
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
