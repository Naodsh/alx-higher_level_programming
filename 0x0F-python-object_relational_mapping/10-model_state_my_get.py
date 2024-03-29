#!/usr/bin/python3
"""
Prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <mysql username> \
                <mysql password> <database name> <state name>")
        sys.exit(1)

    # Create a connection to the MySQL server
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with the specified name
    state = session.query(State).filter(State.name == state_name).first()

    # Print the result or "Not found" if no state matches the name
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
