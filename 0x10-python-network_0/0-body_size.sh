#!/bin/bash

# Check if URL is provided as argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request using curl and store response body in a variable
# response=$("curl -sI $1 | grep -i 'Content-Length' | awk '{print $2}'")
response=$(curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}')
# If Content-Length header is present, print its value (size of body), otherwise print 0
if [ -n "$response" ]; then
    echo "$response"
else
    echo "0"
fi
