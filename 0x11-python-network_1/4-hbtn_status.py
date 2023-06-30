#!/usr/bin/python3
"""fetching url"""
import requests


r = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print(f"\t- type: {type(r.text)}")
print(f"\t- content: {r.text}")
