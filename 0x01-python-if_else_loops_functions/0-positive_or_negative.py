#!/usr/bin/python3
import random

# Generate a random signed number each time the program is executed
number = random.randint(-10, 10)

# Print the generated number
print("The number is:", number)

# Check whether the number is positive, negative, or zero
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
