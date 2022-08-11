#!/usr/bin/python3
"""
This module implements `rectangle` class
"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """setter y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area od the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print to stdout a rectangle using #"""
        print("\n" * self.__y +
              "\n".join(" " * self.__x + "#" * self.__width
                        for i in range(self.__height)))

    def __str__(self):
        """returns (<id>) <x>/<y> - <width>/<height> """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                self.__x,
                                                                self.__y,
                                                                self.__width,
                                                                self.__height)

    def update(self, *args):
        """
        set attributes in an order.
        If no args given: set attributes according to kwargs
        """
        if len(args):
            for a, b in enumerate(args):
                if a == 0:
                    self.id = b
                elif a == 1:
                    self.width = b
                elif a == 2:
                    self.height = b
                elif a == 3:
                    self.x = b
                else:
                    self.y = b

        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Return dictionary representation"""
        dic = {}
        dic["id"] = self.id
        dic["width"] = self.width
        dic["height"] = self.height
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
