#!/usr/bin/python3
"""class checking function."""


def is_kind_of_class(obj, a_class):
    """ True if the object is an instance of,
        || if the object is an instance of a class that inherited from,
        |   the specified class
    """
    return isinstance(obj, a_class)
