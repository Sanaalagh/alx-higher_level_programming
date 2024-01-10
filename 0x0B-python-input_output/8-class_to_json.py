#!/usr/bin/python3
"""
Returns the dictionary description for JSON serialization of an object
"""


def class_to_json(obj):
    return vars(obj)
