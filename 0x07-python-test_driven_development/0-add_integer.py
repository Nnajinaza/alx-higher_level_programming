#!/usr/bin/python3
"""Defines a function that adds two values"""


def add_integer(a, b=98):
    """Returns the sum of two values
    Args:
        a (int): first value passed
        b (int): second value passed
    Raises:
        TypeError: if either of the values are non-integer or non-float
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
