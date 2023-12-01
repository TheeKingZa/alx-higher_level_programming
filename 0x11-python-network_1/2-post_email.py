#!/usr/bin/python3
"""
This script takes a URL and an email address
as command-line arguments.
It sends an HTTP POST request to the specified URL
with the email parameter in the request body.
The response is printed after decoding it as UTF-8.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    # Get the URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare data for the HTTP POST request
    value = {"email": email}
    data = urllib.parse.urlencode(value).encode("ascii")

    # Create a request object with the URL and data
    request = urllib.request.Request(url, data)

    # Open the URL and send the HTTP POST request
    with urllib.request.urlopen(request) as response:
        # Print the response after decoding it as UTF-8
        print(response.read().decode("utf-8"))
