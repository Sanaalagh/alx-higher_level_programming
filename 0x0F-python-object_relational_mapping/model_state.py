#!/usr/bin/python3
"""
Definition of the State class which inherits from Base, an instance
of declarative_base(), linking it to the states table in MySQL.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Instance of the declarative base
Base = declarative_base()


class State(Base):
    """
    Definition of the State class which corresponds
    to the states table in MySQL.
    Attributes:
        id (Column): The state's id.
        name (Column): The state's name.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
