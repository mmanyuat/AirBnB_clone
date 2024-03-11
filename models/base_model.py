#!/usr/bin/python3
""" Importing uuid_module to access the uuid4 function & importing datetime"""
import uuid
from datetime import datetime


def set_attribute(obj, key, value):
    """set attribute based on key value"""
    if key in ['created_at', 'updated_at']:
        setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
    else:
        setattr(self, key, value)


class BaseModel:
    """
    A class that defines all common attributes for other classes
    """
    def __init__(self, *args, **kwargs):
        """ the class constructor """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    set_attribute(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """this method returns string representation of instance object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Method that updates time to the current datetime"""
        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Method that converts instance attributes into a dictionary"""

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
