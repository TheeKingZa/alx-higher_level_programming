#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using urllib
"""

import urllib.request

# Define the URL to be fetched
url = "https://alx-intranet.hbtn.io/status"

# Use 'with' statement to open the URL, ensuring proper resource handling
with urllib.request.urlopen(url) as response:
    # Read the body of the response
    body = response.read()

    # Decode the body into UTF-8 format
    utf8_content = body.decode('utf-8')

# Print the information in the specified format
print("Body response:")
print(f"\t- type: {type(body)}")
print(f"\t- content: {body}")
print(f"\t- utf8 content: {utf8_content}")
