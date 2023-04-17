#!/usr/bin/python3
"""Base class for the rest of the project"""


class Base:
    """defining base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constuctor to initialize"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
