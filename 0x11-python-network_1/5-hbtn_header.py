#!/usr/bin/python3
"""
Display the X-Request-Id header
variable of a request to a given
URL
"""
import sys
import requests


if __name__ == "__main__":
    # Get the URL from the command-line arguments
    url = sys.argv[1]

    # Make an HTTP GET request to
    # specified URL
    r = requests.get(url)

    # Print Value of the
    # X-Request-Id
    # header
    # if present
    print(r.headers.get("X-Request-Id"))
