#!/usr/bin/python3
"""Square class with private instance attribute size"""

class Square:
    """
    Arguments:
        size: size of Square
    """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """Returns the area of a Square instance"""
            return (self.__size)**2

        @property
        def size(self):
            """Getter of the private attribute size"""
            return (self.__size)

        @size.setter
        def size(self, value):
            """Setter for the size private attribute"""
            if type(size) is not int:
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        def my_print(self):
            """Prints to stdout the square with the character #"""
            if self.__size == 0:
                print()
            else:
                for rows in range(self.__size):
                    print("#" * self.__size)
