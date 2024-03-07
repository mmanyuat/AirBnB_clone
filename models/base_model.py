#!/usr/bin/python3
""" Importing uuid_module to access the uuid4 function"""
import uuid
""" Importing datetime module specially datetime class"""
from datetime import datetime

class BaseModel:
    """
    A class that defines all common attributes for other classes
    """

    def __init__(self):
        """ the class constructor """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """this method returns string representation of instance object"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Method that updates time to the current datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """ Method that converts instance attributes into a dictionary"""

        obj_dict = self.__dict__.copy()
        obj_dict ['__class__'] = self.__class__.__name__
        obj_dict ['created_at'] = self.created_at.isoformat()
        obj_dict ['updated_at'] = self.updated_at.isoformat()
        return obj_dict
