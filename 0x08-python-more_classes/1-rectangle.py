#!/usr/bin/python3
"""a detailed class of that explains tectangle more"""


class Rectangle:
    """a class that defines rectangle"""
    def __init__(self, width=0, height=0):
        """function with optional arguments"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """property function"""
        return self._width

    @width.setter
    def width(self, value):
        """a setter function"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """a getter function"""
        return self._height

    @height.setter
    def height(self, value):
        """a setter function"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
