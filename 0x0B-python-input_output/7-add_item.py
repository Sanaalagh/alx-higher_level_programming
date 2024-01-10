#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a file
"""

import sys
import os.path


def save_to_json_file(my_obj, filename):
    """
    Args:
        my_obj: Python object to be saved
        filename: name of the file to save to
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)


if __name__ == "__main__":
    filename = "add_item.json"
    my_list = []

    if os.path.isfile(filename):
        my_list = load_from_json_file(filename)

    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, filename)
