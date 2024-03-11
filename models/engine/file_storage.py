#!/usr/bin/python3
"""Importing Json Module"""
import json
from models.base_model import BaseModel

class FileStorage:
    """ A class that serialises instance to json and deserialise instance"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Method that returns the dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """ sets the dictionay with <obj class name> """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_data = {}
        for key, obj in FileStorage.__objects.items():
            json_data[key] = obj.to_dict()
            with open(FileStorage.__file_path, 'w') as f:
                json.dump(json_data, f)

    def reload(self):
        """ Deserializes the json file to object """

        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj = BaseModel(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
