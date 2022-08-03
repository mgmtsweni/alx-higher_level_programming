#!/usr/bin/python3
"""A function that adds attributes to objects."""


def add_attribute(obj, attribute, value):
    """Add a new attribute to an object if possible."""
    if ('__dict__' in dir(obj)):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
