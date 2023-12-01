#!/usr/bin/python3
"""
This script fetches the content of
https://alx-intranet.hbtn.io/status
using the requests module and prints
information about the response,
including its type and content,
with a specific format.
"""
import requests


if __name__ == "__main__":
    # URL to fetch
    url = "https://alx-intranet.hbtn.io/status"

    # Make an HTTP GET request to the specified URL
    response = requests.get(url)

    # Print header for the response information
    print("Body response:")

    # Print the type of the response content
    print("\t- type: {}".format(type(response.text)))

    # Print the content of the response
    print("\t- content: {}".format(response.text))
