#!/usr/bin/python3
"""class checking function."""


def inherits_from(obj, a_class):
    """ True:
        if the object is an instance of a class |
        that inherited from the specified class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
