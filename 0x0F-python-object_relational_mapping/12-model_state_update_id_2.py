#!/usr/bin/python3
"""  a script that changes the name of a State object from the
database hbtn_0e_6_usa  """

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

    # Find the State with ID 2
    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:
        # Update the name of the State
        state_to_update.name = "New Mexico"
        session.commit()
        print("State name updated successfully!")
    else:
        print("State with ID 2 not found.")
