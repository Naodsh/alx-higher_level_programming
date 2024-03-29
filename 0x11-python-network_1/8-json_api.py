#!/usr/bin/python3
"""
Sends a POST request to
http://0.0.0.0:5000/search_user with a letter as a parameter.
Displays the id and name if response body is properly
JSON formatted and not empty.
"""

import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    try:
        response = requests.post(url, data={'q': letter})
        data = response.json()

        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
