#!/usr/bin/python3
"""appending to a text file"""


def append_write(filename="", text=""):
    """a function that appends text to a file"""
    with open(filename, mode="a", encoding="utf-8") as new:
        y = new.write(text)
    return y
