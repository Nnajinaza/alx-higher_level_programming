#!/usr/bin/pyton3
import sys
from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer(), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
