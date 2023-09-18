#!/usr/bin/python3
import json

class Base:
    """Class representing the base of all other classes."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance with an ID."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        list_dicts = [{"id": obj['id'], **obj} for obj in list_dictionaries]
        return json.dumps(list_dicts)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to a JSON file."""
        if list_objs is None:
            list_objs = []
        # Create a list of dictionaries from the list of instances
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        # Convert the list of dictionaries to a JSON string
        json_string = cls.to_json_string(list_dicts)
        # Write the JSON string to a file with the class name as the filename
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes from a dictionary."""
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**dict) for dict in list_dicts]
        except FileNotFoundError:
            return []

    def to_dictionary(self):
        """Return the dictionary representation of an instance."""
        return self.__dict__
