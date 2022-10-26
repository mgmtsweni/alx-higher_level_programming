#!/usr/bin/python3
"""A script that takes your GitHub credentials use GitHub API to display id"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    auth = HTTPBasicAuth(argv[1], argv[2])
    url = 'https://api.github.com/user'
    res = requests.get(url, auth)
    id = res.json()
    print(id.get('id'))
