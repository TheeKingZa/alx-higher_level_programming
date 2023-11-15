[<](https://github.com/TheeKingZa/alx-higher_level_programming/tree/master//README.md) 0x04 [>](https://github.com/TheeKingZa/alx-higher_level_programming/tree/master//README.md)

# More Data structures.

# Need to Know
* [What are sets and how to use them](#what-are-sets-and-how-to-use-them)?
* [What are the most common methods of set and how to use them?](#common-methods-of-sets-and-their-usage)
* [When to use sets versus lists?](#when-to-use-sets-versus-lists)
* [How to iterate into a set?](#iterating-over-a-set-or-dictionary)
* [What are dictionaries and how to use them?](#what-are-the-dictionaries-and-how-to-use-them)
* [When to use dictionaries versus lists or sets?](#sets-vs-lists)
* [What is a key in a dictionary?](#dictionaries)
* [How to iterate over a dictionary?](#iterating-over-a-set-or-dictionary)
* [What is a lambda function?](#what-is-a-lambda-function)
* [What are the map, reduce and filter functions?](#map-reduce-and-filter-functions)

# What are Sets and how to use them?
          A set is an unordered collection of unique elements. In Python, you can create a set using curly braces {} or by using the set() constructor.
          Here's an example:
                    code

                              # Create a set
                              my_set = {1, 2, 3, 4, 5}


# Common methods of sets and their usage:

          * add(element):
                    Adds an element to the set.
          * remove(element):
                    Removes an element from the set. Raises an error if the element is not present.
          * discard(element):
                    Removes an element from the set if it exists, without raising an error.
          * union(other_set):
                    Returns a new set containing elements from both sets.
          * intersection(other_set):
                    Returns a new set containing elements that are present in both sets.
          * difference(other_set):
                    Returns a new set containing elements present in the first set but not in the second set.
          * isdisjoint(other_set):
                    Returns True if the sets have no elements in common, otherwise False.

# Sets vs Lists 
          Use sets when you want to store a collection of unique items and perform operations like intersection, union, or difference. Use lists when you need an ordered collection of items and duplicates are allowed.

# Iterating over a Set or Dictionary:
          You can use a for loop to iterate over both sets and dictionaries:

                    code--
                              # Iterating over a set
                              for item in my_set:
                                        print(item)
                    
                              # Iterating over a dictionary
                              for key, value in my_dict.items():
                                        print(key, value)



# Dictionaries:
          A dictionary is a collection of key-value pairs, where each key is unique. Keys are used to access values. In Python, dictionaries are created using curly braces {} and colons to separate keys and values.

          --code--

          # Creating a dictionary
          my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Common operations and methods with dictionaries:
          Accessing values:
                    value = my_dict[key]
          Adding a new key-value pair:
                    my_dict[new_key] = new_value
          Updating a value:
                    my_dict[key] = new_value
          Deleting a key-value pair:
                    del my_dict[key]
          Checking if a key exists:
                    if key in my_dict:
          Getting a list of keys:
                    keys = my_dict.keys()
          Getting a list of values:
                    values = my_dict.values()
          Getting key-value pairs:
                    items = my_dict.items()

# What is a Lambda Function
          A lambda function is an anonymous function (a function without a name) defined using the lambda keyword. It's often used for short, simple operations.

                    code
                              # Lambda function to double a number
                              double = lambda x: x * 2
                              result = double(5)  # result will be 10

# Map, Reduce, and Filter Functions
          These are built-in higher-order functions in Python that operate on iterables like lists, sets, or dictionaries.

                    * map(function, iterable):
                              Applies a function to each element in the iterable and returns an                        iterator with the results.
                    * filter(function, iterable):
                              Returns an iterator with elements from the iterable that satisfy                         the given function.
                    * reduce(function, iterable):
                              Applies a function to the elements of the iterable in a cumulative                       way, reducing it to a single value.
                              (Note: reduce used to be in the built-in namespace but is now in the functools module.)

          Here's an example of using map, filter, and reduce:

                    Code

                              from functools import reduce

                              numbers = [1, 2, 3, 4, 5]

                              # Using map to square each number
                              squared = list(map(lambda x: x ** 2, numbers))

                              # Using filter to get even numbers
                              evens = list(filter(lambda x: x % 2 == 0, numbers))

                              # Using reduce to calculate the sum of numbers
                              sum_result = reduce(lambda x, y: x + y, numbers)

-------------------------------------------------------------------
[^](#more-data-structures)
