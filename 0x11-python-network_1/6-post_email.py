#!/usr/bin/python3
"""A script that sends a POST request and displays the body of the response"""
import requests
from sys import argv


if __name__ == '__main__':
    value = {'email': argv[2]}
    data = requests.post(argv[1], value)
    print(data.text)
