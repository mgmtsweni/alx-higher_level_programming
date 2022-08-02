#!/usr/bin/python3
"""function that writes to text file"""


def write_file(filename="", text=""):
    """writes to text file and returns num chars written"""
    with open(filename, mode="w", encoding="UTF-8") as f:
        return (f.write(text))
