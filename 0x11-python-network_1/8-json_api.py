#!/usr/bin/python3
"""
A Python script that takes an optional letter
as a command-line argument,
sends an HTTP POST request to
http://0.0.0.0:5000/search_user
with the letter as a parameter,
and prints the result or an error message.
"""
import sys
import requests


if __name__ == "__main__":
    # Get the letter from the command-line arguments
    # or set it to an empty string if not provided
    letter = "" if len(sys.argv) == 1 else sys.argv[1]

    # Prepare data for the HTTP POST request
    # with the letter as a parameter
    payload = {"q": letter}

    # Make an HTTP POST request to
    # http://0.0.0.0:5000/search_user
    # with the payload
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        # Try to parse the response as JSON
        response = r.json()

        # Check if the response is an empty dictionary
        if response == {}:
            print("No result")
        else:
            # Print the result in the format [id] name
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        # Print an error message if the response is not a valid JSON
        print("Not a valid JSON")
