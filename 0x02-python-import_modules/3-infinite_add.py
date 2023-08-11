#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    # Initialize a variable to store the sum of arguments
    total = 0

    # Loop through command-line arguments (excluding script name)
    for i in range(1, len(sys.argv)):
        # Convert each argument to an integer and add it to the total
        total += int(sys.argv[i])

    # Print the total sum of arguments
    print(total)
