#!/usr/bin/python3
"""
A Python script that takes a URL as a command-line
argument, sends an HTTP GET request to the URL,
and displays the body of the response.
If the response status code is 400 or higher,
it prints an error message with the status code.
"""
import sys
import requests


if __name__ == "__main__":
    # Get the URL from the command-line arguments
    url = sys.argv[1]

    # Make an HTTP GET request to the specified URL
    r = requests.get(url)

    # Check if the status code is 400 or higher
    if r.status_code >= 400:
        # Print an error message with the status code
        print("Error code: {}".format(r.status_code))
    else:
        # Print the body of the response
        print(r.text)
