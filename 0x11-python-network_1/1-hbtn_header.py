#!/usr/bin/python3
"""script that returns value of X-Requst_Id"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        y = res.info()
        print(y["X-Request-Id"])
