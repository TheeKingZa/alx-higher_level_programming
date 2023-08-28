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
------------------------
4Advanced Tasks
---------------

* 100-safe_print_integer_err.py.
--------------------------------
* The safe_print_integer_err function first attempts to print the provided integer value using the "{:d}".format() format specifier.
-----
* If a TypeError or ValueError occurs during the formatting process (e.g., if value is not an integer), the respective exception is caught.
-----
* Inside the except block, an error message is printed to the standard error stream using the sys.stderr stream. The sys.exc_info() function is used to retrieve information about the current exception, and [1] accesses the exception message.
-----
* The function returns False to indicate that printing was not successful if an exception occurred, and True if printing was successful.
--------------------------------------------------------------------------------
------------------------------------------
101-safe_function.py 
---------------------

* The safe_function function takes two arguments: fct (a function) and *args (a variable number of arguments).
-----
* Inside the function, the try block attempts to execute the provided function fct with the provided arguments *args.
-----
* If an exception occurs during the function execution, the except block catches the exception. The error message associated with the exception is printed to the standard error stream using the sys.stderr stream.
-----
* If no exception occurs during the function execution, the else block is executed. In this case, the result of the function execution (res) is returned.
-----

* If an exception occurs during the function execution, the function returns None to indicate that an exception occurred.
-----
---------------------------------------------

102-magic_calculation.py
------------------------

* The magic_calculation function takes two arguments, a and b, which are used in the calculation.
----
* Inside the function, there's a loop that iterates from 1 to 2 (inclusive) using the range(1, 3) construct.
----
* Within the loop, there's a try block. If the value of i becomes greater than a, a custom exception of type Exception is raised with the message 'Too far'.
----
* If no exception occurs in the try block, the calculation result += a ** b / i is performed.
----
* If an exception is caught, the except block is executed. In this block, the value of result is set to b + a, and the loop is broken using the break statement.
----
* After the loop, the function returns the final value of result, which could be either the calculated value or b + a depending on whether the exception was raised.
-----------------------------------------------------------------
---------------------------------------
103-python.c 
---------------------------------------
step by step

---------------
1.
Include Header Files:
---------------
The code starts by including the necessary header files: Python.h (Python C API) and stdio.h (standard input/output).

---------------
2.
Define print_python_float Function:
---------------
The print_python_float function takes a PyObject pointer p as an argument. This function is responsible for printing information about Python float objects.

---------------
3.
Check if p is a Valid PyFloatObject:
---------------
The function starts by checking if the given p is a valid PyFloatObject using the PyFloat_CheckExact function. If it's not a PyFloatObject, it prints an error message and returns.

---------------
4.
Extract Float Value and Convert to String:
---------------
If p is a PyFloatObject, it extracts the float value from the object using (PyFloatObject *)p)->ob_fval. It then converts the float value to a string representation using PyOS_double_to_string.

---------------
5.
Print Float Value:
---------------
The string representation of the float value is printed using printf.

---------------
6.
Define print_python_bytes Function:
---------------
Similar to print_python_float, this function is responsible for printing information about Python bytes objects.

---------------
7.
Check if p is a Valid PyBytesObject:
---------------
The function checks if p is a valid PyBytesObject using PyBytes_CheckExact. If not, it prints an error message and returns.

---------------
8.
Get Size and Access Raw Byte Data:
---------------
If p is a valid PyBytesObject, it gets the size of the bytes object using PyBytes_Size. It also accesses the raw byte data using (((PyBytesObject *)(p))->ob_sval).

---------------
9.
Print Size and Byte Data:
---------------
The size of the bytes object is printed. Then, the string representation of the byte data is printed, followed by the first few bytes of the bytes object in hexadecimal format.

---------------
10.
Define print_python_list Function:
---------------
This function is responsible for printing information about Python list objects.

---------------
11.
Check if p is a Valid PyListObject:
---------------
The function checks if p is a valid PyListObject using PyList_CheckExact. If not, it prints an error message and returns.

---------------
12.
Get Size of the List:
---------------
If p is a valid PyListObject, it gets the size of the list using PyList_GET_SIZE.

---------------
13.
Print Size and Allocation Details:
---------------
The size of the list and the allocated memory are printed.

---------------
14.
Iterate Through List Elements:
---------------
The function iterates through each element of the list using a loop. It gets the current element using PyList_GET_ITEM.

---------------
15.
Check Item Type and Print Information:
---------------
For each element, it checks if the item is a bytes object using PyBytes_Check and calls print_python_bytes if true. Similarly, it checks if the item is a float object using PyFloat_Check and calls print_python_float if true.

---------------
16.
Print Element Number and Type Name:
---------------
It prints the element number and its type name using printf.

---------------
17.
Finalize Loop:
---------------
The loop iterates through all elements of the list.

---------------
18.
Complete print_python_list:
---------------
After the loop, if p was not a valid PyListObject, an error message is printed.
===============--------------
---------------===============
===============---------------
---------------===============
===============---------------
---------------===============
===============---------------
---------------===============
