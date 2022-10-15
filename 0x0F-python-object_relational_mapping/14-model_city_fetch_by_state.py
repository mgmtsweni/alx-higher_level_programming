#!/usr/bin/python3
""" script that prints all City objects from the database hbtn_0e_0_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()

    rows = session.query(State.name, City.id, City.name).\
        filter(State.id == City.state_id).order_by(City.id)
    for city, state in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()
