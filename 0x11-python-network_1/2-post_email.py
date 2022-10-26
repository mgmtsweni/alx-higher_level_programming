#!/usr/bin/python3
"""A script that sends a POST request and displays the body of the response"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    value = {'email': argv[2]}
    data = urllib.parse.urlencode(value).encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
