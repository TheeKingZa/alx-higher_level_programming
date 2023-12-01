#!/usr/bin/python3
"""
takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id variable
found in the header of the response.
"""

import sys
import urllib.request

if __name__ == "__main__":
    # Get the URL from the command-line arguments
    url = sys.argv[1]

    # Create a request object for the specified URL
    request = urllib.request.Request(url)

    # Open the URL and get the HTTP response
    with urllib.request.urlopen(request) as response:
        # Print the value of the "X-Request-Id" header
        print(dict(response.headers).get("X-Request-Id"))
