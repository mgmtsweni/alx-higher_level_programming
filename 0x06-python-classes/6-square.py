#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            return (self.__size)**2

        def position(self):
            return (self.__position)

        @property
        def size(self):
            return (self.__size)

        @size.setter
        def size(self, value):
            if type(size) is not int:
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        def area(self):
            return (self.__size)**2

        def my_print(self):
            if self.__size == 0:
                print()
            else:
                for rows in range(self.__size):
                    print("#" * self.__size)

        def postion(self, value):
            if (len(value) != 2) or (type(value) is not tuple) \
                or (type(value[0]) is not int) or (type(value[1]) is not int) \
                or (value[0] < 0) or (value[1] < 0):
                raise TypeError("position must be a tuple of 2 positive integers")
            else:
                self.__position = value
