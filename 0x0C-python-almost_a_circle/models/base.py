#!/usr/bin/python3
"""
This module implements `base` class of all other classes
"""


class base():
    """
    implementation
    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
           Base.__nb_objects += 1
           self.id = Base.__nb_objects
