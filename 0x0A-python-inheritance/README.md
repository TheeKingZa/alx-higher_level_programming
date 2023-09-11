Python - Inheritance
---------------------
0x0A
----

NEED TO KNOW?
-------------

- Why Python programming is awesome
- What is a superclass, baseclass or parentclass?
- What is a subclass?
- How to list all attributes and methods of a class or instance?
- When can an instance have new attributes?
- How to inherit class from another?
- How to define a class with multiple base classes?
- What is the default class every class inherit from?
- How to override a method or attribute inherited from the base class?
- Which attributes or methods are available by heritage to subclasses?
- What is the purpose of inheritance?
- What are, when and how to use isinstance, issubclass, type and super built-in functions?

-----

	Welcome to this Python programming guide where we'll explore some fundamental concepts that every Python developer should be aware of.
---------------------------------------------------------------------------

	Why Python programming is awesome?
---------------------------------------------------------------------------
		Python is awesome for many reasons:
---------------------------------------------------------------------------

	* It has a simple and easy-to-read syntax, making it accessible to beginners.
* It has a vast standard library with pre-built modules and functions.
* It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
* It is a versatile language used in web development, data science, artificial intelligence, and more.
---------------------------------------------------------------------------

	What is a superclass, base class, or parent class?
---------------------------------------------------------------------------
* In Python, a superclass, base class, or parent class is a class that is extended or inherited by another class. It serves as a template for creating subclasses. Subclasses inherit attributes and methods from their superclass.

---------------------------------------------------------------------------
	What is a subclass?
---------------------------------------------------------------------------
* A subclass is a class that inherits attributes and methods from a superclass. It can also have its own attributes and methods. Subclasses allow for code reusability and can add specific functionality to a base class.

---------------------------------------------------------------------------
	How to list all attributes and methods of a class or instance?
---------------------------------------------------------------------------
* You can use the built-in dir() function to list all attributes and methods of a class or an instance.

For example:

==Code==

class MyClass:
    def my_method(self):
        pass

print(dir(MyClass))

------------------------------------------------------------------------------

	When can an instance have new attributes?
An instance in Python can have new attributes added at any time. You can simply assign a value to a new attribute for an instance, like this:

==Code==

obj = MyClass()
obj.new_attribute = "Hello, World!"

-----------------------------------------------------------------------------

How to inherit a class from another?
To inherit a class from another, use the class definition of the superclass in the definition of the subclass. Here's an example:

==Code==

class ParentClass:
    # Parent class code

class ChildClass(ParentClass):
    # Child class code

-------------------------------------------------------------------------------

How to define a class with multiple base classes?
Python supports multiple inheritance, which means you can define a class with multiple base classes by listing them in the class definition. For example:

==Code==
class ClassA:
    # Class A code

class ClassB:
    # Class B code

class MultipleInheritance(ClassA, ClassB):
    # Multiple inheritance class code

--------------------------------------------------------------------------------

What is the default class every class inherits from?
In Python, the default class that every class inherits from is called object. This is known as the base class for all classes in Python.

How to override a method or attribute inherited from the base class?
To override a method or attribute inherited from the base class, define the same method or attribute in the subclass. The subclass's version will be used instead of the base class's version.

Which attributes or methods are available by heritage to subclasses?
Subclasses inherit all public and protected attributes and methods from their superclass. Private attributes and methods (those starting with a double underscore) are not directly accessible in subclasses.

What is the purpose of inheritance?
Inheritance is a fundamental concept in object-oriented programming that allows for code reuse and the creation of hierarchies of related classes. It promotes modularity and makes code more maintainable.

What are, when, and how to use isinstance, issubclass, type, and super built-in functions?
isinstance(object, class): Checks if an object is an instance of a specified class.
issubclass(subclass, superclass): Checks if a class is a subclass of another class.
type(object): Returns the type of an object.
super(): Returns a temporary object of the superclass, allowing you to call its methods.
These functions are useful for type checking, method resolution, and working with inheritance in Python.

===================================================================================================
