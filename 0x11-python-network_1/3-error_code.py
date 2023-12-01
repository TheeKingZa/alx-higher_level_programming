#!/usr/bin/python3

"""
This script takes a URL as a command-line
argument and attempts to open and read
the URL using an HTTP GET request.
If successful, it prints the decoded response.
If the request results in an HTTP error,
it prints the error code.
"""

if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        # Attempt to open the URL and read the response
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        # Handle HTTP errors by printing the error code
        print('Error code:', er.code)
