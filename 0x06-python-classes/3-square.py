#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Initialize th square class"""
    def __init__(self, size=0):
        """
        Args:
            size (int): The value of the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return (self.__size * self.__size)
