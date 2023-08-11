#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

# Assigning values to variables
a = 10
b = 5

# Calling the imported functions and printing the results
add_result = add(a, b)
sub_result = sub(a, b)
mul_result = mul(a, b)
div_result = div(a, b)

# Printing the results
print(f"{a} + {b} = {add_result}")
print(f"{a} - {b} = {sub_result}")
print(f"{a} * {b} = {mul_result}")
print(f"{a} / {b} = {div_result}")
