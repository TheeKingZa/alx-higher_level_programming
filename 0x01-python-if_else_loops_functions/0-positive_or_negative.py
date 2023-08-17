#!/usr/bin/python3
import random
# import random module
number = random.randint(-10, 10)
# Generate integer from -10 to 10

#check number to print corresponding message.
if number > 0:
    print(f"{number:d} is positive")
elif number == 0:
    print(f"{number:d} is zero")
else:
    print(f"{number:d} is negative")
