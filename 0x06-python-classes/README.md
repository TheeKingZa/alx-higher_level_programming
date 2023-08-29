------------------------------------------------------------------------------------
Python - Classes and Objects
----------------------------
0x06
----
------------------------------------------------------------------------------------------------
1.
Why Python Programming is Awesome:
------------------------------------------------------------------------------------------------
	Python is often praised for its simplicity, readability, and versatility. It has a large community and a wide range of libraries, making it suitable for various tasks from web development to data analysis and machine learning.

------------------------------------------------------------------------------------------------
2.
What is OOP (Object-Oriented Programming):
------------------------------------------------------------------------------------------------
	OOP is a programming paradigm that organizes data and functionality into objects. It focuses on creating reusable and modular code by defining classes and objects.

------------------------------------------------------------------------------------------------
3.
"First-Class Everything":
------------------------------------------------------------------------------------------------
	In Python, everything is an object, which means everything can be assigned to a variable, passed as an argument, and returned from a function.

------------------------------------------------------------------------------------------------
4.
What is a Class:
------------------------------------------------------------------------------------------------
	A class is a blueprint for creating objects. It defines the structure and behavior that its instances will have.

------------------------------------------------------------------------------------------------
5.
What is an Object and an Instance:
------------------------------------------------------------------------------------------------
	An object is a concrete entity created from a class. An instance is a specific occurrence of an object.

------------------------------------------------------------------------------------------------
6.
Difference Between a Class and an Object or Instance:
------------------------------------------------------------------------------------------------
	A class is a template, while an object/instance is an actual instantiation of that template.

------------------------------------------------------------------------------------------------
7.
What is an Attribute:
------------------------------------------------------------------------------------------------
	An attribute is a piece of data associated with a class or object. It can be a variable or a value.

------------------------------------------------------------------------------------------------
8.
Public, Protected, and Private Attributes:
------------------------------------------------------------------------------------------------
	In Python, attributes are public by default. Protected attributes have a single underscore prefix (e.g., _protected). Private attributes have a double underscore prefix (e.g., __private).

------------------------------------------------------------------------------------------------
9.
What is self:
------------------------------------------------------------------------------------------------
	self is a reference to the instance of the class. It is used to access attributes and methods within the class.

10.
What is a Method:
------------------------------------------------------------------------------------------------
	A method is a function defined within a class, and it operates on instances of that class.
------------------------------------------------------------------------------------------------

11.
Special __init__ Method and How to Use It:
------------------------------------------------------------------------------------------------
	__init__ is a special method (constructor) that gets called when an object is created. It initializes the object's attributes.

------------------------------------------------------------------------------------------------
12.
Data Abstraction, Data Encapsulation, and Information Hiding:
------------------------------------------------------------------------------------------------

	* Data Abstraction: Hiding the complex implementation details and showing only the necessary features.
	* Data Encapsulation: Bundling data (attributes) and methods that operate on the data into a single unit (class).
	* Information Hiding: Restricting access to certain details of an object and exposing only what's necessary.

------------------------------------------------------------------------------------------------
13.
What is a Property:
------------------------------------------------------------------------------------------------
	A property is a special kind of attribute that provides controlled access and modification through methods (getters and setters).

------------------------------------------------------------------------------------------------
14.
Difference Between an Attribute and a Property in Python:
------------------------------------------------------------------------------------------------
	An attribute is a variable associated with an object, while a property provides controlled access to attributes.

------------------------------------------------------------------------------------------------
15.
Pythonic Way to Write Getters and Setters:
------------------------------------------------------------------------------------------------
	In Python, properties are often used instead of explicit getter and setter methods. The @property decorator is used for getters, and the @<attribute>.setter decorator is used for setters.
------------------------------------------------------------------------------------------------
16.
How to Dynamically Create Arbitrary New Attributes:
------------------------------------------------------------------------------------------------
	You can dynamically create attributes using the dot notation or the setattr() function.

------------------------------------------------------------------------------------------------
17.
How to Bind Attributes to Objects and Classes:
------------------------------------------------------------------------------------------------
	Attributes are bound to objects by assigning values to them. They can also be bound to classes, serving as class attributes.

------------------------------------------------------------------------------------------------
18.
What is the __dict__ of a Class and/or Instance:
------------------------------------------------------------------------------------------------
	The __dict__ attribute of a class or instance is a dictionary containing the attributes and methods defined for that class or instance.

------------------------------------------------------------------------------------------------
19.
How Does Python Find Attributes of an Object or Class:
------------------------------------------------------------------------------------------------
	Python searches for attributes first in the instance, then in the class, and finally in the base classes.
------------------------------------------------------------------------------------------------
20.
How to Use the getattr() Function:
------------------------------------------------------------------------------------------------
	The getattr() function is used to access the value of an attribute of an object. It takes the object and attribute name as arguments. If the attribute doesn't exist, it can return a default value.
------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------
===CODE===

-----------
#!/usr/bin/python3
"""
This module provides examples for various object-oriented programming concepts.
"""

# Example 1: Why Python Programming is Awesome
print("Python programming is awesome because of its simplicity and versatility.")

# Example 2: Class Definition
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

# Example 3: Object and Instance
my_car = Car("Toyota", "Camry")

# Example 4: Public, Protected, and Private Attributes
class BankAccount:
    def __init__(self):
        self.balance = 0         # Public attribute
        self._transaction_log = []  # Protected attribute
        self.__pin = 1234        # Private attribute

# Example 5: Method Definition
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius ** 2

# Example 6: Special __init__ Method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Example 7: Property
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

# Example 8: Dynamically Create Attributes
class Student:
    pass

student = Student()
setattr(student, "name", "John")
print(student.name)  # Output: John

# Example 9: __dict__ of a Class and Instance
print(Car.__dict__)      # Class attributes and methods
print(my_car.__dict__)   # Instance attributes

# Example 10: Using getattr() Function
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book = Book("Python 101", "Alice Smith")
attr_name = "title"
print(getattr(book, attr_name))  # Output: Python 101

# Summary:
# Python's simplicity and versatility make it awesome.
# OOP organizes data and behavior into objects.
# "First-class everything" means everything in Python is an object.
# A class is a blueprint for creating objects.
# An object is a concrete instance of a class.
# Attributes are data associated with a class or object.
# Access to attributes can be controlled using public, protected, and private access specifiers.
#  refers to the instance within a class.
# Methods are functions defined within a class.
#  is a special method used for object initialization.
# Data Abstraction hides complexity, Encapsulation bundles data and methods, Information Hiding restricts access.
# Properties provide controlled access to attributes.
# Attributes are variables, properties are methods.
#  accesses attribute values dynamically.
