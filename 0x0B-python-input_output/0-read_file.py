#!/usr/bin/python3
"""reading textfiles"""


def read_file(filename=""):
    """a function that reads textfiles"""
    with open('filename', encoding='utf-8') as f:
        f.read()
