#!/bin/bash
# Get the byte size of HTTP response header given for URL 
curl -s "$1" | wc -c

# Get the byte size of the HTTP response header for a given URL.
# The $1 represents the first command-line argument passed to the script.
# It assumes that the user provides a URL as an argument when running the script.

# curl -s "$1": Uses curl to make a silent (-s) request to the provided URL ($1).
# The -s flag makes curl operate in silent mode, so it doesn't show progress or error messages.

# | (pipe): Takes the output of the curl command and passes it as input to the next command.

# wc -c: Counts the number of bytes in the input.
# Here, it counts the bytes in the HTTP response header obtained from the curl command.

# The final result is the byte size of the HTTP response header for the given URL.

# To run the script, the user needs to provide a URL as a command-line argument.
# For example: ./script.sh http://example.com
