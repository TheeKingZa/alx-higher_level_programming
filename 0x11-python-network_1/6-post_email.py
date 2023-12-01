#!/usr/bin/python3
"""
A Python script that takes a URL and
an email address as command-line arguments,
sends a POST request to the specified
URL with the email as a parameter,
and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    # Get the URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare data for the HTTP POST request
    data = {"email": email}

    # Make an HTTP POST request to the specified URL
    response = requests.post(url, data=data)

    # Display the body of the response
    print(response.text)
