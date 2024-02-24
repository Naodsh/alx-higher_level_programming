from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./7-model_state_fetch_all.py <mysql username>\
                <mysql password> <database name>")
        sys.exit(1)

    # Create connection to MySQL server
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and display their IDs and names
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()
