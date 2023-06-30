#!/usr/bin/python3
"""displays the value of the variable X-Request-Id in the response header"""
import requests
import sys

url = sys.argv[1]
r = requests.get(url)
h = r.headers.get('X-Request-Id')
print(h)
