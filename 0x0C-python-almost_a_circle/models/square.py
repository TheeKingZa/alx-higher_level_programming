#!/usr/bin/python3
# models/square.py
"""
Module contains the square.
representation of square inherits from Recatangle.
"""
import json
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class of a SQUARE"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance"""
        # Initialize a Square by calling the constructor of the Rectangle class
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter For size attribute"""
        return (self.width)

    @size.setter
    def size(self, value):
        """Setter For size attribute"""
        # Validate and set both width and height to the same size value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes using args and kwargs"""
        if args:
            # If args is not empty, assign attributes in order: id, size, x, y
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            # If args is empty, use kwargs
            # (keyworded arguments) to assign attributes
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a SQUARE"""
        # Return a dictionary with square attributes
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
        }

    @staticmethod
    def from_dictionary(dict):
        """Create Square instance from a dictionary."""
        # Create a new Square instance using the values in the dictionary
        return Square(**dict)

    @staticmethod
    def to_json_string(list_squares):
        """Convert a list of Square instances to a JSON string."""
        if list_squares is None or len(list_squares) == 0:
            return "[]"
        # Use list comprehension to convert each Square to a dictionary
        dict_list = [square.to_dictionary() for square in list_squares]
        # Use json.dumps to convert the list of dictionaries to a JSON string
        return json.dumps(dict_list)

    @staticmethod
    def from_json_string(json_string):
        """Create a list of Square instances from a JSON string."""
        if json_string is None or json_string == "":
            return []
        # Use json.loads to convert the JSON string to a list of dictionaries
        dict_list = json.loads(json_string)
        # Use list comprehension
        # to create Square instances from the dictionaries
        return [Square.create(**square_dict) for square_dict in dict_list]

    @classmethod
    def save_to_file(cls, squares):
        """Save a list of squares to a JSON file."""
        if squares is None or len(squares) == 0:
            json_data = "[]"
        else:
            # Convert the list of squares to
            # a JSON string using to_json_string method
            json_data = cls.to_json_string(
                    [s.to_dictionary() for s in squares]
            )
        # Write the JSON data to a file with the class name as the filename
        with open(cls.__name__ + ".json", "w") as file:
            file.write(json_data)

    @classmethod
    def load_from_file(cls):
        """Load a list of squares from a JSON file."""
        try:
            with open(cls.__name__ + ".json", "r") as file:
                json_data = file.read()
                data = cls.from_json_string(json_data)
                instances = []
                for d in data:
                    try:
                        # Create instances from the
                        # loaded data using create method
                        instance = cls.create(**d)
                        instances.append(instance)
                    except Exception as e:
                        print(f"Error creating instance: {e}")
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **kwargs):
        """Create a new Square instance"""
        id_arg = kwargs.get('id')
        size_arg = kwargs.get('size')
        x_arg = kwargs.get('x', 0)
        y_arg = kwargs.get('y', 0)
        # Create a new Square instance with the provided arguments
        square = cls(size_arg, x_arg, y_arg, id_arg)
        return square

    def area(self):
        """Calculate and Return Area of the SQUARE."""
        return (self.width ** 2)

    def display(self):
        """Prints the Square's shape using '#' characters"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """Return String representation of the square"""
        return (
                f"[Square] ({self.id}) {self.x}/{self.y}"
                f"- {self.width}"
        )

    @classmethod
    def from_json_string(cls, json_string):
        """Create a list of square instances from a JSON string."""
        if json_string is None or json_string == "":
            return []
        json_list = json.loads(json_string)
        return [cls.create(**obj) for obj in json_list]
