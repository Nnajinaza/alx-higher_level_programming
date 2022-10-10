#!/usr/bin/pyton3
"""Improve the files model_city.py"""
from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from model_state import Base, State


class City(Base):
    """
        Improve the files model_city.py save it as relationship_city.py
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
