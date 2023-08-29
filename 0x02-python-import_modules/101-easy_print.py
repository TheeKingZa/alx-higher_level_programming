#!/usr/bin/python3

# Importing sys module to access stdout
import sys

# Using a list comprehension to write the desired output to stdout
# We iterate over a range with just one element (1), so the loop runs once
# Within the loop, we use sys.stdout.write to write the string to stdout
[sys.stdout.write("#pythoniscool\n") for i in range(1)]
