#!/usr/bin/python3
"""
Returns the JSON representation of an object (string)
"""


import json


def to_json_string(my_obj):
    """
    Args:
        my_obj: Python object to be converted to JSON string
    Returns:
        JSON representation of the object
    """
    return json.dumps(my_obj)


if __name__ == "__main__":
    my_list = [1, 2, 3]
    s_my_list = to_json_string(my_list)
    print(s_my_list)
