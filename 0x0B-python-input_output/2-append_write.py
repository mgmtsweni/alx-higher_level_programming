#!/usr/bin/python3
"""
function for append_write method.
"""


def append_write(filename="", text=""):
    """appends to text file and returns num chars added"""
    with open(filename, "a", encoding='utf-8') as a_file:
        return a_file.write(text)
