#!/bin/bash
# Get the byte size of HTTP response header given for URL 
curl -s "$1" | wc -c
