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

    @staticmethod
    def to_json_string(list_dictionaries):
        """to return JSON str repr"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return []
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
