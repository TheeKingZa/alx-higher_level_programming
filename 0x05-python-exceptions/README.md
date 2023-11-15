[<](https://github.com/TheeKingZa/alx-higher_level_programming/tree/master/0x04-python-more_data_structures/README.md) 0x05 [>](https://github.com/TheeKingZa/alx-higher_level_programming/tree/master/0x06-python-classes/README.md)

# Exceptions
# Need To Know!
* [What’s the difference between errors and exceptions?](#whats-the-difference-between-errors-and-exceptions)
* [What are exceptions and how to use them?](#to-use-exceptions)
* [When do we need to use exceptions?](#when-do-we-need-to-use-exceptions)
* [How to correctly handle an exception?](#how-to-correctly-handle-an-exception)
* [What’s the purpose of catching exceptions?](#whats-the-purpose-of-catching-exceptions)
* [How to raise a builtin exception?](#how-to-raise-a-builtin-exception)
* [When do we need to implement a clean-up action after an exception?](#when-do-we-need-to-implement-a-clean-up-action-after-an-exception)

# What’s the difference between errors and exceptions?
	In Python, errors and exceptions are terms often used interchangeably but have distinct meanings. An error is a generic term for any unexpected behavior that disrupts the normal execution of a program. On the other hand, an exception is a specific event that indicates a problem during the execution of a program, leading to the generation of an exception object.

[^](#exceptions)

# What are exceptions and how to use them?
	Exceptions in Python are events that occur during program execution that disrupt the normal flow of the program. They are raised (or thrown) when an error occurs. Exceptions can be built-in, such as ZeroDivisionError or ValueError, or user-defined.

[^](#exceptions)

# To use exceptions
	you enclose the code that might raise an exception in a try block. If an exception occurs, it is caught by the corresponding except block. This allows you to gracefully handle errors and prevent program termination.

		pyCode
	
   		try:
     		# Code that might raise an exception
       		
	 	result = 10 / 0
		except ZeroDivisionError:
    		# Handle the specific exception
    		print("Division by zero is not allowed.")

[^](#exceptions)

# When do we need to use exceptions?
	Exceptions are used to handle exceptional cases, situations where the normal flow of the program cannot continue. They help in creating robust and fault-tolerant code by allowing you to anticipate and gracefully manage errors.

	Use exceptions when dealing with input validation, file I/O, network operations, or any situation where unexpected errors may occur.

[^](#exceptions)

# How to correctly handle an exception?
	To correctly handle an exception, enclose the potentially problematic code in a try block and provide one or more corresponding except blocks to catch and handle specific exceptions. This ensures that even if an exception occurs, your program can recover or exit gracefully without crashing.

		Code
			try:
   			# Code that might raise an exception
    			result = int(input("Enter a number: "))
			except ValueError:
    			# Handle the specific exception
    			print("Invalid input. Please enter a valid number.")

[^](#exceptions)

# What’s the purpose of catching exceptions?
	The primary purpose of catching exceptions is to gracefully handle errors and prevent the program from crashing. Catching exceptions allows you to take specific actions based on the type of error encountered, improving the overall robustness of your code.

[^](#exceptions)

# How to raise a built-in exception?
	You can raise a built-in exception explicitly using the raise keyword. This is useful when you want to indicate an error condition based on certain criteria.

	pyCode
		if x < 0:
  		raise ValueError("Input must be a non-negative number.")

[^](#exceptions)

# When do we need to implement a clean-up action after an exception?
	In some cases, you might need to perform clean-up actions, such as closing files or releasing resources, regardless of whether an exception occurred or not. To achieve this, you can use the finally block.

		python
		Copy code
			try:
			    # Code that might raise an exception
			    file = open("example.txt", "r")
			    # Process the file
			except FileNotFoundError:
			    # Handle file not found exception
			    print("File not found.")
			finally:
			    # Clean-up action
			    file.close()

The finally block ensures that the clean-up actions are executed, whether an exception occurred or not.

[^](#exceptions)





