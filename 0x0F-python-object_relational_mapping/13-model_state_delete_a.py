#!/usr/bin/python3
""""
a script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""

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

    # Find all State objects with names containing the letter "a"
    states_to_delete = session.query(State).filter(
            State.name.like('%a%')).all()

    if states_to_delete:
        # Delete the selected states
        for state in states_to_delete:
            session.delete(state)
        session.commit()
        print("States with names containing 'a' deleted successfully!")
    else:
        print("No states with names containing 'a' found.")
