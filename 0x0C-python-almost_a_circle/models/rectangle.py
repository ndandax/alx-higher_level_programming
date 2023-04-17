#!/usr/bin/python3
"""the rectangle class"""
from models.base import base


class Rectangle(Base):
    """class inheriting from base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing the class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super(). __init__()

    @property
    def width(self):
        """getting width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value


    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value


    @property
    def x(self):
        """getting x"""
        return self.__x

    @x.setter
    def x(self):
        """set the value of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x can must be >= 0")
        self.__x = value


    @property
    def y(self):
        """getting y"""
        return self.__y

    @setter.y
    def y(self):
        """set the value of y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """defining area"""
        return self.__height * self__width

    def __str__(self):
        """updating by overring __str__ method """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updating the Rectangle"""
        attributes = ["id", "width", "height", "x", "y"]
        x = 0

        if args is not None and len(args) > 0:
            for arg in args:
                if x < 5:
                    setattr(self, attributes[x], arg)
                    i += 1

        elif (kwargs is not None):
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns a dictionary representation of the rectangle"""
        return ({
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        })
