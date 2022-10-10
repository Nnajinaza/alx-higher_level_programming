#!/usr/bin/python3

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
    state1 = State(name='Louisiana')
    session.add(state1)
    session.commit()
    print("{}".format(state1.id))
