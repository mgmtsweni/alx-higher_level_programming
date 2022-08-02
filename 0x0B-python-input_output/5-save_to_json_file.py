#!/usr/bin/python3
"""function for save_to_json_file method."""


import json


def save_to_json_file(my_obj, filename):
    """Writes a Python obj to file using JSON represenation"""
    with open(filename, "w",) as j_file:
        json.dump(my_obj, j_file)
