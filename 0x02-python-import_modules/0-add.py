#!/usr/bin/python3
# Importing the function from add_0.py
add_module = __import__("add_0")

# Assigning values to variables
a = 1
b = 2

# Calling the add function and printing the result
print(f"{a} + {b} = {add_module.add(a, b)}")
