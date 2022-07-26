#!/usr/bin/python3
"""This function print_square using a character"""


def print_square(size):
    """prints a square with "#"'s that has a length of size """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
