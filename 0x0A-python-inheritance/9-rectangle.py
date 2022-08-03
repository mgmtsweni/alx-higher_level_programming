#!/usr/bin/python3
"""AA function that applies Geomatric Class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""

    def __init__(self, width, height):
        """validate and initialize width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        
        self.__width = width
        self.__height = height
    
    def area(self):
        """area of ractangle"""
        return (self.__width * self.__height)
    
    def __str__(self):
        """prints"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                        self.__width, self.__height)
