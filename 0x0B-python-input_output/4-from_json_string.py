#!/usr/bin/python3
"""json module"""
import json


def from_json_string(my_str):
    """a function returning json presantation of a string"""
    return json.loads(my_str)
