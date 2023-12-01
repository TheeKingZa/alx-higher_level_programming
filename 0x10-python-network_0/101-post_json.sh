#!/bin/bash
# Sends json POST request to URL given with json file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
