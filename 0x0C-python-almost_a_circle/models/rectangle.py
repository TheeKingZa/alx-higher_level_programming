#!/usr/bin/python3
"""
Module containing the Rectangle class.
Representing a RECTANGLE.
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): rectangle's position.
            y (int): rectangle's position.
            id (int):
                The ID of the instance.
                If None, it will be auto-generated.
        """
        # Call the constructor of the Base class to handle the ID.
        super().__init__(id)
        # Validate and assign width, height, x, and y attributes.
        self.__width = 0
        self.__height = 0
        self.__x = 0
        self.__y = 0
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getter and setter methods for private attributes
    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x attribute."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Display the rectangle by printing '#' characters.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + "#" * self.width)

    def __str__(self):
        """
        Custom string representation of the Rectangle instance.

        Returns:
            str: A formatted string representing the Rectangle.
        """
        return (
                f"[Rectangle] ({self.id}) {self.x}/{self.y}"
                f" - {self.width}/{self.height}"
        )

    def update(self, *args, **kwargs):
        """Update
        the attributes of RECTANGLE instance.

        Args:
            *args:
                if provided.
                assign values to attribute in order
            *kwargs:
                if provided.
                assigns values to attributes using key_value.
        """
        largs = len(args)
        # arg length
        if args:
            if largs >= 1:
                self.id = args[0]
            if largs >= 2:
                self.width = args[1]
            if largs >= 3:
                self.height = args[2]
            if largs >= 4:
                self.x = args[3]
            if largs >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return
        the dictionary representation of a rectangle.
        """
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
        }
