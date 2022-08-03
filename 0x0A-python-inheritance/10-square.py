#!/usr/bin/python3
"""A function that applies Geomatric Class"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """inherits from Rectangle"""
    def __init__(self, size):
        """initializes size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    
    def area(self):
        """area of a square"""
        return self.__size ** 2
