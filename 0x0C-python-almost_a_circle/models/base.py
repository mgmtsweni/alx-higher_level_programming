#!/usr/bin/python3
"""
This module implements `base` class of all other classes
"""


class Base():
    """implementation"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize id, increment class attribute if
        no id and set as id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
