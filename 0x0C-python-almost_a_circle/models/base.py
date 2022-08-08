#!/usr/bin/python3
"""Defining a class Baseimport json
"""


import json



class Base:
    """creating a private class attribute"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
