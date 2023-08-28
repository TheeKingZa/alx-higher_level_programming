#!/usr/bin/python3

def raise_exception_msg(message=""):
    """
    Raises a NameError exception with a custom message.

    Args:
        message (str): The custom error message to include with the exception.

    Raises:
        NameError:
            Always raised when this function is called,
            with the provided message.
    """
    raise NameError(message)
