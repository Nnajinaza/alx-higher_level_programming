#!/usr/bin/python3
"""Lists all the cities in the database by their respective states.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys
from venv import create

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    args = session.query(State.name, City.id,
                         City.name).outerjoin(State).order_by(City.id).all()
    for arg in args:
        print('{}: ({}) {}'.format(arg[0], arg[1], arg[2]))
