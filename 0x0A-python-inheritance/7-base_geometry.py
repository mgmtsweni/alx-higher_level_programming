#!/usr/bin/python3
"""class BaseGeometry."""


class BaseGeometry:
    """A base geometry."""
    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates value to be an int grater than 0."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
