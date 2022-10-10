#!/usr/bin/pyton3
"""Write a python file that contains the class definition of a State and an instance Base = declarative_base():
"""
from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer(), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
