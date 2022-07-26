#!/usr/bin/python3


'''Define a class of rectangle'''


class Rectangle:
    '''the initialization of the class'''

    number_of_instances = 0

    height = True
    width = True

    def __init__(self, width=0, height=0):
        """
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ""
        else:
            return '\n'.join('#' * self.width for _ in range(self.height))

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

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

    def area(self):
        return (self.height * self.width)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            perimeter = (self.height + self.width) * 2
            return perimeter
