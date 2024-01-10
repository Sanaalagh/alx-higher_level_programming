#!/usr/bin/python3
"""
Writes an object to a text file, using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Args:
        my_obj: Python object to be saved
        filename: name of the file to save to
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)


if __name__ == "__main__":
    my_list = [1, 2, 3]
    filename = "my_list.json"
    save_to_json_file(my_list, filename)
