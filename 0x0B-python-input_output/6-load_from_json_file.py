#!/usr/bin/python3
"""function for load_from_json_file method."""


import json


def load_from_json_file(filename):
    """Creates a Python obj from JSON file"""
    with open(filename, "r") as j_file:
        my_obj = json.load(j_file)
        return my_obj
