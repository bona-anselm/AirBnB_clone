#!/usr/bin/python3
""" Creates a class module """
import uuid
from datetime import datetime
import models


class BaseModel():
    """ A BaseModel class that defines all common attributes/methods
        for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel
        Args:
            *args (any): unused
            **kwargs (dict): key & value pair of attributes
        """

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Prints the class names, ids and a dictionary representation
            of their instances
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """  updates the public instance attribute updated_at with the
            current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__
            of the instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
