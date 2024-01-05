#!/usr/bin/python3
def magic_string():
     """
     Increment the count attribute and return a formatted string
     """
     magic_string.count = getattr(magic_string, 'count', 0) + 1
     return "BestSchool" + (", BestSchool" * magic_string.count)
