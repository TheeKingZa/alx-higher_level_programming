[<](https://github.com/TheeKingZa/alx-higher_level_programming/tree/master/0x02-python-import_modules/README.md) 0x03 [>](https://github.com/TheeKingZa/alx-higher_level_programming/tree/master/0x04-python-more_data_structures/README.md)
# Data Structures: Lists, Tuples

# NEED TO KNOW?

* [What are lists and how to use them](#what-are-lists-and-how-to-use-them)?
* [What are the differences and similarities between strings and lists?](#differences-and-similarities-between-strings-and-lists)
* [What are the most common methods of lists and how to use them?](#common-methods-of-lists)
* [How to use lists as stacks and queues?](#using-lists-as-stacks-and-queues)
* [What are list comprehensions and how to use them?](#list-comprehensions)
* [What are tuples and how to use them?](#tuples)
* [When to use tuples versus lists?](#when-to-use-tuples-vs-lists)
* [What is a sequence?](#Sequence)
* [What is tuple packing?](#tuple-packing)
* [What is sequence unpacking?](#sequence-unpacking)
* [What is the del statement and how to use it?](#the-del-statement)

# What are Lists and how to use them?
	Lists are ordered collections of items in Python. They can contain elements of different data types, and they are mutable, meaning you can modify their contents after creation.


	Here's an example of creating a list and accessing its elements:

	pycode
 		my_list = [1, 2, 3, 'four', 5.0]
		print(my_list[0])  

	Output: 1

# Differences and Similarities between Strings and Lists
	Both strings and lists are sequences,
 	but strings hold a sequence of characters,
  	while lists can hold various data types.
	Strings are immutable,
 	meaning you can't change their characters directly,
  	whereas lists are mutable.
	
 	Similarity:
  		Both strings and lists can be indexed and sliced to access specific elements or sublists.


# Common Methods of Lists:
	Some common list methods include append(), insert(), pop(), remove(), extend(), and sort().
		Here's an example of using some of these methods:

		pyCode

			my_list = [1, 2, 3]
			my_list.append(4)
			my_list.insert(1, 5)
			my_list.pop()
			my_list.remove(2)
			my_list.extend([6, 7])
			my_list.sort()
			print(my_list)  

		# Output: [1, 3, 5, 6, 7]



# Using Lists as Stacks and Queues
	You can use a list as a stack (Last-In-First-Out) by using append() to add elements and pop() to remove the last element.
	You can use a list as a queue (First-In-First-Out) by using append() to enqueue and pop(0) to dequeue.


# List Comprehensions
	List comprehensions provide a concise way to create lists. They consist of an expression followed by at least one for clause.
		Here's an example of list comprehension:

		pyCode
			squared_numbers = [x ** 2 for x in range(1, 6)]
			print(squared_numbers)

		# Output: [1, 4, 9, 16, 25]


# Tuples
	Tuples are similar to lists but are immutable. They are used to group related data together.
		Here's an example of creating and using a tuple:

		pyCode
			my_tuple = (1, 'two', 3.0)
			print(my_tuple[1])  # Output: 'two'

# When to Use Tuples vs. Lists
	Use lists when you need a collection that can be modified. Use tuples when you want to create a collection of items that should not change.


# Sequence
	A sequence is an ordered collection of items. Strings, lists, and tuples are examples of sequences in Python.


# Tuple Packing
	Tuple packing is the process of creating a tuple by placing comma-separated values inside parentheses.
		pyCode
			coordinates = 10, 20
			print(coordinates)  # Output: (10, 20)

# Sequence Unpacking:
	Sequence unpacking is the process of assigning the values of a sequence to multiple variables.
		pyCode
  			x, y = coordinates
			print(x)  # Output: 10
# The del Statement:
	The del statement is used to delete a reference to an object. It can be used to remove items from lists and other data structures.
		pyCode
			my_list = [1, 2, 3]
			del my_list[1]
			print(my_list)

		# Output: [1, 3]
----
[^](#data-structures-lists-tuples
)
