#!/usr/bin/python3
"""function to write to a file"""


def append_write(filename="", text=""):
    """write to the file"""
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
