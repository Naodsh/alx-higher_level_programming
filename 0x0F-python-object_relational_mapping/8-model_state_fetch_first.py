#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./8-model_state_fetch_first.py <mysql username>\
                <mysql password> <database name>")
        sys.exit(1)

    # Create connection to MySQL server
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first State object
    first_state = session.query(State).order_by(State.id).first()

    # Print the result or "Nothing" if no states found
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close session
    session.close()
