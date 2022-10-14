#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa
    filters by the letter 'a'
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()

    st = '%a%'
    states = session.query(State).filter(State.name.like(st)).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
