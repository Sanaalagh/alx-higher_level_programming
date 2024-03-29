#!/usr/bin/python3
"""Defines the City model."""
from sqlalchemy import Integer, String, Column, ForeignKey
from model_state import Base


class City(Base):

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
