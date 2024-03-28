#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]

    r = requests.get(url, auth=(username, password))
    if r.status_code == 200:
        print(r.json().get('id'))
    else:
        print(None)
