#!/usr/bin/python3

import requests

"""
This script fetches the content of
https://intranet.hbtn.io/status using the
requests module and prints information
about the response, including its type
and content.
"""

if __name__ == "__main__":
    # Make an HTTP GET request to https://....
    r = requests.get("https://intranet.hbtn.io/status")

    # Print information about the response
    print("Body response: ")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
