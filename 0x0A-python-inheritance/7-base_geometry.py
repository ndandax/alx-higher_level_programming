#!/usr/bin/python3
"""defines an empty class BaseGeometry."""


class BaseGeometry:
    """class that represent base geometry"""

    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer value:
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
