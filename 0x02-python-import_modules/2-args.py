#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys
    # Get the number of arguments passed (excluding the script name)
    count = len(sys.argv) - 1

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    # Iterate over the arguments and print each argument with it's position
    for i in range(count):
        # i + 1 is the position of the argument (starting at 1)
        # sys.argv[i + 1] gets the actual value
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
