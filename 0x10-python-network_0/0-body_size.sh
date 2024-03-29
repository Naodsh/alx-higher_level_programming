#!/bin/bash
# This script takes a URL as argument, sends a request to that URL, and displays the size of the body of the response in bytes
# It uses curl with the -s (silent mode) option

curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}'
