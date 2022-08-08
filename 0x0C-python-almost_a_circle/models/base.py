#!/usr/bin/python3
"""Defining a class Baseimport json"""
import json
import csv


class Base:
    """creating a private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializing the class"""
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
        """loads from json file"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to json"""
        if list_objs is None:
            pass
        else:
            filename = cls.__name__ + ".json"
            new_list = []
            for i in list_objs:
                new_list.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(new_list))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_form_file(cls):
        filename = cls.__name__ + ".json"
        new_ls = []
        with open(filename, 'r') as f:
            new_ls = cls.from_json_string(f.read())
        for i, j in enumerate(new_ls):
            new_ls[i] = cls.create(**new_ls[i])
        return new_ls

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes a list of Rectangles/Squares in csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a list of Rectangles/Squares in csv"""
        filename = cls.__name__ + ".csv"
        lists = []
        with open(filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for args in csv_reader:
                if cls.__name__ == "Rectangle":
                    dictionary = {"id": int(args[0]),
                                  "width": int(args[1]),
                                  "height": int(args[2]),
                                  "x": int(args[3]),
                                  "y": int(args[4])}
                elif cls.__name__ == "Square":
                    dictionary = {"id": int(args[0]), "size": int(args[1]),
                                  "x": int(args[2]), "y": int(args[3])}
                    obj = cls.create(**dictionary)
                    lists.append(obj)
        return lists
