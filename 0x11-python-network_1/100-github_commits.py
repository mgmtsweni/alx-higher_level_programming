#!/usr/bin/python3
"""A script that takes 2 arguments"""
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        argv[2], argv[1])
    res = requests.get(url)
    commits = res.json()
    i = 0
    for key in commits[0:10]:
        print(key.get('sha') + ': ', end="")
        print(key.get('commit').get('author').get('name'))
