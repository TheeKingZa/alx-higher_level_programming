Python - Everything is object
-----------------------------
0x09
-----

NEED TO KNOW?
--------------

Why Python programming is awesome
What is an object
What is the difference between a class and an object or instance
What is the difference between immutable object and mutable object
What is a reference
What is an assignment
What is an alias
How to know if two variables are identical
How to know if two variables are linked to the same object
How to display the variable identifier (which is the memory address in the CPython implementation)
What is mutable and immutable
What are the built-in mutable types
What are the built-in immutable types
How does Python pass variables to functions
-----------------------------------------------------------

Why Python Programming is Awesome
Python is an awesome programming language for several reasons:

Readability: Python's syntax is easy to read and write, making it an excellent choice for beginners and experienced programmers alike.

Versatility: Python can be used for a wide range of applications, from web development and data analysis to artificial intelligence and game development.

Large Standard Library: Python comes with a rich standard library that simplifies common tasks, reducing the need for writing extensive custom code.

Community and Support: Python has a vast and active community of developers who contribute to its growth. You can find extensive documentation, tutorials, and help online.

Understanding Python Concepts
What is an Object?
An object in Python is a fundamental data structure that represents a real-world entity or concept. Everything in Python is an object, including numbers, strings, lists, and even functions. Each object has attributes and methods associated with it.

Class vs. Object (Instance)
Class: A class is a blueprint or template for creating objects. It defines the structure and behavior of objects of that class.

Object (Instance): An object is a specific instance created based on a class. It has its own unique data and can access the methods defined in the class.

Immutable vs. Mutable Objects
Immutable Object: Immutable objects cannot be changed after they are created. Examples include strings and tuples. Any operation that appears to modify an immutable object creates a new object.

Mutable Object: Mutable objects can be modified after creation. Examples include lists and dictionaries. Changes to mutable objects directly affect the original object.

Reference and Assignment
Reference: In Python, a reference is a connection between a variable and the object it refers to. Multiple variables can refer to the same object.

Assignment: Assignment is the process of associating a variable with a value or object. For example, x = 5 assigns the value 5 to the variable x.

Identical Variables and Object Linkage
Identical Variables: Two variables are identical if they refer to the same object. You can use the is keyword to check if two variables are identical.

Same Object: You can use the id() function to check if two variables are linked to the same object. If their id values match, they reference the same object.

Displaying Variable Identifier
To display the variable identifier (memory address) in CPython, you can use the id() function. For example: print(id(variable_name)).

Mutable and Immutable
Mutable objects can be changed after creation, while immutable objects cannot be modified.

Built-in Types
Python has both built-in mutable and immutable types:

Mutable Types: Examples include lists, dictionaries, and sets.

Immutable Types: Examples include integers, floats, strings, and tuples.

Passing Variables to Functions
Python passes variables to functions by reference. When you pass an object (e.g., a list) to a function and modify it within the function, the changes are reflected outside the function because you are working with the same object reference.
