#!/usr/bin/python3
"""sending POST request"""
import requests
import sys


email = sys.argv[2]
url = sys.argv[1]
res = requests.post(url, data={'email': email})
