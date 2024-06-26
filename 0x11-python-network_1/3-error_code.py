#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL,
and displays the body of the response.
Handles urllib.error.HTTPError exceptions
and prints "Error code:" followed by the HTTP status code.
"""

import urllib.request
import urllib.error
import sys


def display_response(url):
    """
    Sends a request to the URL and displays the body of the response.
    Handles urllib.error.HTTPError exceptions and prints
    "Error code:" followed by the HTTP status code.
    Args:
        url (str): The URL to send the request to.
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    url = sys.argv[1]
    display_response(url)
