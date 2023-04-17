#!/usr/bin/python3
"""inheriting from the Base class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defining a square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing class"""
        super().__init__(size, size, x, y, id)
        self.size = self.width

    @property
    def size(self):
        """get property"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """overloading to str"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """updating the square class"""
        attbt = ["id", "size", "x", "y"]
        y = 0

        if args is not None and len(args) > 0:
            for arg in args:
                if y < 4:
                    setattr(self, attbt[y], arg)
                    y += 1

        elif (kwargs is not None):
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return a dictionary representation of the Square class"""
        return ({
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
            })
