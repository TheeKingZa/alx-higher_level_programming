#!/bin/bash
# Bash script that sends a POST request to given URL.

# Check if URL is provided as an argument
if [ -z "$1" ]; then
	    echo "Usage: $0 <URL>"
	        exit 1
fi

# Set the variables for the POST request
email="test@gmail.com"
subject="I will always be here for PLD"

# Use curl to send a POST request to the provided URL with the specified variables
curl -s -X POST "$1" -d "email=$email&subject=$subject"

