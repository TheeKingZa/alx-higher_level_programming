#!/bin/bash
# Display all HTTP methods the server of given URL will be accepted.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
