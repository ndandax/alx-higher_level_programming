#!/usr/bin/python3
"""defines a class rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class inherited from BaseGeometry"""

    def __init__(self, width, height):
        """function that intialize a new Rectangle.
        Args:
            width (int): width of the Rectangle.
            height (int): height of the Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
