#!/usr/bin/python3
"""
Creates an Object from a JSON file
"""

import json


def load_from_json_file(filename):
    """
    Args:
        filename: name of the JSON file to load from
    Returns:
        Python object created from the JSON file
    """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)

if __name__ == "__main__":
    filename = "my_list.json"
    my_list = load_from_json_file(filename)
    print(my_list)
