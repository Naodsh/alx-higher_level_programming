#!/usr/bin/python3
""" a script that adds the State object “Louisiana” to the database
hbtn_0e_6_usa """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create an engine to connect to the MySQL server
    engine = create_engine(
            f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}")

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object for Louisiana
    new_state = State(name="Louisiana")

    # Add the new state to the database
    session.add(new_state)
    session.commit()

    # Print the new state's ID
    print(new_state.id)
