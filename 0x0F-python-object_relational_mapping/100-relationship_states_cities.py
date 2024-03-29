#!/usr/bin/python3
"""Create states"""
from sqlalchemy import create_engine, true
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
    session.close()
