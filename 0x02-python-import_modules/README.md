0x02.  Python-Import_Modules
--------------------


Learning is the need to know the following:
-----------------------------------------
* Why Python programming is awesome?
* How to import functions from another file?
* How to use imported functions?
* How to create a module?
* How to use the built-in function dir()?
* How to prevent code in your script from being executed when imported?
* How to use command line arguments with your Python programs?
========================================================================


* Why Python programming is awesome:
----------------------------------------------
Python is awesome for many reasons. It has a simple and readable syntax, extensive libraries, and a large supportive community. It's versatile and can be used for various applications, from web development and data analysis to artificial intelligence and scientific computing.

----------------------------------------------
* How to import functions from another file:
----------------------------------------------
To import functions from another file, you can use the import statement. Let's say you have a file named my_module.py with a function called my_function. In your main script, you can do:

=======code=======

import my_module

result = my_module.my_function()

-----------------------------------------------
* How to use imported functions:
----------------------------------------------
  Once you've imported a function, you can use it just like any other function in your script. In the example above, we used my_module.my_function() to call the imported function.

----------------------------------------------
* How to create a module:
----------------------------------------------
A module is simply a Python file containing functions, classes, and variables. You can create a module by creating a .py file. For example, to create a module named my_module, create a file named my_module.py and define your functions, classes, and variables in it.

----------------------------------------------
* How to use the built-in function dir():
----------------------------------------------
The dir() function is used to find out what names a module or object defines. It returns a list of valid attributes for the given object. For example:

=======code=======

import math

print(dir(math))  # Prints a list of attributes in the math module

----------------------------------------------
* How to prevent code in your script from being executed when imported:
----------------------------------------------
In Python, you can use the if __name__ == "__main__": construct to prevent certain code from running when the script is imported as a module. This allows you to have code that is only executed when the script is run directly, not when it's imported.

=======code=======

def my_function():
    # Your function code here

if __name__ == "__main__":
    # Code here will only run when the script is run directly, not when imported
    result = my_function()
    print(result)

----------------------------------------------
* How to use command line arguments with your Python programs:
----------------------------------------------
You can use the sys module to access command line arguments. Here's a basic example:

=======code=======
import sys

# The first command line argument is the script name itself, so we skip it
arguments = sys.argv[1:]

for arg in arguments:
    print("Argument:", arg)
You can run this script from the command line and pass arguments like this: python my_script.py arg1 arg2.
--------------------------------------------------------------------------------------------

