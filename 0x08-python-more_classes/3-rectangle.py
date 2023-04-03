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
        return self.__width

    @width.setter
    def width(self, value):
        """a setter function"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """a getter function"""
        return self.__height

    @height.setter
    def height(self, value):
        """a setter function"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        returns the rectangle area
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """defines perimeter"""
        perimeter = (self.__width + self.__height)*2
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return perimeter

    def __str__(self):
        """prints string format"""
        list = []
        for i in range(self.__height):
            for k in range(self.__width):
                list.append("#")

            if i != self.__height - 1:
                list.append("\n")
        if (self.__width == 0 or self.__height == 0):
            return ""
        else:
            return "".join(list)
