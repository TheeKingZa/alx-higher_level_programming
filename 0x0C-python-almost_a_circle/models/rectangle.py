#!/usr/bin/python3
# models/rectangle.py

import json

class Rectangle:
    """Class representing a RECTANGLE"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance"""
        self.id = id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle's shape using '#' characters"""
        result = ""
        for _ in range(self.__y):
            result += "\n"
        for _ in range(self.__height):
            result += ' ' * self.__x + '#' * self.__width + "\n"
        return result

    def __str__(self):
        """Return a string representation of the rectangle"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Update attributes using args and kwargs"""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    @staticmethod
    def to_json_string(list_rectangles):
        """Convert a list of Rectangle instances to a JSON string"""
        if list_rectangles is None or len(list_rectangles) == 0:
            return "[]"
        dict_list = [rectangle.to_dictionary() for rectangle in list_rectangles]
        return json.dumps(dict_list)

    @classmethod
    def from_json_string(cls, json_string):
        """Create a list of Rectangle instances from a JSON string"""
        if json_string is None or json_string == "":
            return []
        dict_list = json.loads(json_string)
        return [cls.create(**rectangle_dict) for rectangle_dict in dict_list]

    @classmethod
    def create(cls, **kwargs):
        """Create a new Rectangle instance"""
        id_arg = kwargs.get('id')
        width_arg = kwargs.get('width')
        height_arg = kwargs.get('height')
        x_arg = kwargs.get('x', 0)
        y_arg = kwargs.get('y', 0)
        rectangle = cls(width_arg, height_arg, x_arg, y_arg, id_arg)
        return rectangle

    @classmethod
    def load_from_file(cls):
        """Load a list of rectangles from a JSON file"""
        try:
            with open(cls.__name__ + ".json", "r") as file:
                json_data = file.read()
                data = cls.from_json_string(json_data)
                instances = []
                for d in data:
                    try:
                        instance = cls.create(**d)
                        instances.append(instance)
                    except Exception as e:
                        print(f"Error creating instance: {e}")
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to a JSON file."""
        if list_objs is None:
            list_objs = []
            # Convert the list of dictionaries to a JSON string
            json_string = cls.to_json_string(list_objs)
            # Write the JSON string to a file with
            #the class name as the filename
            filename = cls.__name__ + ".json"
            with open(filename, "w") as file:
                file.write(json_string)
