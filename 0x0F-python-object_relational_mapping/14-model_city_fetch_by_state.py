#!/usr/bin/python3
"""
script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create an engine to connect to the MySQL server
    engine = create_engine(
            f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}")

    # Bind the engine to the metadata of the Base class so that the
    # declaratives can be accessed through a DBSession instance
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects joined with State and sort by City ID
    cities = session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all()

    # Print City objects in the specified format
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
