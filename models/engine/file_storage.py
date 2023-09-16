#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """Represent an abstracted storage engine."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of objects."""
        return self.__class__.__objects

    def new(self, obj):
        """Add an object to the storage."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__class__.__objects[key] = obj

    def save(self):
        """Serialize objects to the JSON file."""
        obj_dict = {
            key: obj.to_dict() for key, obj in self.__class__.__objects.items()
        }
        with open(self.__class__.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize the JSON file to objects."""
        try:
            with open(self.__class__.__file_path) as file:
                obj_dict = json.load(file)
                for data in obj_dict.values():
                    cls_name = data.pop("__class__", None)
                    if cls_name:
                        obj = eval(cls_name)(**data)
                        self.new(obj)
        except FileNotFoundError:
            pass
