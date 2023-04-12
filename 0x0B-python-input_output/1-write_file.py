#!/usr/bin/python3
"""writing to a file"""


def write_file(filename="", text=""):
    """a fuction that writes text to a file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        y = f.write(text)
    return y
