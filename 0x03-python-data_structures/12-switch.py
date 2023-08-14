#!/usr/bin/python3

# Initialize variables 'a' and 'b'
a = 89
b = 10

# Swap the values of 'a' and 'b' using tuple unpacking
a, b = b, a

# Print the updated values of 'a' and 'b'
print("a={:d} - b={:d}".format(a, b))
