#!/usr/bin/python3
"""
    Write a script that prints the State object with the name
    passed as argument from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, Session
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State)

    for state in states:
        if (sys.argv[4] == state.name):
            print("{}".format(state.id))
            break
    else:
        print("Not found")
