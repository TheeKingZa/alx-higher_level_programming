#!/usr/bin/python3
"""
Module containing the RECTANGLE class.
"""

# models/rectangle.py

# Import the Base class from base.py
from models.base import Base


class Rectangle(Base):
    """Rectangle class
    @ inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize
        Constructor for RECTANGLE class.

        Args:
        instance(int) with
            @ width:
                Width of the RECTANGLE.
            @ height:
                Height of the RECTANGLE.
            @ x:
                x-coordinate of the RECTANGLE's position.
            @ y:
                y-coordinate of the RECTANGLE's posistion.
            @ id:
                Id of instance..
        """
        # Call the constructor of the Base class with the provided id
        super().__init__(id)
        # Validate and assign instances.
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
        Calculate and Return.
        Area of RECTANGLE

        Returns:
            int:
                Area of Rectangle.
        """
        return (self.width * self.height)

    def display(self):
        """
        Display the RECTANGLE.
        by printing '#' character.
        """
        for  _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Custom striing representation..
        ..of the RECTANGLE instance.

        Returns:
            str:
                A formatted string format.
                representing Rectangle.
        """
        return (
                f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}"
        )

    def update(self, *args, **kwargs):
        """
        Update attributes of RECTANGLE instatnce.

        Args:
            *args (list):
                values to update attributes in the order:
                    - 1st argument: id attribute.
                    - 2nd arg: width attr.
                    - 3rd arg: height attr.
                    - 4th arg: x attr.
                    - 5th arg: y attr.
            **kwargs (dict): Keyword arguments to update
                        the attributes by name.
        """
        num_args = len(args)
        if args:
            if num_args >=1:
                self.id = args[0]
            if num_args >= 2:
                self.width = args[1]
            if num_args >= 3:
                self.height = args[2]
            if num_args >= 4:
                self.x = args[3]
            if  num_args >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

