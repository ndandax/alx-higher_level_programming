#!/usr/bin/python3
""" a class that inherits from list"""


class MyList(list):
    """class definition"""
    def print_sorted(self):
        """ function that prints in sorted form"""
        print(sorted(self))
