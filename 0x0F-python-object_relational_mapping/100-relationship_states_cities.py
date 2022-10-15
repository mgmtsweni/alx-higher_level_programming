#!/usr/bin/python3
""" a script that creates the State “California”
    with the City “San Francisco” from the database
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

    new = State(name="California")
    new.cities.append(City(name="San Francisco"))

    session.add(new)
    session.commit()
    session.close()
