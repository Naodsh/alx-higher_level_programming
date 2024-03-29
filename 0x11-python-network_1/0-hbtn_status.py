#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using urllib package
and displays the body of the response.
"""

import urllib.request


def fetch_status():
    """
    Fetches the status from the specified URL and
    displays the body of the response.
    """
    url = 'https://alx-intranet.hbtn.io/status'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        body = response.read()

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))


if __name__ == "__main__":
    fetch_status()
