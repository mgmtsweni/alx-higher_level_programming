#!/usr/bin/python3
"""A script to display X-Request-Id value"""
import urllib.request
from sys import argv


if __name__ == '__main__':
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        body = response.headers
        print(body['X-Request-Id'])
