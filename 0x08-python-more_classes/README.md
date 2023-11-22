# More_Classes
[<](https://github.com/TheeKingZa/alx-higher_level_programming/tree/master/0x07-python-test_driven_development/README.md) 0x08 [>](https://github.com/TheeKingZa/alx-higher_level_programming/tree/master/0x09-python-everything_is_object/README.md)
---

# NEED TO KNOW?
-------------
* [What is OOP?]()
* [“first-class everything”?]()
* [What is a class?]()
* [What is an object and an instance?]()
* [What is the difference between a class and an object or instance?]()
* [What is an attribute?]()
* [What are and how to use public, protected and private attributes?]()
* [What is self?]()
* [What is a method?]()
* [What is the special __init__ method and how to use it?]()
* [What is Data Abstraction, Data Encapsulation, and Information Hiding?]()
* [What is a property?]()
* [What is the difference between an attribute and a property in Python?]()
* [What is the Pythonic way to write getters and setters in Python?]()
* [What are the special __str__ and __repr__ methods and how to use them?]()
* [What is the difference between __str__ and __repr__?]()
* [What is a class attribute?]()
* [What is the difference between a object attribute and a class attribute?]()
* [What is a class method?]()
* [What is a static method?]()
* [How to dynamically create arbitrary new attributes for existing instances of a class?]()
* [How to bind attributes to object and classes?]()
* [What is and what does contain __dict__ of a class and of an instance of a class?]()
* [How does Python find the attributes of an object or class?]()
* [How to use the getattr function?]()



What is OOP? Object-Oriented Programming (OOP) is a programming paradigm that organizes data and functions into objects. It focuses on the concept of objects, which are instances of classes, and enables code reusability and modularity.

"First-class everything": In Python, everything is considered an object, including functions. This means you can pass functions as arguments to other functions, assign them to variables, and even return them from other functions.

What is a class? A class is a blueprint for creating objects. It defines the structure and behavior that its instances will have. It serves as a template for creating objects with shared attributes and methods.

What is an object and an instance? An object is a concrete instantiation of a class. An instance is another term for an object, emphasizing that it is created from a class definition.

Difference between a class and an object/instance: A class is a blueprint, while an object/instance is a specific instance created from that blueprint. Classes define the structure, and objects/instances hold the data and behavior.

What is an attribute? An attribute is a variable associated with a class or an instance. It can store data related to the class or instance.

Public, protected, and private attributes: In Python, attributes can have different levels of visibility. Public attributes are accessible from anywhere. Protected attributes are indicated with a single underscore and should be considered non-public. Private attributes are indicated with double underscores and are meant to be private to the class.

What is self? self is a reference to the instance of a class. It is typically the first parameter in instance methods and is used to access and manipulate instance-specific attributes and methods.

What is a method? A method is a function defined within a class. It operates on the attributes of the class and can be called on instances of the class.

Special init method: __init__ is a special method (constructor) in Python classes. It is automatically called when an instance of the class is created and is used to initialize its attributes.

Data Abstraction, Data Encapsulation, and Information Hiding: These are principles of OOP. Data abstraction refers to presenting essential features of an object while hiding unnecessary details. Data encapsulation is bundling data and methods that operate on it into a single unit. Information hiding is the concept of restricting access to certain attributes or methods to prevent unintended interference.

What is a property? A property is a special attribute in Python that allows you to control the access and modification of an object's data.

Difference between an attribute and a property: Attributes store data, while properties provide a way to control access and modification of that data through methods like getters and setters.

Pythonic way to write getters and setters: Python uses @property for getters and @<attribute>.setter for setters to define properties and control attribute access.

Special str and repr methods: These are used to define human-readable and unambiguous representations of objects, respectively. They are called by built-in functions like str() and repr().

Difference between str and repr: __str__ provides a user-friendly, human-readable string, while __repr__ is meant for debugging and should be an unambiguous representation.

Class attribute: A class attribute is an attribute shared among all instances of a class. It's defined within the class but outside any instance methods.

Difference between object attribute and class attribute: Object attributes are specific to instances and can vary between them. Class attributes are shared among all instances and are constant across them.

Class method: A class method is a method that operates on class-level attributes and can be called on the class itself.

Static method: A static method is a method defined within a class that does not depend on instance-specific attributes. It can be called on the class itself without creating an instance.

Dynamically creating attributes: You can add new attributes to existing instances of a class by simply assigning values to them.

Binding attributes to objects and classes: Attributes can be bound to both instances and classes, depending on where they are defined.

__dict__ of a class and an instance: __dict__ is a dictionary that stores the attributes of a class or an instance.

How Python finds attributes: Python looks for attributes first in the instance's namespace, then in the class's namespace, and finally in the namespaces of parent classes (if it's an inherited attribute).

How to use the getattr function: getattr(object, attribute_name, default) is used to get the value of an attribute from an object. If the attribute doesn't exist, it returns the default value.
-------------------------------------------

[^](#need-to-know)

