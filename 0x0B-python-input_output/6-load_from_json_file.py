#!/usr/bin/python3
"""
Creates an Object from a JSON file
"""


import json


def load_from_json_file(filename):
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
