#!/usr/bin/python3
"""A script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user"""
import requests
from sys import argv


if __name__ == '__main__':
    if len(argv) < 2 or argv[1].isdigit():
        value = {"q": ""}
        res = requests.post('http://0.0.0.0:5000/search_user', value)
        print("No result")
    else:
        value = {"q": argv[1]}
        res = requests.post('http://0.0.0.0:5000/search_user', value)
        head = res.headers['Content-Type']
        if head != 'application/json':
            print("Not a valid JSON")
        else:
            response = res.json()
            print("[{}] {}".format(response.get("id"), response.get("name")))
