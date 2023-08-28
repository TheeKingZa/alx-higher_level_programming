-----------------
 Python - Exceptions
--------------------
0x05
-----

Need To Know!
--------------

Why Python programming is awesome
What’s the difference between errors and exceptions
What are exceptions and how to use them
When do we need to use exceptions
How to correctly handle an exception
What’s the purpose of catching exceptions
How to raise a builtin exception
When do we need to implement a clean-up action after an exception?

===================================================================
--------------------------------------------------------------------

1. Why Python Programming is Awesome:
--------------------------------------------------------------------
Python is awesome for several reasons:
--------------------------------------------------------------------

 * Readability: Python's clean and straightforward syntax makes code easy to read and understand.
 * Versatility: It can be used for web development, data analysis, artificial intelligence, scientific computing, and more.
 * Large Standard Library: Python comes with a vast collection of modules and libraries that simplify development.
 *  Community: Python has a thriving community that creates and maintains numerous open-source packages.
 * Cross-Platform: Python code can run on various platforms without modification.

--------------------------------------------------------------------
2. Difference between Errors and Exceptions:
--------------------------------------------------------------------

 * Errors: Errors are mistakes that prevent the program from running, often caused by syntax or logic issues.
 * Exceptions: Exceptions are events that disrupt the normal flow of a program, typically caused by runtime errors like dividing by zero or accessing an index out of range.

--------------------------------------------------------------------
3. What are Exceptions and How to Use Them:
--------------------------------------------------------------------
Exceptions are objects raised at runtime to handle unexpected situations. They allow you to handle errors gracefully instead of crashing the program. You can use the try, except, and finally blocks to work with exceptions.


===code===

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")

--------------------------------------------------------------------
4. When to Use Exceptions:
--------------------------------------------------------------------
Use exceptions when you expect certain errors to occur and want to handle them in a controlled manner. They're particularly useful when dealing with user input or external resources.

--------------------------------------------------------------------
5. How to Correctly Handle an Exception:
--------------------------------------------------------------------
To handle exceptions, enclose the risky code in a try block and provide corresponding except blocks for each exception you want to catch.

===code===

try:
    value = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a valid number.")
--------------------------------------------------------------------
6. Purpose of Catching Exceptions:
--------------------------------------------------------------------
Catching exceptions allows your program to continue running even if an error occurs. It prevents crashes and gives you a chance to handle errors gracefully.

--------------------------------------------------------------------
7. How to Raise a Built-in Exception:
--------------------------------------------------------------------
You can raise exceptions using the raise statement, optionally providing an exception type and an error message.


===code===

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed!")
    return a / b

--------------------------------------------------------------------
8. When to Implement Clean-Up Actions after an Exception:
--------------------------------------------------------------------
You can use the finally block to implement clean-up actions that need to occur regardless of whether an exception was raised or not. This is useful for releasing resources or closing files.

===code===

	file = None
	try:
		file = open("data.txt", "r")
		content = file.read()
	except FileNotFoundError:
		print("File not found!")
	finally:
		if file:
			file.close()
=============================================================================
