#!/usr/bin/python3
class Base:
    """Base class for all shapes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class.

        Parameters:
            id (int): ID of the instance.

        Attributes:
            id (int): ID of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
