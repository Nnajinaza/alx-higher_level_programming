#!/usr/bin/python3
"""function to write to a file"""


def write_file(filename="", text=""):
    """write to the file"""
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
