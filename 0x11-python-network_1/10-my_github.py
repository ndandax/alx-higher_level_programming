#!/usr/bin/python3
"""using github API to get user id"""
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    r = requests.get('https://api.github.com/user',
                     auth=(user, password))
    if r.status_code >= 400:
        print('None')
    else:
        print(r.json().get('id'))
