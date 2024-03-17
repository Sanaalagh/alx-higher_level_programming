#!/usr/bin/python3
"""
A script that lists all City objects from the database hbtn_0e_14_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import Base and State
from model_city import City  # Import City

if __name__ == "__main__":
    # Create an engine that connects to the given database URL
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Bind the engine to the metadata of the Base class so that the
    # declaratives can be accessed through a DBSession instance
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    # Create a session
    session = DBSession()

    # Query all cities joined with their states, ordered by city.id
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Iterate and print city and state data
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
