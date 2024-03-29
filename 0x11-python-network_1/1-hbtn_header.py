#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL, and displays the value
of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys


def fetch_x_request_id(url):
    """
    Fetches the value of the X-Request-Id variable from the header
    of the response.

    Args:
        url (str): The URL to send the request to.
    """
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        header = response.info()
        x_request_id = header.get('X-Request-Id')
        print(x_request_id)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_x_request_id(url)
