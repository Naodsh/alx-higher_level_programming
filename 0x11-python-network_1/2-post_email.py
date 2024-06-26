#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter and
displays the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys


def post_email(url, email):
    """
    Sends a POST request to the specified URL with the email as a parameter
    and displays the body of the response.
    Args:
        url (str): The URL to send the request to.
        email (str): The email to be sent as a parameter.
    """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
