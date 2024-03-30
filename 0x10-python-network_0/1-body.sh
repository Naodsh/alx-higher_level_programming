#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -o /dev/null -w "%{http_code}" "$1" | { read -r status_code; [ "$status_code" -eq 200 ] && curl -s "$1"; }
