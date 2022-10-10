#!/usr/bin/pyton3
"""
    Write a Python file similar to model_state.py named model_city.py
    that contains the class definition of a City.
"""
import sys
from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """
    Your script should take 3 arguments: mysql username,
    mysql password and database name
    You must use the module SQLAlchemy
    You must import State and Base from model_state - from
    model_state import Base, State
    Your script should connect to a MySQL server running
    on localhost at port 3306
    Results must be sorted in ascending order by cities.id
    Results must be display as they are in the example
    below (<state name>: (<city id>) <city name>)
    """
    __tablename__ = 'cities'
    id = Column(Integer(), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
