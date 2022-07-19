#!/usr/bin/python3
"""
Defines class Square with private attribute size
"""
class Square:
    """
    Arguments:
        size: size of Square
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
