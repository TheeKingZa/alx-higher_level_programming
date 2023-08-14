#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    # Get a list of all names defined in the hidden_4 module
    names = dir(hidden_4)

    # Loop through each name and print if it doesn't start with "__"
    for name in names:
        if not name.startswith("__"):
            print(name)
