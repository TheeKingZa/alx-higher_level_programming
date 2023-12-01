#!/usr/bin/python3
"""
A Python script that takes GitHub credentials
(username and password)
as command-line arguments,
sends an HTTP GET request to
https://api.github.com/user
with basic authentication,
and prints the user's GitHub ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    # Get GitHub username and password from
    # command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Create HTTPBasicAuth object
    # for authentication
    auth = HTTPBasicAuth(username, password)

    # Make an HTTP GET request to
    # https://api.github.com/user
    # with basic authentication
    r = requests.get("https://api.github.com/user", auth=auth)

    # Print the user's GitHub ID from
    # the JSON response
    print(r.json().get("id"))
