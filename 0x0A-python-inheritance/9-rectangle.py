#!/usr/bin/python3

"""defineing a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class inherited from BaseGeometry"""

    def __init__(self, width, height):
        """Intializing a new Rectangle:
        Args:
            width (int): width of the Rectangle.
            height (int): height of the Rectangle"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """return the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """return the print() and str() representation of a Rectangle"""
        rect_desc = "[" + str(self.__class__.__name__) + "] "
        rect_desc += str(self.__width) + "/" + str(self.__height)
        return (rect_desc)
