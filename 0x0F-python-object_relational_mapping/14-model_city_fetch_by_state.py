#!/usr/bin/python3
"""
a Python file similar to model_state.py named model_city.py that contains
the class definition of a City.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State, City
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

    # Query all City objects and sort by ID
    cities = session.query(City).order_by(City.id).all()

    # Print City objects in the specified format
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")
